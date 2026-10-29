# PR2337 — actual repaired workflow

Selected actual archived diagnostic fields;these are not a new live terminal session or CT-pixel image. Full raw results stay private. No values below are supplied test scores.

Selected verbatim archived CLI/traceback lines:

> Found normalization scheme in checkpoint: minmax
> Inference complete.

```json
{
  "actual_prediction_CLI_exit": 0,
  "actual_dataset_normalization_request": [
    "instance_minmax"
  ],
  "actual_model_forwards": 1,
  "actual_normalized_input_shape": [1, 128, 128, 128],
  "independent_minmax_max_abs": 0.0,
  "actual_logit_shape": [1, 2, 128, 128, 128],
  "actual_logits_finite": true,
  "actual_written_coordinates": [
    [64, 64, 64]
  ]
}
```

Actual archived diagnostic fields from a complete repository CLI on the fixed exposed S5 CT control. Return-preserving instrumentation is disclosed. Repeated operations on ONE CT/annotation pair;not independent samples, model quality or a new personal review. Raw CT, masks, weights and predictions remain private. The checkpoint was genuinely produced by the actual short configured generic training workflow;its normalization/EMA metadata is unedited. This is the minmax alias only,not full nnU-Net/global-statistics/all-normalizers/quality proof. The separate released z-score guide is not a paired PR2337 z-score control.
