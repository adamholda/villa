# Real packed CT: producer and identity controls

Selected actual archived diagnostic fields,formatted JSON. Private paths,account/host/per-job identifiers and precise timestamps omitted;numeric fields unchanged. Actual library workflow after real packing,not a live terminal or full trainingCLI.

Actual producer message portions;timestamp prefixes/private path lines omitted:

```text
Found 512 samples
Sample shape: (32, 32, 32) (3D)
Grid layout: (8, 8, 8)
Cell size: (32, 32, 32)
Volume shape: (256, 256, 256)
Data type: uint8
  Level 0: shape=(256, 256, 256), chunks=(32, 32, 32)
  Level 0: shape=(256, 256, 256), chunks=(32, 32, 32)
Writing 512 samples with 1 workers...
Conversion complete!
  Resolution levels: 1
  Splits: 0 train, 0 val, 512 unassigned
```

Both arms exactly preserve all512source images,masks,padding and unlabeled statuses. Original and repaired canonical identity digest(sorted by original filename):

```text
67c270e2bc534154eb4e004566317a9838eb3c4f3fd30ca243d9be821aa14ee9
```

Actual train/validation loaders cover all512items without overlap. Full native CT/released TIFF hashes and packed/source-TIFF trees unchanged;actual producer/consumer origins qualified. One pair and correlated tiles,not512independent annotations. No model or training.
