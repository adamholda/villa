# Repaired: declared axis reaches real inference

Actual trained Reader inference on a fixed PHerc0841CTsurface crop.

The same layers and released Reader checkpoint produce the expected8x80.

Public excerpt: private paths, account/host identifiers, per-job IDs and precise timestamps are omitted. Numeric fields are copied unchanged from the actual recorded comparison. No CT pixels, weights or prediction images.

## Actual CLI message fields

```text
Selected source layer indices=[5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21]
Input level=0 shape=(depth=28, height=8, width=80) chunks=(8, 80) patch=128 stride=128 requested_overlap=0.500 blend_mode=constant tta_mirror=False
Selected 1 patches for inference
```

## Actual output fields (pretty-printed)

```json
{
  "name": "repaired-narrow-zyx",
  "returncode": 0,
  "shape": [
    8,
    80
  ],
  "dtype": "uint8",
  "decoded_sha256": "0ef35266d9a52ecedea9515031a80160919d0a3827bdccddc2d93ed35dd27bca"
}
```

[All selected records](selected-fields.json). Full raw records remain private. This is archived output,not a new live terminal or a model-quality result.
