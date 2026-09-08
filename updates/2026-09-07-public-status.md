# Public status update — 2026-09-07

Deutsch: [Öffentliches Status-Update](./2026-09-07-public-status_DE.md)

<!-- AUTO_VALUES_START -->
## Summary

September 7 was an active runtime-repair and validation day. The important change was not another static release-note rollover: AlgoSphere was restarted visibly, the local runtime stack came back with the supervisor and core services running, and the ML autopilot resumed a real QUICK run. At the same time, the day exposed two remaining truth gaps that must not be hidden by a generic nightly summary: same-run resume is still not proven, and Watch-vs-Research behavior still needs a causal parity check rather than a threshold change.

The previous nightly text incorrectly said that no new development proof existed today and therefore carried September 5 work forward as the main development story. That was incomplete. This update corrects the dated narrative while preserving the distinction between observed runtime state, reported implementation work and still-open proof.

## What changed today

### Runtime restart and service recovery

- A visible restart was completed successfully during the repair session.
- The runtime supervisor was present as a single supervisor instance.
- Point13 / ACTIVE_PAPER, Research Forward, Research Autopilot, Local ML Autopilot and WebUI were reported running after restart.
- The currently active QUICK run is a new runtime run identity (`run_f6cf…` in the repair session). The earlier run had been interrupted and work resumed under a new run id.
- Because the resumed work did **not** preserve the same run id, `Same-Run-Resume` is still **not PASS**. Recovery worked, but exact same-run continuation remains an open acceptance item.

### ML progress

- The 23:45 publisher observed `ML AUTOPILOT QUICK RUNNING`.
- Profile: `quick`.
- Phase: `MODEL_TRAIN`.
- Current symbol: `MYXUSDT`.
- Progress: `3/5` coins.
- State source: `LIVE_STAGE_HEARTBEAT`.
- Freshness classification: `CURRENT_REPORT`.
- Source timestamp: `2026-09-07T22:45:00.432722Z`.

This is current runtime evidence, but it is not the same as proof that the run will terminalize correctly or that a candidate is scientifically good.

### Watch vs Research: behavior still under investigation

- WATCH is allowed to create research/watch trades.
- RESEARCH is not supposed to create those trades in the same role; its purpose remains evaluation/research rather than simply duplicating Watch execution.
- Today showed a visible difference: Watch can produce trades while Research may remain without trades.
- That difference must **not** be "fixed" by loosening thresholds or forcing trades.
- The required next check is a causal Watch-vs-Research parity comparison using identical timestamps, coins and market states, following the funnel through eligibility, assignment, setup gates, decision creation and outcome handling.
- The investigation must determine whether the difference is a legitimate no-setup result or a pipeline/assignment defect.
- The active QUICK training must not be interrupted for that analysis.

## Important corrections to previous assumptions

- A successful restart is not the same as same-run resume. The runtime recovered, but continuity under the exact original run identity remains unproven.
- A live `RUNNING` label is not enough by itself; fresh stage heartbeat and current progress are required.
- `NO TRADE` in Research is not automatically a failure. It may be a correct setup-gate result. The code must first prove where Watch and Research diverge.
- Watch activity alone does not prove that Research assignment, funnel parity or outcome persistence are correct.
- The public publisher must not say `NO_NEW_DEVELOPMENT_PROOF_TODAY` when current repair/runtime evidence exists but was not ingested by its source-selection logic.

## Operational state from local reports

- Runtime release reported in explicit field: `not verified`.
- Acceptance report label (not executable version): `v125`.
- WebUI source version: `v90_8_10_127`.
- Explicit package/update manifest: `not verified`.
- Application source version: `v90_8_5`.
- Historical source-hotfix identifier: `v90_8_5_23`.
- ML: `ML AUTOPILOT QUICK RUNNING` · `quick` · `MODEL_TRAIN` · `MYXUSDT` · `3/5`.
- State source: `LIVE_STAGE_HEARTBEAT`.
- Freshness classification: `CURRENT_REPORT`.
- Live trading reported by source: `No`.
- Real capital: `0`.
- Automatic promotion: `No`.

The WebUI source version is not claimed as the executing runtime release. The explicit runtime-release field remains unverified.

## Current blockers / not yet proven

- **P0:** Same-Run-Resume — recovery after interruption worked, but continuation under the exact same run id is not yet proven.
- **P0:** QUICK terminalization — the active run must complete with correct identity, one terminal result and persisted learning memory.
- **P0:** QUICK → BALANCED — only a genuinely promising QUICK may trigger BALANCED, and this still needs prospective runtime proof.
- **P0:** Watch-vs-Research parity — determine whether the current trade/no-trade difference is expected setup behavior or an assignment/pipeline defect.
- **P0:** Research Forward freshness/outcomes — keep proving fresh functional cycles rather than only process existence.
- **P0:** Current Truth / stale detection — runtime and WebUI must distinguish fresh worker truth from historical stage state.
- **P0:** Historical OpenAI outcome repair — older suspicious settlements with `entry_price == exit_price` remain a separate unresolved data-quality item until provenance and rebuild are proven.
- **P0:** Runtime context gate — latest observed artifact remains `FAIL_INCOMPLETE_V3_CONTEXT`; this publication did not rerun the gate.
- **P0:** Live readiness remains closed. No automatic live or real-capital promotion.

## What the nightly publisher still gets wrong

The scheduler and GitHub upload work. The remaining problem is source selection and narrative generation.

The nightly currently prefers dated reviewed summaries and a small set of projected reports. If fresh work is present only in newer repair/runtime artifacts that are not recognized by the publisher, it falls back to older development text and can emit `NO_NEW_DEVELOPMENT_PROOF_TODAY_PREVIOUS_DATED_WORK_PRESERVED` even though material work happened.

The next publisher revision should therefore build the daily narrative deterministically from structured evidence for the publication day:

1. `today_completed`
2. `today_verified`
3. `today_failed_or_blocked`
4. `runtime_state`
5. `active_scientific_run`
6. `important_corrections`
7. `current_todo`
8. `still_not_proven`

It should ingest current acceptance/repair summaries, runtime heartbeats, scientific-run events, experiment memory, Watch/Forward status and blocker reports before falling back to an older reviewed summary. Old release notes remain history, not the default daily headline.

## Safety boundary

The boundary remains `LIVE=false`, `DIRECT_ACTION=0`, `CONSUMER=0`, `REAL_CAPITAL=0`. No automatic live trading and no automatic real-capital promotion.

[Current status](../CURRENT_STATUS.md) · [Roadmap](../docs/progress/ROADMAP.md) · [Tests](../docs/verification/TEST_RESULTS.md) · [Source projection](../evidence/DAILY_SUMMARY.json)
<!-- AUTO_VALUES_END -->