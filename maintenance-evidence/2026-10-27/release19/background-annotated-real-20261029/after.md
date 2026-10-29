# PR2307: repaired CLI and dataset retain all requested background regions

Same fixed CT and authentic annotations, actual module CLI with the three-file PR repair. The new background-aware cache and dataset both contain all4 expected regions; exact CT/annotation/padding checks pass.

## Verbatim selected CLI output

```text
BLOSC_NTHREADS not set; defaulting to 1 for patch-cache stability.
Detected 2D patch size (256, 256), setting 2D operations
Found 2 valid patches in 'control'
Found 4 BG-only patches in 'control'
Total valid patches found across all 1 volumes: 2
Total BG-only patches found: 4
Patch cache generation complete: 1 cache(s) written, 1 volumes scanned, 0 skipped.
Patches found: 2 FG, 4 BG, 0 unlabeled FG.
```

## Actual diagnostic record, pretty-printed

```json
{
  "case": "enabled_after_foreground_cache",
  "arm": "repaired",
  "contract_matches": true,
  "actual_CLI_exit": 0,
  "written_caches": 1,
  "scanned_volumes": 1,
  "skipped_volumes": 0,
  "foreground_patches": 2,
  "background_requested": true,
  "expected_background_patches": 4,
  "cached_background_patches": 4,
  "dataset_background_patches": 4,
  "all_returned_CT_annotation_padding_exact": true,
  "reuse_cache_bytes_preserved": null
}
```

One fixed real CT plane with original published ink/reviewed annotations. No raw pixels or arrays. Archived-output browser capture, not a new live terminal or human training session. The missing-cache rejection is a library error. No model, training, quality or new personal-review claim.
