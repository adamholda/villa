# PR2304 — actual original counter and EMA mismatches

Selected actual archived diagnostics;not a new live terminal or CT-pixel image.

```json
{
  "all_native_CLI_exit_codes": [
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0
  ],
  "actual_successful_optimizer_updates": 1,
  "actual_scheduler_calls": 2,
  "reported_optimizer_step": 2,
  "GradScaler_scale_before": 65536.0,
  "GradScaler_scale_after": 32768.0,
  "saved_noEMA_optimizer_step": null,
  "full_resume_start_and_update_count": [
    4,
    0
  ],
  "weights_only_start_and_update_count": [
    0,
    0
  ],
  "weights_only_EMA_equals_loaded_main": false
}
```

Verbatim archived native CLI line (controlled overflow):

```text
  0%|          | 0/4 [00:08<?, ?it/s, loss=0.5695, lr=1.00e-04]AMP gradient overflow at step 1: network.shared_encoder.stem.convs.0.conv.weight
```

Nine actual complete native CLI contexts on ONE exposed PHerc0841 control and original released 2D ink/reviewed masks transported on plane14. The overflow/resume arms load the released trained Reader;the paired FP32 EMA controls use their predeclared fresh-He initialization. Return-preserving state/step observers are disclosed. Each overflow arm deliberately changes ONE real gradient element to +inf before the real GradScaler unscale;this is a controlled fault,not a naturally observed incident. All9native CLI processes exit0:the original error is silent counter/EMA behavior,not a fabricated exception. Three fixed validation regions have no positive ink;this is engineering correctness,not ink quality,independent samples,native3D ink labels or registration truth. The extra2305history composition is a separately identified zero-update control,not another fix or contribution. The shared job exited1 because its separate generic group failed;native2304qualifies independently and no generic success is claimed. Raw CT,masks,weights,predictions and produced checkpoints stay private. This supplement does not imply a new personal review.
