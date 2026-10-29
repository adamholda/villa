# PR2305 — actual paired history controls

Selected fields from the actual complete six-context native training record. Only the public PR2305 training file differs across original and repaired source arms. No scheduler instance or serialized state was modified by the observers. Typed checkpoint policy and hard optimizer PRE-step guards apply before actual updates.

```json
{
  "genuine_producer_optimizer_updates": 2,
  "actual_optimizer_updates_total": 3,
  "actual_complete_native_CLI_contexts": 6,
  "genuine_producer_best_val_loss": 0.5637056827545166,
  "actual_controls": {
    "metric-mismatch": {
      "actual_CLI_exit_code": 0,
      "actual_typed_weights_only": false,
      "actual_start_step": 4,
      "actual_restored_best": null,
      "actual_optimizer_updates": 0,
      "actual_origins_qualified": true
    },
    "foreign-output": {
      "actual_CLI_exit_code": 0,
      "actual_typed_weights_only": false,
      "actual_start_step": 4,
      "actual_restored_best": null,
      "actual_optimizer_updates": 0,
      "actual_origins_qualified": true
    },
    "weights-only": {
      "actual_CLI_exit_code": 0,
      "actual_typed_weights_only": true,
      "actual_start_step": 0,
      "actual_restored_best": null,
      "actual_optimizer_updates": 1,
      "actual_origins_qualified": true
    }
  },
  "producer_artifacts_and_original_input_trees_unchanged": true,
  "all_six_actual_process_origins_qualified": true,
  "scores_or_checkpoint_metadata_fabricated": false,
  "later_worse_score_overwrite_or_quality_result_claimed": false,
  "fresh_personal_review_claimed": false
}
```

All empty full resumes make zero updates. Metric mismatch and a different output directory retain fresh best-history state. Weights-only initialization starts at zero, loads the genuine producer model and makes exactly one new update without inheriting old best history. The common producer made two updates, so the entire gate made three. Original source/data/regions/recipe and state/hash controls are fixed; there is no AMP/GPU result transfer or model-quality claim.

Original flat control and published 2D ink/reviewed annotations are historically exposed control data, not an independent held-out quality dataset or 3D ink truth. Actual archived diagnostics, not a live terminal. Raw result SHA256: `3f9ab583c3eee9aede190ac2a5d99d2b2da25e331b298d7a73e970ece714830b`.
