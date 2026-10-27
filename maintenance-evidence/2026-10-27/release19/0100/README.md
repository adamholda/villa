# 0100 — Recent checkpoint/debug-history retention

**ARCHIVED EVIDENCE VIEW — not a new terminal run.**

|Recorded result|Original|Repaired|
|---|---:|---:|
|Methods|6|6|
|Assertion failures|2|0|
|Errors / skips|0 / 0|0 / 0|
|Passing|4|6|

Controlled original assertion: `test_checkpoint_history_registration.CheckpointHistoryRegistrationTests.test_debug_caller_keeps_three_recent_files`.

**Before:** Repeated registration of the same epoch can prune extra checkpoint/debug history.

**After:** Retain distinct recent epochs and preserve older best/unrelated files.

**Limits:** Small real checkpoints/sentinel debug files;not training. No extra training,ink-quality,adoption or award result is inferred.

AI-assisted investigation,implementation,test preparation and validation orchestration. Computational resources were provided by the e-INFRA CZ project (ID:90254),supported by the Ministry of Education,Youth and Sports of the Czech Republic. Code/data attribution is separate.

## Provenance and review status

Publication base: `39a8cf3a124bdd5540ee826e1cb30047c8dc8c85`. [Selected records and file hashes](selected-records.json).

[#652](https://github.com/ScrollPrize/villa/pull/652) by bruniss (trainer groundwork); [#806](https://github.com/ScrollPrize/villa/pull/806) by giorgioangel (trainer/EMA groundwork); [#2252](https://github.com/ScrollPrize/villa/pull/2252) by campbelltron1 (distinct auxiliary work).

Focused overlap checks are not exhaustive novelty evidence. Author review and real-scroll workflow commentary remain pending. This archived report is not a terminal capture or a new experiment.
