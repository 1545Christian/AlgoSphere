# Public status update — 2026-09-05

Deutsch: [Öffentliches Status-Update](./2026-09-05-public-status_DE.md)

<!-- AUTO_VALUES_START -->
## Summary

September 5 was mainly about separating real scientific progress from technical/process success and tightening the path toward `LIVE_READINESS`.

The most important finding was a concrete Factory/QUICK identity-propagation defect. It was repaired and a new Research Core was activated, but the fix was deliberately **not** declared end-to-end complete because the first production attempt after the patch had no valid `eligible` Factory queue row and therefore stopped before expensive work.

At the same time, Research Forward / Watch liveness was rechecked, a BALANCED run failed technically at GPU preflight, and a historical OpenAI settlement-quality defect was confirmed. These failures remain visible as failures; they are not reclassified as scientific rejects or progress.

## What was achieved today

### Factory / QUICK identity propagation

A specific root cause was found:

```text
missing_field = factory_queue_id
root_cause = Prebind wrote queue_id, ResumeStore validated factory_queue_id
```

The affected paths were repaired:

- `algosphere/research/pipeline.py`
- `algosphere/research/resume.py`
- `research_autopilot_v35.py`

A new Research Core was built and activated:

```text
4095edd8490527f55e4da2d86c9fd2dd3a904ccad3a4ba81d6ea25c400235a33
```

Focused validation result:

```text
15 passed
```

The following production attempt then stopped correctly with:

```text
FACTORY_QUICK_NO_ELIGIBLE_QUEUE_ROW
EXPENSIVE_WORK_STARTED = false
```

This means the known `factory_queue_id` propagation defect is technically repaired, but a real new canonical Factory→QUICK end-to-end run is **still open**. The old row had already moved from `eligible` to `selected`, so AlgoSphere did not force an invalid launch.

### Standalone QUICK result correctly classified

One standalone QUICK completed technically:

```text
expected = 120
actual = 120
nested_pass = 2
nested_rejected = 46
fast_rejected = 72
exit_code = 0
```

However, the run did not carry the required Factory identity from start, including `factory_attempt_id`, `factory_hypothesis_id` and `hypothesis_fingerprint`.

Therefore:

```text
run_6ae != canonical B scientific completion
```

Post-hoc identity binding is not allowed. A technically completed run is not automatically accepted as canonical scientific evidence.

### Factory identity contract tightened

New Factory runs must persist their identity from launch through the complete chain, including:

```text
factory_attempt_id
factory_hypothesis_id
hypothesis_fingerprint
factory_generation
source_memory_lesson_id
run_id
research_epoch_id
dataset_hash
feature_contract_hash
cost_contract_hash
runtime_core_hash
```

The targeted B hypothesis is already known, but expensive computation may start only after:

```text
IDENTITY_AT_START = PASS
```

The required path remains:

```text
B scientific terminal
→ Memory B
→ qualified Candidate Freeze
→ BALANCED/OOS
```

### Research Forward / Research Watch liveness

Fresh evidence up to about 23:35 showed that Research Watch was **not dead**, contrary to an earlier suspicion.

Current observed state:

```text
RESEARCH_FORWARD_PROCESS          PASS / live
RESEARCH_WATCH_DECISION_CYCLES   PASS / fresh
WATCH_SETUP_EVALUATION            PASS / active
WATCH_CLOSED_OUTCOMES             no new visible outcomes since ~18:59
```

TUT, ADA, ONDO, MYX and ENA continued to receive real setup evaluations. Many current decisions were legitimate `GATE_SETUP_BLOCKED / NO TRADE` results caused by regime, missing setup, range position, expected return, volume-Z or spot/futures basis conditions.

The remaining issue is closed-outcome liveness and WebUI truth: `PROCESS RUNNING != OUTCOME ACTIVITY` remains a binding rule.

### Checkpoint / resume / process handling

The following technical contracts are currently improved or preserved:

- Windows checkpoint-write PermissionError: PASS
- resume after technical abort reuses completed coins/phases: PASS
- explicit identity fields for new Factory runs: PASS
- duplicate research-worker prevention: PASS
- launcher / venv / base-Python / worker classification: PASS

A technical abort must not be rewritten as a scientific reject.

## Failures and blockers observed today

### BALANCED technical failure

BALANCED run:

```text
run_id = run_96d3dccd5523425ca84f395287ff8464
reason = GPU watchdog / BLOCKED_PREFLIGHT
```

Classification:

```text
TECHNICAL FAILED
```

This is **not** a scientific reject. Evidence is preserved and the GPU/CUDA/watchdog root cause must be isolated without weakening folds, samples, quality gates or forcing a CPU fallback for XGBoost.

### Unbound QUICK still needs classification

A separate QUICK remained active/unbound:

```text
run_id = run_4725ea54a68343a2ad186d73c08d5765
profile = QUICK
factory binding = missing
```

