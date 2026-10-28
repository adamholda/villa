# PR2329 / After: invalid worker count rejects before any write

**Archived PBS25068983,S3 real CT control.** Saved actual CLI output,not a new terminal session.

CLI arguments through a source-verified runpy launcher:

```text
<case>/ct.zarr/0 <case>/mask.zarr --task threshold --threshold 127 --num-workers -1 --num-levels 1 --level 0
```

Selected tool output,retaining archive order:

```text
usage: zarr_tasks [-h] [--task TASK] [-n NUM_WORKERS] [--inplace]
zarr_tasks: error: argument -n/--num-workers: number of workers must be positive
```

**Frozen checks:** Exit2 (argument rejection). Entire owned tree unchanged: true. No output created.

Owned scratch paths are shown as `<case>`;traceback frames,progress redraws and other lines are omitted. Buffered stderr/stdout can place the original error before its earlier status messages. The successful log also contains a resource_tracker cleanup warning.

Source log:`cli-s3-repaired-negative.log`  
SHA256:`5ee4e5d83531ae2e437a64c5c9accfe7dc324c124b8df68f114dcce10858e397`

[All eight records,source/input hashes and scope](selected-records.json). Zero/default host-worker expansion was not run. No human incident,training,model-quality or acceptance claim. MetaCentrum/e-INFRA CZ(ID:90254).
