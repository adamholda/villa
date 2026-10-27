# Zero-range: recorded real-CT CLI behavior

These are direct excerpts of actual archived CLI output from PBS25051344, not a live terminal screenshot. Scratch/interpreter paths and progress-bar redraws are redacted; messages and outcomes are unchanged. Fixed S3/S5 CT values use constructed isotropic format2 headers.

## Before: unsupported separate output silently modifies input

Recorded command (paths redacted):

```text
<python> -m vesuvius.image_proc.run.zarr_tasks <case>/input.zarr <case>/output.zarr --task zero-range --z-start 8 --z-end 15 --num-workers 1
```

Recorded tool output:

```text
Using 1 worker processes
Input array shape: (32, 32, 32)
Input array chunks: (8, 8, 8)
Input array dtype: uint8
Task: zero-range | z=[8, 15] | replace_value=0
  Shape: (32, 32, 32), Chunks: (8, 8, 8)
  Z-range: [8, 15]
  Chunks to process: 16
Zero-range complete: <case>/input.zarr
Filled z-range: [8, 15] with value 0
```

Recorded exit code: **0**. Input tree unchanged: **false**. Output tree unchanged: **true**.

## After: the same unsupported form is rejected before modification

Recorded command (paths redacted):

```text
<python> -m vesuvius.image_proc.run.zarr_tasks <case>/input.zarr <case>/output.zarr --task zero-range --z-start 8 --z-end 15 --num-workers 1
```

Recorded tool output:

```text
Error: zero-range operates in place; omit output_zarr and use --inplace
```

Recorded exit code: **1**. Input tree unchanged: **true**. Output tree unchanged: **true**.

## After: supported explicit in-place form still completes

Recorded command (paths redacted):

```text
<python> -m vesuvius.image_proc.run.zarr_tasks <case>/input.zarr --task zero-range --z-start 8 --z-end 15 --num-workers 1 --inplace
```

Recorded tool output:

```text
Using 1 worker processes
Input array shape: (32, 32, 32)
Input array chunks: (8, 8, 8)
Input array dtype: uint8
Task: zero-range | z=[8, 15] | replace_value=0
  Shape: (32, 32, 32), Chunks: (8, 8, 8)
  Z-range: [8, 15]
  Chunks to process: 16
Zero-range complete: <case>/input.zarr
Filled z-range: [8, 15] with value 0
```

Recorded exit code: **0**. Input tree unchanged: **false**. Output tree unchanged: **true**.

[Source log hashes, exact array checks and all 32 recorded outcomes](cli-excerpts.json). These repeated controlled routes are not independent user incidents. No training, ink quality, native registration or upstream acceptance is claimed. AI assisted implementation and validation orchestration. Computational resources were provided by the e-INFRA CZ project (ID:90254), supported by the Ministry of Education, Youth and Sports of the Czech Republic. CT data rights and Villa code attribution remain separate.
