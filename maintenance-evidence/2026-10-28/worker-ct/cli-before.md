# PR2329 / Before: invalid worker count fails after output creation

**Archived PBS25068983,S3 real CT control.** Saved actual CLI output,not a new terminal session.

CLI arguments through a source-verified runpy launcher:

```text
<case>/ct.zarr/0 <case>/mask.zarr --task threshold --threshold 127 --num-workers -1 --num-levels 1 --level 0
```

Selected tool output,retaining archive order:

```text
ValueError: Number of processes must be at least 1
Using -1 worker processes
Input array shape: (48, 64, 80)
Input array chunks: (16, 16, 16)
Input array dtype: uint8
Task: threshold | value=127.0 | erase_blank=False
Total items to process: 60
```

**Frozen checks:** Exit1. Input unchanged: true. Partial output created: true;all output voxels remain zero. The process pool rejects -1 after prepare.

Owned scratch paths are shown as `<case>`;traceback frames,progress redraws and other lines are omitted. Buffered stderr/stdout can place the original error before its earlier status messages. The successful log also contains a resource_tracker cleanup warning.

Source log:`cli-s3-original-negative.log`  
SHA256:`e8a646e8485a4f0dc4ca6de12680921406fabf995c4c8df12d8ef572154ada2e`

[All eight records,source/input hashes and scope](selected-records.json). Zero/default host-worker expansion was not run. No human incident,training,model-quality or acceptance claim. MetaCentrum/e-INFRA CZ(ID:90254).
