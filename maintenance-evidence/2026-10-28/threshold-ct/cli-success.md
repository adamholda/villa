# PR2327 / After: separate mask output completes exactly

**Archived PBS25069058,S3 real CT control.** Actual saved full-CLI output,not a new terminal session.

CLI arguments through a source-verified runpy launcher:

```text
<case>/input.zarr/0 <case>/mask.zarr --task threshold --threshold 127 --num-levels 1 --num-workers 1 --level 0
```

Selected tool output:

```text
Using 1 worker processes
Input array shape: (48, 64, 80)
Input array chunks: (16, 16, 16)
Input array dtype: uint8
Task: threshold | value=127.0 | erase_blank=False
Total items to process: 60
Thresholding complete. OME-Zarr pyramid saved to: <case>/mask.zarr
```

**Frozen checks:** Exit0. Input unchanged:true. Every output value equals uint8 where(original_CT>127,255,0).

Owned scratch paths use `<case>`;progress redraws/other lines are omitted. Successful logs also contain a resource_tracker cleanup warning. Original loss was on owned disposable copies;native CT stayed unchanged.

Source log:`cli-s3-repaired-separate_output.log`  
SHA256:`36d0edb282313e75f388dc595cace0c18c4a6fcadd7170b1110aa3c85c8c78d6`

[All12 outcomes,input/source/log hashes and scope](selected-records.json). The earlier pre-CT driver failure is preserved;this authorized successor changed only two checkout paths. No user incident,physical-frame,training or quality claim. MetaCentrum/e-INFRA CZ(ID:90254).
