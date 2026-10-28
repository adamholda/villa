# PR2327 / Before: parent output erases its CT input

**Archived PBS25069058,S3 real CT control.** Actual saved full-CLI output,not a new terminal session.

CLI arguments through a source-verified runpy launcher:

```text
<case>/input.zarr/0 <case>/input.zarr --task threshold --threshold 127 --num-levels 1 --num-workers 1 --level 0
```

Selected tool output:

```text
Output path <case>/input.zarr already exists. Overwrite? (y/n): Using 1 worker processes
Input array shape: (48, 64, 80)
Input array chunks: (16, 16, 16)
Input array dtype: uint8
Task: threshold | value=127.0 | erase_blank=False
Total items to process: 60
Thresholding complete. OME-Zarr pyramid saved to: <case>/input.zarr
```

**Frozen checks:** Exit0 after overwrite consent. Input unchanged: false. Original nonzero input voxels:245,760;afterward:0.

Owned scratch paths use `<case>`;progress redraws/other lines are omitted. Successful logs also contain a resource_tracker cleanup warning. Original loss was on owned disposable copies;native CT stayed unchanged.

Source log:`cli-s3-original-selected_array_parent.log`  
SHA256:`282f7e25e74b5425c2a2b2922773ccf8b7885625d7b7e7029fae02c9af5fded7`

[All12 outcomes,input/source/log hashes and scope](selected-records.json). The earlier pre-CT driver failure is preserved;this authorized successor changed only two checkout paths. No user incident,physical-frame,training or quality claim. MetaCentrum/e-INFRA CZ(ID:90254).
