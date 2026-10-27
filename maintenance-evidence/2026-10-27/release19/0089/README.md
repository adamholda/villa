# 0089 � Saved AMP-policy YAML/CLI roundtrip

**ARCHIVED EVIDENCE VIEW � not a new terminal run.**

|Recorded result|Original|Repaired|
|---|---:|---:|
|Methods|7|7|
|Assertion failures|3|0|
|Errors / skips|0 / 0|0 / 0|
|Passing|4|7|

Controlled original assertion: `test_amp_policy_roundtrip.AmpPolicyRoundtripTests.test_explicit_dtype_does_not_erase_saved_disabled_policy`.

**Before:** Saved AMP enablement/dtype policy can be lost on YAML/API/CLI reload.

**After:** Persist and merge the saved policy while retaining legacy defaults and explicit overrides.

**Limits:** Actual YAML loader/writer,parser/merge and source precision block with Torch dtypes;no training/autocast/scaler;1702/1496/509 credited. No extra training,ink-quality,adoption or award result is inferred.

AI-assisted investigation,implementation,test preparation and validation orchestration. Computational resources were provided by the e-INFRA CZ project (ID:90254),supported by the Ministry of Education,Youth and Sports of the Czech Republic. Code/data attribution is separate.

## Provenance and review status

Publication base: `39a8cf3a124bdd5540ee826e1cb30047c8dc8c85`. [Selected records and file hashes](selected-records.json).

[#1702](https://github.com/ScrollPrize/villa/pull/1702) by ge-al (existing AMP controls); [#1496](https://github.com/ScrollPrize/villa/pull/1496) by axiosdevs (existing precision control); [#509](https://github.com/ScrollPrize/villa/pull/509) by bruniss (training groundwork).

Focused overlap checks are not exhaustive novelty evidence. Author review and real-scroll workflow commentary remain pending. This archived report is not a terminal capture or a new experiment.
