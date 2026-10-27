# Standalone transpose guard: actual bounded CT comparison

Protocol0114 / PBS25055499. **No common coordinate/routing patch.** Current-main non-fiber dependency files are verified; unused changed fiber packages are omitted. This is not a full-repository/current-installer test.

|Result|Original|Repaired|
|---|---:|---:|
|Standalone methods|8|8|
|Assertion failures|4|0|
|Passing|4|8|
|Errors/skips|0/0|0/0|

All24 CT-backed records pass:8 original prepare-only hazards,8 repaired full-CLI rejections and8 valid full-CLI controls. Six destructive prepare records erase245760 nonzero voxels in disposable copies;two nested cases only add a subtree. Native inputs remain unchanged. These repeat two CT inputs,not independent incidents.

## Before: direct prepare accepts an overlapping path

Recorded prepare_only_not_CLI output (scratch paths/progress redraws redacted):

```text
Input array shape: (48, 64, 80)
Input array chunks: (16, 16, 16)
Input array dtype: uint8
Task: transpose | order=xzy | perm=[2, 0, 1]
Output array shape: (80, 48, 64)
Output array chunks: (16, 16, 16)
```

## After: full CLI rejects overlap before prompting

Recorded full_CLI output (scratch paths/progress redraws redacted):

```text
Error: transpose output overlaps its input; use a separate output directory
```

## After: valid selected-array CLI still completes

Recorded full_CLI output (scratch paths/progress redraws redacted):

```text
Input array shape: (48, 64, 80)
Input array chunks: (16, 16, 16)
Input array dtype: uint8
Task: transpose | order=xzy | perm=[2, 0, 1]
Output array shape: (80, 48, 64)
Output array chunks: (16, 16, 16)
Total items to process: 60
Transpose complete. OME-Zarr pyramid saved to: <case>/output.zarr
```

[Primary log hashes, all case records and source hashes](standalone-records.json). Valid controls prove exact one-level transposed values/dtypes/shapes and input preservation. Metadata agreement preserves current behavior;physical frames,group-worker routing,higher pyramids,URI stores,races and training/quality/adoption are outside scope. Old0045/0069 results remain historical. This is one existing repair packet,not a new contribution count.

AI-assisted investigation,implementation,test preparation and orchestration. Computational resources were provided by the e-INFRA CZ project (ID:90254),supported by the Ministry of Education,Youth and Sports of the Czech Republic. Code and CT data attribution remain separate.
