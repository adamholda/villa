# Real packed CT: producer and controls

Selected actual archived fields; formatted JSON, not a live terminal or full training CLI. Private paths, accounts/hosts, per-job IDs and precise timestamps are omitted. Numerical fields are unchanged. One fixed S5 CT/released binary fiber pair; two correlated128cube crops.

Actual producer message portions below; timestamp prefixes and private path lines are omitted.

```text
Found 2 samples
Sample shape: (128, 128, 128) (3D)
Grid layout: (2, 2, 2)
Cell size: (160, 160, 160)
Volume shape: (320, 320, 320)
Data type: uint8
  Level 0: shape=(320, 320, 320), chunks=(32, 32, 32)
  Level 0: shape=(320, 320, 320), chunks=(32, 32, 32)
Writing 2 samples with 1 workers...
Conversion complete!
  Resolution levels: 1
  Splits: 0 train, 0 val, 2 unassigned
  Labels: All 2 samples have labels
```

Actual consumer controls (maximum absolute image difference):

|Contract|Original|Repaired|
|---|---:|---:|
|Z-score fitting128cube|0.0|0.0|
|Identity overlapping neighbor|0.0|0.0|

All image/mask/padding references and final native/packed/TIFF trees match. Actual producer imports and both consumer-process module/library origins qualified. One common producer CLI plus six library records; no model, trainer, quality, ink or biological interpretation.
