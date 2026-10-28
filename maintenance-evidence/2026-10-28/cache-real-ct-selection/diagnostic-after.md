# PR2330 / Repair computes and loads the requested S5 selection

Actual archived0128/PBS25084792 module-CLI output below is verbatim. The separate cache/dataset record is actual harness diagnostics, pretty-printed for readability; it is not CLI output or training. Both original and repaired commands exit0.

## Actual CLI output

```text
Detected 3D patch size (48, 64, 80), setting 3D operations
Finding valid patches of size: (48, 64, 80) at full resolution with bounding box coverage >= 0.95 and labeled fraction >= 0.1.

Processing volumes:   0%|          | 0/2 [00:00<?, ?it/s][2026-10-28 16:12:36,030] WARNING:vesuvius.models.datasets.find_valid_patches: Volume 's3' has no label array available at index 0; skipping validation
[2026-10-28 16:12:36,030] INFO:vesuvius.models.datasets.find_valid_patches: Volume 's5' has no labels at index 1; collecting unlabeled FG patches from image data
[2026-10-28 16:12:36,030] INFO:vesuvius.models.datasets.find_valid_patches: DEBUG: image_array type=Group, hasattr(keys)=True, hasattr(shape)=False
[2026-10-28 16:12:36,031] INFO:vesuvius.models.datasets.find_valid_patches: DEBUG: image_array keys=['0']
[2026-10-28 16:12:36,036] INFO:vesuvius.models.datasets.find_valid_patches: Using image level 0 for unlabeled volume 's5' with patch size (48, 64, 80)
[2026-10-28 16:12:36,036] INFO:vesuvius.models.datasets.find_valid_patches: Unlabeled volume 's5': image shape (48, 64, 80), target patch (48, 64, 80), candidate positions 1

Processing volume 's3' (1/2)

Processing volume 's5' (2/2)


  s5 (unlabeled):   0%|          | 0/1 [00:00<?, ?it/s][A

                                                       [A[2026-10-28 16:12:36,040] INFO:vesuvius.models.datasets.find_valid_patches: Unlabeled volume 's5': 1 unlabeled FG patches identified (100.00% of candidates) in 0.00s

Processing volumes: 100%|██████████| 2/2 [00:00<00:00, 148.77it/s]
Found 1 unlabeled foreground patches in 's5'

Total valid patches found across all 2 volumes: 0
Total unlabeled foreground patches found: 1
Patch cache generation complete: 1 cache(s) written, 2 volumes scanned, 0 skipped.
Patches found: 0 FG, 0 BG, 1 unlabeled FG.
```

[Exact CLI log and SHA256](./repaired-selection_change-select_s5_without_force-actual-cli.log): `91312c0a1af991eef144f5a1854364d562eac6bb86ee9fc4e36fbf3f5d749dca`

## Actual cache/dataset diagnostic

```json
{
  "arm": "repaired",
  "scenario": "selection_change",
  "step": "select_s5_without_force",
  "selection": [
    "s5"
  ],
  "requested_ids": [
    "s5"
  ],
  "actual_cache_and_dataset_ids": [
    "s5"
  ],
  "selection_contract_matches": true,
  "written_caches": 1,
  "scanned_volumes": 2,
  "skipped_volumes": 0,
  "cache_files": 2,
  "reuse_preserves_bytes": false,
  "exact_raw_CT_item_hashes": {
    "s5": "65e39496172ffd6f678f77d5b3f7d80cc31e68750295b2cdfc3ad2eeb364d4ac"
  },
  "image_tree_unchanged": true,
  "missing_labels_stay_unlabeled": true,
  "actual_CLI_and_ConfigManager_and_dataset": true,
  "model_or_training": false
}
```

The supported image-only path uses fixed real S3/S5 CT crops and no annotations/model/training. Native input trees remain unchanged. One run:112s x1CPU/0GPU; e-INFRA CZ90254. Two reused crops, not eight independent samples or incidents. [All records](selected-records.json), raw result SHA256 `b5c9cf6195a98d02b581c89feeac72c4e6f14d6daedb3762821900bcbdbb3cf2`. Original/repaired production hashes and frozen input/oracle scope are retained privately; no CT pixels, arrays or raw account logs are published.
