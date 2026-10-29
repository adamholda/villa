# Original: silent wrong output frame

Actual trained Reader inference on a fixed PHerc0841CTsurface crop.

Declared ZYX CT input should produce8x80.The actual command exits0but produces28x8.

Public excerpt: private paths, account/host identifiers, per-job IDs and precise timestamps are omitted. Numeric fields are copied unchanged from the actual recorded comparison. No CT pixels, weights or prediction images.

## Actual CLI message fields

```text
Selected source layer indices=[5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21]
Input level=0 shape=(depth=80, height=28, width=8) chunks=(28, 8) patch=128 stride=128 requested_overlap=0.500 blend_mode=constant tta_mirror=False
Selected 1 patches for inference
```

## Actual output fields (pretty-printed)

```json
{
  "name": "original-narrow",
  "returncode": 0,
  "shape": [
    28,
    8
  ],
  "dtype": "uint8",
  "decoded_sha256": "a041007d3897d92dcc6bd0679d755b8a3b78cd0d44f9316a6c9f8d92e7dc6e1e"
}
```

[All selected records](selected-fields.json). Full raw records remain private. This is archived output,not a new live terminal or a model-quality result.
