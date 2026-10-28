# PR2302 / After: supported separate output completes

**Archived PBS24944947, S3 real CT control.** This is saved tool output, not a new terminal execution.

**Scenario:** Separate sibling output; same fixed CT crop.

```text
Shape: (32, 32, 32)
Chunks: (16, 16, 16)
Dtype: uint8
Merge statistics:
  Empty (both inputs): 0
  Copied from input1: 0
  Copied from input2: 4
  Merged (maximum): 4
Writing OME-Zarr metadata...
Copied metadata.json from input1
Done! Output saved to <case>/inputs/a.zarr.merged
```

**Frozen result checks:** Recorded exit: 0. Inputs unchanged: true. Exact output values: true. Replacing the stale separate output is intentional.

Owned scratch prefix is replaced by `<case>`; progress redraws/other lines are omitted. Both exit0 logs also contain a resource_tracker cleanup warning.

Source log: `cli-s3-patched-valid_sibling_prefix.log`  
SHA256: `52a2e02906a655542a445dc213435c9d69e7931aa03206a828d820ba926044f9`

[Full selected records and exact hashes](cli-records.json). Controlled disposable stores, not a user incident or model-quality result. PR2244 / stantheman0128 is common to both arms. MetaCentrum / e-INFRA CZ (ID:90254).
