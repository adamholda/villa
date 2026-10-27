# Villa maintenance draft PRs, 27 October 2026

All 19 requested packets are public drafts for author review. This is a technical evidence index, not a human-use attestation or an award claim. Each PR discloses its actual validation context and pending requirements. PR2328 follows ChaseHendrick PR2295; the common proposal is not attributed to the follow-up.

|Packet|Draft PR|Archived evidence|Screenshot|
|---|---|---|---|
|0045 Reject overlapping local input/output trees in transpose|[#2326](https://github.com/ScrollPrize/villa/pull/2326)|[Report](0045/README.md) / [records and hashes](0045/selected-records.json)|[Image](0045/evidence.jpg)|
|0050 Reject overlapping local input/output trees in threshold|[#2327](https://github.com/ScrollPrize/villa/pull/2327)|[Report](0050/README.md) / [records and hashes](0050/selected-records.json)|[Image](0050/evidence.jpg)|
|0049 Preserve declared axes and transforms in transpose planning|[#2328](https://github.com/ScrollPrize/villa/pull/2328)|[Report](0049/README.md) / [records and hashes](0049/selected-records.json)|[Image](0049/evidence.jpg)|
|0046 Reject nonpositive explicit Zarr worker counts|[#2329](https://github.com/ScrollPrize/villa/pull/2329)|[Report](0046/README.md) / [records and hashes](0046/selected-records.json)|[Image](0046/evidence.jpg)|
|0067 Keep dataset cache targets, selections and values consistent|[#2330](https://github.com/ScrollPrize/villa/pull/2330)|[Report](0067/README.md) / [records and hashes](0067/selected-records.json)|[Image](0067/evidence.jpg)|
|0052 Gather validation confusion counts at sample granularity|[#2331](https://github.com/ScrollPrize/villa/pull/2331)|[Report](0052/README.md) / [records and hashes](0052/selected-records.json)|[Image](0052/evidence.jpg)|
|0073 Map labeled packed volumes before unlabeled entries|[#2332](https://github.com/ScrollPrize/villa/pull/2332)|[Report](0073/README.md) / [records and hashes](0073/selected-records.json)|[Image](0073/evidence.jpg)|
|0077 Exclude neighboring packed volumes from patch normalization|[#2333](https://github.com/ScrollPrize/villa/pull/2333)|[Report](0077/README.md) / [records and hashes](0077/selected-records.json)|[Image](0077/evidence.jpg)|
|0081 Pass configured rotation axes to training augmentation|[#2334](https://github.com/ScrollPrize/villa/pull/2334)|[Report](0081/README.md) / [records and hashes](0081/selected-records.json)|[Image](0081/evidence.jpg)|
|0083 Advance generic AMP consumers only after successful updates|[#2335](https://github.com/ScrollPrize/villa/pull/2335)|[Report](0083/README.md) / [records and hashes](0083/selected-records.json)|[Image](0083/evidence.jpg)|
|0093 Save the completed epoch in the final checkpoint|[#2336](https://github.com/ScrollPrize/villa/pull/2336)|[Report](0093/README.md) / [records and hashes](0093/selected-records.json)|[Image](0093/evidence.jpg)|
|0095 Restore saved minmax normalization aliases for inference|[#2337](https://github.com/ScrollPrize/villa/pull/2337)|[Report](0095/README.md) / [records and hashes](0095/selected-records.json)|[Image](0095/evidence.jpg)|
|0100 Register existing checkpoint history before pruning|[#2338](https://github.com/ScrollPrize/villa/pull/2338)|[Report](0100/README.md) / [records and hashes](0100/selected-records.json)|[Image](0100/evidence.jpg)|
|0089 Preserve saved AMP policy across YAML and CLI loading|[#2339](https://github.com/ScrollPrize/villa/pull/2339)|[Report](0089/README.md) / [records and hashes](0089/selected-records.json)|[Image](0089/evidence.jpg)|
|0090 Reset EMA state on weights-only checkpoint loads|[#2340](https://github.com/ScrollPrize/villa/pull/2340)|[Report](0090/README.md) / [records and hashes](0090/selected-records.json)|[Image](0090/evidence.jpg)|
|0094 Account for gradient accumulation in scheduler horizons|[#2341](https://github.com/ScrollPrize/villa/pull/2341)|[Report](0094/README.md) / [records and hashes](0094/selected-records.json)|[Image](0094/evidence.jpg)|
|0027 Reject separate output paths for in-place zero-range edits|[#2342](https://github.com/ScrollPrize/villa/pull/2342)|[Report](0027/README.md) / [records and hashes](0027/selected-records.json)|[Image](0027/evidence.jpg)|
|0097 Print finalizer names in data channel order|[#2343](https://github.com/ScrollPrize/villa/pull/2343)|[Report](0097/README.md) / [records and hashes](0097/selected-records.json)|[Image](0097/evidence.jpg)|
|0102 Align the inference guide and help with the current CLI|[#2344](https://github.com/ScrollPrize/villa/pull/2344)|[Report](0102/README.md) / [records and hashes](0102/selected-records.json)|[Image](0102/evidence.jpg)|

Screenshots are unmodified browser captures of passive archived reports. No raw CT pixels, weights, predictions or complete cluster logs are included. The 0045 report explicitly uses coordinate work common to both historical arms; its standalone main-context gate is pending. The 0067 report is one grouped cache packet including its identity foundation. The initial failed z-score control remains failed; the explicitly corrected successor is disclosed in PR2337. No full-stack runtime, real training benefit, adoption or maintainer acceptance is inferred.
