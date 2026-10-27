# 0090 � Generic weights-only EMA reset

**ARCHIVED EVIDENCE VIEW � not a new terminal run.**

|Recorded result|Original|Repaired|
|---|---:|---:|
|Methods|7|7|
|Assertion failures|3|0|
|Errors / skips|0 / 0|0 / 0|
|Passing|4|7|

Controlled original assertion: `test_generic_weights_only_ema.GenericWeightsOnlyEmaTests.test_partial_weights_only_seeds_ema_from_loaded_and_retained_main`.

**Before:** A weights-only restore can leave EMA seeded from pre-load weights/history.

**After:** Reset EMA from the actual loaded main state and retain full-resume behavior.

**Limits:** Actual CPU checkpoint/history states and extracted caller/EMA methods;full resume controls retained;no fulltrainer/training;652/806 credited. No extra training,ink-quality,adoption or award result is inferred.

AI-assisted investigation,implementation,test preparation and validation orchestration. Computational resources were provided by the e-INFRA CZ project (ID:90254),supported by the Ministry of Education,Youth and Sports of the Czech Republic. Code/data attribution is separate.

## Provenance and review status

Publication base: `39a8cf3a124bdd5540ee826e1cb30047c8dc8c85`. [Selected records and file hashes](selected-records.json).

[#652](https://github.com/ScrollPrize/villa/pull/652) by bruniss (extra-state groundwork); [#806](https://github.com/ScrollPrize/villa/pull/806) by giorgioangel (EMA/counter feature); [#1475](https://github.com/ScrollPrize/villa/pull/1475) by jaideepsaipadhi (different partial-load reporting); [#1819](https://github.com/ScrollPrize/villa/pull/1819) by giorgioangel (different Hecate path).

Focused overlap checks are not exhaustive novelty evidence. Author review and real-scroll workflow commentary remain pending. This archived report is not a terminal capture or a new experiment.
