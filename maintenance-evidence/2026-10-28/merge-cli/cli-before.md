# PR2302 / Before: input loss despite exit 0

**Archived PBS24944947, S3 real CT control.** This is saved tool output, not a new terminal execution.

**Scenario:** Output equals first disposable input.

```text
Shape: (32, 32, 32)
Chunks: (16, 16, 16)
Dtype: uint8
Merge statistics:
  Empty (both inputs): 0
  Copied from input1: 0
  Copied from input2: 8
  Merged (maximum): 0
Writing OME-Zarr metadata...
Done! Output saved to <case>/inputs/a.zarr
```

**Frozen result checks:** Recorded exit: 0. Input unchanged: false. Lost nonzero input voxels: 8,192. Original input sidecars removed.

Owned scratch prefix is replaced by `<case>`; progress redraws/other lines are omitted. Both exit0 logs also contain a resource_tracker cleanup warning.

Source log: `cli-s3-baseline-equal_first.log`  
SHA256: `20dc047429bf8d7a7470c06254124c15e2a038a32477315959210bc064cd8932`

[Full selected records and exact hashes](cli-records.json). Controlled disposable stores, not a user incident or model-quality result. PR2244 / stantheman0128 is common to both arms. MetaCentrum / e-INFRA CZ (ID:90254).
