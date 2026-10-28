# PR2302 / After: overlapping output rejected safely

**Archived PBS24944947, S3 real CT control.** This is saved tool output, not a new terminal execution.

**Scenario:** Output equals first disposable input.

```text
Error: merge output overlaps an input; use a separate output directory: '<case>/inputs/a.zarr' and '<case>/inputs/a.zarr'
```

**Frozen result checks:** Recorded exit: 1 (intended rejection). Full tree unchanged: true. Overwrite prompt: false. Both input markers retained.

Owned scratch prefix is replaced by `<case>`; progress redraws/other lines are omitted. Both exit0 logs also contain a resource_tracker cleanup warning.

Source log: `cli-s3-patched-equal_first.log`  
SHA256: `84a30984734c0e64a4ee7e2e42c40351b0e4c0b7d5bfd144c4de13ed458ae2ba`

[Full selected records and exact hashes](cli-records.json). Controlled disposable stores, not a user incident or model-quality result. PR2244 / stantheman0128 is common to both arms. MetaCentrum / e-INFRA CZ (ID:90254).
