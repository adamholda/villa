# Exact controls and preservation

Public excerpt: private paths, account/host identifiers, per-job IDs and precise timestamps are omitted. Numeric fields are copied unchanged from the actual recorded comparison. No CT pixels, weights or prediction images.

Selected actual driver fields,not CLIstdout. Five operations reuse ONE real control crop.

```json
{
  "gate_passed": true,
  "actual_CLI_calls": 5,
  "original_declared_layout_nonmatches": 1,
  "original_wide_control": 1,
  "repaired_declared_layout_matches": 3,
  "wide_control_exact": true,
  "repaired_storage_permutation_predictions_exact": true,
  "native_input_and_weights_unchanged": true,
  "generated_input_tree_unchanged": true,
  "output_hashes": {
    "original-wide": "f2fc3a803da6df64bb533785a59103395eba5e8f73f6deff510d1b8fd470a755",
    "repaired-wide": "f2fc3a803da6df64bb533785a59103395eba5e8f73f6deff510d1b8fd470a755",
    "repaired-narrow-zyx": "0ef35266d9a52ecedea9515031a80160919d0a3827bdccddc2d93ed35dd27bca",
    "repaired-narrow-yxz": "0ef35266d9a52ecedea9515031a80160919d0a3827bdccddc2d93ed35dd27bca"
  }
}
```

Wide original/repaired predictions match.Repaired narrow storage-axis permutations match. This is geometry/input routing,not ink/model quality or recovered text.
