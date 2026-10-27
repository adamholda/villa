# 0081 � Honor configured rotation axes

**ARCHIVED EVIDENCE VIEW � not a new terminal run.**

|Recorded result|Original|Repaired|
|---|---:|---:|
|Methods|9|9|
|Assertion failures|6|0|
|Errors / skips|0 / 0|0 / 0|
|Passing|3|9|

Controlled original assertion: `test_rotation_axes_wiring.RotationAxesWiringTests.test_anisotropic_equal_plane_admissibility`.

**Before:** The supported configuration-to-transform path can drop rotation-axis constraints.

**After:** Forward the configured constraints to the supported factories/callers.

**Limits:** CPU CLI/config/factory/caller contract;no training/quality proof. No extra training,ink-quality,adoption or award result is inferred.

AI-assisted investigation,implementation,test preparation and validation orchestration. Computational resources were provided by the e-INFRA CZ project (ID:90254),supported by the Ministry of Education,Youth and Sports of the Czech Republic. Code/data attribution is separate.

## Provenance and review status

Publication base: `39a8cf3a124bdd5540ee826e1cb30047c8dc8c85`. [Selected records and file hashes](selected-records.json).

[#509](https://github.com/ScrollPrize/villa/pull/509) by bruniss (existing rotation-axis control); [#666](https://github.com/ScrollPrize/villa/pull/666) by bruniss (quarter-turn/transpose refactor); [#1020](https://github.com/ScrollPrize/villa/pull/1020) by pscamillo (distinct ring augmentation); [#1796](https://github.com/ScrollPrize/villa/pull/1796) by khj1222 (distinct Copy TTA).

Focused overlap checks are not exhaustive novelty evidence. Author review and real-scroll workflow commentary remain pending. This archived report is not a terminal capture or a new experiment.
