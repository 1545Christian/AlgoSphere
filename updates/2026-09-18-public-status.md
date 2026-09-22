# Public status update — 2026-09-18

Deutsch: [Öffentliches Status-Update](./2026-09-18-public-status_DE.md)

## Summary

September 18 closed several items that were still open in the September 17 public status.

The most important changes are:

- Trade Like Che Context V2 is now active in Research Forward Shadow with the new 34-strategies-per-coin contract and a confirmed 170/170 health check.
- Paper Context V2 Shadow remains active and continued without interruption during the Research Forward activation.
- The WebUI now aggregates all open Paper / Watch / Research Forward / OpenAI positions into one open-positions view and loads substantially less overview data.
- Research & Models now has an operator-controlled training surface instead of only passive status.
- A full-history ENA one-coin pilot completed successfully as an execution test, but the ML result was **DEGRADED** versus the Rule baseline and was correctly not promoted.
- The read-only Market Intelligence Robustness Gate is implemented and remains evidence-gated.
- OpenAI AI-only now receives the missing 3D / 7D and explicit structure/support-resistance context plus open-position context.
- The current OpenAI request path is being compacted because the last measured full request was unnecessarily large; this refactor is **not yet forward-proven**.
- A legacy-system audit found no mandatory old component blocking the ENA pilot, but several useful areas remain only partially represented in the current system.

Live trading remains disabled. Real capital remains zero. Automatic promotion remains disabled.

## Research Forward / Trade Like Che Context V2

The Context V2 runtime contract is now active.

Current contract:

- 5 active coins
- 26 CURRENT strategy evaluations per coin
- 8 CONTEXT_V2 evaluations per coin
- 34 total evaluations per coin
- 170 expected evaluations in total
- 170 confirmed active evaluations

Runtime health: **PASS**

Fresh Context V2 Shadow decisions are visible, including explicit `NO_TRADE / NO_CURRENT_SETUP` evidence. CURRENT and CONTEXT_V2 remain separated in the runtime projection.

Only Supervisor and Research Forward were minimally reloaded for this activation. Paper Context V2, Point13, OpenAI and Market Data were not interrupted.

## WebUI and operator usability

A major projection and performance repair was completed.

The global open-positions view now includes open positions from:

- Paper
- Watch
- Research Forward
- OpenAI

The observed browser checkpoint showed 2 Paper, 1 Watch, 2 Research Forward and 0 OpenAI open positions.

Performance also improved materially:

- 24h cold overview: about 2.61 s
- 24h warm overview: about 0.03 s
- 24h payload: about 0.74 MB instead of 4.79 MB
- roughly 84.5% less overview payload

Detailed evidence is now loaded on demand instead of being forced into the main overview response.

The broader information architecture is still considered too dense and a later redesign remains open, but the concrete missing/open-position projection defects were repaired.

## Market Intelligence and ENA pilot

The Market Intelligence V2.1 research path remains based on:

- 3 existing feature arms
- 4 architecture variants
- 7 horizons
- a private model family
- a private model family
- causal OOS evaluation
- Rule-baseline preservation

The explicit single-market pilot completed with full-history readiness, causal OOS evaluation and matched Rule/ML comparison. Exact row counts, architecture counts, horizon counts, folds and registry identifiers are intentionally not published.


The scientific result is intentionally not presented as a success:

`RULE_VS_ML = DEGRADED`

Therefore:

- `candidate_eligible = false`
- Challenger eligibility = false
- promotion allowed = false
- Rule artifact preserved = yes

This is an important outcome: the pipeline now preserves and exposes a negative ML result instead of converting technical completion into a promotion.

## Robustness Gate

A versioned read-only Robustness Gate is implemented between OOS Candidate evidence and later Challenger eligibility.

It checks evidence dimensions including multi-fold walk-forward, recent OOS, coin/state/horizon/feature stability, cost stress, calibration, tail risk and sample support. Optional dimensions include small controlled ablation, parameter-neighborhood and data-perturbation checks.

No automatic promotion is performed.

The gate must now be evaluated against the newer full-history single-market pilot evidence. A completed training run is not automatically equivalent to `ROBUST_OOS_READY`.

## Canonical Memory and lifecycle

The current chain is substantially implemented:

`Decision → Trade → Outcome → Canonical Memory → Learning → Lifecycle`

but the audit still found real gaps:

- historical Decision → Trade linkage is incomplete for some older outcomes
- Memory → Learning is only available for eligible evidence
- per-trade Learning Delta is not yet visible
- CURRENT vs CONTEXT_V2 separation is complete in runtime, but still only partial in Canonical Memory
- promotion-history persistence is partial
- Challenger is not an active operational promotion state
- Champion is currently mainly a frozen Paper fallback rather than a newly promoted model

Paper remains operational and simulated. No real-capital Champion exists.

## Legacy audit

The older Preisvorhersage / AlgoSphere code and historical evidence were compared with the current system.

The current implementation was judged stronger for:

- full-history / OOS governance
- walk-forward leakage protection
- Rule-vs-ML separation
- artifact and feature-hash contracts
- trade evidence
- signal/trade identity
- exit / MFE / MAE tracking

No mandatory legacy capability was found that blocks the completed single-market pilot.

Still partial and worth later research:

- Telegram / manual-signal provenance
- explicit 1m / 5m / 15m entry confirmation
- persistent Pending / Recheck behavior
- canonical import of old manual trades with prior-signal provenance
- Recency weighting as a research comparison, not as an automatic migration

Old model artifacts remain historical evidence and are not treated as current compatible models.

## OpenAI AI-only

The OpenAI input-contract audit identified missing higher-timeframe, structure and position-context information. Exact timeframe and prompt-field composition are intentionally not published.

The minimal input patch now provides multi-timeframe context, broader-market context, structure, volatility, news, aggregated learning context and current simulated-position context where applicable. Exact field composition is intentionally not published.


A reliable Futures/Spot basis source was not available and is therefore not fabricated.

A redacted request export was produced without a new paid call.

One important efficiency issue remains: the pre-compaction request was unnecessarily large. Exact token counts and per-market batching details are intentionally not published.

## What remains open

1. Complete the compact OpenAI request / single-plan contract and verify it on the next normal paid call without generating a test call.
2. Prove whether the OpenAI path produces better causal outcomes; current decision quality is not yet established.
3. Evaluate the new ENA pilot through the Robustness Gate instead of treating training completion as model quality.
4. Close the remaining Canonical Memory gaps: per-trade Learning Delta, full CURRENT/V2 separation, and promotion history.
5. Resolve the remaining legacy-partial areas only through controlled evidence/replay, not by copying old code.
6. Continue browser/UI simplification and table pagination/virtualization where large histories remain slow or dense.
7. Keep broad multi-coin training and automatic promotion blocked until evidence supports them.
8. Rerun / classify the complete project test suite when the current parallel work settles; focused green suites do not equal global scientific acceptance.

## Safety boundary

`LIVE=false` · `REAL_CAPITAL=0` · automatic promotion disabled.

The project remains research-first and fail-closed.

[Current status](../CURRENT_STATUS.md) · [Roadmap](../docs/progress/ROADMAP.md) · [Documented work](../docs/progress/COMPLETED_WORK.md) · [Test results](../docs/verification/TEST_RESULTS.md)
