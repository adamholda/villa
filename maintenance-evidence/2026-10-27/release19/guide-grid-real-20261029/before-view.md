# PR2344 — actual original behavior

Selected actual archived diagnostic fields;these are not a new live terminal session or CT-pixel image. Full raw results stay private. No values below are supplied test scores.

Verbatim archived parser-error fragments (private file arguments omitted):

> unrecognized arguments: --config-yaml
> unrecognized arguments: --intensity-properties-json

```json
{
  "actual_parser_rejections": [
    {
      "actual_command": "01-original-advertised-flag",
      "actual_exit": 2,
      "expected_exit": 2
    },
    {
      "actual_command": "03-old-public-intensity-option",
      "actual_exit": 2,
      "expected_exit": 2
    },
    {
      "actual_command": "06-old-frame-parser",
      "actual_exit": 2,
      "expected_exit": 2
    }
  ],
  "original_help_default": "rotation",
  "corrected_help_default": "mirroring",
  "original_unsupported_flag": "--config-yaml",
  "additional_public_row_unsupported_flag": "--intensity-properties-json",
  "old_unsupported_frame_choice": "surface_frame",
  "each_rejection_writes_no_output": true
}
```

Actual archived diagnostic fields from a complete repository CLI on the fixed exposed S5 CT control. Actual unmodified module CLI execution with exit/origin/output checks. Repeated operations on ONE CT/annotation pair;not independent samples, model quality or a new personal review. Raw CT, masks, weights and predictions remain private. The requested box stayed 32:160. Source review proved the full-volume grid selection at 64:192 selection before this successor;the old 0144 incorrect-coordinate-oracle failure is preserved. The one-channel binary output is not text, quality, pyramid, OME or multi-target evidence.
