# Current public roadmap

Publication: **2026-09-17**. This is the human-reviewed roadmap while the nightly publisher remains paused.

## Current lifecycle contract

The intended training lifecycle remains:

`HYPOTHESIS → QUICK → ROBUST_OOS → CHALLENGER → PAPER → CHAMPION`

`candidate_eligible` is eligibility / artifact metadata. It is **not** a separate operating stage.

A Rule artifact that passes its own evidence must remain preserved even if an ML selector rejects or selects nothing useful. **ML selector collapse is not Rule failure.**

## P0 — runtime / data path before retraining

- **OPEN · 2026-09-17:** Finish and prove the Research Forward `WinError 10013` recovery through the existing shared market-data reader.
- **OPEN · 2026-09-17:** Allow the centrally confirmed 1-minute Futures hot-file tail only after strict freshness/availability validation when the direct socket fails.
- **OPEN · 2026-09-17:** Reject stale local files; do not create a second reader or parallel market-data path.
- **OPEN · 2026-09-17:** Prove `START_ALGOSPHERE.cmd` clearly in both already-running and genuinely stopped/orphaned states.
- **OPEN · 2026-09-17:** Complete the isolated-browser audit of Cockpit, Trading, OpenAI and Research after runtime stability is restored.
- **OPEN · 2026-09-17:** Recheck Forecast propagation and Research open-position visibility after the runtime restart.
- **OPEN · 2026-09-17:** Re-verify Trade-Like-CHE Capture and OpenAI NO_TRADE in the running browser after the runtime fix.

## P0 — OpenAI AI-only V2

- **ACTIVE / NEEDS OUTCOMES · 2026-09-17:** Keep `OPENAI_AI_MARKET_ANALYST_V2` independent from local Rule / ML / Watch / Research / Paper directional bias.
- **ACTIVE / NEEDS OUTCOMES · 2026-09-17:** Continue local monitoring of armed scenarios and open positions under the existing Paper path.
- **OPEN · 2026-09-17:** Accumulate multiple completed causal V2 outcomes before making any performance claim.
- **OPEN · 2026-09-17:** Keep one-open-position-per-symbol exclusion and block duplicate OpenAI entry analysis while a symbol is open.
- **OPEN · 2026-09-17:** Keep paid-call cadence tied to `last_successful_paid_call`, not blocked attempts.
- **OPEN · 2026-09-17:** Configure a trusted model-price source before publishing exact OpenAI USD cost estimates.

## P0 — unified trade memory / evidence

- **IMPLEMENTED / NEEDS PROSPECTIVE PROOF · 2026-09-17:** Maintain one executed-trade memory contract across Paper, Watch, Research Forward and OpenAI.
- **IMPLEMENTED / NEEDS PROSPECTIVE PROOF · 2026-09-17:** Keep unknown historical values explicit (`PENDING_PATH_SETTLEMENT`, `NOT_APPLICABLE`, `NOT_RECONSTRUCTABLE`) instead of coercing them to zero.
- **OPEN · 2026-09-17:** Continue proving the unified contract prospectively on new natural trades, not only repaired/backfilled records.
- **OPEN · 2026-09-17:** Preserve the separation between `openai_market_evaluations` and actual executed OpenAI trades.

## P0 — ML / Factory

- **PAUSED · 2026-09-17:** Broad training remains intentionally paused.
- **PAUSED · 2026-09-17:** Factory / hypothesis producer remains intentionally paused.
- **OPEN · 2026-09-17:** Preserve Rule evidence independently from ML-selector success.
- **OPEN · 2026-09-17:** Resume QUICK only after runtime/data/evidence paths are stable and under the corrected Rule/history/threshold contract.
- **OPEN · 2026-09-17:** Run genuine ROBUST_OOS only after QUICK evidence is valid and sufficiently dense.
- **OPEN · 2026-09-17:** Promote to CHALLENGER only after ROBUST_OOS PASS; no shortcut from QUICK to Paper/Live.

## P0 — full verification

- **OPEN · 2026-09-17:** Rerun the complete project test suite after the runtime/data-source repair.
- **OPEN · 2026-09-17:** Explicitly close or classify the earlier full-suite failures instead of treating focused green suites as global acceptance.
- **OPEN · 2026-09-17:** Preserve the distinction between focused regression PASS, runtime acceptance and scientific/profitability evidence.

## P1 — WebUI / operator usability

- **IMPLEMENTED / NEEDS FINAL BROWSER PROOF · 2026-09-17:** Compact full SHA/decision/trade/outcome IDs into readable suffixes while keeping full IDs in tooltips/details.
- **IMPLEMENTED / NEEDS FINAL BROWSER PROOF · 2026-09-17:** Keep table typography and spacing consistent across active/closed trades, Watch/Research, OpenAI, strategies and candidates.
- **IMPLEMENTED / NEEDS FINAL BROWSER PROOF · 2026-09-17:** Keep Trade-Like-CHE entry-time/entry-price aliases mapped correctly.
- **IMPLEMENTED / NEEDS FINAL BROWSER PROOF · 2026-09-17:** Keep ADX as display/analysis data only until explicitly promoted to a modeling feature.
- **OPEN · 2026-09-17:** Finish Cockpit clipping/scrolling/table-height/open-position consistency review.
- **OPEN · 2026-09-17:** Finish OpenAI large-table/layout review and Forecast visibility check.
- **OPEN · 2026-09-17:** Finish Research open/closed status consistency review.

## P1 — research quality and learning

- **OPEN · 2026-09-17:** Continue settling Research counterfactuals at 15m / 45m / 1h / 3h / 8h.
- **OPEN · 2026-09-17:** Expand Strategy × Coin × Side × Regime × Volatility × Outcome learning once enough clean observations exist.
- **OPEN · 2026-09-17:** Measure whether unified/canonical memory materially changes later selection before claiming a complete self-learning loop.
- **OPEN · 2026-09-17:** Keep Local ML Canaries clearly labelled as observation/counterfactual paths rather than real position-management paths.

## P1 — publication / evidence

- **PAUSED · 2026-09-17:** Automatic nightly publication remains stopped by the operator.
- **OPEN · 2026-09-17:** Repair nightly source selection before re-enabling it so current engineering evidence is not replaced by stale narrative.
- **OPEN · 2026-09-17:** Keep public status human-reviewed while the nightly publisher is paused.

## P2 — later / distribution work

Lower priority until runtime/data/trading/research truth is stable:

- installer/distribution cleanup
- secure credential storage
- demo/client packaging
- retention/root cleanup
- approved model-bundle loading
- public documentation/disclaimer polish
- broader hardware/resource optimization

## Current safety boundary

`LIVE=false` · `REAL_CAPITAL=0` · `ORDERS=0`

Training paused · Factory paused · no automatic promotion.

[Current status](../../CURRENT_STATUS.md) · [Reviewed September 17 update](../../updates/2026-09-17-public-status.md) · [Completed engineering work](COMPLETED_WORK.md) · [Test results](../verification/TEST_RESULTS.md)
