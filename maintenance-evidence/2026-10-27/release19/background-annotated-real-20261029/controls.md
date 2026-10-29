# PR2307: actual missing-cache error and unchanged controls

Selected actual records from the uncached library case and fixed-grid controls. This is the actual ConfigManager/ZarrDataset error, not a claimed human CLI failure.

```json
{
  "fixed_plane": 14,
  "shape": [
    1024,
    1024
  ],
  "whole_fixed_grid": 16,
  "foreground_regions": 2,
  "background_regions": 4,
  "original_missing_cache": {
    "case": "enabled_missing_cache",
    "arm": "original",
    "contract_matches": false,
    "actual_ValueError": null,
    "enumerated_without_validated_cache": 16,
    "data_file_tree_preserved": true
  },
  "repaired_missing_cache": {
    "case": "enabled_missing_cache",
    "arm": "repaired",
    "contract_matches": true,
    "actual_ValueError": "Background sampling needs a matching patch cache; run `vesuvius.find_patches --config <config.yaml>` to regenerate it.",
    "enumerated_without_validated_cache": null,
    "data_file_tree_preserved": true
  },
  "disabled_foreground_positions_identical": true,
  "final_original_input_hashes_unchanged": true,
  "all_six_process_origins_qualified": true
}
```

The old PHerc0841 control was originally selected using released labels and later exposed. It is one correlated 1024-square plane, not an independent heldout sample. Direct2D mask mapping:reviewed ink1,reviewed nonink0,unreviewed2. No artificial ignore pixels or depth replication. No scanner repair, model, training, quality, native registration or new personal review. Whole original source hashes are unchanged.
