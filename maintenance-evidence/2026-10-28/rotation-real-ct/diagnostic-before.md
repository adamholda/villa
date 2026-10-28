# PR2334 / Before: configured z and none are ignored

**PARTIAL/INSTRUMENTED actual CT + released fiber-mask workflow.** Archived 0122/PBS25069581. Selected fields from hashed actual JSON/log records, not a full trainer/CLI terminal session or CT pixel image.

Actual ConfigManager/parser -> ZarrDataset constructor/getter -> factory-created quarter-turn/transpose members. Whole fixed S5 cube 256x256x256, no positive-crop search.

|Recorded field|Actual value|
|---|---|
|Setting|z|
|Manager axes|[0]|
|Factory members|Rot90Transform axes[0, 1, 2]; TransposeAxesTransform axes[0, 1, 2]|
|Requested contract matches|False|
|Actual getter CT/mask/padding exact|True|
|Selected-member operations|8|
|Draws moving/flipping depth|5|
|Every output matches independent permutation|True|

The same arm with `none` has 2 quarter-turn/transpose members and 8 selected-member calls; contract match: False.

Selected actual sampled record (first forbidden-depth draw if present, otherwise first fixed-seed member):

```json
{
  "kind": "Rot90Transform",
  "seed": 0,
  "actual_parameters": {
    "num_rot_per_combination": [
      1
    ],
    "axis_combinations": [
      [
        1,
        3
      ]
    ],
    "crop_shape": [
      256,
      256,
      256
    ]
  },
  "joint_values_equal_reference": true,
  "moves_or_flips_depth_axis": true
}
```

Instrumentation disables the composed pipeline only for loading, restores it, and executes selected actual members with an unchanged-parameter observer. Mirrors, intensity/low-resolution, full pipeline, model/training/quality and anatomical-instance interpretation are not demonstrated. Inputs remain unchanged.

Source `original.log` SHA256:`46256106b498d8d1e25c09fdbe0e4c0907d01abb063f3ce1b2de0c403e591a75`. [All 6 records / 40 member observations/source and input hashes](selected-records.json). Binary fiber-mask labels are not ink or reviewed negative truth. MetaCentrum/e-INFRA CZ90254.
