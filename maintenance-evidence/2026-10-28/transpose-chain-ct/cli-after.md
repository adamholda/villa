# PR2328 / After: plan and CLI restore the exact CT zyx array

**Archived 25069083 S3 real-CT workflow.** Actual saved CLI output,not a new terminal session.

Arguments through a source-verified runpy launcher;plan uses the same arguments plus `--dry-run`:

```text
<case>/s3-producer-xzy.zarr <case>/s3-repaired-producer_xzy_to_zyx.zarr --task transpose --transpose-order zyx --num-levels 1 --num-workers 1 --level 0
```

Actual plan:

```text
task       transpose
input      <case>/s3-producer-xzy.zarr (level 0)
           shape (80, 48, 64), chunks (16, 16, 16), uint8, 60 chunks, 0.2 MB uncompressed
output     <case>/s3-repaired-producer_xzy_to_zyx.zarr
           level 0 shape (48, 64, 80), uint8, 0.2 MB uncompressed, 1 levels
workers    1, about 60 chunks each
Dry run: nothing was written.
```

Actual execution excerpt:

```text
Using 1 worker processes
Input array shape: (80, 48, 64)
Input array chunks: (16, 16, 16)
Input array dtype: uint8
Task: transpose | order=zyx | perm=[1, 2, 0]
Output array shape: (48, 64, 80)
Output array chunks: (16, 16, 16)
Transpose complete. OME-Zarr pyramid saved to: <case>/s3-repaired-producer_xzy_to_zyx.zarr
```

**Frozen checks:** Both commands exit0. Plan matches written shape:(48, 64, 80). Named-axis contract:True. Expected shape:(48, 64, 80). Input unchanged:true. Dry run writes nothing. Every output voxel equals the independent array-permutation reference.

Owned scratch paths use `<case>`;progress redraws/other lines are omitted. Successful logs also retain resource_tracker cleanup warnings. Actual common CLI produced the xzy input;no hand-edited producer header. Native inputs stayed unchanged.

Logs:`cli-s3-repaired-producer_xzy_to_zyx-plan.log` / `cli-s3-repaired-producer_xzy_to_zyx-run.log`. SHA256s:`dbe37441edbbf92db231d2cc67e24c63225722f27b092dea2fa7fbc514066610` / `93f41f12c36b9a6cf9ab6e8c213ca88859db6467ce6e8d6e4df538eb2511d7c6`.

[All18 calls,source/input/log hashes and scope](selected-records.json). Canonical headers were tool-generated over real CT,not native physical-frame/registration evidence. Common2295 routing/pitch/planning/default work is ChaseHendrick's. No training/quality/user-incident claim. MetaCentrum/e-INFRA CZ90254.
