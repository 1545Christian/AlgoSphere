# Current public status

Publication date: **2026-09-14**. This is a human-reviewed status while the nightly publisher is paused. Runtime observations, implementation reports and acceptance proofs remain separate.

## Current operating boundary

- Training: **PAUSED**
- Factory / hypothesis producer: **PAUSED**
- Live trading: **No**
- Real capital: **0**
- Automatic promotion: **No**
- WebUI source version last reported: `v90_8_10_162`
- Application source version last reported: `v90_8_5`
- Safety boundary remains fail-closed.

The project is intentionally not resuming broad ML training yet. The current priority is to prove the active Paper / Watch / Research / OpenAI / Outcome / Memory path first.

## What is currently working

- Active Paper, Research Watch and Research Forward are running on current Futures data.
- The WebUI integrity/liveness defects were repaired: 1-hour liveness semantics, decision-time freshness, 7/7 signed baselines, proven live-input provenance and no observed historical fallback in the repaired acceptance report.
- Local trade outcome capture was repaired for **58 local 100-USDT trades**:
  - Active Paper 4/4 decision IDs linked
  - Research Watch 26/26
  - Research Forward 28/28
- The documented chain is now `Decision → Trade → Outcome → Canonical Memory` for that repaired set.
- Exit subreason, trailing state, MFE/MAE, post-exit 30m/60m/120m/horizon and learning classification were persisted for the repaired local set.
- The no-capital counterfactual path is authorized and visible in the runtime/WebUI.

## Expected-net / Research correction

The 0.30% expected-net guard remains a hard Paper protection.

The important correction is that Research no longer needs to forget a valid setup merely because expected net is not yet proven.

Current semantics:

- `NO_SETUP` → no setup, no observation required.
- `SETUP_MATCH + EXPECTED_NET_RETURN_UNPROVEN` → no Paper/Live trade, but preserve a no-capital counterfactual.
- `SETUP_MATCH + expected_net >= 0.30%` → may continue through normal Paper economics.

The initial counterfactual backfill created **49** observations. At the recorded checkpoint **13 were settled through 8h** and **36 were pending**.

## Missed-edge evidence

The latest forward-path audit found **49 unique blocked market setups**. Within that limited sample:

- 13 unique missed scalp opportunities (15–45m)
- 2 unique missed intraday opportunities (1–3h)
- 0 confirmed missed swing opportunities (3–8h)
- 4 adverse-first / bad-entry cases
- 15 cases where edge appeared only after excessive drawdown
- 15 unclear/pending cases

This does **not** mean the Paper guard should be weakened. It means Research must preserve blocked setups long enough to learn whether the block was correct.

## Market-phase / strategy-family learning

The current sample already shows that edge varies by regime and strategy family. Range and Up samples were stronger overall than Down / Strong-Down. `basis_dislocation` was particularly strong in the recorded Range sample; `volatility_scaled_momentum` held up better in Down than `relative_strength_pullback`.

These are research observations only, not production-rule changes.

## OpenAI AI-only status

The OpenAI process is technically alive under `OPENAI_AI_ONLY_FUTURES_PAPER_V1` with Futures-only pricing, 100-USDT canonical notional, its own position manager, horizon settlement and integrity PASS in the latest acceptance report.

However, the latest reviewed state had **no new natural AI-only fills**. The observed status was `OPENAI_AI_ONLY_PAPER_TICK_COMPLETE`.

Therefore the current truth is:

**OpenAI is running, but a fresh natural AI-only `decision → entry → managed exit → outcome → learning` chain is still not proven end to end.**

The earlier historical OpenAI comparison remains qualified because audits found stale per-coin context, Spot-related inputs, inherited local direction, immediate-entry assumptions and historical exit-time interpretation problems. The prospective path was rebuilt to avoid those issues.

Still open in the OpenAI research layer:

- 45m and 8h horizon variants
- multi-horizon candidate variants
- `selected_variant_id`
- separately stored rejected variants
- full NO_TRADE missed-opportunity classification by horizon

## ML / Factory status

Training and Factory remain intentionally paused.

The recent ML root cause was not simply a bad model. The training/research contract had drifted from the earlier Rule contract: history length, thresholds and early filtering could reduce a historically active Rule to only a handful of signals before ML saw it.

ENAUSDT LONG `basis_dislocation` remains the key reference case. The older Rule contract was reproduced with a materially larger causal signal set and a reproducible OOS trade set.

The binding lesson is:

**ML selector collapse is not Rule failure. A Rule artifact that passes its own evidence must not be deleted because ML rejects or selects nothing useful.**

The intended lifecycle is now:

`HYPOTHESIS → QUICK → ROBUST_OOS → CHALLENGER → PAPER → CHAMPION`

`candidate_eligible` is metadata / eligibility, not a separate operating stage.

## Current priorities

1. Collect natural new Paper / Watch / Forward / counterfactual outcomes.
2. Prove the first complete natural OpenAI AI-only forward chain.
3. Continue settling the counterfactual backlog and measure which blocked setup families actually contain edge.
4. Use the repaired exit/post-exit evidence for later learning without changing exit parameters prematurely.
5. Preserve Rule evidence independently from ML selector success when training resumes.
6. Resume the corrected lifecycle only after the active trading/research paths are trustworthy.
7. Keep GitHub status human-reviewed while the nightly publisher is paused.

## Publication note

The previous nightly files on September 8–13 repeatedly carried older September 5/6 narrative because the source-selection layer did not ingest all recent engineering evidence. The nightly upload itself had been running, but the narrative was incomplete. It is currently paused by the operator to prevent another stale overwrite.

See the [reviewed September 14 update](updates/2026-09-14-public-status.md), [roadmap](docs/progress/ROADMAP.md) and [completed engineering work](docs/progress/COMPLETED_WORK.md).
