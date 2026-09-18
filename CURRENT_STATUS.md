# Current public status

Publication date: **2026-09-18**. Human-reviewed.

## Operating boundary

- Live trading: **No**
- Real capital: **0**
- Automatic promotion: **No**
- Paper / Shadow research: active
- Training: operator-controlled; no broad automatic training
- Factory / hypothesis producer: not automatically resumed
- Safety boundary: fail-closed

## What is confirmed working

### Research Forward / Trade Like Che Context V2

The updated Research Forward contract is active and health-checked:

- 5 active coins
- 26 CURRENT variants per coin
- 8 CONTEXT_V2 variants per coin
- 34 total per coin
- 170 expected total
- 170 active
- health check: **PASS**

Fresh Context V2 Shadow decisions are visible, including explicit `NO_TRADE / NO_CURRENT_SETUP` evidence.

Paper Context V2 stayed active and was not interrupted by the minimal Research Forward activation.

### WebUI

The open-position projection now aggregates open positions from Paper, Watch, Research Forward and OpenAI.

At the recorded browser checkpoint:

- Paper open: 2
- Watch open: 1
- Research Forward open: 2
- OpenAI open: 0

Performance also improved materially:

- 24h cold overview: ~2.61 s
- 24h warm overview: ~0.03 s
- 24h payload: ~0.74 MB versus 4.79 MB before

Detailed data is loaded on demand.

### Research & Models operator

The Training & Research page now exposes operator-controlled actions for one-coin testing and active-universe training, plus readiness, lifecycle, Rule-vs-ML, artifact and run-state visibility.

Nothing auto-starts and no automatic activation/promotion was enabled.

### ENA one-coin pilot

The explicit ENA pilot completed:

- full-history ready
- feature provenance revalidated
- OOS contract ready
- 756 OOS result rows
- 126 Rule-baseline rows
- all 3 feature arms
- all 4 architectures
- all 7 horizons
- Logistic + HistGradientBoosting
- identical folds for Rule and ML: 2026-07 / 2026-08 / 2026-09
- Registry ID 7

Result:

- `RULE_VS_ML = DEGRADED`
- `candidate_eligible = false`
- Challenger eligibility = false
- promotion allowed = false
- Rule artifact preserved = yes

The negative result is preserved rather than hidden or promoted.

### Robustness Gate

A read-only, versioned robustness contract exists between OOS Candidate evidence and later Challenger eligibility.

The gate requires evidence across multi-fold walk-forward, recent OOS, stability, cost stress, calibration, tail risk and sample support, with controlled optional ablation/perturbation checks.

The newer ENA pilot still needs to be evaluated through this gate before any claim of `ROBUST_OOS_READY`.

### OpenAI AI-only

The input-contract gap identified in the real request was partially closed.

The request path now supports:

- 1m / 5m / 15m / 1h / 1D / 3D / 7D context
- BTC / ETH context
- regime / range position
- explicit structure / support-resistance summary
- volume / volatility
- news
- aggregated learning memory
- open-position context when present

No reliable Futures/Spot basis source was available, so no basis value is fabricated.

A redacted actual-request export was created without a new paid call.

The next optimization is still in progress: the measured pre-compaction request was ~73,933 input tokens and ~4,438 output tokens, so the builder is being reduced to a compact market context and one explicit plan per symbol. This is **not yet forward-proven**.

## What remains incomplete

### Canonical Memory / Learning / Lifecycle

The chain `Decision → Trade → Outcome → Canonical Memory → Learning → Lifecycle` exists, but it is not completely closed.

Known gaps:

- some historical Decision→Trade linkage remains incomplete
- per-trade Learning Delta is not visible
- CURRENT vs CONTEXT_V2 separation is partial in Canonical Memory
- promotion history is only partially persisted
- Challenger is not yet an active operational promotion state
- Champion is mainly a frozen Paper fallback, not a newly promoted model

### Legacy-parity questions

The legacy audit found no mandatory old capability blocking the ENA pilot.

Still partial:

- Telegram/manual-signal provenance
- explicit 1m/5m/15m entry-confirmation sequence
- persistent Pending/Recheck parity
- canonical import of manual trades with prior-signal provenance
- Recency weighting only as a research comparison

These are research items, not instructions to copy old implementation into the current system.

### Model quality

The main scientific problem remains open: technical completion of the pipeline has not yet produced demonstrated ML uplift.

The ENA pilot explicitly showed ML degradation versus Rule baseline. That is useful evidence, but not a model-quality success.

OpenAI decision quality is also not yet established; more causal settled outcomes are needed.

### Verification

Focused suites are green in the affected areas, but focused regression PASS is not equivalent to global scientific/runtime acceptance. The complete suite and earlier failures still need explicit closure/classification after current parallel work settles.

## Current priorities

1. Finish local validation of the compact OpenAI request / single-plan contract, then use the next normal paid call as forward proof.
2. Evaluate the new ENA pilot through the Robustness Gate.
3. Close the remaining Canonical Memory / Learning / Promotion-history gaps.
4. Continue simplifying the WebUI and add pagination/virtualization where large histories remain heavy.
5. Investigate legacy-partial areas through controlled replay/evidence only.
6. Keep broad multi-coin training and automatic promotion blocked until evidence justifies them.
7. Continue collecting prospective Paper / Watch / Research / OpenAI outcomes.
8. Rerun/classify the complete project test suite once the current parallel work is stable.

## Safety boundary

`LIVE=false` · `REAL_CAPITAL=0` · automatic promotion disabled.

No documentation update authorizes live trading or real-capital execution.

See the [September 18 update](updates/2026-09-18-public-status.md), [roadmap](docs/progress/ROADMAP.md), [completed work](docs/progress/COMPLETED_WORK.md) and [test results](docs/verification/TEST_RESULTS.md).
