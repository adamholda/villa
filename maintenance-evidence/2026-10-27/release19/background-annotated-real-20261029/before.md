# PR2307: original background request reuses foreground-only cache

Actual supported 2D module CLI after a foreground-only cache. Original exits0 and loads0 of4 independently expected background regions. The disabled2-foreground control is unchanged.

## Verbatim selected CLI output

```text
BLOSC_NTHREADS not set; defaulting to 1 for patch-cache stability.
Detected 2D patch size (256, 256), setting 2D operations
Patch cache generation complete: 0 cache(s) written, 0 volumes scanned, 1 skipped.
Patches found: 2 FG, 0 BG, 0 unlabeled FG.
```

## Actual diagnostic record, pretty-printed

```json
{
  "case": "enabled_after_foreground_cache",
  "arm": "original",
  "contract_matches": false,
  "actual_CLI_exit": 0,
  "written_caches": 0,
  "scanned_volumes": 0,
  "skipped_volumes": 1,
  "foreground_patches": 2,
  "background_requested": true,
  "expected_background_patches": 4,
  "cached_background_patches": 0,
  "dataset_background_patches": 0,
  "all_returned_CT_annotation_padding_exact": true,
  "reuse_cache_bytes_preserved": true
}
```

One fixed real CT plane with original published ink/reviewed annotations. No raw pixels or arrays. Archived-output browser capture, not a new live terminal or human training session. The missing-cache rejection is a library error. No model, training, quality or new personal-review claim.
