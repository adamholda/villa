# October 2026 Villa maintenance: 27 public proposals

Updated28October2026. This index covers one monthly maintenance bundle,not27 accepted or independent prize contributions.

## Current review state

All27 PRs are open and unmerged. **Three are ready for review;24 remain drafts.** All original author-verification boxes are checked. The normal signed-in author UI identifies the stage restriction as **“Author has reached the open pull request limit.”** This prevents further author draft-to-ready transitions. The configured numeric cap was not read. Keeping all27 PRs open requires upstream capacity to be freed or a maintainer change/exception to this restriction. No ready-state bypass or repeated denied mutation was attempted.

The Vercel status separately says **“Authorization required to deploy.”** across the24 draft heads. This is deployment authorization,not a measured failure of the bounded code tests. The API reports no merge conflicts for the27 individual PRs. No full-portfolio runtime or complete CI pass is implied.

| PR | Proposal | GitHub stage |
|---|---|---|
| [#2271](https://github.com/ScrollPrize/villa/pull/2271) | Fix selected OME-Zarr input routing in scale workers | Ready for review |
| [#2275](https://github.com/ScrollPrize/villa/pull/2275) | Reject paired TIFF exports outside secondary array coverage | Ready for review |
| [#2302](https://github.com/ScrollPrize/villa/pull/2302) | Reject overlapping merge stores and incompatible declared grids | Ready for review |
| [#2303](https://github.com/ScrollPrize/villa/pull/2303) | Honor declared depth axes in flat ink inference | Draft |
| [#2304](https://github.com/ScrollPrize/villa/pull/2304) | Preserve successful update history and EMA state on native ink resume | Draft |
| [#2305](https://github.com/ScrollPrize/villa/pull/2305) | Preserve best-checkpoint history across native ink resume | Draft |
| [#2306](https://github.com/ScrollPrize/villa/pull/2306) | Handle polynomial and short-run learning-rate scheduler boundaries | Draft |
| [#2307](https://github.com/ScrollPrize/villa/pull/2307) | Wire background patch requests through cache generation and dataset loading | Draft |
| [#2326](https://github.com/ScrollPrize/villa/pull/2326) | Reject overlapping local input/output trees in transpose | Draft |
| [#2327](https://github.com/ScrollPrize/villa/pull/2327) | Reject overlapping local input/output trees in threshold | Draft |
| [#2328](https://github.com/ScrollPrize/villa/pull/2328) | Preserve declared axes and transforms in transpose planning | Draft |
| [#2329](https://github.com/ScrollPrize/villa/pull/2329) | Reject nonpositive explicit Zarr worker counts | Draft |
| [#2330](https://github.com/ScrollPrize/villa/pull/2330) | Keep dataset cache targets, selections and values consistent | Draft |
| [#2331](https://github.com/ScrollPrize/villa/pull/2331) | Gather validation confusion counts at sample granularity | Draft |
| [#2332](https://github.com/ScrollPrize/villa/pull/2332) | Map labeled packed volumes before unlabeled entries | Draft |
| [#2333](https://github.com/ScrollPrize/villa/pull/2333) | Exclude neighboring packed volumes from patch normalization | Draft |
| [#2334](https://github.com/ScrollPrize/villa/pull/2334) | Pass configured rotation axes to training augmentation | Draft |
| [#2335](https://github.com/ScrollPrize/villa/pull/2335) | Advance generic AMP consumers only after successful updates | Draft |
| [#2336](https://github.com/ScrollPrize/villa/pull/2336) | Save the completed epoch in the final checkpoint | Draft |
| [#2337](https://github.com/ScrollPrize/villa/pull/2337) | Restore saved minmax normalization aliases for inference | Draft |
| [#2338](https://github.com/ScrollPrize/villa/pull/2338) | Register existing checkpoint history before pruning | Draft |
| [#2339](https://github.com/ScrollPrize/villa/pull/2339) | Preserve saved AMP policy across YAML and CLI loading | Draft |
| [#2340](https://github.com/ScrollPrize/villa/pull/2340) | Reset EMA state on weights-only checkpoint loads | Draft |
| [#2341](https://github.com/ScrollPrize/villa/pull/2341) | Account for gradient accumulation in scheduler horizons | Draft |
| [#2342](https://github.com/ScrollPrize/villa/pull/2342) | Reject separate output paths for in-place zero-range edits | Draft |
| [#2343](https://github.com/ScrollPrize/villa/pull/2343) | Print finalizer names in data channel order | Draft |
| [#2344](https://github.com/ScrollPrize/villa/pull/2344) | Align the inference guide and help with the current CLI | Draft |

## Evidence and limits

- [Original19 evidence packets and screenshots](https://github.com/adamholda/villa/tree/2ed9417977547ed8b876f501147e2e24d7b6c314/maintenance-evidence/2026-10-27/release19) remain archived unchanged.
- [PR2326 standalone0114 proof](https://github.com/adamholda/villa/blob/54e3c7803e50a9fd4f74e03137dbc9901a9fe5ad/maintenance-evidence/2026-10-27/release19/0045/standalone-README.md):8/8 repaired methods against4 original assertions/4controls and24 CT records,without the old common coordinate patch. Original hazards are prepare-only;repaired rejection/valid controls use full CLI. The PR now leads with this newer result;old16-method evidence remains linked history. Later tests/results are not claimed personally reviewed by the author.
- [PR2342 direct archived CLI proof](https://github.com/adamholda/villa/blob/54e3c7803e50a9fd4f74e03137dbc9901a9fe5ad/maintenance-evidence/2026-10-27/release19/0027/cli-proof.md) supplements the completed6-method/32-record zero-range comparison,without a rerun.
- PR2328 depends on ChaseHendrick's open/unmerged [#2295](https://github.com/ScrollPrize/villa/pull/2295). Only our follow-up increment is ours;the common routing,pitch,planning and default work remains credited.
- PR2330 includes the0055 foundation. The46-method dataset composition and11-method native checkpoint composition are separate bounded integration evidence,not a full portfolio or real training result.
- PR2337 preserves its first failed z-score control and the explicitly authorized corrected successor;the failure was not retrospectively relabeled.

All38 originally embedded image links were checked to load,and all38 images were visually reviewed on28October. They are readable and correspond to their stated records. Most are **archived test/source report captures**,not actual tool-session error/success screenshots. Direct archived CLI captures are distinguished in captions. These images therefore do **not** establish blanket compliance with every [Villa contribution requirement](https://github.com/ScrollPrize/villa/blob/39a8cf3a124bdd5540ee826e1cb30047c8dc8c85/CONTRIBUTING.md);genuine human-written workflow context and any missing real-scroll demonstration remain separate. No new evidence-image assets were uploaded or substituted during this check. No CT pixels,weights,predictions or full private cluster logs are published.

The one October form draft covers all27 public URLs with these limits. No form entry,terms acceptance or submission has occurred. No personal incident,novel letter/text discovery,quality/performance gain,adoption,acceptance or award is claimed. Four failed/held candidates and prior scientific STOPs stay excluded.

AI assistance was used for source investigation,implementation,tests,validation orchestration,analysis and technical drafting. Computational resources were provided by the e-INFRA CZ project (ID:90254),supported by the Ministry of Education,Youth and Sports of the Czech Republic. Villa's MIT code and CT data rights/attribution remain separate.


## Submission criteria check,28 October2026

All27 PRs are already public and open. The author cannot mark24 drafts ready because of GitHub's open-PR limit;maintainers can still inspect their diffs,tests and evidence. This is separate from unresolved real-scroll demonstration and human-written workflow requirements. **Not all27 are certified to satisfy every contribution criterion.** See the [per-PR criteria/evidence inventory](submission-criteria.md).

PR2302 now has [direct archived CLI excerpts](../../2026-10-28/merge-cli/README.md) and before/rejection/supported-success captures,from the completed PBS24944947 run with exact log hashes. No rerun or new user incident. The screenshot scope and cleanup warning are disclosed. The one monthly form draft records the public-draft access note and these evidence gaps;it remains unsubmitted.


## Actual worker CT CLI follow-up,28October2026

PR2329 now has [actual original/rejection/supported-success output](../../2026-10-28/worker-ct/README.md) from0117/PBS25068983:2 original late negative-worker errors,2 repaired pre-write argument rejections,4 valid exact real-CT masks.72s x1CPU/0GPU final/reconciled;native input hashes unchanged. Original zero/default worker expansion is excluded. The existing production helper and original checked statement stay unchanged;later evidence is not represented as newly personally reviewed. The all27 [criteria inventory](submission-criteria.md) now has5 direct CT CLI packets,3partial/instrumented CT packets and19CPU/generated/source-only packets. This is not blanket upstream compliance or an extra repair.

The separate threshold0116 attempt stopped at a test-driver checkout-path check before scientific imports/CT/CLI records. Its failed result and2CPU-seconds remain preserved and deferred. No threshold outcome screenshots or success claim.73final records charge29904CPU coreseconds/6332GPU seconds,no active project reservation. All27PRs remain public/open with3ready/24draft;the author-limit restriction and unresolved genuine workflow requirements remain. One form draft is still unsubmitted.
