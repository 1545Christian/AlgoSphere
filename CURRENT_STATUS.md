# Current public status

Publication date: **2026-09-21**. Human-reviewed from the latest internal project handoff.

## Operating boundary

- Live trading: **No**
- Real capital: **0**
- Automatic promotion: **No**
- Demo / Testnet: **Not started**
- Elite / UTA: **Deferred**
- Paper / Shadow research: active
- Training: operator-controlled
- Safety boundary: fail-closed

## Latest WebUI / current-truth proof

The latest reviewed WebUI checkpoint has moved beyond the earlier 90.8.10.199 proof.

Latest accepted build in the internal handoff: **90.8.10.239**.

Reported browser-accepted scope:

- B37_EXIT_LABEL_SEMANTICS = PASS
- B38_NO_TRADE_CURRENT_TRUTH = PASS
- B39_FULL_WEBUI_SWEEP = PASS
- BROWSER_ACCEPTANCE_PASS = PASS
- friendly host/private browser path = PASS
- no Failed to fetch
- Paper CURRENT and CONTEXT_V2 remain separated

At that checkpoint, Paper CURRENT showed **124 settled / +4.03 USDT / PF 1.09 / 0 open**, with API ↔ DOM matching for the checked scope.

CONTEXT_V2 showed **501 decisions / 0 settled / 0 open** at that same checkpoint.

These figures describe current UI/runtime truth for the checked population. They are not a claim of predictive superiority or live profitability.

## Canonical Memory / learning

The **current writer path** is clean:

- CURRENT_MEMORY_WRITER = PASS
- SINGLE_LEARNING_WRITER = PROVEN
- PARALLEL_LEARNING_ENGINE = NOT_FOUND

However, the latest trust review does **not** treat the entire historical/canonical memory population as closed.

Open historical/current reconciliation issues still include:

- Paper CURRENT rows where Delta exists but Contribution/lane lineage is incomplete
- Paper CONTEXT_V2 with no comparable settled canonical outcome population
- TLC CONTEXT_V2 rows with Outcome but incomplete Contribution/Delta
- Research Forward join mismatches around identity/lane/state
- OpenAI lacking a fully trusted settled learning chain in the checked sample

The current writer can therefore be trusted separately from the unresolved historical archive.

## Exact-only OpenAI memory repair

A small OpenAI canonical repair remains blocked.

The intended 3-row repair discovered 4 possible rows during re-check:

- authorized target rows: 3
- discovered target rows: 4
- target-set drift: YES

The apply was correctly **not** forced because a writer-free maintenance state was also not safely proven.

The next valid step is:

1. establish a writer-free maintenance window
2. classify the fourth row
3. explicitly re-authorize the exact target IDs
4. execute one exact-only transaction
5. verify target/non-target mutation and SQLite integrity
6. restart runtime cleanly

No synthetic or broad historical repair is authorized.

## OpenAI AI-only

A concrete OpenAI paper-loop bug was found and patched on disk.

The bug could allow a valid OPEN observation to be overwritten after a temporary Futures BBO/history failure.

Focused patch validation: **49 PASS**.

The remaining work is:

- activate the patch in the controlled runtime
- verify the old failure mode no longer reproduces
- reconcile the earlier approximately **+43.49 USDT** interpretation against the current canonical source, population, date range and cost contract
- define one trusted current OpenAI number for the UI

Therefore:

- OpenAI decision path: active
- runtime patch activation: pending
- historical +43.49 reconciliation: pending
- OpenAI number trust: not closed
- OpenAI profitability: not proven

## Market Intelligence / training

The ENA full-history one-coin pilot remains the important model-quality result:

- Rule vs ML = DEGRADED
- candidate_eligible = false
- no Challenger promotion
- no automatic promotion
- Rule evidence preserved

Broad training remains blocked until model-quality evidence improves.

## Research handoff / storage

The future Research → Memory projection and future snapshot writer improvements remain in place.

Natural forward proof for some future handoff/storage contracts is still pending.

No broad historical compaction/delete/vacuum is authorized.

## Demo / Packaging / Release

Bitget Demo/Testnet has **not started**.

Current gate: **M2 = BLOCKED_BY_M1**.

M1 is not closed because Memory trust and OpenAI number trust are still incomplete.

Still not done:

- Demo execution router proof
- real Bitget Demo order ACK/fill/position/exit cycle
- fees and reconciliation
- restart/reconnect recovery
- Paper → Demo handoff
- TLC → Demo handoff
- OpenAI → Demo handoff
- fallback to current simulated path

Important boundaries:

- Demo Connected ≠ Live
- Demo/Testnet ≠ real capital
- Live remains disabled

## Current critical path

The project should not return to broad WebUI re-audits unless a new regression is observed.

1. classify OpenAI target-set drift (3 vs 4)
2. create safe maintenance state
3. exact-only canonical apply
4. controlled runtime restart
5. activate CH06 OpenAI patch
6. reconcile current/historical OpenAI numbers
7. close M1 if current Memory/UI/OpenAI trust gates pass
8. only then start Bitget Demo/Testnet M2

## Scientific boundary

Infrastructure progress does not prove trading edge.

Still not proven: durable ML uplift, CONTEXT_V2 uplift, OpenAI profitability, a new Challenger → Paper → Champion cycle, or Demo/live readiness.

## Safety boundary

LIVE=false · REAL_CAPITAL=0 · automatic promotion disabled · Demo/Testnet not started.