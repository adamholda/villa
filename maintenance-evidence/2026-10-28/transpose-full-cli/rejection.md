# PR2326 / Repair rejects before prompting and preserves the whole tree

Actual archived0123/PBS25071129 CLI output on a disposable fixed S5 CT copy. This is not a live terminal or CT pixel image. The paired S3 records are also linked.

Entry point and recorded CLI arguments (the driver uses a source-verifying runpy wrapper):

```sh
python -m vesuvius.image_proc.run.zarr_tasks input.zarr/0 input.zarr --task transpose --transpose-order zyx --num-levels 1 --num-workers 1 --level 0
```

Exit code:1;overwrite prompt:False. Whole case tree unchanged:True;nonzero input voxels:245760. These counts are actual verification records,not extra text printed by the CLI.

### Actual archived CLI stdout/stderr

```text
Error: transpose output overlaps its input; use a separate output directory
```

[Exact CLI log](cli-rejection.log) SHA256:`5729c3622d5b2acea437431b254ea0d66903846394e7537e36cf1069f6d131d0`. [All8 records and hashes](selected-records.json).

Constructed format2 headers over real CT. Identity order is the destructive-route case;the valid control uses xzy. Native CT remains unchanged. No physical-frame,race,group-routing,training or quality claim. Cleanup warnings are retained. e-INFRA CZ90254.
