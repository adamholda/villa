# PR evidence and submission criteria,28 October2026

All27 proposals are public and open. Three are ready for review and24 are drafts. GitHub's author open-PR limit blocks further draft-to-ready transitions. Maintainers can still inspect all27 public diffs,tests and evidence. The numeric configured cap was not read; no limit workaround is requested. Vercel deployment authorization is separate.

This is an evidence inventory,not certification that all27 satisfy [Villa's contribution rules](https://github.com/ScrollPrize/villa/blob/39a8cf3a124bdd5540ee826e1cb30047c8dc8c85/CONTRIBUTING.md). Those rules require real-scroll use and before/after tool evidence,actual workflow motivation,human-written relevance for AI-assisted PRs,and personal code review. Original checked author statements are preserved;they do not invent an earlier human encounter or establish that AI-drafted prose was human-written. Later supplements do not imply a fresh personal review.

The archived images have correct source/context labels. A test-summary image can be accurate while still leaving the real-scroll tool demonstration requirement unmet. Four packets have direct archived CT CLI evidence;three have partial/instrumented CT evidence;20 use CPU/generated-store/source-only checks. These are evidence classes,not accepted fixes or prize counts. No full training/CUDA-overflow/DDP performance or model-quality result is claimed.

|PR|GitHub stage|Evidence scope / unresolved technical limit|
|---|---|---|
|[#2271](https://github.com/ScrollPrize/villa/pull/2271) Fix selected OME-Zarr input routing in scale workers|Ready|Real S3/S5 scale CLI before/after; four actual archived CLI captures.|
|[#2275](https://github.com/ScrollPrize/villa/pull/2275) Reject paired TIFF exports outside secondary array coverage|Ready|Real S3/S5 paired-export CLI before/after; four actual archived CLI captures.|
|[#2302](https://github.com/ScrollPrize/villa/pull/2302) Reject overlapping merge stores and incompatible declared grids|Ready|Real S3/S5 merge CLI; three new archived output captures show loss, rejection and exact supported output. Grid headers are constructed.|
|[#2303](https://github.com/ScrollPrize/villa/pull/2303) Honor declared depth axes in flat ink inference|Draft|CT input delivery to an untrained recording model; no trained-model inference benefit.|
|[#2304](https://github.com/ScrollPrize/villa/pull/2304) Preserve successful update history and EMA state on native ink resume|Draft|CPU checkpoint/source blocks and controlled skip flags; no actual CUDA overflow or full training.|
|[#2305](https://github.com/ScrollPrize/villa/pull/2305) Preserve best-checkpoint history across native ink resume|Draft|CPU checkpoints/models with supplied scores; no full training.|
|[#2306](https://github.com/ScrollPrize/villa/pull/2306) Handle polynomial and short-run learning-rate scheduler boundaries|Draft|CPU scheduler boundary microcases.|
|[#2307](https://github.com/ScrollPrize/villa/pull/2307) Wire background patch requests through cache generation and dataset loading|Draft|CT-backed cache wiring with engineered labels; general scanner remains held.|
|[#2326](https://github.com/ScrollPrize/villa/pull/2326) Reject overlapping local input/output trees in transpose|Draft|Original hazards are prepare-only; repaired rejection and valid selected-array controls are real CT CLI. Later0114 review not inferred.|
|[#2327](https://github.com/ScrollPrize/villa/pull/2327) Reject overlapping local input/output trees in threshold|Draft|Generated-store threshold path safety; missing real-scroll tool demonstration.|
|[#2328](https://github.com/ScrollPrize/villa/pull/2328) Preserve declared axes and transforms in transpose planning|Draft|Generated-store planning/frame tests; depends on unmerged2295 by ChaseHendrick.|
|[#2329](https://github.com/ScrollPrize/villa/pull/2329) Reject nonpositive explicit Zarr worker counts|Draft|Parser/config controls; no real-scroll task execution.|
|[#2330](https://github.com/ScrollPrize/villa/pull/2330) Keep dataset cache targets, selections and values consistent|Draft|Generated-store cache integration including0055; separate46-method composition is not real training.|
|[#2331](https://github.com/ScrollPrize/villa/pull/2331) Gather validation confusion counts at sample granularity|Draft|CPU tensors/counts and actual gather with supplied collective/state; no actual DDP.|
|[#2332](https://github.com/ScrollPrize/villa/pull/2332) Map labeled packed volumes before unlabeled entries|Draft|Generated-store packed mapping and loader method.|
|[#2333](https://github.com/ScrollPrize/villa/pull/2333) Exclude neighboring packed volumes from patch normalization|Draft|Generated-store packed normalization/item reads.|
|[#2334](https://github.com/ScrollPrize/villa/pull/2334) Pass configured rotation axes to training augmentation|Draft|Config/CLI/augmentation forwarding; no training run.|
|[#2335](https://github.com/ScrollPrize/villa/pull/2335) Advance generic AMP consumers only after successful updates|Draft|CPU successful-update consumers with supplied skip flags; no actual CUDA overflow.|
|[#2336](https://github.com/ScrollPrize/villa/pull/2336) Save the completed epoch in the final checkpoint|Draft|CPU checkpoint/reduced epoch loop; no full trainer.|
|[#2337](https://github.com/ScrollPrize/villa/pull/2337) Restore saved minmax normalization aliases for inference|Draft|CPU normalization alias checks; failed control and corrected successor retained.|
|[#2338](https://github.com/ScrollPrize/villa/pull/2338) Register existing checkpoint history before pruning|Draft|Small CPU checkpoints and sentinel debug files; no real-scroll training.|
|[#2339](https://github.com/ScrollPrize/villa/pull/2339) Preserve saved AMP policy across YAML and CLI loading|Draft|YAML/API/CLI and Torch dtype policy; no actual autocast/scaler workload.|
|[#2340](https://github.com/ScrollPrize/villa/pull/2340) Reset EMA state on weights-only checkpoint loads|Draft|CPU weights-only/EMA state roundtrips; no full trainer.|
|[#2341](https://github.com/ScrollPrize/villa/pull/2341) Account for gradient accumulation in scheduler horizons|Draft|Scheduler factory/tiny CPU parameter-update controls; no full trainer.|
|[#2342](https://github.com/ScrollPrize/villa/pull/2342) Reject separate output paths for in-place zero-range edits|Draft|Real CT CLI before/rejection/valid controls; constructed isotropic headers, separate depth STOP.|
|[#2343](https://github.com/ScrollPrize/villa/pull/2343) Print finalizer names in data channel order|Draft|Source/printed-name order; no full numeric finalizer.|
|[#2344](https://github.com/ScrollPrize/villa/pull/2344) Align the inference guide and help with the current CLI|Draft|Documentation/extracted argparse checks; no inference.|

PR2302's [direct archived CLI records](../../2026-10-28/merge-cli/README.md) preserve original source hashes and state that baseline exit0 logs contain a cleanup warning. The controlled loss is not an observed user incident. PR2328's common routing/pitch/planning/defaults are ChaseHendrick's2295 work. Other prior-work credits and failed/held exclusions remain in each PR.

One October maintenance-bundle form draft includes all27 URLs with these limits. It has not been entered or submitted,and no terms accepted. Public drafts are available to reviewers;publication alone is not proof of eligibility,acceptance or an award. Remaining genuine human-workflow requirements cannot be filled with invented prose or CT-wrapped toy demonstrations.
