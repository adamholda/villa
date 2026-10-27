# 0077 � Packed neighbor normalization isolation

**ARCHIVED EVIDENCE VIEW � not a new terminal run.**

|Recorded result|Original|Repaired|
|---|---:|---:|
|Methods|8|8|
|Assertion failures|5|0|
|Errors / skips|0 / 0|0 / 0|
|Passing|3|8|

Controlled original assertion: `test_packed_normalization.PackedNormalizationTests.test_2d_normalization_excludes_neighbor`.

**Before:** A packed read can include a neighboring sample in instance normalization.

**After:** Bound each mapped read to its own extent while retaining its own gaps.

**Limits:** Actual item reads/normalization;combined dataset gate separate. No extra training,ink-quality,adoption or award result is inferred.

AI-assisted investigation,implementation,test preparation and validation orchestration. Computational resources were provided by the e-INFRA CZ project (ID:90254),supported by the Ministry of Education,Youth and Sports of the Czech Republic. Code/data attribution is separate.

## Provenance and review status

Publication base: `39a8cf3a124bdd5540ee826e1cb30047c8dc8c85`. [Selected records and file hashes](selected-records.json).

[#802](https://github.com/ScrollPrize/villa/pull/802) by giorgioangel (separate scale/dilation/cache and distributed-validation work); [#1483](https://github.com/ScrollPrize/villa/pull/1483) (different native flat-padding normalization); [#1646](https://github.com/ScrollPrize/villa/pull/1646) (different native flat-padding normalization); [#1773](https://github.com/ScrollPrize/villa/pull/1773) (different native flat-padding normalization); [#2169](https://github.com/ScrollPrize/villa/pull/2169) (different native flat-padding normalization).

Focused overlap checks are not exhaustive novelty evidence. Author review and real-scroll workflow commentary remain pending. This archived report is not a terminal capture or a new experiment.