It must first be classified as scientifically necessary or redundant. If redundant, it should be ended in a controlled way while preserving checkpoint/evidence and releasing its lease; it must not be labelled REJECT.

### OpenAI historical settlement data-quality defect

A repeated historical pattern was confirmed:

```text
HORIZON_SETTLEMENT
entry_price == exit_price
gross_pnl = 0
net_pnl = -0.12 USDT
```

This is treated as a data-quality/settlement defect, not real trading evidence.

All affected historical OpenAI outcomes must be rebuilt locally from the original prediction/reference time, direction, intended horizon and the actual historical settlement price. No new OpenAI calls are required for this rebuild.

Hard rules:

- never silently reuse the entry/reference price as exit price
- apply costs exactly once
- keep LONG/SHORT PnL direction correct
- if a real historical settlement price is unavailable, store `NOT_CAPTURED`, `DATA_MISSING` or `BLOCKED`
- do not create duplicate rebuilt outcomes
- WebUI must show the rebuilt ledger exactly

A new TUTUSDT AI-only outcome of about `+2.20 USDT` appeared late today, which shows that new evaluation rows can be produced again, but its settlement-price source is **not yet fully verified** and therefore is not treated as trusted performance proof.

### Codex budget exhausted

The broader runtime-liveness repair task covering Watch writer/reader liveness, OpenAI settlement/evaluation, WebUI stale/current-truth and duplicate writer/reader cleanup was not completed because the Codex usage limit was reached.

Therefore:

- no PASS claim is made for the interrupted task
- unknown partial changes are not treated as completed
- no new Codex work should be started until reset/additional credits
- local deterministic repair and cheap preflight come first

## Current operational snapshot

The 23:45 public snapshot reported:

- runtime release: `v125`
- ML autopilot: `QUICK_FAILED`
- profile: `quick`
- phase: `ERROR`
- symbol: `not verified`
- progress: `0/0`
- stage truth: `LAST_COMPLETED_STAGE`
- live trading: `No`
- real capital: `0`
- automatic promotion: `disabled`
- snapshot: `2026-09-05T22:44:59.312634Z`

The repository also exposes separate package/update metadata `v90_8_10_127`. These identifiers have different scopes and must not be presented as if they were the same runtime observation.

## Current priority path

The project priority is now explicitly:

```text
Factory/B clean
→ qualified candidates
→ Freeze
→ BALANCED/OOS
→ Reference V1
→ Challenger
→ Prospective
→ Paper
→ Champion
→ LIVE_READINESS_GATE
→ Elite Canary
→ controlled scaling
```

No shortcut from QUICK directly to live trading is acceptable.

## Current P0 / still open

1. Obtain a genuinely `eligible` Factory queue row through the canonical selector.
2. Prove Factory identity byte-for-byte through Guard → Research Channel → active Core → Pipeline/Resume.
3. Start the targeted identity-bound B run only after `IDENTITY_AT_START = PASS`.
4. Terminalize B scientifically and persist Memory B.
5. Freeze only genuinely qualified `nested_pass` candidates.
6. Run BALANCED/OOS only on those winners; no new broad discovery first.
7. Resolve GPU watchdog / `BLOCKED_PREFLIGHT` root cause.
8. Implement/freeze Reference Benchmark Contract V1 before comparison.
9. Repair Challenger → Shadow → Prospective → Paper lifecycle.
10. Prove Paper execution parity and Paper Outcome Memory end-to-end.
11. Rebuild all faulty historical OpenAI settlements from local historical prices.
12. Prove the current OpenAI settlement-price source for new outcomes.
13. Keep Current Truth / stale detection authoritative in backend and WebUI.
14. Complete the full `LIVE_READINESS_GATE` before any Elite Canary.

## Additional learning / market-intelligence work kept open

AlgoSphere must increasingly learn by:

```text
Strategy × Coin × Side × Regime × Volatility × Outcome
```

and must separate higher-timeframe market bias from actual entry timing. Market-wide shocks and post-shock rebounds also remain explicit open work. The WebUI should explain these states in normal language rather than only exposing technical labels.

## Safety boundary

The public/runtime safety boundary remains:

```text
LIVE=false
DIRECT_ACTION=0
CONSUMER=0
REAL_CAPITAL=0
```

No automatic live trading, no automatic real-capital promotion and no gate relaxation to manufacture candidates.

## Technical evidence

Hashes, public-register records, verification limits and historical artifacts remain available separately. They are evidence, not a substitute for the development summary above.

See [Current status](../CURRENT_STATUS.md), [Test results](../docs/verification/TEST_RESULTS.md), [Roadmap](../docs/progress/ROADMAP.md) and the [Evidence summary](../evidence/EVIDENCE_SUMMARY.md).
<!-- AUTO_VALUES_END -->
