# Current public status

Publication date: **2026-09-17**. This is a human-reviewed status while the nightly publisher remains paused.

## Current operating boundary

- Training: **PAUSED**
- Factory / hypothesis producer: **PAUSED**
- Live trading: **No**
- Real capital: **0**
- Automatic promotion: **No**
- OpenAI model in latest V2 acceptance: `gpt-5.6-luna`
- OpenAI prompt contract: `OPENAI_AI_MARKET_ANALYST_V2`
- WebUI source version later reported in the same work session: `90.8.10.184`
- Safety boundary remains fail-closed.

The project is still intentionally not resuming broad ML training. The current priority is to finish and prove the runtime/data/evidence path first.

## What is materially better now

### OpenAI AI-only V2

The OpenAI branch has moved from a rigid directional flow to an independent multi-scenario analyst:

- current Futures data is used for technical availability,
- local Rule / ML / Watch / Research / Paper direction fields are rejected before the API call,
- BTC and ETH are context only,
- active analysis symbols are ADA / ENA / MYX / ONDO / TUT,
- multiple conditional scenarios can be armed and monitored locally,
- paid-call cadence is based on the last successful call rather than blocked attempts,
- one open OpenAI position per symbol is enforced,
- open symbols are excluded from duplicate OpenAI entry analysis until close/settlement.

The first real V2 proof reported 5 coin analyses, 9 scenarios, 6 armed scenarios, 0 schema errors and 0 real orders. Later in the same work session the unified-memory audit reported 3 current executed OpenAI AI-only trades and one open TUTUSDT position under monitoring.

The important boundary is unchanged: the profitability of the new V2 analyst is **not yet proven**. It needs multiple completed causal V2 outcomes.

### Unified executed-trade memory

Paper, Watch, Research Forward and OpenAI now use one existing capture path for comparable executed-trade evidence.

Current required fields include stable trade/strategy/setup identity, symbol/side, real entry/exit time and price, market phase, expected-net source/status, MFE/MAE with timestamps, costs, stop/target/exit reason, data-quality/provenance and margin/notional where source evidence exists.

At the recorded checkpoint, current executed-trade sets had 0 missing required core fields:

- Paper market-context: 35
- Watch: 19
- Research Forward: 28
- OpenAI AI-only: 3

All 66 previously executed OpenAI AI-only outcomes were also reported with trade identity, strategy, setup, market phase and MFE/MAE timing.

Unknown historical values are no longer silently treated as zero. Explicit states such as `PENDING_PATH_SETTLEMENT`, `NOT_APPLICABLE` and `NOT_RECONSTRUCTABLE` are used instead.

### WebUI / projection repairs

The following were repaired or improved:

- Trade-Like-CHE entry price/time alias mismatch,
- ADX added as causal display/analysis data from closed 5-minute Futures candles,
- negative Volume-Z no longer paints the whole indicator cell red,
- compact ID rendering across trade/research/OpenAI/strategy tables,
- larger/more readable table typography without exposing full hashes,
- Trade-Like-CHE Capture projection repaired to use the canonical outcome value,
- OpenAI NO_TRADE projection corrected to include the canonical prediction ledger instead of only the evaluation ledger.

The broader Cockpit / Trading / OpenAI / Research layout audit was still in progress when the runtime problem below interrupted final verification.

## Important runtime problem still open

The most important remaining blocker from the latest work log is not a trading rule problem but a runtime/data-source problem.

Research Forward was observed starting and then failing on the first ADAUSDT direct Bitget refresh with:

`WinError 10013`

At the same time, the central market-data loader already had fresh 1-minute Futures data.

The intended repair stays inside the existing shared reader: if the direct socket fails, the reader may use the centrally confirmed hot-file tail only after strict freshness and availability checks. Stale files must still be rejected. No second market-data reader or parallel data path should be introduced.

The attached engineering log ends while this fallback is being designed. **This fix is therefore not yet accepted as complete.** It needs a successful restart plus a fresh Research Forward cycle without the socket failure.

## START_ALGOSPHERE behavior

Another user-visible issue was clarified: when the supervisor is already healthy, `START_ALGOSPHERE.cmd` can intentionally refuse a duplicate launch and return successfully, which looks like "nothing happened" to the user. The start path was being adjusted so an already-running healthy state becomes visible and opens the WebUI instead of appearing to fail silently.

That behavior still needs final proof together with the runtime/socket fix.

## OpenAI cost control

The project is tracking call/hour/day/token budgets. In the latest V2 acceptance state the project intentionally did not display an exact USD cost because no trusted local price configuration for `gpt-5.6-luna` was present.

Exact USD cost reporting remains open until a verified model-price source is configured.

## ML / Factory status

Training and Factory remain intentionally paused.

The current lifecycle contract remains:

`HYPOTHESIS → QUICK → ROBUST_OOS → CHALLENGER → PAPER → CHAMPION`

`candidate_eligible` remains metadata/eligibility, not a separate stage.

Rule evidence must be preserved independently from ML selector success. **ML selector collapse is not Rule failure.**

The work from September 16 did not reopen Training or Factory.

## Test / verification state

Focused regression results from the latest work are strong:

- OpenAI V2 related suite: 263/263 PASS
- unified-memory related relevant suite: 264 PASS
- final focused post-memory changes: 121 PASS
- ADX/display focused suite: 154 PASS
- Trade-Like-CHE entry projection focused suite: 22 PASS
- compact-table WebUI focused suite: 14 PASS

These focused results are useful evidence, but they do **not** by themselves prove that the earlier full-suite checkpoint with 1,307 tests / 64 failures is fully closed. A complete suite rerun and explicit classification of all earlier failures remains open.

## Current priorities

1. Finish and prove the Research Forward `WinError 10013` fallback through the existing shared reader.
2. Prove `START_ALGOSPHERE.cmd` for both already-running and genuinely stopped/orphaned states.
3. Complete the isolated-browser audit of Cockpit, Trading, OpenAI and Research after runtime stability is restored.
4. Recheck Forecast propagation and Research open-position visibility after restart.
5. Re-verify Capture and NO_TRADE in the running browser after the runtime fix.
6. Accumulate several causal OpenAI V2 settlements before judging performance.
7. Configure trusted model pricing before publishing exact OpenAI USD costs.
8. Rerun the complete project test suite and close/classify the earlier full-suite failures.
9. Keep Training / Factory paused until runtime and evidence paths are trustworthy.
10. Keep Live disabled and Real Capital at 0.

## Publication note

The automatic nightly publisher remains paused by the operator. This status and the September 17 updates are human-reviewed so newer engineering work is not overwritten by stale narrative selection.

See the [reviewed September 17 update](updates/2026-09-17-public-status.md), [roadmap](docs/progress/ROADMAP.md), [completed engineering work](docs/progress/COMPLETED_WORK.md) and [test results](docs/verification/TEST_RESULTS.md).
