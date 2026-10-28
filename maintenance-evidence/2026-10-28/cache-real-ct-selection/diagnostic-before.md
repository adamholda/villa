# PR2330 / Original silently reuses S3 after S5 is requested

Actual archived0128/PBS25084792 module-CLI output below is verbatim. The separate cache/dataset record is actual harness diagnostics, pretty-printed for readability; it is not CLI output or training. Both original and repaired commands exit0.

## Actual CLI output

```text
Detected 3D patch size (48, 64, 80), setting 3D operations
Patch cache generation complete: 0 cache(s) written, 0 volumes scanned, 2 skipped.
Patches found: 0 FG, 0 BG, 1 unlabeled FG.
```

[Exact CLI log and SHA256](./original-selection_change-select_s5_without_force-actual-cli.log): `378dbecad313365b0fb21b368181fbcfb9d758a9ddac968d0b1f572e4b7e4f54`

## Actual cache/dataset diagnostic

```json
{
  "arm": "original",
  "scenario": "selection_change",
  "step": "select_s5_without_force",
  "selection": [
    "s5"
  ],
  "requested_ids": [
    "s5"
  ],
  "actual_cache_and_dataset_ids": [
    "s3"
  ],
  "selection_contract_matches": false,
  "written_caches": 0,
  "scanned_volumes": 0,
  "skipped_volumes": 2,
  "cache_files": 1,
  "reuse_preserves_bytes": true,
  "exact_raw_CT_item_hashes": {
    "s3": "8acf79e601eb1846db80e42d7380c3a5d6de1f2e8e2071eaa459174691db06ad"
  },
  "image_tree_unchanged": true,
  "missing_labels_stay_unlabeled": true,
  "actual_CLI_and_ConfigManager_and_dataset": true,
  "model_or_training": false
}
```

The supported image-only path uses fixed real S3/S5 CT crops and no annotations/model/training. Native input trees remain unchanged. One run:112s x1CPU/0GPU; e-INFRA CZ90254. Two reused crops, not eight independent samples or incidents. [All records](selected-records.json), raw result SHA256 `b5c9cf6195a98d02b581c89feeac72c4e6f14d6daedb3762821900bcbdbb3cf2`. Original/repaired production hashes and frozen input/oracle scope are retained privately; no CT pixels, arrays or raw account logs are published.
