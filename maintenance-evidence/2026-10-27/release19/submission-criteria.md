# PR evidence and submission criteria,28 October2026

All27 proposals are public and open. Three are ready for review and24 are drafts. GitHub's author open-PR limit blocks further draft-to-ready transitions. Maintainers can still inspect all27 public diffs,tests and evidence. The numeric configured cap was not read; no limit workaround is requested. Vercel deployment authorization is separate.

This is an evidence inventory,not certification that all27 satisfy [Villa's contribution rules](https://github.com/ScrollPrize/villa/blob/39a8cf3a124bdd5540ee826e1cb30047c8dc8c85/CONTRIBUTING.md). Those rules require real-scroll use and before/after tool evidence,actual workflow motivation,human-written relevance for AI-assisted PRs,and personal code review. Adam has adopted the workflow statements now present in all27PRs;the commentary has no AI label,and technical/experiment disclosures remain separate. Original checked author statements are preserved without inventing an earlier incident. Later supplements do not imply a fresh personal review.

The archived images have correct source/context labels. A test-summary image can be accurate while still leaving the real-scroll tool demonstration requirement unmet. Eight packets have direct archived CT CLI evidence;three have partial/instrumented CT evidence;16 use CPU/generated-store/source-only checks. These are evidence classes,not accepted fixes or prize counts. No full training/CUDA-overflow/DDP performance or model-quality result is claimed.

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
|[#2326](https://github.com/ScrollPrize/villa/pull/2326) Reject overlapping local input/output trees in transpose|Draft|0123 fullCLI:2original exit0source overwrites,2repaired pre-prompt whole-tree rejections,4exact valid transposes. Earlier0114prepare-only hazards remain history;later personal review not inferred.|
|[#2327](https://github.com/ScrollPrize/villa/pull/2327) Reject overlapping local input/output trees in threshold|Draft|0119 full real-CT CLI:2 original silent input replacements,2 repaired pre-prompt rejections,8 valid exact masks. Earlier0116 path failure is preserved.|
|[#2328](https://github.com/ScrollPrize/villa/pull/2328) Preserve declared axes and transforms in transpose planning|Draft|0120 actual CT producer/plan/consumer CLI:2original named-axis nonmatches/2controls,repaired4/4;18calls. Depends on unmerged2295 by ChaseHendrick;no native registration/global-translation claim.|
|[#2329](https://github.com/ScrollPrize/villa/pull/2329) Reject nonpositive explicit Zarr worker counts|Draft|0117 real S3/S5 CT CLI:2 original late -1 failures,2 repaired early rejections,4 valid exact one-worker masks. Zero/default expansion not run.|
|[#2330](https://github.com/ScrollPrize/villa/pull/2330) Keep dataset cache targets, selections and values consistent|Draft|Generated-store cache integration including0055; separate46-method composition is not real training.|
|[#2331](https://github.com/ScrollPrize/villa/pull/2331) Gather validation confusion counts at sample granularity|Draft|CPU tensors/counts and actual gather with supplied collective/state; no actual DDP.|
|[#2332](https://github.com/ScrollPrize/villa/pull/2332) Map labeled packed volumes before unlabeled entries|Draft|Generated-store packed mapping and loader method.|
|[#2333](https://github.com/ScrollPrize/villa/pull/2333) Exclude neighboring packed volumes from patch normalization|Draft|Generated-store packed normalization/item reads.|
|[#2334](https://github.com/ScrollPrize/villa/pull/2334) Pass configured rotation axes to training augmentation|Draft|0124 whole CT/released binary mask:actual config/parser/ZarrDataset and complete composed pipeline;6configs/12item reads,return-preserving spatial observers,exact joint references/unrestricted controls. Instrumented dataset evidence,not trainer/model/human training CLI. Old0122partial and9-methodCPU results remain history.|
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

One October maintenance-bundle form draft includes all27 URLs with these limits. It has not been entered or submitted,and no terms accepted. Public drafts are available to reviewers;publication alone is not proof of eligibility,acceptance or an award. Author-approved motivation is now supplied;remaining supported-workflow evidence cannot be replaced with invented incidents or CT-wrapped toy demonstrations.


## Worker CT follow-up,28October2026

Existing2329 production code is unchanged. [Actual archived CLI evidence](../../2026-10-28/worker-ct/README.md) comes from completed PBS25068983/0117:8 records,72s x1CPU/0GPU,inputs unchanged. This adds a real-data context to the existing parser repair,not another independent fix or a test-method count. The old summary remains historical. New screenshots do not infer personal review or human-written workflow commentary. Separately,0116 failed before CT because of a driver source-path error;that run remains preserved/deferred with zero CT outcomes and2CPU-seconds charged. No silent retry.


## Authorized threshold successor0119

After Adam's explicit post-failure approval,exactly two test-driver checkout paths were corrected in a separate frozen successor;all12 inputs/cases/scientific oracles were unchanged. [Actual archived CT CLI evidence](../../2026-10-28/threshold-ct/README.md) records completed PBS25069058:original calls lose245760nonzero input voxels per disposable crop despite exit0;repaired calls preserve the whole tree before prompting. Eight valid controls remain exact.98s x1CPU/0GPU final/reconciled. The old0116 failure is preserved/charged2seconds and is not marked passed. No new production repair,incident,human-written relevance or personal-review attestation. No blanket upstream compliance.


## Actual named-axis producer/consumer follow-up

[0120/PBS25069083](../../2026-10-28/transpose-chain-ct/README.md) uses the actual common2295 CLI to produce xzy CT stores,then actual paired dry-run/fullCLI consumers. Original plans and writes the wrong named-axis shape while exiting0;repair restores every CT voxel to the expected shape and preserves valid controls. Eight compound consumers plus two producers are18calls,not18unit methods/incidents.133s x1CPU/0GPU;native inputs unchanged. Four-file common proposal context is explicit,not full2295 or native physical-frame proof. New supplement is not presumed personally reviewed;genuine human-written relevance and other workflow gates remain. No blanket compliance.


## Partial actual annotated-pair orientation follow-up

[0122/PBS25069581](../../2026-10-28/rotation-real-ct/README.md) supplements2334 using one whole fixed S5 CT cube and its released binary fiber mask. Actual loader/factory plus selected member calls honor z/none after repair,retain unrestricted behavior,and match independent joint permutations.6 configuration records and40 repeated member observations are not independent data samples or unittest methods.96s x1CPU/0GPU final/reconciled. Three browser captures show selected actual diagnostic fields,not raw CLI error/success or a full trainer. The pipeline is bypassed for loading,restored,and selected members execute with an unchanged-parameter observer. No ink-quality,anatomical-instance,full augmentation or personal-review claim. Current classification7direct/4partial/16CPU-source;47current embeds/6historical links,53cumulative unique reviewed images. All author/workflow gates remain.


## Full original/repaired transpose alias check

[0123](../../2026-10-28/transpose-full-cli/README.md) closes2326's narrow full-original-CLI gap:8calls on2fixed reusedCTcrops,not8independent incidents or unit methods.2original identity-order calls erase source voxels despite exit0;repair rejects and preserves the full trees;4actual xzy controls remain exact. Constructed format2 headers,source-verifying runpy wrapper,416non-fiber source closure/existing environment;no installer/full-repository,race,group routing,frame/training/quality proof.3actual CLI captures replace2prior embeds preserved as history. Current classes8direct/3partial/16CPU-source;48current embeds/8historical links,56unique reviewed images. Human-written relevance and actual human workflow remain separate;no blanket contribution-rule certification.


## Complete composed annotated-pair dataset supplement

[0124/PBS25080112](../../2026-10-28/rotation-composed-ct/README.md) extends2334's earlier partial evidence. The actual ZarrDataset getter retains its complete composed augmentation pipeline,including ordinary intensity/noise members;spatial observers return original sampled parameters.6configuration records/12complete item reads on one fixed whole S5 CT/released fiber-mask pair give original2factory nonmatches/1control and repaired3matches. All mask/padding references,301079foreground voxels and unrestricted parameter/image/mask/padding streams remain exact. This is not12independent samples,12unit methods,a trainer/model,DDP,ink-quality or a raw human CLI demonstration.71s x1CPU/0GPU final/reconciled,no retry. Three unmodified browser captures show actual archived diagnostic fields;the0122images remain historical links. Current classes8direct/3instrumented/16CPU-source;48current embeds/11historical links,59cumulative unique reviewed images. Later personal review is not inferred;all27 are not certified compliant.
