# Public status update — 2026-09-14

Deutsch: [Öffentliches Status-Update](./2026-09-14-public-status_DE.md)

## Summary

The last days were not about restarting broad ML training. They were about separating trading, research, counterfactual learning, OpenAI AI-only and canonical outcome memory cleanly enough that later training can learn from the right evidence.

The public nightly publisher is currently paused by the operator. This update is therefore a manually reviewed status based on the latest local acceptance and repair reports.

The most important correction is conceptual: **"do not trade" must not mean "do not observe and learn".** Paper still keeps the hard expected-net protection, while Research Watch / Research Forward can now preserve blocked setup matches as no-capital counterfactuals and settle them later across multiple horizons.

At the same time, the OpenAI AI-only process is alive, but it is **not yet proven as a complete natural forward-trade chain**. A `TICK_COMPLETE` heartbeat is not the same as a fresh AI-only fill, managed exit, outcome and learning cycle.

## Current operating boundary

- Training: **paused**
- Factory / hypothesis producer: **paused**
- Live trading: **disabled**
- Real capital: **0**
- Automatic promotion: **disabled**
- OpenAI remains independent from local ML direction
- No proven-rule thresholds or exit parameters were changed in the latest repair steps

The current priority is to prove the trading/research evidence path first, then resume the training lifecycle.

## Paper / Watch / Research: expected-net semantics repaired

The 0.30% expected-net guard was traced to `VisiblePaperEngine._forward_fill` with the canonical 12-bps cost model.

That protection is still correct for Paper / future Live. The problem was that the same blocker was effectively deleting Research setup matches before they could be observed.

The intended semantics are now:

- `NO_SETUP` → no setup exists; no counterfactual required.
- `SETUP_MATCH + expected_net unproven` → **no Paper/Live trade**, but preserve a no-capital counterfactual observation.
- `SETUP_MATCH + expected_net >= 0.30%` → may continue through normal Paper economics.

This keeps capital protection strict while preserving research information.

## No-capital counterfactual path

The new Research counterfactual path is now authorized in the fail-closed runtime.

Current documented state:

- Research Watch: `ACTIVE_NO_CAPITAL`
- Research Forward: `WATCH_NO_CAPITAL`
- 90 strategies loaded in Forward
- Paper promotion from counterfactuals: `false`
- WebUI counterfactual forward path: visible
- Live remains unchanged and disabled

The initial backfill created **49 counterfactuals**. At the recorded checkpoint, **13 were settled through 8h** and **36 were still pending**.

Each blocked setup can now be evaluated later at 15m / 45m / 1h / 3h / 8h together with MFE, MAE and cost-adjusted result without creating a capital trade.

## Missed-edge audit

The forward-path audit found that market opportunity existed even when Paper correctly refused to trade.

Across **49 unique blocked market setups**:

- 13 unique missed scalp opportunities (15–45m)
- 2 unique missed intraday opportunities (1–3h)
- 0 confirmed missed swing opportunities (3–8h)
- 4 bad-entry / adverse-first cases
- 15 cases where edge appeared only after too much drawdown
- 15 cases remained unclear/pending at the audit checkpoint

This confirms that some information was being lost by the research funnel even though Paper protection itself was doing its job.

## Market phase / strategy-family evidence

The same audit also showed that edge is not uniform across market phases.

Examples from the current limited sample:

- Range regimes were positive overall and `basis_dislocation` was especially strong in the recorded range sample.
- Up regimes were positive overall in the recorded sample.
- Down regimes were weaker overall; `volatility_scaled_momentum` held up better than `relative_strength_pullback`.
- Strong-down had little data and weak results.

These observations are research evidence, not yet production rules. The purpose is to preserve Strategy × Coin × Side × Regime × Outcome information for later training instead of flattening everything into one win/loss label.

## Local trade outcome / canonical memory repair

A separate gap existed in the local Paper/Watch/Forward outcome chain.

The latest repair linked **58 local 100-USDT trades** end-to-end:

- Active Paper: 4/4 decision IDs linked
- Research Watch: 26/26
- Research Forward: 28/28

The documented chain is now:

`Decision → Trade → Outcome → Canonical Memory`

For those 58 trades, the repair also persisted:

- exit subreason
- trailing state
- MFE / MAE
- post-exit 30m / 60m / 120m / horizon settlement
- learning classification

