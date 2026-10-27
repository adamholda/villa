# 0052 — Native confusion per-sample count rows

**ARCHIVED EVIDENCE VIEW — not a new terminal run.**

|Recorded result|Original|Repaired|
|---|---:|---:|
|Methods|11|11|
|Assertion failures|4|0|
|Errors / skips|0 / 0|0 / 0|
|Passing|7|11|

Controlled original assertion: `test_confusion_sample_rows.ConfusionSampleRowsTests.test_all_ignored_sample_retains_zero_row_until_trim`.

**Before:** A whole-local-batch count row does not align with Accelerate dataset-sample trimming.

**After:** Gather int64 count rows per input sample,retain ignored zero rows,then sum after trimming.

**Limits:** Real CPU counts and pinned gather with supplied collective/state;no actualDDP/training. No extra training,ink-quality,adoption or award result is inferred.

AI-assisted investigation,implementation,test preparation and validation orchestration. Computational resources were provided by the e-INFRA CZ project (ID:90254),supported by the Ministry of Education,Youth and Sports of the Czech Republic. Code/data attribution is separate.

## Provenance and review status

Publication base: `39a8cf3a124bdd5540ee826e1cb30047c8dc8c85`. [Selected records and file hashes](selected-records.json).

[#1927](https://github.com/ScrollPrize/villa/pull/1927) by AndreasHad04 (existing MPS/dtype behavior, retained); [#2126](https://github.com/ScrollPrize/villa/pull/2126) by AndreasHad04 (separate held-out isolation proposal); [#2118](https://github.com/ScrollPrize/villa/pull/2118) by bruniss (native training groundwork).

Focused overlap checks are not exhaustive novelty evidence. Author review and real-scroll workflow commentary remain pending. This archived report is not a terminal capture or a new experiment.
