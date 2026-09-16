# Public status update — 2026-09-17

Deutsch: [Öffentliches Status-Update](./2026-09-17-public-status_DE.md)

## Summary

The nightly publisher remains paused. This is a human-reviewed update covering the work from September 15–16 and the current early-September-17 state.

The project made real progress in three areas: the OpenAI AI-only path is now materially more independent and usable, the trade-memory contract has been unified across Paper / Watch / Research / OpenAI, and several WebUI projection defects were fixed. At the same time, one important runtime problem is still open: Research Forward can fail on a direct Bitget socket refresh with `WinError 10013` even while the central market-data loader already has fresh 1-minute Futures data. A strict fresh-data fallback through the existing shared reader was being implemented, but the attached work log does not yet contain a final acceptance proof for that repair.

Training and Factory remain intentionally paused. Live trading remains disabled and real capital remains zero.

## OpenAI AI-only Market Analyst V2

The OpenAI path was substantially revised without creating a second architecture, queue, evaluator or writer.

### Fixed data-freshness root cause

A real defect was found in the freshness check: the age of an already-computed signal was mixed up with the freshness of the underlying Bitget candles. This could mark genuinely fresh Futures data as `TECHNICAL_UNAVAILABLE` simply because the signal object itself was around 100 seconds old.

The repaired V2 path separates those concepts and uses current Futures market data for technical availability.

### Independent analysis contract

The V2 acceptance report records:

- independent analysis: PASS
- local direction included in prompt: NO
- Rule / ML / Watch / Research / Trade-Like-CHE / Paper direction fields are rejected before the API call
- BTC and ETH are context only
- active analysis universe: ADA, ENA, MYX, ONDO, TUT

The flow is now:

`fresh Futures data → independent OpenAI analysis → conditional scenarios → existing local Paper monitor → confirmed trigger → local position management → settlement → existing OpenAI memory`

### Multi-scenario model

The new `OPENAI_AI_MARKET_ANALYST_V2` / `STRICT_INDEPENDENT_MULTI_SCENARIO_JSON_SCHEMA_V2` contract can express multiple machine-readable scenarios such as range fades, trend pullbacks, continuations, breakout/breakdown, failed breakout/breakdown, reversals and NO_TRADE.

Each scenario carries trigger logic, entry zone, invalidation, emergency stop, two targets, runner condition, expiry and stable identity.

The first real V2 proof reported:

- 5 coin analyses
- 9 scenarios in the cycle
- 6 armed scenarios under local monitoring
- 0 schema errors
- 0 real orders

Later in the same work session, the unified-memory audit reported three current executed OpenAI AI-only trades in the current-trade set and one open TUTUSDT position under monitoring. The exact profitability of the new V2 contract is still not proven; several completed causal V2 outcomes are required before making a performance claim.

### Cadence / cost control

The new cadence is event-aware:

- local check about every 5 minutes
- paid call on a relevant event or at most after 30 minutes
- minimum 5-minute gap between paid calls
- blocked attempts update `last_blocked_attempt` only
- refresh timing is based on `last_successful_paid_call`

This prevents a blocked attempt from postponing the next required analysis.

The model reported in the V2 acceptance state is `gpt-5.6-luna`. Call and token budgets remain active. A trustworthy USD cost estimate is not shown because no confirmed local model-price configuration existed in the project at that checkpoint.

### Open-position exclusion

The OpenAI path now enforces at most one open OpenAI position per symbol. Once a symbol enters, competing scenarios from that analysis cycle are blocked and the symbol is excluded from new OpenAI entry analysis until close/settlement. Local monitoring continues during the open position.

## Unified trade-memory contract

Paper, Watch, Research Forward and OpenAI now use the same existing capture path for the information needed to compare and learn from executed trades.

The contract includes:

- stable trade / strategy / setup identifiers
- role / strategy family
- symbol / side
- entry and exit timestamps and real prices
- market phase
- expected net with source and status
- MFE / MAE and timestamps
- fees, slippage, funding and net result
- stop, target and exit reason
- entry / exit data quality
- market-data provenance
- margin / notional where source evidence exists

At the recorded checkpoint, the current executed-trade sets had zero missing required core fields:

