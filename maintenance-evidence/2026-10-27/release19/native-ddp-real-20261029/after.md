# PR2331 — Repaired unique-sample counts

Actual archived full native training CLI / two real CPU-Gloo ranks / released Reader and original PHerc0841 flat control. Return-preserving observers;selected actual fields below. Distinct verbatim stdout lines precede pretty-printed JSON where present.

```text
sampling_audit={"patches": 61, "strategy": "uniform"}
Using dimensionality (2D) from ConfigManager
Using 2D convolutions (nn.Conv2d)
Using 2D normalization (nn.InstanceNorm2d)

{
  "actual_training_CLI_exit_code": 0,
  "real_Gloo_ranks": 2,
  "actual_optimizer_updates_per_rank": [1, 1],
  "actual_validation_draws": 4,
  "unique_fixed_validation_samples": 3,
  "actual_gather_input_shape": [2, 4],
  "actual_gather_returned_shape": [3, 4],
  "actual_gather_returned_rows_tp_fp_fn_tn": [
    [0, 0, 0, 14253],
    [0, 0, 0, 16204],
    [0, 0, 0, 16384]
  ],
  "actual_written_counts_tp_fp_fn_tn": [0, 0, 0, 46841],
  "independent_unique_sample_counts": [0, 0, 0, 46841],
  "contract_matches": true,
  "actual_balanced_accuracy": 1.0
}
```

Three fixed validation regions have no positive ink. Balanced accuracy is1.0inBOTHarms;this proves padded count weighting,not an ink-quality improvement. Original2D annotations are a single-plane flat storage carrier,not volumetricinktruth. The historical control was label-selected/exposed,not independentheldoutdata.

Actual archived output,not a new live terminal or CT-pixel image. Raw result SHA256`a3e485531f2a542667c541ee33f6e5cf2e57471a603535114c3474ee64397f81`.
