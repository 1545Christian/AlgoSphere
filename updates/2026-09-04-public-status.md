# Public status update — 2026-09-04

Deutsch: [Öffentliches Status-Update](./2026-09-04-public-status_DE.md)

<!-- AUTO_VALUES_START -->
## Summary

September 4 was no longer a single v117 update. It became a longer repair and runtime-validation day leading to the currently observed `v90_8_10_125` runtime. The main goal was to make the local learning chain genuinely autonomous: training must not depend on a separate research evaluator, new scientific work must not disappear behind old `COIN_DONE`/resume state, Research Forward must be functionally healthy rather than merely represented by a launcher PID, and the WebUI must use a fixed local HTTP endpoint with self-healing health checks.

The 23:45 nightly correctly published the current runtime snapshot, but its development summary was still too heavily based on the older v117 release-note template. This page has therefore been corrected to reflect the evidence-backed work actually observed during the day.

## What was actually achieved today

### ML autonomy and learning loop

- The v117 separation remains the foundation: `LOCAL_ML_AUTOPILOT` is the normal training authority; Codex/Chat are not runtime prerequisites.
- v122/v123 corrected a real P0 gap: generation of new adaptive hypotheses must no longer depend indirectly on a separate Research Evaluator. The Local-ML daemon reads persistent memory, semantically deduplicates previous work, creates new admissible hypotheses itself and can launch QUICK.
- `factory_exhausted -> WAITING FOR JOB` is no longer accepted as a normal operating state. Adaptive mutation followed by bounded family discovery is expected to produce genuinely new work; only real search-space exhaustion may wait.
- New semantic factory generations were added to the `COIN_DONE`/`RUN_COMPLETE` resume compatibility contract so that new scientific work cannot be hidden by an older completed checkpoint.
- The intended autonomous loop remains QUICK → result → memory → BALANCED on promising evidence, otherwise the next novel hypothesis.

### Actual scientific-run evidence

- A QUICK run reached terminal completion at `2026-09-04T18:42:15Z`.
- Its standardized experiment-memory record was persisted (`status=RECORDED`, `scientific_result=COMPLETED`).
- This was **not a performance PASS**: the stored best-candidate entry for `ENAUSDT / basis_dislocation / logistic / long` remained `factory_exhausted` and contained no reliable PF/PnL/trade metrics. This is a scientific completion/reject state, not a trading success.
- Autonomous QUICK work later continued. At the nightly snapshot, runtime `v90_8_10_125` was active in `CHECKPOINT` on `MYXUSDT`, with `3/5 coins` completed and `LIVE_STAGE_HEARTBEAT` as the current truth source.
- The research autopilot reported `eligible experiments = 1`; automatic promotion remained disabled.

### Research Forward / Watch

- Research Forward is functionally separated from the Research Evaluator: it has its own supervisor service and no-capital child trader while the evaluator remains separate.
- Health no longer means only “a process exists”; the contract includes child heartbeat and functional no-capital state.
- v123 validate-only: PASS with 90 strategies, 18 each for ADA/ENA/MYX/ONDO/TUT, `capital_allowed=false`.
- Watch/Research remain exploration and evidence roles. Their lessons must later feed segmented eligibility/memory and only reach Paper after additional prospective confirmation.

### WebUI / runtime recovery

- A live PowerShell launcher alone no longer counts as a healthy WebUI.
- The supervisor checks the actual endpoint `http://127.0.0.1:8012/api/ping`.
- A dead HTTP child is retired and restarted in a controlled way.
- The local browser opens loopback; a remembered or random port is not treated as runtime truth.
- Additional diagnostics are written to `reports/webui_runtime_error.txt`.
- Fixed local entry and HTTP health are now code contracts; long-run self-healing still needs continued observation.

### OpenAI / freshness / cost control

- OpenAI remains a second analysis/prediction engine, not a prerequisite for local ML autonomy.
- v122 sets the normal Luna cadence to 30 minutes and separates Web/News at 120 minutes.
- Unchanged context may suppress a new second-opinion call for at most 60 minutes.
- Local context older than 45 minutes should not be sent to OpenAI; `STALE` must be visible.
- Scheduler check, API attempt, successful request and prediction time are shown separately in the WebUI.

## Failures / assumptions corrected today

- Earlier code-PASS conclusions were partly too optimistic: real Windows operation showed that Local ML could remain in `WAITING FOR JOB` even though the code contract claimed autonomy.
- New factory work could be hidden by old `COIN_DONE`/`RUN_COMPLETE` checkpoints. This was treated as a resume/novelty defect.
- Research Forward could appear “started” while its actual no-capital child trader was not functionally healthy. The health contract was tightened accordingly.
- A running or completed QUICK is not automatically a good candidate. `scientific_result=COMPLETED` and `factory_exhausted` must remain separate from performance or promotion success.
- WebUI “running” truth may no longer be inferred from a launcher PID; actual HTTP health is required.
- These failed attempts remain part of the evidence and are not relabeled as completed progress.

## Current runtime state at the nightly snapshot

- Runtime release: `v90_8_10_125`
- ML autopilot: `QUICK_RUNNING`
- Profile: `quick`
- Phase: `CHECKPOINT`
- Symbol: `MYXUSDT`
- Progress: `3/5 coins`
- Stage truth: `LIVE_STAGE_HEARTBEAT`
- Live trading: `No`
- Real capital: `0`
- automatic promotion: `disabled`
- Snapshot: `2026-09-04T22:45:00.015712Z`

## Current TODO / not yet proven

1. Observe the currently running QUICK to a terminal result and clearly distinguish scientific completion, reject, promising candidate and technical failure.
2. After each terminal run prove correct run/core/factory identity, exactly one terminalization, persisted Unified Memory and the resulting next autonomous action.
3. On promising evidence, prospectively prove QUICK → BALANCED; on reject, autonomously move to the next semantically deduplicated hypothesis.
4. P0 remains open: existing FeatureCaches should be extended incrementally with new candles instead of being unnecessarily rebuilt.
5. Research Forward must generate fresh cycle/decision/watch evidence over a longer Windows run and not merely look technically `RUNNING`.
6. The WebUI must remain reachable on `127.0.0.1:8012` and correctly replace a dead HTTP child without unnecessarily restarting unrelated heavy jobs.
7. Market Data / Regime / Watch / Forward still need freshness, source-isolation and shared Decision/Feature/Risk/Exit parity checks.
8. OpenAI freshness, 30/120-minute cadence, stale blocking and real Prediction→Outcome→Memory effect still need long-run proof.
9. Watch/Market-Intelligence learning must not only archive outcomes; it must attribute good/bad/too-early/too-late decisions by Strategy × Coin × Side × Regime × Volatility × Shock/Event context and later measurably influence Paper eligibility.
10. `PROVEN_CLOSED` remains bound to current runtime/browser/ledger evidence; code PASS alone is insufficient.

## Safety boundary

The boundary remains `LIVE=false`, `DIRECT_ACTION=0`, `CONSUMER=0`, `REAL_CAPITAL=0`. No automatic live trading and no automatic real-capital promotion.

## Technical evidence

Hashes, public-register records, verification limits and historical artifacts remain available separately. They are evidence, not a substitute for the development summary above.

See [Current status](../CURRENT_STATUS.md), [Test results](../docs/verification/TEST_RESULTS.md), [Roadmap](../docs/progress/ROADMAP.md) and the [Evidence summary](../evidence/EVIDENCE_SUMMARY.md).
<!-- AUTO_VALUES_END -->
