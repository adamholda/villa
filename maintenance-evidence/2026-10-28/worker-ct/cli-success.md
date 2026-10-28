# PR2329 / After: one-worker CT threshold completes exactly

**Archived PBS25068983,S3 real CT control.** Saved actual CLI output,not a new terminal session.

CLI arguments through a source-verified runpy launcher:

```text
<case>/ct.zarr/0 <case>/mask.zarr --task threshold --threshold 127 --num-workers 1 --num-levels 1 --level 0
```

Selected tool output,retaining archive order:

```text
Using 1 worker processes
Input array shape: (48, 64, 80)
Input array chunks: (16, 16, 16)
Input array dtype: uint8
Task: threshold | value=127.0 | erase_blank=False
Total items to process: 60
Thresholding complete. OME-Zarr pyramid saved to: <case>/mask.zarr
```

**Frozen checks:** Exit0. Input unchanged: true. Every output value equals uint8 where(original_CT>127,255,0).

Owned scratch paths are shown as `<case>`;traceback frames,progress redraws and other lines are omitted. Buffered stderr/stdout can place the original error before its earlier status messages. The successful log also contains a resource_tracker cleanup warning.

Source log:`cli-s3-repaired-positive.log`  
SHA256:`0d9a56feaf94723daefbb2ba6169f7df2b3806b092244c33408c16f023e3dfd4`

[All eight records,source/input hashes and scope](selected-records.json). Zero/default host-worker expansion was not run. No human incident,training,model-quality or acceptance claim. MetaCentrum/e-INFRA CZ(ID:90254).
