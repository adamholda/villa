# PR2307: actual missing-cache error and unchanged controls

Actual ConfigManager/ZarrDataset ValueError (verbatim text, not a claimed human CLI failure):

```text
Background sampling needs a matching patch cache; run `vesuvius.find_patches --config <config.yaml>` to regenerate it.
```

Selected actual diagnostic fields, pretty-printed:

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
    "contract_matches": false,
    "enumerated_without_validated_cache": 16,
    "data_file_tree_preserved": true
  },
  "repaired_missing_cache": {
    "contract_matches": true,
    "data_file_tree_preserved": true
  },
  "disabled_foreground_positions_identical": true,
  "final_original_input_hashes_unchanged": true,
  "all_six_process_origins_qualified": true
}
```

The old PHerc0841 control was originally selected using released labels and later exposed. It is one correlated 1024-square plane, not an independent heldout sample. Direct2D mask mapping:reviewed ink1,reviewed nonink0,unreviewed2. No artificial ignore pixels or depth replication. No scanner repair, model, training, quality, native registration or new personal review. Whole original source hashes are unchanged.
