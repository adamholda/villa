# PR2306 — actual repaired workflow

Selected actual archived diagnostic fields;these are not a new live terminal session or CT-pixel image. Full raw results stay private. No values below are supplied test scores.

Selected verbatim archived CLI/traceback lines:

> Using step learning rate scheduler over 1 epochs
> Using scheduler : StepLR (per-iteration: False)
> Training Finished!

```json
{
  "actual_CLI_exit": 0,
  "actual_scheduler": "StepLR",
  "actual_step_size": 1,
  "actual_optimizer_updates": 1,
  "actual_training_and_validation_forwards": 2,
  "actual_saved_epoch": 0,
  "actual_saved_normalization": "minmax",
  "actual_saved_EMA_counter": 1,
  "actual_checkpoint_sha256": "b27a7d836ac714e6907da8a4f6814ce3d6a95a9a5ae9e2922f2919f5f5b80b5b"
}
```

Actual archived diagnostic fields from a complete repository CLI on the fixed exposed S5 CT control. Return-preserving instrumentation is disclosed. Repeated operations on ONE CT/annotation pair;not independent samples, model quality or a new personal review. Raw CT, masks, weights and predictions remain private. The actual explicit CLI StepLR default is tested here. Earlier 0159 used the default poly scheduler; its source-only 0161 StepLR prediction is not this measured error. Other polynomial/warmup boundaries remain historical CPU tests.
