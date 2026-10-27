# 0050 — Threshold local-tree guard

**ARCHIVED EVIDENCE VIEW — not a new terminal run.**

|Recorded result|Original|Repaired|
|---|---:|---:|
|Methods|9|9|
|Assertion failures|5|0|
|Errors / skips|0 / 0|0 / 0|
|Passing|4|9|

Controlled original assertion: `test_threshold_paths.ThresholdPathTests.test_cli_nested_output_rejects`.

**Before:** A threshold output parent can replace the selected input array.

**After:** Reject overlapping local trees while retaining separate outputs.

**Limits:** Generated-store selected-array scope;same store-safety family as0045/public2302. No extra training,ink-quality,adoption or award result is inferred.

AI-assisted investigation,implementation,test preparation and validation orchestration. Computational resources were provided by the e-INFRA CZ project (ID:90254),supported by the Ministry of Education,Youth and Sports of the Czech Republic. Code/data attribution is separate.

## Provenance and review status

Publication base: `39a8cf3a124bdd5540ee826e1cb30047c8dc8c85`. [Selected records and file hashes](selected-records.json).

[#1682](https://github.com/ScrollPrize/villa/pull/1682) by kadenpool (shared store creation); [#2295](https://github.com/ScrollPrize/villa/pull/2295) by ChaseHendrick (separate routing, pitch and planning proposal).

Focused overlap checks are not exhaustive novelty evidence. Author review and real-scroll workflow commentary remain pending. This archived report is not a terminal capture or a new experiment.