- Paper market-context: 35
- Watch: 19
- Research Forward: 28
- OpenAI AI-only: 3

All 66 previously executed OpenAI AI-only outcomes were also reported with trade identity, strategy, setup, market phase and MFE/MAE timing.

For 38 very old OpenAI trades, `source_margin_usdt` remains unknown because the original entry evidence contained no margin, notional or leverage. Those values are intentionally not invented. Unknown values now carry explicit states such as `PENDING_PATH_SETTLEMENT`, `NOT_APPLICABLE` or `NOT_RECONSTRUCTABLE` instead of silently becoming zero.

The 854 `openai_market_evaluations` remain analyses/counterfactuals, not executed trades, and therefore do not receive fake execution fields.

## WebUI / Trade-Like-CHE improvements

Several visible defects were real projection/UI problems rather than missing trade data.

### Trade-Like-CHE entry price

The ONDOUSDT entry existed in storage (`0.3391`), but the repository exposed `entry_price` / `opened_at` while the UI expected `entry_price_raw` / `entry_time`. The projection now exposes the expected aliases and keeps safe fallbacks.

### ADX / indicator display

A negative Volume-Z value previously colored the entire indicator cell red, incorrectly making ADX / ATR / RSI look negative. Indicator presentation was separated. ADX was also added as a causal display/analysis metric from closed 5-minute Futures candles. It is not currently an ML or entry feature.

A natural cycle reported 40/40 current variants with numeric ADX and zero missing ADX values.

### Compact IDs / table layout

Full SHA / decision / trade / outcome IDs remain available for audit, tooltip and detail views, while visible tables now show compact suffixes. The same rendering rule was applied across active/closed trades, Watch/Research, OpenAI, strategies and candidates.

### Capture and NO_TRADE projection

Two additional display/data-projection bugs were found late in the session:

- Trade-Like-CHE `Capture` used an unpopulated alias even though the canonical net-return value existed.
- OpenAI `NO_TRADE` read only the evaluations ledger while many valid NO_TRADE predictions were stored in the canonical prediction ledger.

Both were corrected in the existing projection path and regression tests were reported green. Final end-to-end browser verification was interrupted by the subsequent start/runtime problem described below.

## Runtime / start-path issue still open

The user-visible start problem had two layers:

1. `START_ALGOSPHERE.cmd` can appear to do nothing when the supervisor is already healthy because duplicate startup is intentionally refused. The start path was being adjusted to make that state visible and open the WebUI instead of failing silently.
2. More importantly, Research Forward was observed starting and then failing on the first ADAUSDT direct Bitget refresh with `WinError 10013`.

At the same time, the central market-data loader already had fresh 1-minute Futures data. The intended repair is to keep one shared reader and, only when the direct socket fails, allow the existing reader to use the centrally confirmed hot-file tail after strict freshness/availability checks. Stale files must still be rejected.

The attached work log ends while this fallback is being designed. **This runtime/data-source repair must therefore remain OPEN until a fresh restart plus Research Forward cycle proves it.**

## Project independence / Codex boundary

AlgoSphere must run without Codex. Codex is used to understand, repair and test the project, not as a required runtime/trading controller. Recent work preserved that boundary: no second runtime helper layer, no second memory pipeline, no second OpenAI evaluator and no new queue subsystem were introduced.

## ML / Factory / test-suite state

Broad training and Factory remain paused. The existing lifecycle contract remains:

`HYPOTHESIS → QUICK → ROBUST_OOS → CHALLENGER → PAPER → CHAMPION`

Rule evidence must remain independent from ML-selector success: ML selector collapse is not Rule failure.

The focused regression suites from the September 16 work were strong (263/263 around OpenAI V2, 264 relevant tests around unified memory, 154 focused tests around ADX/display, plus smaller focused suites). These are meaningful checks, but they do **not** prove that the earlier full-suite checkpoint of 1,307 tests / 64 failures has been completely closed. Full-suite hygiene remains an explicit open verification item until the complete suite is rerun and every previous failure is resolved or intentionally classified.

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

1. Finish and prove the Research Forward `WinError 10013` market-data fallback without introducing a second data path.
2. Prove `START_ALGOSPHERE.cmd` behavior clearly for both already-running and stopped/orphaned states.
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
