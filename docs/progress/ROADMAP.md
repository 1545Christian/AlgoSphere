# Current public roadmap

Publication: **2026-09-21**. Human-reviewed.

## Immediate P0 — close M1 without reopening proven work

- **CLOSED for current scope:** WebUI build 90.8.10.239 browser acceptance.
- **OPEN:** classify OpenAI exact-repair target drift (3 authorized vs 4 discovered).
- **OPEN:** establish a writer-free maintenance state.
- **OPEN:** perform one exact-only canonical repair on explicitly authorized target IDs.
- **OPEN:** restart runtime and prove single-writer / no-lock state.
- **OPEN:** activate the OpenAI paper-loop patch in runtime.
- **OPEN:** reconcile the historical ~+43.49 USDT view against current canonical source/population/time/cost contract.
- **OPEN:** close M1 only when current Memory/UI/OpenAI trust gates agree.

## P0 — Memory

- **PROVEN CURRENT PATH:** current memory writer.
- **PROVEN:** single learning writer; no parallel learning engine found.
- **OPEN LEGACY/RECONCILIATION:** incomplete historical Contribution/Delta/lane/state chains.
- **RULE:** classified non-reconstructable legacy gaps must not be synthesized.

## P0 — OpenAI

- **PATCHED ON DISK:** OPEN-observation overwrite bug.
- **FOCUSED TESTS:** 49 PASS.
- **OPEN:** controlled runtime activation.
- **OPEN:** number reconciliation and current canonical UI truth.
- **OPEN:** causal profitability evidence.

## P0 — model quality

- **OPEN:** improve/explain Rule-vs-ML degradation before broad training.
- **OPEN:** collect enough prospective CONTEXT_V2 evidence.
- **OPEN:** preserve Rule evidence independently from ML.

## M2 — Bitget Demo/Testnet

Status: **BLOCKED_BY_M1 / NOT STARTED**

After M1 closes:

- define/verify simulated vs Bitget Demo execution routing
- prove credentials and permissions remain Demo-only
- execute one complete Demo Futures E2E cycle
- reconcile order → fill → position → exit → fees → outcome
- prove reconnect/restart recovery
- prove Paper/TLC/OpenAI handoff to Demo separately
- prove safe fallback to simulated mode

## Later — Live

- Normal Futures only after Demo/stability proof.
- Elite / UTA remains deferred beyond stable Normal Futures.
- Real capital remains disabled.

## Verification principles

- already-proven scope is not reopened without evidence of regression
- source patch ≠ runtime-active patch
- current writer trust ≠ historical archive completeness
- technical PASS ≠ scientific uplift
- Demo ≠ Live