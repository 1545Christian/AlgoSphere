# Current public roadmap

Publication: **2026-09-18**. Human-reviewed.

## Lifecycle contract

`HYPOTHESIS → QUICK → ROBUST_OOS → CHALLENGER → PAPER → CHAMPION`

`candidate_eligible` is eligibility metadata, not an operating stage.

Rule evidence remains preserved independently from ML-selector success.

## P0 — model quality and research closure

- **OPEN:** Evaluate the completed ENA one-coin pilot through the versioned Robustness Gate.
- **OPEN:** Explain the observed Rule-vs-ML degradation before any broader training run.
- **OPEN:** Keep broad multi-coin training blocked until comparable Rule/ML populations, OOS folds and evidence are valid.
- **OPEN:** Preserve negative ML results instead of treating technical run completion as model success.
- **OPEN:** Complete the currently running ML/Memory root-cause audit before changing the model stack again.

## P0 — Canonical Memory / continuous learning

- **OPEN:** Make per-trade Learning Delta explicit and visible.
- **OPEN:** Finish CURRENT / CONTEXT_V2 separation inside Canonical Memory, not only runtime projections.
- **OPEN:** Persist and expose promotion history consistently.
- **OPEN:** Keep Decision→Trade→Outcome→Memory→Learning identity complete for new prospective evidence.
- **OPEN:** Do not create training requests until evidence thresholds are genuinely met.

## P0 — OpenAI AI-only

- **IMPLEMENTED / NEEDS FORWARD PROOF:** 3D / 7D context, explicit structure/support-resistance and open-position context added.
- **OPEN:** Finish compact request projection and one-plan-per-symbol response contract.
- **OPEN:** Verify the compact contract only on the next normal paid call; do not generate a paid test call.
- **OPEN:** Reduce request size materially from the observed ~73.9k input-token baseline without removing causal decision context.
- **OPEN:** Accumulate causal settled outcomes before judging OpenAI trading quality.
- **OPEN:** Keep no second local trading-decision engine after OpenAI.

## P0 — Research Forward / Context V2

- **CLOSED:** Research Forward Context V2 activation.
- **CLOSED:** 34 evaluations per coin / 170 total health contract.
- **CLOSED:** Fresh V2 NO_TRADE evidence visible.
- **OPEN:** Continue prospective evidence collection while CURRENT and V2 remain separated.

## P1 — WebUI / operator usability

- **CLOSED:** Global open-position projection across Paper / Watch / Research Forward / OpenAI.
- **CLOSED:** Main overview payload and load-time reduction.
- **OPEN:** Simplify duplicated/dense page layouts.
- **OPEN:** Add server-side pagination / table virtualization for large histories.
- **OPEN:** Keep CURRENT, V2, Paper, Watch, Research and OpenAI semantics visibly distinct.
- **OPEN:** Keep the training operator explicit and manual; no hidden auto-start.

## P1 — legacy evidence / parity research

- **OPEN:** Determine canonical import contract for historical manual trades with prior-signal provenance.
- **OPEN:** Quantify Telegram signal provenance quality before using it as training evidence.
- **OPEN:** Compare legacy 1m/5m/15m entry confirmation through replay before adopting anything.
- **OPEN:** Compare persistent Pending/Recheck semantics through replay/state evidence.
- **OPEN:** Measure Recency Weighting as a research variant only; do not migrate legacy half-lives by default.
- **OPEN:** Keep old models as historical evidence only unless current feature/dataset/lifecycle compatibility is proven.

## P1 — verification

- **OPEN:** Rerun/classify the complete project test suite after current parallel work settles.
- **OPEN:** Keep focused regression PASS distinct from runtime acceptance and scientific evidence.
- **OPEN:** Preserve explicit failure / NEEDS_MORE_EVIDENCE states.

## P2 — later

Lower priority until research truth and lifecycle closure improve:

- broader multi-coin training
- automated promotion
- installer/distribution cleanup
- secure credential packaging
- demo/client packaging
- broader resource optimization
- documentation/file-name cleanup without breaking existing public links

## Safety boundary

`LIVE=false` · `REAL_CAPITAL=0` · automatic promotion disabled.

[Current status](../../CURRENT_STATUS.md) · [September 18 update](../../updates/2026-09-18-public-status.md) · [Completed work](COMPLETED_WORK.md) · [Test results](../verification/TEST_RESULTS.md)