Historical values that cannot be reconstructed are shown explicitly as `NOT_CAPTURED` / `NOT_APPLICABLE` rather than invented.

## WebUI / current-truth fixes

Two real liveness projection defects were corrected:

1. the API default incorrectly used 72 hours instead of the intended 1-hour liveness window;
2. data freshness was checked against the current clock instead of the timestamp of the relevant decision.

The repaired WebUI report showed:

- integrity: `PASS`
- operational: `true`
- signed baselines: 7/7 PASS
- live-input provenance: proven
- historical fallback: not observed

Trade-management fields now expose captured entry/exit state, MFE/MAE, decision IDs, canonical outcome IDs, post-exit horizons and learning classifications. Missing source data is shown explicitly instead of being silently filled.

## OpenAI AI-only: alive, but still not fully proven

The OpenAI branch currently reports:

- policy: `OPENAI_AI_ONLY_FUTURES_PAPER_V1`
- Futures-only price basis
- canonical notional: 100 USDT
- position manager: `CAUSAL_FUTURES_MARKET_MANAGEMENT_V1`
- integrity: PASS
- horizon settlement and exit-too-early detection available

However, the latest status contained **no new natural AI-only fills**. The observed state was `OPENAI_AI_ONLY_PAPER_TICK_COMPLETE`.

Therefore the correct public statement is:

**the OpenAI process is running, but a fresh natural AI-only decision → entry → managed exit → outcome → learning chain is still pending proof.**

The earlier historical OpenAI curve must also remain qualified. Previous audits found stale per-coin context, Spot-related inputs, inherited local direction, immediate-entry assumptions and historical exit-time interpretation problems. After Futures reconstruction, the early control window was lower than the originally published comparison, and the continuation was materially negative.

The prospective OpenAI path was rebuilt to use fresh Futures context, no local-ML direction, no Spot fallback and no X9 logic, with entries only after the OpenAI response and its structured condition are available.

Still incomplete in the OpenAI research layer:

- 45m and 8h horizon variants
- multi-horizon candidate variants
- `selected_variant_id`
- separately stored rejected variants
- full NO_TRADE missed-opportunity classification by horizon

These extensions were intentionally not mixed into the recent Paper/Research repair scope.

## ML / Factory: why training remains paused

The recent ML problem was not simply "the model rejected a bad strategy".

The training/research path had drifted away from the earlier private Rule contract. Changes in research-contract and pre-filtering details could reduce a historically active Rule to only a handful of usable signals before ML even saw it.

a private reference candidate is the key reference case. The older private Rule contract was reproduced with a materially larger causal signal set and a reproducible OOS trade set. The lesson is now explicit:

**ML selector collapse is not the same as Rule failure.**

A Rule artifact that passes its own evidence must not be deleted only because the ML selector rejects or produces zero useful selections.

The intended lifecycle is:

`HYPOTHESIS → QUICK → ROBUST_OOS → CHALLENGER → PAPER → CHAMPION`

`candidate_eligible` is metadata / eligibility, not a separate operating stage.

Training and Factory remain paused until the currently active trading/research paths are sufficiently proven and the corrected Rule-preservation contract can be resumed without reopening the same failure mode.

## Current priorities

1. Collect natural new Paper / Watch / Forward / counterfactual outcomes.
2. Prove the first complete natural OpenAI AI-only forward chain.
3. Continue settling the new counterfactual backlog and measure which blocked setup families actually contain edge.
4. Use the repaired exit/post-exit evidence for later learning rather than immediately changing exit parameters.
5. Keep Rule evidence independent from ML selector success when training resumes.
6. Resume `HYPOTHESIS → QUICK → ROBUST_OOS → CHALLENGER → PAPER → CHAMPION` only after the active paths above are trustworthy.
7. Keep the public GitHub narrative human-reviewed while the nightly publisher is paused.

## Safety boundary

This remains a research system. No live trading or real-capital promotion is enabled. Paper, Watch, Research and OpenAI outcomes are research evidence and do not imply future profitability.

[Current status](../CURRENT_STATUS.md) · [Roadmap](../docs/progress/ROADMAP.md) · [Completed engineering work](../docs/progress/COMPLETED_WORK.md) · [Tests](../docs/verification/TEST_RESULTS.md)
