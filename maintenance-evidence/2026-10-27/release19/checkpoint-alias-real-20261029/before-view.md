# PR2337 — actual original behavior

Selected actual archived diagnostic fields;these are not a new live terminal session or CT-pixel image. Full raw results stay private. No values below are supplied test scores.

Selected verbatim archived CLI/traceback lines:

> Found normalization scheme in checkpoint: minmax
> An error occurred during inference: Error initializing Volume: Invalid normalization_scheme: 'minmax'. Must be one of ['none', 'instance_zscore', 'global_zscore', 'instance_minmax', 'percentile_minmax', 'ct']

```json
{
  "actual_prediction_CLI_exit": 1,
  "actual_dataset_normalization_request": [
    "minmax"
  ],
  "actual_model_forwards": 0,
  "verbatim_error_fragment": "Invalid normalization_scheme: 'minmax'.",
  "authentic_checkpoint_metadata_edited": false
}
```

Actual archived diagnostic fields from a complete repository CLI on the fixed exposed S5 CT control. Return-preserving instrumentation is disclosed. Repeated operations on ONE CT/annotation pair;not independent samples, model quality or a new personal review. Raw CT, masks, weights and predictions remain private. The checkpoint was genuinely produced by the actual short configured generic training workflow;its normalization/EMA metadata is unedited. This is the minmax alias only,not full nnU-Net/global-statistics/all-normalizers/quality proof. The separate released z-score guide is not a paired PR2337 z-score control.
