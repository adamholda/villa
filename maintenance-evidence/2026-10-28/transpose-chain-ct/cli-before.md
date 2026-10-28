# PR2328 / Before: xzy input is relabeled without restoring zyx

**Archived 25069083 S3 real-CT workflow.** Actual saved CLI output,not a new terminal session.

Arguments through a source-verified runpy launcher;plan uses the same arguments plus `--dry-run`:

```text
<case>/s3-producer-xzy.zarr <case>/s3-original-producer_xzy_to_zyx.zarr --task transpose --transpose-order zyx --num-levels 1 --num-workers 1 --level 0
```

Actual plan:

```text
task       transpose
input      <case>/s3-producer-xzy.zarr (level 0)
           shape (80, 48, 64), chunks (16, 16, 16), uint8, 60 chunks, 0.2 MB uncompressed
output     <case>/s3-original-producer_xzy_to_zyx.zarr
           level 0 shape (80, 48, 64), uint8, 0.2 MB uncompressed, 1 levels
workers    1, about 60 chunks each
Dry run: nothing was written.
```

Actual execution excerpt:

```text
Using 1 worker processes
Input array shape: (80, 48, 64)
Input array chunks: (16, 16, 16)
Input array dtype: uint8
Task: transpose | order=zyx | perm=[0, 1, 2]
Output array shape: (80, 48, 64)
Output array chunks: (16, 16, 16)
Transpose complete. OME-Zarr pyramid saved to: <case>/s3-original-producer_xzy_to_zyx.zarr
```

**Frozen checks:** Both commands exit0. Plan matches written shape:(80, 48, 64). Named-axis contract:False. Expected shape:(48, 64, 80). Input unchanged:true. Dry run writes nothing. Output is exactly the producer's preoriented values,not the original zyx crop.

Owned scratch paths use `<case>`;progress redraws/other lines are omitted. Successful logs also retain resource_tracker cleanup warnings. Actual common CLI produced the xzy input;no hand-edited producer header. Native inputs stayed unchanged.

Logs:`cli-s3-original-producer_xzy_to_zyx-plan.log` / `cli-s3-original-producer_xzy_to_zyx-run.log`. SHA256s:`d974aa80b42077c705c30a75423c47b6fda170a7f473232b451486015d513a6b` / `aa6119b232f7b572c123373ab823ba9b06b07d46db242b476ea75058e4d0e3e8`.

[All18 calls,source/input/log hashes and scope](selected-records.json). Canonical headers were tool-generated over real CT,not native physical-frame/registration evidence. Common2295 routing/pitch/planning/default work is ChaseHendrick's. No training/quality/user-incident claim. MetaCentrum/e-INFRA CZ90254.
