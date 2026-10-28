# PR2327 / After: overlapping output rejects before writes

**Archived PBS25069058,S3 real CT control.** Actual saved full-CLI output,not a new terminal session.

CLI arguments through a source-verified runpy launcher:

```text
<case>/input.zarr/0 <case>/input.zarr --task threshold --threshold 127 --num-levels 1 --num-workers 1 --level 0
```

Selected tool output:

```text
Error: threshold output overlaps its input; use a separate output directory
```

**Frozen checks:** Nonzero exit (intended rejection). Entire owned tree unchanged:true. Overwrite prompt:false.

Owned scratch paths use `<case>`;progress redraws/other lines are omitted. Successful logs also contain a resource_tracker cleanup warning. Original loss was on owned disposable copies;native CT stayed unchanged.

Source log:`cli-s3-repaired-selected_array_parent.log`  
SHA256:`ba8ed2031c82b85fbbe8f942dd6f1f475923107260aede9f734ee0223fd4e54a`

[All12 outcomes,input/source/log hashes and scope](selected-records.json). The earlier pre-CT driver failure is preserved;this authorized successor changed only two checkout paths. No user incident,physical-frame,training or quality claim. MetaCentrum/e-INFRA CZ(ID:90254).
