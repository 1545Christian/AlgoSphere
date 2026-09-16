# Documented engineering work

Items below are dated source reports and reviewed repair results. They are not a claim that every end-to-end requirement is closed.

## September 16 — reviewed engineering progress

### OpenAI AI-only Market Analyst V2

- Fixed a false stale-data classification where signal age was confused with underlying Bitget candle freshness.
- Verified independent OpenAI analysis: local Rule/ML/Watch/Research/Trade-Like-CHE/Paper direction fields are rejected before the API call.
- BTC/ETH are context only; active analysis coins are ADA, ENA, MYX, ONDO and TUT.
- Replaced the rigid OpenAI flow with `OPENAI_AI_MARKET_ANALYST_V2` and a strict multi-scenario JSON contract.
- Added machine-readable scenario support for range fade, pullback/rally, continuation, breakout/breakdown, failed breakout/breakdown, reversal and NO_TRADE.
- Scenario payload includes trigger, entry zone, invalidation, emergency stop, two targets, runner condition, expiry and stable IDs.
- Paid-call cadence now distinguishes successful calls from blocked attempts; blocked attempts no longer postpone the next max-age refresh.
- Added one-open-position-per-symbol exclusion so open coins remain locally monitored but are excluded from duplicate OpenAI entry analysis until settlement.
- First real V2 proof reported 5 coin analyses, 9 scenarios, 6 armed scenarios, 0 schema errors and 0 real orders.
- Existing runtime/storage architecture was extended; no second queue, evaluator, terminal writer or parallel database was introduced.
- OpenAI V2 relevant regression suite: **263/263 PASS**, plus Python compile, JavaScript syntax, real Bitget data fetch, real OpenAI V2 call and WebUI API check.

### Unified trade-memory contract

- Paper, Watch, Research Forward and OpenAI were unified onto the same existing executed-trade capture path.
- Current required fields now include IDs, role/strategy family, symbol/side, real entry/exit time and price, market phase, expected-net source/status, MFE/MAE with timestamps, costs, stop/target/exit reason, data quality/provenance and margin/notional when source evidence exists.
- Current executed-trade checkpoint reported 0 missing required core fields for:
  - Paper market-context: 35
  - Watch: 19
  - Research Forward: 28
  - OpenAI AI-only: 3
- All 66 previously executed OpenAI AI-only outcomes were reported with trade ID, strategy, setup, market phase and MFE/MAE timing.
- 38 very old OpenAI trades still have unknown `source_margin_usdt` because the historical source never recorded margin/notional/leverage; values were intentionally not invented.
- Unknown values now use explicit states such as `PENDING_PATH_SETTLEMENT`, `NOT_APPLICABLE` and `NOT_RECONSTRUCTABLE` instead of silently becoming zero.
- 854 `openai_market_evaluations` remain correctly separated as analyses/counterfactuals, not executed trades.
- Relevant unified-memory suite: **264 PASS**; final focused post-change suite: **121 PASS**; 0 reported failures in those focused runs.

### Trade-Like-CHE / WebUI fixes

- Fixed a Trade-Like-CHE projection mismatch where stored `entry_price` / `opened_at` were not mapped to UI fields `entry_price_raw` / `entry_time`.
- Productive ONDOUSDT proof showed recorded entry `0.3391` with matching effective entry.
- Added safe aliases/fallbacks for entry time and raw entry price.
- Added causal ADX calculation from closed 5-minute Futures candles as display/analysis data only; ADX is not an ML or entry feature.
- Fixed UI coloring so a negative Volume-Z value no longer paints ADX/ATR/RSI as negative.
- Natural decision round reported 40/40 current variants with numeric ADX and 0 missing ADX values.
- Compact ID rendering added globally: full IDs remain available for audit/tooltips/details while tables show readable suffixes.
- Desktop table typography/layout made more compact and readable across active/closed trades, Watch/Research, OpenAI, strategies and candidates.
- Late-session projection fixes identified and corrected:
  - Trade-Like-CHE Capture used an unpopulated alias despite canonical outcome data being present.
  - OpenAI NO_TRADE looked only at the evaluation ledger while valid NO_TRADE predictions also lived in the canonical prediction ledger.

