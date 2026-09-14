# Documented engineering work

Items below are dated source reports and reviewed repair results. They are not a claim that every end-to-end requirement is closed.

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
- OpenAI strategy was intentionally **not** changed by the Paper/Research counterfactual repair.

## OpenAI AI-only — current reviewed state

- OpenAI runs under `OPENAI_AI_ONLY_FUTURES_PAPER_V1` with Futures-only pricing and 100-USDT canonical notional.
- OpenAI integrity, position-manager and horizon-settlement checks were reported PASS in the latest acceptance state.
- A fresh natural OpenAI AI-only `decision → entry → managed exit → outcome → learning` chain is **still not proven**; the latest reviewed state had no new natural fills and only `OPENAI_AI_ONLY_PAPER_TICK_COMPLETE`.
- Earlier historical OpenAI performance remains qualified because audits found stale per-coin context, Spot-related inputs, inherited local direction, immediate-entry assumptions and historical exit-time interpretation problems.
- The prospective OpenAI path was rebuilt to remove local-ML direction, Spot fallback and X9 logic from the active AI-only path.
- 45m / 8h variants, multi-horizon candidate storage, selected/rejected variant identity and full NO_TRADE-by-horizon learning remain open.

## ML / Factory — current reviewed state

- Training remains intentionally paused.
- Factory / hypothesis producer remains intentionally paused.
- The recent root-cause review showed that training-contract drift could remove Rule signal density before ML evaluation through history-length, threshold and early-filter changes.
- ENAUSDT LONG `basis_dislocation` remains the reference case for preserving Rule evidence independently from ML-selector success.
- Binding interpretation: **ML selector collapse is not Rule failure**.
- Intended lifecycle: `HYPOTHESIS → QUICK → ROBUST_OOS → CHALLENGER → PAPER → CHAMPION`.
- `candidate_eligible` is eligibility/artifact metadata, not a separate operating stage.

## Earlier documented work

- **2026-09-05 · Implementation reported by source:** Windows checkpoint writes, reuse of completed phases and duplicate research-worker prevention were repaired in the V2 baseline.
- **2026-09-05 · Implementation reported by source:** `queue_id` / `factory_queue_id` identity defect repaired; new research core activated; 15 focused tests documented PASS.
- **2026-09-05 · Blocker:** real Factory→QUICK end-to-end proof remained open; one launch stopped at `FACTORY_QUICK_NO_ELIGIBLE_QUEUE_ROW` before expensive computation.
- **2026-09-06 · Publisher work:** GitHub Nightly v5.4.x installed with staged line-ending normalization, bounded report reading and coverage warnings.
- **2026-09-08–13 · Publication observation:** nightly upload itself ran, but the automatic narrative repeatedly carried older September 5/6 text because current repair/runtime evidence was not fully selected by the publisher.

[Current status](../../CURRENT_STATUS.md) · [Outstanding work](ROADMAP.md) · [Reviewed September 14 update](../../updates/2026-09-14-public-status.md)
