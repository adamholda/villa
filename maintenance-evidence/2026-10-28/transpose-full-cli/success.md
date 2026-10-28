# PR2326 / Supported separate-output transpose stays exact

Actual archived0123/PBS25071129 CLI output on a disposable fixed S5 CT copy. This is not a live terminal or CT pixel image. The paired S3 records are also linked.

Entry point and recorded CLI arguments (the driver uses a source-verifying runpy wrapper):

```sh
python -m vesuvius.image_proc.run.zarr_tasks input.zarr/0 output.zarr --task transpose --transpose-order xzy --num-levels 1 --num-workers 1 --level 0
```

Exit code:0;overwrite prompt:False. Every output voxel matches independent transpose(2,0,1);shape[80, 48, 64];input tree unchanged. These counts are actual verification records,not extra text printed by the CLI.

### Actual archived CLI stdout/stderr

```text
Using 1 worker processes
Input array shape: (48, 64, 80)
Input array chunks: (16, 16, 16)
Input array dtype: uint8
Task: transpose | order=xzy | perm=[2, 0, 1]
Output array shape: (80, 48, 64)
Output array chunks: (16, 16, 16)
Total items to process: 60

transpose:   0%|          | 0/60 [00:00<?, ?it/s]
transpose:   2%|▏         | 1/60 [00:02<02:53,  2.94s/it]
transpose:  42%|████▏     | 25/60 [00:03<00:03, 11.42it/s]
transpose:  80%|████████  | 48/60 [00:03<00:00, 24.85it/s]
transpose: 100%|██████████| 60/60 [00:03<00:00, 18.67it/s]
Transpose complete. OME-Zarr pyramid saved to: output.zarr
/storage/praha1/home/holdaa/vesuvius-first-letters-pilot-20261022/fiber/python/cpython-3.14.0-linux-x86_64-gnu/lib/python3.14/multiprocessing/resource_tracker.py:297: UserWarning: resource_tracker: There appear to be 1 leaked semaphore objects to clean up at shutdown: {'/mp-lciaq6fb'}
  warnings.warn(
```

[Exact CLI log](cli-success.log) SHA256:`5f52284f517e9b8d96e67552747b57779ceed0baf1928ed5f9e1bae652234aef`. [All8 records and hashes](selected-records.json).

Constructed format2 headers over real CT. Identity order is the destructive-route case;the valid control uses xzy. Native CT remains unchanged. No physical-frame,race,group-routing,training or quality claim. Cleanup warnings are retained. e-INFRA CZ90254.