### Runtime/start-path investigation

- Clarified that `START_ALGOSPHERE.cmd` can appear to do nothing when a healthy supervisor is already running because duplicate startup is intentionally refused.
- Start-path UX was being adjusted so an already-running state becomes visible and opens the WebUI rather than looking like a failed start.
- A more important runtime blocker was found: Research Forward could start and then fail on the first ADAUSDT direct Bitget refresh with `WinError 10013`.
- At the same time, the central market-data loader already had fresh 1-minute Futures data.
- The intended repair is to stay inside the existing shared reader and allow a centrally confirmed hot-file tail only after strict freshness/availability validation when the direct socket fails.
- This fallback does **not** yet have final acceptance proof in the attached work log and remains OPEN.

## September 14 — reviewed current repair state

- WebUI release/integrity tests repaired; reviewed status reported `INTEGRITY_STATUS = PASS`, `OPERATIONAL = true`, 7/7 signed baselines PASS.
- Liveness semantics corrected from an incorrect 72-hour default to the intended 1-hour window.
- Freshness projection corrected to evaluate data against the relevant decision timestamp rather than only the current clock.
- Local trade outcome capture repaired for **58 local 100-USDT trades**.
- Decision-ID linking repaired across Active Paper (4/4), Research Watch (26/26) and Research Forward (28/28).
- Exit subreason, trailing state, MFE/MAE, post-exit 30m/60m/120m/horizon and learning classification persisted for the repaired local set.
- Expected-net blocker traced to `VisiblePaperEngine._forward_fill`; 0.30% remains a hard Paper protection.
- Research semantics repaired so `SETUP_MATCH + EXPECTED_NET_RETURN_UNPROVEN` can be observed as a no-capital counterfactual instead of being discarded.
- Initial counterfactual backfill created **49** observations; **13** were settled through 8h and **36** were pending at the recorded checkpoint.
- Market-phase / missed-edge audit completed over 49 unique blocked setups; the audit found missed scalp/intraday opportunities as well as adverse-first and excessive-drawdown cases.
- Historical pseudo-edge rows without expected-net proof were reclassified and no longer presented as Paper-allowed.
- Fail-closed runtime authorization was updated specifically for no-capital Research Watch / Research Forward counterfactual observation.
- Runtime restart completed with Active Paper protection unchanged, Research Watch `ACTIVE_NO_CAPITAL`, Research Forward `WATCH_NO_CAPITAL`, and WebUI counterfactual visibility enabled.

## ML / Factory — current reviewed state

- Training remains intentionally paused.
- Factory / hypothesis producer remains intentionally paused.
- The current lifecycle remains `HYPOTHESIS → QUICK → ROBUST_OOS → CHALLENGER → PAPER → CHAMPION`.
- `candidate_eligible` is eligibility/artifact metadata, not a separate stage.
- Rule evidence must remain preserved independently from ML-selector success: ML selector collapse is not Rule failure.

## Earlier documented work

- **2026-09-05 · Implementation reported by source:** Windows checkpoint writes, reuse of completed phases and duplicate research-worker prevention were repaired in the V2 baseline.
- **2026-09-05 · Implementation reported by source:** `queue_id` / `factory_queue_id` identity defect repaired; new research core activated; 15 focused tests documented PASS.
- **2026-09-05 · Blocker:** real Factory→QUICK end-to-end proof remained open; one launch stopped at `FACTORY_QUICK_NO_ELIGIBLE_QUEUE_ROW` before expensive computation.
- **2026-09-06 · Publisher work:** GitHub Nightly v5.4.x installed with staged line-ending normalization, bounded report reading and coverage warnings.
- **2026-09-08–13 · Publication observation:** nightly upload itself ran, but the automatic narrative repeatedly carried older September 5/6 text because current repair/runtime evidence was not fully selected by the publisher.

[Current status](../../CURRENT_STATUS.md) · [Outstanding work](ROADMAP.md) · [Reviewed September 17 update](../../updates/2026-09-17-public-status.md)
