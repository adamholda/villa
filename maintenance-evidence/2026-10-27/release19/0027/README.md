# 0027 — Zero-range output-argument guard

**ARCHIVED EVIDENCE VIEW — not a new terminal run.**

Actual fixed S3/S5 CLI gate:32 records. Eight original wrong-output calls exit0/change input;all eight repaired calls reject before prompting/preserve trees. Eight valid in-place controls per arm remain exact.

|Recorded result|Original|Repaired|
|---|---:|---:|
|Methods|6|6|
|Assertion failures|3|0|
|Errors / skips|0 / 0|0 / 0|
|Passing|3|6|

Controlled original assertion: `test_direct_constructor_rejects_output_without_opening_data`.

**Before:** An output argument is accepted although zero-range writes into its input.

**After:** Reject that unsupported output before prompting/reads;preserve explicit/implicit in-place use.

**Limits:** Six unchanged methods and32 fixed S3/S5 CLI gates under0112;constructed isotropic headers over actual CT. Separate depth-scaling STOP remains. No extra training,ink-quality,adoption or award result is inferred.

AI-assisted investigation,implementation,test preparation and validation orchestration. Computational resources were provided by the e-INFRA CZ project (ID:90254),supported by the Ministry of Education,Youth and Sports of the Czech Republic. Code/data attribution is separate.

## Provenance and review status

Publication base: `39a8cf3a124bdd5540ee826e1cb30047c8dc8c85`. [Selected records and file hashes](selected-records.json).

[#1431](https://github.com/ScrollPrize/villa/pull/1431) by axiosdevs (selected-input routing); [#1682](https://github.com/ScrollPrize/villa/pull/1682) by kadenpool (shared store creation); [#2295](https://github.com/ScrollPrize/villa/pull/2295) by ChaseHendrick (separate task-core proposal).

Focused overlap checks are not exhaustive novelty evidence. Author review and real-scroll workflow commentary remain pending. This archived report is not a terminal capture or a new experiment.
