# Current public status

Publication date: **2026-09-07**. Runtime observations, implementation reports and acceptance proofs remain separate.

## Operational state from local reports

- Runtime release reported in explicit field: `not verified`.
- Acceptance report label (not executable version): `v125`.
- WebUI source version: `v90_8_10_127`.
- Explicit package/update manifest: `not verified`.
- Application source version: `v90_8_5`.
- Historical source-hotfix identifier: `v90_8_5_23`.
- ML: `ML AUTOPILOT QUICK RUNNING` · quick · MODEL_TRAIN · MYXUSDT · 3/5.
- State source: `LIVE_STAGE_HEARTBEAT`.
- Freshness classification: `CURRENT_REPORT`.
- Source timestamp: `2026-09-07T22:45:00.432722Z`.
- Live trading reported by source: `No`; Real Capital: `0`; Promotion reported by source: `No`.

A current report timestamp is not proof of a fresh worker by itself. A schema label or WebUI source version does not prove the version of executing code.

This publisher only reads reports. It starts no training, orders, promotions or capital actions.

## Most recent documented development

- **2026-09-07 · Runtime recovery:** the local stack was visibly restarted and core services returned under the supervisor.
- **2026-09-07 · ML observation:** a real QUICK run is active with fresh stage heartbeat, profile `quick`, phase `MODEL_TRAIN`, symbol `MYXUSDT`, progress `3/5`.
- **2026-09-07 · Important limitation:** recovery used a new run identity, therefore exact Same-Run-Resume remains open and is not reported as PASS.
- **2026-09-07 · Watch/Research investigation:** Watch may create trades while Research can remain `NO TRADE`; this must be resolved through causal funnel parity on identical timestamps/coins/market states, not by forcing trades or loosening thresholds.
- **2026-09-07 · Publisher defect identified:** the nightly can incorrectly fall back to older reviewed development text when current repair/runtime artifacts are not part of its source-selection set.

## Current blockers and next proof

- Same-Run-Resume under the exact original run id.
- Correct terminalization of the active QUICK with identity, one terminal result and persisted learning memory.
- Prospective QUICK → BALANCED only for genuinely promising evidence.
- Watch-vs-Research parity across eligibility, assignment, setup gates, decisions and outcomes.
- Fresh Research Forward functional cycles/outcomes over a longer run.
- Current Truth / stale detection across runtime and WebUI.
- Historical OpenAI outcome repair for suspicious `entry_price == exit_price` settlements.
- Latest observed runtime-context gate remains `FAIL_INCOMPLETE_V3_CONTEXT`; the public publisher did not rerun it.
- Live readiness remains closed; no automatic real-capital promotion.

## GitHub nightly status

The scheduler and GitHub upload are working. The remaining defect is the automatic narrative/source-selection layer. The publisher must ingest current-day repair/acceptance summaries, runtime heartbeats, scientific-run events, experiment memory, Watch/Forward state and blocker reports before falling back to older dated summaries.

The intended daily sections are: `today_completed`, `today_verified`, `today_failed_or_blocked`, `runtime_state`, `active_scientific_run`, `important_corrections`, `current_todo`, and `still_not_proven`.

## Research eligibility

No eligible experiment is reported by the latest projected eligibility source; this is not launch authorization.
Source timestamp: `2026-09-07T22:44:32.920542Z`.

## Safety boundary

`LIVE=false`, `DIRECT_ACTION=0`, `CONSUMER=0`, `REAL_CAPITAL=0` remain the operating boundary.

See the [dated update](updates/2026-09-07-public-status.md), [roadmap](docs/progress/ROADMAP.md) and [test evidence](docs/verification/TEST_RESULTS.md).