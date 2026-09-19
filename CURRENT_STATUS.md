# Current public status

Publication date: **2026-09-19**. Human-reviewed.

## Operating boundary

- Live trading: **No**
- Real capital: **0**
- Automatic promotion: **No**
- Paper / Shadow research: active
- Training: operator-controlled; no broad automatic training
- Safety boundary: fail-closed

## Confirmed working

### Trade Like Che CURRENT / CONTEXT_V2

- CURRENT and CONTEXT_V2 projections are separated again in the WebUI.
- NO_TRADE evidence is stored and projected through the existing canonical paths.
- latest browser proof: CONTEXT_V2 40 decisions / 32 settled / 40 memory; CURRENT 72 decisions / 77 settled at that checkpoint.
- variant/filter/scroll state survives background refresh.
- WebUI version at final browser proof: **90.8.10.196**.

### Canonical Learning → CONTEXT_V2 selector

The existing CONTEXT_V2 selector now consumes matching Canonical Learning Delta evidence instead of relying only on market-state/context-fit.

Matching is variant-safe by coin, side, strategy family and market state. Counterfactual/NO_TRADE evidence is not counted as an executed trade.

New decision traces can preserve base score, market-state delta, memory delta, final score and without-vs-with-memory decision reasoning.

Focused validation: **75 passed**.

### Research storage future writer

research_runs growth was traced to large unique active_strategies snapshots plus duplicate physical *_json aliases alongside decoded canonical fields.

Classic content deduplication is not the answer: 329 runs had active_strategies and 328 snapshots were unique.

The future writer now drops duplicate physical aliases and keeps the decoded canonical representation. Historical rows were not migrated or deleted.

Representative evidence-based estimate: ~134.5 MB before versus ~65.3–71.7 MB after, nominally ~49% smaller future snapshots.

### Research → Canonical handoff

normalize_report() previously dropped compact candidate/rule evidence from active_strategies before the standardized Research/Memory handoff.

The future handoff now projects compact artifact/strategy identity, nested-fold metrics, data/code/execution identity, baseline/stress evidence and setup/threshold/exit-policy/feature hashes.

Full strategy payloads are not copied into Canonical Memory.

Current proof state: **AWAITING_REAL_RUN**. No natural post-patch Research/QUICK handoff has yet provided end-to-end proof.

## Still incomplete

### Historical Canonical backfill

The scoped Exact-only operator was corrected to the real schema:

- canonical_trade_outcomes.decision_id → memory_decisions.decision_id
- Contributions/Deltas link by canonical_outcome_id

Read-only exact-chain proof:

- PAPER/CURRENT: 17 exact chains, but 17/17 show Contribution/Delta source_population = TRADE_LIKE_CHE
- PAPER/CONTEXT_V2: no Outcomes/Contributions/Deltas
- TLC/CURRENT: 30 exact chains
- TLC/CONTEXT_V2: 30 exact chains

The historical apply remains blocked by repeated `sqlite3.OperationalError: database is locked`. No repair commit is claimed.

### Canonical state completeness

Historical gaps remain visible rather than being synthesized:

- market_state_version missing across target legacy populations
- market_state_id missing in parts of the population, including PAPER/CONTEXT_V2
- LEGACY_SCHEMA_GAP markers remain evidence

### Model quality

The main scientific problem remains open: technical pipeline completion has not yet demonstrated durable ML uplift. The ENA pilot remained Rule-vs-ML DEGRADED and was not promoted.

## Current priorities

1. Apply the scoped historical backfill only after the active SQLite writer is safely paused.
2. Explain and repair the PAPER/CURRENT Contribution/Delta population mismatch without relabeling history.
3. Obtain a natural future Research/QUICK handoff to prove the new compact evidence projection end-to-end.
4. Continue prospective CURRENT vs CONTEXT_V2 evidence collection with strict lane/variant separation.
5. Keep the new Canonical Learning Delta → CONTEXT_V2 selector trace verifiable on future decisions.
6. Continue WebUI simplification and pagination/virtualization for large histories.
7. Keep broad training and automatic promotion blocked until actual uplift and robustness are demonstrated.

## Safety boundary

`LIVE=false` · `REAL_CAPITAL=0` · automatic promotion disabled.

No documentation update authorizes live trading or real-capital execution.

See the [September 19 update](updates/2026-09-19-public-status.md), [roadmap](docs/progress/ROADMAP.md), [completed work](docs/progress/COMPLETED_WORK.md) and [test results](docs/verification/TEST_RESULTS.md).