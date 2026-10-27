# 0095 � Saved minmax/rescale aliases reach inference

**ARCHIVED EVIDENCE VIEW � not a new terminal run.**

|Recorded result|Original|Repaired|
|---|---:|---:|
|Methods|8|8|
|Assertion failures|4|0|
|Errors / skips|0 / 0|0 / 0|
|Passing|4|8|

Controlled original assertion: `test_checkpoint_minmax_alias_global_control.CheckpointMinmaxAliasTests.test_current_minmax`.

**Before:** Saved minmax/rescale aliases can reach inference without selecting the intended normalizer.

**After:** Map the existing aliases to the supported minmax normalization behavior.

**Limits:** Explicitly authorized corrected global-zscore control;failed0104 remains separately preserved/charged. No extra training,ink-quality,adoption or award result is inferred.

AI-assisted investigation,implementation,test preparation and validation orchestration. Computational resources were provided by the e-INFRA CZ project (ID:90254),supported by the Ministry of Education,Youth and Sports of the Czech Republic. Code/data attribution is separate.

## Provenance and review status

Publication base: `39a8cf3a124bdd5540ee826e1cb30047c8dc8c85`. [Selected records and file hashes](selected-records.json).

[#1386](https://github.com/ScrollPrize/villa/pull/1386) by TAUIL-Abd-Elilah (nnU-Net mapping); [#2295](https://github.com/ScrollPrize/villa/pull/2295) by ChaseHendrick (separate routing proposal); [#1446](https://github.com/ScrollPrize/villa/pull/1446) (different intensity-normalization write-through correction).

Focused overlap checks are not exhaustive novelty evidence. Author review and real-scroll workflow commentary remain pending. This archived report is not a terminal capture or a new experiment.
