# 0067 � Coherent cache target/selection/value packet

**ARCHIVED EVIDENCE VIEW � not a new terminal run.**

|Recorded result|Original|Repaired|
|---|---:|---:|
|Methods|22|22|
|Assertion failures|11|0|
|Errors / skips|0 / 0|0 / 0|
|Passing|11|22|

Controlled original assertion: `test_cache_unlabeled_allowlist.UnlabeledAllowlistCacheTests.test_distinct_nonempty_allowlists_have_distinct_pools`.

**Before:** Cache selection/value handling can reuse a different unlabeled pool or omit required constraints.

**After:** Keep target identity,allowlist identity,required-cache and null-value semantics coherent.

**Limits:** 0055 target identity common in this final comparison;its foundation separately4/4;related mechanisms grouped once. No extra training,ink-quality,adoption or award result is inferred.

AI-assisted investigation,implementation,test preparation and validation orchestration. Computational resources were provided by the e-INFRA CZ project (ID:90254),supported by the Ministry of Education,Youth and Sports of the Czech Republic. Code/data attribution is separate.

## Provenance and review status

Publication base: `39a8cf3a124bdd5540ee826e1cb30047c8dc8c85`. [Selected records and file hashes](selected-records.json).

[#509](https://github.com/ScrollPrize/villa/pull/509) by bruniss (dataset groundwork); [#666](https://github.com/ScrollPrize/villa/pull/666) by bruniss (dataset groundwork); [#1682](https://github.com/ScrollPrize/villa/pull/1682) by kadenpool (store creation).

Focused overlap checks are not exhaustive novelty evidence. Author review and real-scroll workflow commentary remain pending. This archived report is not a terminal capture or a new experiment.
