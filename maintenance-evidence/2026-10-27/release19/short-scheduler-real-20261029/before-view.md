# PR2306 — actual original behavior

Selected actual archived diagnostic fields;these are not a new live terminal session or CT-pixel image. Full raw results stay private. No values below are supplied test scores.

Selected verbatim archived CLI/traceback lines:

> Using step learning rate scheduler over 1 epochs
> Using scheduler : StepLR (per-iteration: False)
> ZeroDivisionError: division by zero

```json
{
  "actual_CLI_exit": 1,
  "actual_scheduler": "StepLR",
  "actual_step_size": 0,
  "actual_model_parameters": 142243708,
  "actual_train_loss": 0.8063495755195618,
  "actual_optimizer_updates": 1,
  "actual_model_forwards": 1,
  "actual_error": "ZeroDivisionError('division by zero')"
}
```

Actual archived diagnostic fields from a complete repository CLI on the fixed exposed S5 CT control. Return-preserving instrumentation is disclosed. Repeated operations on ONE CT/annotation pair;not independent samples, model quality or a new personal review. Raw CT, masks, weights and predictions remain private. The actual explicit CLI StepLR default is tested here. Earlier 0159 used the default poly scheduler; its source-only 0161 StepLR prediction is not this measured error. Other polynomial/warmup boundaries remain historical CPU tests.
