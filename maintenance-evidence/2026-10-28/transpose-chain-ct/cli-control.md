# PR2328 / Valid control: canonical CT to xzy stays exact

**Archived 25069083 S3 real-CT workflow.** Actual saved CLI output,not a new terminal session.

Arguments through a source-verified runpy launcher;plan uses the same arguments plus `--dry-run`:

```text
<case>/s3-seed.zarr <case>/s3-repaired-canonical_zyx_to_xzy.zarr --task transpose --transpose-order xzy --num-levels 1 --num-workers 1 --level 0
```

Actual plan:

```text
task       transpose
input      <case>/s3-seed.zarr (level 0)
           shape (48, 64, 80), chunks (16, 16, 16), uint8, 60 chunks, 0.2 MB uncompressed
output     <case>/s3-repaired-canonical_zyx_to_xzy.zarr
           level 0 shape (80, 48, 64), uint8, 0.2 MB uncompressed, 1 levels
workers    1, about 60 chunks each
Dry run: nothing was written.
```

Actual execution excerpt:

```text
Using 1 worker processes
Input array shape: (48, 64, 80)
Input array chunks: (16, 16, 16)
Input array dtype: uint8
Task: transpose | order=xzy | perm=[2, 0, 1]
Output array shape: (80, 48, 64)
Output array chunks: (16, 16, 16)
Transpose complete. OME-Zarr pyramid saved to: <case>/s3-repaired-canonical_zyx_to_xzy.zarr
```

**Frozen checks:** Both commands exit0. Plan matches written shape:(80, 48, 64). Named-axis contract:True. Expected shape:(80, 48, 64). Input unchanged:true. Dry run writes nothing. Every output voxel equals the independent array-permutation reference.

Owned scratch paths use `<case>`;progress redraws/other lines are omitted. Successful logs also retain resource_tracker cleanup warnings. Actual common CLI produced the xzy input;no hand-edited producer header. Native inputs stayed unchanged.

Logs:`cli-s3-repaired-canonical_zyx_to_xzy-plan.log` / `cli-s3-repaired-canonical_zyx_to_xzy-run.log`. SHA256s:`315636faec266933505b7269383906cd79c63668f9798827063fb5819062a898` / `4acc78a3c923a179a7adad8fbe78a8f7eaf573645df0e31d2acde19f3a3ad484`.

[All18 calls,source/input/log hashes and scope](selected-records.json). Canonical headers were tool-generated over real CT,not native physical-frame/registration evidence. Common2295 routing/pitch/planning/default work is ChaseHendrick's. No training/quality/user-incident claim. MetaCentrum/e-INFRA CZ90254.
