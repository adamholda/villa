"""PBS child: actual configured dataset and selected joint orientation kernels."""
from __future__ import annotations
import argparse
import hashlib
import importlib
import json
from pathlib import Path
import time


def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--source", type=Path, required=True)
    ap.add_argument("--config", type=Path, required=True)
    ap.add_argument("--inputs", type=Path, required=True)
    ap.add_argument("--work", type=Path, required=True)
    ap.add_argument("--arm", choices=["original", "repaired"], required=True)
    a = ap.parse_args()
    c = json.loads(a.config.read_text())
    source = a.source.resolve()
    for name, hashes in c["production_sources"].items():
        assert digest(source / name) == hashes[a.arm], name
    for name, expected in c["common_source_sha256"].items():
        assert digest(source / name) == expected, name
    start = time.monotonic()
    import numpy as np
    import torch
    import zarr
    torch.set_num_threads(1)
    torch.set_num_interop_threads(1)
    from vesuvius.models.configuration.config_manager import ConfigManager
    from vesuvius.models.training.cli import build_parser
    from vesuvius.models.utilities.cli_utils import update_config_from_args
    from vesuvius.models.datasets.zarr_dataset import ZarrDataset
    from vesuvius.models.augmentation.transforms.spatial.rot90 import Rot90Transform
    from vesuvius.models.augmentation.transforms.spatial.transpose import TransposeAxesTransform
    for name in ["vesuvius.models.datasets.zarr_dataset", "vesuvius.models.augmentation.pipelines.training_transforms"]:
        m = importlib.import_module(name)
        assert Path(m.__file__).resolve() == source / (name.replace(".", "/") + ".py")

    def ahash(array):
        return hashlib.sha256(np.ascontiguousarray(array).tobytes()).hexdigest()

    def plain(value):
        if isinstance(value, dict):
            return {k: plain(v) for k, v in value.items()}
        if isinstance(value, (list, tuple)):
            return [plain(v) for v in value]
        if isinstance(value, np.generic):
            return value.item()
        return value

    def objects(node):
        children = []
        for key in ["transforms", "list_of_transforms"]:
            value = getattr(node, key, None)
            if isinstance(value, (tuple, list)):
                children.extend(value)
        child = getattr(node, "transform", None)
        if child is not None:
            children.append(child)
        return [node] + [v for child in children for v in objects(child)]

    image_ref = np.asarray(zarr.open(str(a.inputs / "images/volume.zarr/0"), mode="r")[:], dtype=np.float32)[None]
    mask_ref = np.asarray(zarr.open(str(a.inputs / "labels/volume_fiber.zarr/0"), mode="r")[:], dtype=np.float32)[None]
    pad_ref = np.ones_like(mask_ref)
    assert np.count_nonzero(mask_ref) > 0
    results = []
    for mode in c["modes"]:
        assert time.monotonic() - start < 210
        folder = a.work / mode
        folder.mkdir()
        settings = {"tr_setup": {"model_name": "actual_annotation_geometry", "ckpt_out_base": str(folder / "out")},
            "tr_config": {"patch_size": [256, 256, 256], "num_dataloader_workers": 0}, "model_config": {},
            "dataset_config": {"data_path": str(a.inputs), "targets": {"fiber": {"out_channels": 2}},
                "normalization_scheme": "none", "skip_patch_validation": True, "cache_valid_patches": False,
                "no_spatial": False}}
        path = folder / "config.yaml"
        path.write_text(json.dumps(settings))
        mgr = ConfigManager(verbose=False)
        mgr.load_config(path)
        argv = ["--config", str(path), "--output", str(folder / "out")]
        if mode != "unrestricted":
            argv += ["--rotation-axes", mode]
        args = build_parser().parse_args(argv)
        update_config_from_args(mgr, args)
        expected_manager = {"z": (0,), "none": (), "unrestricted": None}[mode]
        assert mgr.allowed_rotation_axes == expected_manager
        data = ZarrDataset(mgr, is_training=True)
        assert len(data) == 1
        pipeline = data.transforms
        nodes = objects(pipeline)
        operations = [x for x in nodes if isinstance(x, (Rot90Transform, TransposeAxesTransform))]
        signature = sorted([[type(x).__name__, sorted(x.allowed_axes)] for x in operations])
        unrestricted = [["Rot90Transform", [0, 1, 2]], ["TransposeAxesTransform", [0, 1, 2]]]
        expected = [] if mode == "none" else ([["Rot90Transform", [1, 2]], ["TransposeAxesTransform", [1, 2]]] if mode == "z" else unrestricted)
        assert signature == (unrestricted if a.arm == "original" else expected)
        contract = signature == expected
        assert contract == (a.arm == "repaired" or mode == "unrestricted")
        assert any(type(n).__module__.startswith("vesuvius.models.augmentation.transforms.intensity.") for n in nodes)
        # Instrumentation: actual getter without the composed stochastic pipeline,
        # followed by the actual factory-created quarter-turn/transpose members.
        data.transforms = None
        try:
            sample = data[0]
        finally:
            data.transforms = pipeline
        assert sample["patch_info"]["position"] == (0, 0, 0) and not sample["is_unlabeled"]
        assert tuple(sample["image"].shape) == tuple(sample["fiber"].shape) == (1, 256, 256, 256)
        assert torch.equal(sample["image"], torch.from_numpy(image_ref))
        assert torch.equal(sample["fiber"], torch.from_numpy(mask_ref))
        assert torch.equal(sample["padding_mask"], torch.from_numpy(pad_ref))
        row = {"mode": mode, "manager_axes": plain(mgr.allowed_rotation_axes), "factory_signature": signature,
            "expected_signature": expected, "factory_contract_matches": contract, "dataset_items": 1,
            "getter_image_mask_padding_exact": True, "kernel_observations": [],
            "scope": "Instrumented actual dataset getter/factory and selected quarter-turn/transpose leaves;not the full composed augmentation pipeline or training."}
        for operation in operations:
            for seed in c["seeds"]:
                assert time.monotonic() - start < 210
                original_get = operation.get_parameters
                captured = []
                def capture(**sample_data):
                    params = original_get(**sample_data)
                    captured.append(plain(params))
                    return params
                operation.get_parameters = capture
                np.random.seed(seed)
                torch.manual_seed(seed)
                try:
                    output = operation(image=sample["image"].clone(), fiber=sample["fiber"].clone(),
                        padding_mask=sample["padding_mask"].clone(), is_unlabeled=False)
                finally:
                    operation.get_parameters = original_get
                assert len(captured) == 1
                params = captured[0]
                if isinstance(operation, Rot90Transform):
                    def reference(array):
                        for k, axes in zip(params["num_rot_per_combination"], params["axis_combinations"]):
                            array = np.rot90(array, k=k, axes=axes)
                        return array
                    forbidden = any(1 in axes for axes in params["axis_combinations"])
                else:
                    def reference(array):
                        return np.transpose(array, params["axis_order"])
                    forbidden = params["axis_order"][1] != 1
                hashes = {}
                depth_profiles = {}
                for key, raw in [("image", image_ref), ("fiber", mask_ref), ("padding_mask", pad_ref)]:
                    actual = output[key].numpy()
                    assert output[key].device.type == "cpu" and output[key].dtype == torch.float32
                    assert np.array_equal(actual, reference(raw))
                    hashes[key] = ahash(actual)
                    depth_profiles[key] = bool(np.array_equal(actual[0].sum(axis=(1, 2), dtype=np.int64), raw[0].sum(axis=(1, 2), dtype=np.int64)))
                if a.arm == "repaired" and mode == "z":
                    assert not forbidden and all(depth_profiles.values())
                row["kernel_observations"].append({"kind": type(operation).__name__, "seed": seed, "parameters": params,
                    "joint_values_equal_independent_numpy_reference": True, "output_sha256": hashes,
                    "moves_or_flips_depth_axis": forbidden, "per_depth_sums_preserved": depth_profiles,
                    "image_changes": hashes["image"] != ahash(image_ref)})
                del output
        if a.arm == "original" and mode == "z":
            assert any(x["moves_or_flips_depth_axis"] for x in row["kernel_observations"])
        if a.arm == "original" and mode == "none":
            assert any(x["image_changes"] for x in row["kernel_observations"])
        results.append(row)
        print("CONFIG_RECORD=" + json.dumps(row), flush=True)
        del sample, data, pipeline
    assert len(results) == 3
    expected_kernels = 24 if a.arm == "original" else 16
    assert sum(len(x["kernel_observations"]) for x in results) == expected_kernels
    print("ROTATION_CT_RESULT=" + json.dumps({"arm": a.arm, "records": results,
        "kernel_observations": expected_kernels, "elapsed_seconds": time.monotonic() - start}), flush=True)


if __name__ == "__main__":
    main()
