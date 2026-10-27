# 0073 — Packed labeled-prefix mapping

**ARCHIVED EVIDENCE VIEW — not a new terminal run.**

|Recorded result|Original|Repaired|
|---|---:|---:|
|Methods|7|7|
|Assertion failures|3|0|
|Errors / skips|0 / 0|0 / 0|
|Passing|4|7|

Controlled original assertion: `test_packed_mapping_order.PackedMappingOrderTests.test_mapping_metadata_partition_is_independent_of_scanner_enable`.

**Before:** Interleaved packed mapping can disagree with the labeled-prefix boundary.

**After:** Group mappings stably and retain the correct values,positions and labeled boundary.

**Limits:** Generated stores and actual source loader method;combined dataset gate separate. No extra training,ink-quality,adoption or award result is inferred.

AI-assisted investigation,implementation,test preparation and validation orchestration. Computational resources were provided by the e-INFRA CZ project (ID:90254),supported by the Ministry of Education,Youth and Sports of the Czech Republic. Code/data attribution is separate.

## Provenance and review status

Publication base: `39a8cf3a124bdd5540ee826e1cb30047c8dc8c85`. [Selected records and file hashes](selected-records.json).

[#1682](https://github.com/ScrollPrize/villa/pull/1682) by kadenpool (packed-store creation); [#652](https://github.com/ScrollPrize/villa/pull/652) by bruniss (existing trainer behavior).

Focused overlap checks are not exhaustive novelty evidence. Author review and real-scroll workflow commentary remain pending. This archived report is not a terminal capture or a new experiment.
