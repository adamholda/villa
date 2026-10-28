# PR2326 / Original CLI exits0 and erases the selected input

Actual archived0123/PBS25071129 CLI output on a disposable fixed S5 CT copy. This is not a live terminal or CT pixel image. The paired S3 records are also linked.

Entry point and recorded CLI arguments (the driver uses a source-verifying runpy wrapper):

```sh
python -m vesuvius.image_proc.run.zarr_tasks input.zarr/0 input.zarr --task transpose --transpose-order zyx --num-levels 1 --num-workers 1 --level 0
```

Exit code:0;overwrite prompt:True. Actual post-run verifier:nonzero input voxels245760 -> 0. These counts are actual verification records,not extra text printed by the CLI.

### Actual archived CLI stdout/stderr

```text
Output path input.zarr already exists. Overwrite? (y/n): Using 1 worker processes
Input array shape: (48, 64, 80)
Input array chunks: (16, 16, 16)
Input array dtype: uint8
Task: transpose | order=zyx | perm=[0, 1, 2]
Output array shape: (48, 64, 80)
Output array chunks: (16, 16, 16)
Total items to process: 60

transpose:   0%|          | 0/60 [00:00<?, ?it/s]
transpose:   2%|▏         | 1/60 [00:03<03:01,  3.08s/it]
transpose:  52%|█████▏    | 31/60 [00:03<00:02, 13.59it/s]
transpose:  95%|█████████▌| 57/60 [00:03<00:00, 28.23it/s]
transpose: 100%|██████████| 60/60 [00:03<00:00, 18.24it/s]
Transpose complete. OME-Zarr pyramid saved to: input.zarr
```

[Exact CLI log](cli-before.log) SHA256:`0d208c62ebfba81ac044ab0c41113852994646531491591379f9f2122bfdbd7e`. [All8 records and hashes](selected-records.json).

Constructed format2 headers over real CT. Identity order is the destructive-route case;the valid control uses xzy. Native CT remains unchanged. No physical-frame,race,group-routing,training or quality claim. Cleanup warnings are retained. e-INFRA CZ90254.
