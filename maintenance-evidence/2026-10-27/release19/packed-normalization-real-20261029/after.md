# Real packed CT: repaired normalization

Selected actual archived fields; formatted JSON, not a live terminal or full training CLI. Private paths, accounts/hosts, per-job IDs and precise timestamps are omitted. Numerical fields are unchanged. One fixed S5 CT/released binary fiber pair; two correlated128cube crops.

Actual ConfigManager and nontraining ZarrDataset item read, after the unmodified TIFF packing CLI.

The repaired image exactly matches the independent own-sample-plus-gap reference.

```json
{
  "case": "zscore_overlap",
  "arm": "repaired",
  "scheme": "zscore",
  "patch_shape": [
    128,
    128,
    192
  ],
  "own_source_and_gap_reference_matches": true,
  "maximum_absolute_difference": 0.0,
  "actual_mask_and_padding_exact": true,
  "mapping_unchanged": true,
  "actual_ConfigManager_and_dataset_used": true,
  "training_or_model_used": false
}
```

All three repaired contracts match exactly. No model or training was run.
