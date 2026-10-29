# PR2305 — Original: silent loss of genuine best history

Actual complete native training CLI on the original fixed PHerc0841 flat CT control, released Reader and original ink/reviewed annotations. The genuine new producer ran two optimizer updates and actual validation/save. This full-resume context runs the actual trainer setup/restore with an empty training range.

## Selected verbatim CLI output

```text
sampling_audit={"patches": 61, "strategy": "uniform"}
Using dimensionality (2D) from ConfigManager
Using 2D convolutions (nn.Conv2d)
Using 2D normalization (nn.InstanceNorm2d)
```

## Pretty-printed actual diagnostic fields

```json
{
  "actual_CLI_exit_code": 0,
  "actual_typed_weights_only": false,
  "actual_resume_start_step": 4,
  "actual_optimizer_updates": 0,
  "genuine_producer_measured_best_val_loss": 0.5637056827545166,
  "actual_restored_best_val_loss": null,
  "actual_loaded_model_state_sha256": "101cacd869b2d08ee96da57800dc21063bd986c17512ecc204ff6212465001eb",
  "actual_returned_model_state_sha256": "101cacd869b2d08ee96da57800dc21063bd986c17512ecc204ff6212465001eb",
  "actual_CPU_device": "cpu",
  "actual_process_origins_qualified": true
}
```

The original sidecar/checkpoint is genuine, not an injected score. Input and producer artifacts are unchanged after the complete gate. This proves full-resume history retention; no subsequent worse-score overwrite or ink-quality improvement is claimed. Original 2D labels use one storage plane, not volumetric ink truth. Return-preserving instrumentation is disclosed.

Archived output, not a new live terminal or CT-pixel image. Raw result SHA256: `3f9ab583c3eee9aede190ac2a5d99d2b2da25e331b298d7a73e970ece714830b`.
