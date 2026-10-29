# PR2306 — actual controls and boundaries

Selected actual archived diagnostic fields;these are not a new live terminal session or CT-pixel image. Full raw results stay private. No values below are supplied test scores.

```json
{
  "actual_supported_CLI_flag": "--scheduler step",
  "fixed_whole_CT_shape": [256, 256, 256],
  "fixed_train_patch": [128, 128, 128],
  "fixed8_reader_references_exact": true,
  "only_public_lr_schedulers_source_differs": true,
  "repaired_source_Git_blob": "547e5fbd2bc6abf2bc7f8a259b023fd8ad38c89b",
  "one_update_guard_per_arm": 1,
  "original_whole_trees_preserved": true,
  "post_horizon_polynomial_or_quality_proof": false
}
```

Actual archived diagnostic fields from a complete repository CLI on the fixed exposed S5 CT control. Return-preserving instrumentation is disclosed. Repeated operations on ONE CT/annotation pair;not independent samples, model quality or a new personal review. Raw CT, masks, weights and predictions remain private. The actual explicit CLI StepLR default is tested here. Earlier 0159 used the default poly scheduler; its source-only 0161 StepLR prediction is not this measured error. Other polynomial/warmup boundaries remain historical CPU tests.
