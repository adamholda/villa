# 0046 � Positive explicit worker argument

**ARCHIVED EVIDENCE VIEW � not a new terminal run.**

|Recorded result|Original|Repaired|
|---|---:|---:|
|Methods|8|8|
|Assertion failures|2|0|
|Errors / skips|0 / 0|0 / 0|
|Passing|6|8|

Controlled original assertion: `test_zarr_worker_positivity.WorkerArgumentTests.test_negative_workers_rejected`.

**Before:** Explicit zero/negative worker counts pass argument parsing.

**After:** Reject explicit nonpositive counts;leave default/quota selection unchanged.

**Limits:** Parser scope;proposal context also separately8/8;selector/default/affinity work excluded. No extra training,ink-quality,adoption or award result is inferred.

AI-assisted investigation,implementation,test preparation and validation orchestration. Computational resources were provided by the e-INFRA CZ project (ID:90254),supported by the Ministry of Education,Youth and Sports of the Czech Republic. Code/data attribution is separate.

## Provenance and review status

Publication base: `39a8cf3a124bdd5540ee826e1cb30047c8dc8c85`. [Selected records and file hashes](selected-records.json).

[#2295](https://github.com/ScrollPrize/villa/pull/2295) by ChaseHendrick (default/quota/selector proposal, excluded from this delta); [#2064](https://github.com/ScrollPrize/villa/pull/2064) (different ink-worker zero behavior, unchanged).

Focused overlap checks are not exhaustive novelty evidence. Author review and real-scroll workflow commentary remain pending. This archived report is not a terminal capture or a new experiment.
