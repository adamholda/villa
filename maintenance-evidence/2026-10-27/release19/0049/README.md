# 0049 — Named-axis/full-frame transpose planning

**ARCHIVED EVIDENCE VIEW — not a new terminal run.**

**Dependency:** follows unmerged PR2295 by ChaseHendrick at209d3b794. Only our final increment is new here;the original author retains credit for all common routing/pitch/planning/default work.

|Recorded result|Original|Repaired|
|---|---:|---:|
|Methods|9|9|
|Assertion failures|5|0|
|Errors / skips|0 / 0|0 / 0|
|Passing|4|9|

Controlled original assertion: `test_transpose_plan.TransposePlanTests.test_dataset_translation_survives_plan_and_execution`.

**Before:** Transpose planning/runtime assume fixed ZYX and lose parts of declared frames.

**After:** Share read-only named-axis/full-frame specification in planning and preparation.

**Limits:** Explicit2295 core overlay;ChaseHendrick basic pitch/units/routing/planning credited;old0021a counted here once. No extra training,ink-quality,adoption or award result is inferred.

AI-assisted investigation,implementation,test preparation and validation orchestration. Computational resources were provided by the e-INFRA CZ project (ID:90254),supported by the Ministry of Education,Youth and Sports of the Czech Republic. Code/data attribution is separate.

## Provenance and review status

Publication base: `209d3b7940af2768fb8a796249d19c969e608e5f`. [Selected records and file hashes](selected-records.json).

[#2295](https://github.com/ScrollPrize/villa/pull/2295) by ChaseHendrick (the dependency containing routing, pitch, planning and defaults); [#1431](https://github.com/ScrollPrize/villa/pull/1431) by axiosdevs (selected-input routing); [#1682](https://github.com/ScrollPrize/villa/pull/1682) by kadenpool (shared store creation); [#2266](https://github.com/ScrollPrize/villa/pull/2266) by rwe6445 (separate metadata work).

Focused overlap checks are not exhaustive novelty evidence. Author review and real-scroll workflow commentary remain pending. This archived report is not a terminal capture or a new experiment.
