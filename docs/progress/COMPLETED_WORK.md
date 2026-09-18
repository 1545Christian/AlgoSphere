# Documented engineering work

Items below are dated, reviewed engineering results. They are not claims of profitability or global end-to-end closure.

## September 18 — reviewed engineering progress

### Research Forward / Trade Like Che Context V2

- Activated the Context V2 shadow contract in Research Forward.
- Confirmed 5 active coins, 26 CURRENT + 8 CONTEXT_V2 evaluations per coin.
- Confirmed 170 expected / 170 active evaluations and health PASS.
- Fresh Context V2 decisions, including `NO_TRADE / NO_CURRENT_SETUP`, became visible.
- Paper Context V2 remained active.
- Point13, OpenAI and Market Data were not interrupted by the minimal activation.
- Focused affected tests: 33 PASS.

### WebUI projection and performance

- Global “Open” view now aggregates Paper, Watch, Research Forward and OpenAI positions.
- Paper and Watch tabs again show their open positions correctly.
- Research Forward is explicitly labelled as a no-capital forward path.
- OpenAI detail payload is loaded only when its tab is opened.
- 24h cold overview improved to about 2.61 s; warm overview about 0.03 s.
- 24h payload reduced from about 4.79 MB to about 0.74 MB (~84.5% reduction).
- No new WebUI layer or trading logic was introduced.
- 30 relevant tests plus browser/health checks passed.

### Research & Models operator

- Added an operator-facing training surface in the existing Research & Models area.
- One-coin test and active-universe training controls are available.
- Coin / side / strategy-family selection and readiness are visible.
- Lifecycle, Rule-vs-ML, artifacts, current job, last run and error states are visible.
- Controls remain explicit/manual; no automatic training or promotion was enabled.
- Orchestrator suite: 41 PASS; responsive WebUI: 19 PASS; additional dark-WebUI: 14 PASS.

### ENA one-coin pilot

- Registered and executed the explicit ENA pilot through the existing training orchestrator.
- Confirmed full-history readiness, revalidated feature provenance and consistent run/manifest state.
- Produced 756 OOS result rows and 126 Rule-baseline rows.
- Covered all 3 feature arms, all 4 architectures and all 7 horizons with Logistic and HistGradientBoosting.
- Rule and ML used the same 2026-07 / 2026-08 / 2026-09 fold basis.
- Registry ID 7 recorded.
- Result: `RULE_VS_ML = DEGRADED`.
- `candidate_eligible = false`; no Challenger eligibility; no promotion.
- Rule artifact preserved.
- The incomplete earlier attempt was archived rather than discarded.

### Market Intelligence Robustness Gate

- Added a versioned read-only robustness contract between OOS Candidate evidence and Challenger eligibility.
- Required dimensions include multi-fold walk-forward, recent OOS, stability, cost stress, calibration, tail risk and sample support.
- Optional controlled ablation / parameter-neighborhood / perturbation dimensions are supported.
- No new model, tuning or full expensive run was triggered.
- Selected related suites: 61 PASS.

### Canonical Memory / lifecycle audit

The audit confirmed substantial existing coverage but also identified remaining gaps:

- historical Decision→Trade linkage is partial
- Trade→Outcome and Outcome→Memory are working
- Memory→Learning is eligibility-dependent
- per-trade Learning Delta is not yet visible
- runtime CURRENT/V2 separation is stronger than Canonical-Memory separation
- promotion-history persistence is partial
- Challenger is not currently an active promotion path
- Champion remains mainly a frozen Paper fallback

### Legacy Preisvorhersage audit

- Compared current AlgoSphere with the older Preisvorhersage / `Preisvorhersage_Clean` code and stored evidence.
- Confirmed that no mandatory legacy component blocked the ENA pilot.
- Current AlgoSphere is stronger in OOS governance, leakage protection, Rule-vs-ML separation, artifact/feature hashes, trade evidence and MFE/MAE outcome tracking.
- Partial legacy areas remain for later evidence/replay work: Telegram/manual provenance, 1m/5m/15m entry confirmation, Pending/Recheck, manual-trade import and Recency Weighting comparison.
- Old models are not treated as directly compatible current models.

### OpenAI AI-only input contract

- Audited the actual paid request path without generating a new call.
- Identified missing 3D, 7D, explicit support/resistance and open-position context.
- Added 3D/7D context, explicit structure/support-resistance projection and open-position context using existing causal data.
- No reliable Futures/Spot basis source was fabricated.
- Existing 1D/1h/15m/5m/1m, BTC/ETH, news and aggregated memory were preserved.
- Input-patch focused tests: 13 PASS + 36 actionable-plan tests PASS.
- Produced a redacted actual request/response export without a new paid call.
- Measured the pre-compaction request at ~73,933 input tokens / ~4,438 output tokens.
- Compact-request / single-plan-per-symbol work is underway but not yet forward-proven.

### Project workflow guards

- Added a root-cause-first skill focused on finding the first measurable deviation, repairing the canonical path minimally and proving before/after evidence.
- Added a project-closure guard to prevent repeated “done” claims without runtime/UI/artifact/promotion proof and to protect lane/population separation.
- No production runtime behavior was changed by those skill additions.

## September 17 — reviewed engineering progress

See the [September 17 public update](../../updates/2026-09-17-public-status.md) for the earlier OpenAI V2, unified-memory, WebUI projection and runtime work.

## Safety / interpretation

A green focused test suite proves the tested contract, not profitability.

A completed training run proves technical execution, not model quality.

Negative and insufficient evidence is intentionally retained.

[Current status](../../CURRENT_STATUS.md) · [Outstanding work](ROADMAP.md) · [September 18 update](../../updates/2026-09-18-public-status.md)
