# Public status update — 2026-09-17

Deutsch: [Öffentliches Status-Update](./2026-09-17-public-status_DE.md)

## Summary

The nightly publisher remains paused. This is a human-reviewed update covering the work from September 15–16 and the current early-September-17 state.

The project made real progress in three areas: the OpenAI AI-only path is now materially more independent and usable, the trade-memory contract has been unified across Paper / Watch / Research / OpenAI, and several WebUI projection defects were fixed. At the same time, one important runtime problem is still open: a research runtime data-refresh path can fail even while a shared market-data source remains fresh. A strict fallback through the existing shared reader was being implemented, but final acceptance proof was still pending.

Training and Factory remain intentionally paused. Live trading remains disabled and real capital remains zero.

## OpenAI AI-only Market Analyst V2

The OpenAI path was substantially revised without creating a second architecture, queue, evaluator or writer.

### Fixed data-freshness root cause

A real defect was found in the freshness check: signal age and underlying market-data freshness were not sufficiently separated.

The repaired V2 path separates those concepts and uses current Futures market data for technical availability.

### Independent analysis contract

The V2 acceptance report records independent analysis, rejection of local directional hints before the external-model call, and use of broader-market context only. Exact market lists and prompt-field contracts are intentionally omitted.


The flow is now:

`fresh market data → independent analysis → conditional scenarios → controlled simulation → outcome → evidence`

### Multi-scenario model

The current private analysis contract can express multiple machine-readable scenarios such as range fades, trend pullbacks, continuations, breakout/breakdown, failed breakout/breakdown, reversals and NO_TRADE.

Each scenario carries machine-readable conditions and lifecycle metadata; exact execution fields are intentionally not published.

The first real V2 proof completed without schema errors or real orders. Exact market/scenario counts are intentionally omitted.


Later in the same work session, additional simulated outcomes were observed. Exact symbols, trade counts and position details are intentionally omitted.

### Cadence / cost control

The new cadence is event-aware and rate-limited. Exact timing thresholds, retry markers and paid-call scheduling rules are intentionally not published.


This prevents a blocked attempt from postponing the next required analysis.

The external-model integration remained budget-controlled. Exact model-routing and cost configuration are intentionally not published.

### Open-position exclusion

The OpenAI path enforces duplicate-exposure controls during simulated monitoring; exact symbol-level rules are intentionally not published.

## Unified trade-memory contract

Paper, Watch, Research Forward and OpenAI now use the same existing capture path for the information needed to compare and learn from executed trades.

The unified evidence contract preserves enough identity, provenance, outcome and cost context for later comparison, while exact field names and schema details are intentionally not published.


At the recorded checkpoint, the checked evidence populations had the required public-facing integrity. Historical unknowns remain explicitly unknown rather than being invented. Exact row counts, field names, schema labels and internal ledger names are intentionally not published.

## WebUI / Trade-Like-CHE improvements

Several visible defects were real projection/UI problems rather than missing trade data.

### Trade-Like-CHE entry price

A stored entry existed but a projection alias mismatch prevented the UI from reading it correctly. The projection was corrected; the exact symbol, price and field names are intentionally not published.

### ADX / indicator display

An indicator-presentation defect was corrected and a causal display metric was added for analysis. Exact indicator wiring and feature eligibility are intentionally not published.

A natural cycle confirmed the corrected display path across the checked variants.

### Compact IDs / table layout

Audit identifiers remain available internally while public tables use compact display forms. Exact identifier layouts and internal table mappings are intentionally not published.

### Capture and NO_TRADE projection

Two additional projection defects were found and corrected in the existing path. Exact internal aliases and ledger mappings are intentionally not published.


Both were corrected in the existing projection path and regression tests were reported green. Final end-to-end browser verification was interrupted by the subsequent start/runtime problem described below.

## Runtime / start-path issue still open

A runtime/start-path issue remained open. The repair keeps a single governed data path and requires fresh restart plus forward-cycle proof before closure. Exact executable names, transport errors and fallback mechanics are intentionally not published.

## Project independence / Codex boundary

AlgoSphere must run without Codex. Codex is used to understand, repair and test the project, not as a required runtime/trading controller. Recent work preserved that boundary: no second runtime helper layer, no second memory pipeline, no second OpenAI evaluator and no new queue subsystem were introduced.

## ML / Factory / test-suite state

Broad training and Factory remain paused. The existing lifecycle contract remains:

`HYPOTHESIS → QUICK → ROBUST_OOS → CHALLENGER → PAPER → CHAMPION`

Rule evidence must remain independent from ML-selector success: ML selector collapse is not Rule failure.

Focused regression suites passed across the affected areas. A complete project-wide suite still remained an explicit verification item; exact test counts are intentionally omitted.

## What is materially better now

- OpenAI analysis is genuinely separated from local directional bias.
- Fresh candle state is no longer supposed to be rejected because a signal object is older.
- OpenAI has a flexible multi-scenario plan instead of one rigid immediate-direction answer.
- Paid-call cadence is tied to the last successful call, not blocked attempts.
- Open symbols are excluded from duplicate OpenAI entry analysis.
- Paper / Watch / Research / OpenAI executed trades share one comparable memory contract.
- Unknown historical values are explicitly typed instead of being treated as zero.
- Trade-Like-CHE entry-price projection was repaired.
- ADX is available for new decisions as an analysis/display value.
- IDs and large tables are more readable.
- NO_TRADE and Capture projection bugs were identified and corrected in the existing data/UI path.

## What remains open

1. Finish and prove the Research Forward market-data fallback without introducing a second data path.
2. Prove start-path behavior clearly for both already-running and stopped/orphaned states.
3. Complete the broad isolated-browser audit of Cockpit, Trading, OpenAI and Research after the runtime is stable.
4. Recheck Forecast propagation and Research open-position visibility after restart; the work log had not yet recorded final closure.
5. Re-verify Capture and NO_TRADE in the running browser after the runtime fix.
6. Accumulate enough causal OpenAI V2 outcomes to judge whether the new analyst actually improves trading results.
7. Configure a verified model-price source before publishing exact OpenAI USD cost estimates.
8. Rerun the complete project test suite and close/classify the earlier 64 full-suite failures.
9. Keep Training and Factory paused until the runtime/evidence path is stable enough to resume the corrected lifecycle.
10. Keep Live disabled and real capital at zero.

## Safety boundary

`LIVE=false` · `REAL_CAPITAL=0` · `ORDERS=0` · Training paused · Factory paused.

No documentation update authorizes live trading, automatic model promotion or real-capital execution.

[Current status](../CURRENT_STATUS.md) · [Roadmap](../docs/progress/ROADMAP.md) · [Completed work](../docs/progress/COMPLETED_WORK.md) · [Test results](../docs/verification/TEST_RESULTS.md)
