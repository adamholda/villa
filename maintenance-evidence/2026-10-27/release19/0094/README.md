# 0094 � Scheduler horizon with gradient accumulation

**ARCHIVED EVIDENCE VIEW � not a new terminal run.**

|Recorded result|Original|Repaired|
|---|---:|---:|
|Methods|9|9|
|Assertion failures|5|0|
|Errors / skips|0 / 0|0 / 0|
|Passing|4|9|

Controlled original assertion: `test_generic_scheduler_accumulation.GenericSchedulerAccumulationTests.test_capped_cosine`.

**Before:** Per-update scheduler horizons can count microbatches without accumulation conversion.

**After:** Use the intended optimizer-update horizon with accumulation and final flush.

**Limits:** Actual scheduler factory/extracted methods,tiny CPU updates;no fulltrainer/AMP/DDP;axiosdevs1495 credited. No extra training,ink-quality,adoption or award result is inferred.

AI-assisted investigation,implementation,test preparation and validation orchestration. Computational resources were provided by the e-INFRA CZ project (ID:90254),supported by the Ministry of Education,Youth and Sports of the Czech Republic. Code/data attribution is separate.

## Provenance and review status

Publication base: `39a8cf3a124bdd5540ee826e1cb30047c8dc8c85`. [Selected records and file hashes](selected-records.json).

[#1495](https://github.com/ScrollPrize/villa/pull/1495) by axiosdevs (existing per-update scheduler horizon); [#2252](https://github.com/ScrollPrize/villa/pull/2252) by campbelltron1 (distinct auxiliary work).

Focused overlap checks are not exhaustive novelty evidence. Author review and real-scroll workflow commentary remain pending. This archived report is not a terminal capture or a new experiment.
