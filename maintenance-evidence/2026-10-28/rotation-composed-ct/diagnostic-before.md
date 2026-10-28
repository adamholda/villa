# PR2334 / Original ignores the requested z/none orientation

Actual archived0124/PBS25080112diagnostics on the whole fixed S5CT/released binary fiber-mask pair. Full composed dataset pipeline remains enabled;spatial parameter observers return original values. Not a trainer/model or raw human training-CLI session.

## z / actual seed0record

Selected actual JSON fields,pretty-printed for readability;the full verbatim stdout stream is linked below.

```json
{
  "arm": "original",
  "mode": "z",
  "seed": 0,
  "factory_signature": [
    [
      "Rot90Transform",
      [
        0,
        1,
        2
      ]
    ],
    [
      "TransposeAxesTransform",
      [
        0,
        1,
        2
      ]
    ]
  ],
  "factory_contract_matches": false,
  "complete_composed_pipeline_kept_enabled": true,
  "orientation_calls_moving_or_flipping_depth": 1,
  "image_shape": [
    1,
    256,
    256,
    256
  ],
  "image_finite": true,
  "mask_and_padding_equal_independent_reference": true,
  "mask_nonzero_voxels_preserved": true
}
```

## none / actual seed0record

Selected actual JSON fields,pretty-printed for readability;the full verbatim stdout stream is linked below.

```json
{
  "arm": "original",
  "mode": "none",
  "seed": 0,
  "factory_signature": [
    [
      "Rot90Transform",
      [
        0,
        1,
        2
      ]
    ],
    [
      "TransposeAxesTransform",
      [
        0,
        1,
        2
      ]
    ]
  ],
  "factory_contract_matches": false,
  "complete_composed_pipeline_kept_enabled": true,
  "orientation_calls_moving_or_flipping_depth": 1,
  "image_shape": [
    1,
    256,
    256,
    256
  ],
  "image_finite": true,
  "mask_and_padding_equal_independent_reference": true,
  "mask_nonzero_voxels_preserved": true
}
```

All12complete item reads match independent mask/padding compositions and preserve301079released foreground voxels. One pair/repeated seeds,not12independent samples or unit methods. Native/constructed trees unchanged;no training,quality,ink or biological interpretation claim.

[Verbatim selected actual stdout](original-actual-diagnostics.txt). Raw original.log SHA256:`b65d27ff5c678e914a4739b09e00be49968b39a80c1fae179325dda4ced6132f`. [All records](selected-records.json). Final71s x1CPU/0GPU;MetaCentrum/e-INFRA CZ90254. Labels are released binary fibers,not ink or newly reviewed negatives.
