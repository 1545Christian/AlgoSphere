# Public status update — 2026-09-04

Deutsch: [Öffentliches Status-Update](./2026-09-04-public-status_DE.md)

<!-- AUTO_VALUES_START -->
## Summary

v117 separates training authority, evaluation, history/cache handling and OpenAI cost control more clearly. The nightly publication now distinguishes what was implemented, what was actually verified and what remains open.

## What AlgoSphere is intended to do

- Local ML training is intended to run autonomously, discover new strategies and semantically deduplicate identical experiments.
- Paper, Research Forward, Watch, Challenger, Champion and OpenAI remain distinct roles within a shared traceable decision/risk/exit chain.
- Memory is intended to store standardized training/outcome knowledge and later prove that it influences new hypotheses and selections.
- The WebUI is intended to show one trustworthy source per card, keep roles separate and present training, market and OpenAI state clearly.
- No live-trading or real-capital path is enabled automatically; promotion remains fail-closed until required runtime proof exists.

## Implemented in v90_8_10_117

- `LOCAL_ML_AUTOPILOT` is the only normal training start authority; Research Forward runs as an `--evaluate-only` evaluator and is not intended to start a second training job.
- `training_forensic_hold` was removed from normal operation while resource and crash safeguards remain separate.
- The autonomous QUICK → BALANCED follow-up path remains within Local ML.
- History sync was changed to one full scan per run plus targeted new archives and bundled ledger lookups.
- The shared FeatureCache identity contract is `v90_8_5_117_unified_feature_cache_contract_1`; legacy cache namespaces are separated.
- Codex/candidate-builder/dispatcher lineage is archived as historical evidence and is not used by the normal runtime path.
- The v84 version-independent semantic-memory contract is preserved.
- OpenAI is bounded to the default model `gpt-5.6-luna`, low reasoning and a maximum of 2200 output tokens; default cadence is 120 minutes, web-news 360 minutes, with daily limits of 12/4 calls.
- Unchanged OpenAI context is intended to skip a new API call (`UNCHANGED_CONTEXT_SKIPPED`).
- A new immutable v117 research core is rebuilt from the corrected current source.
- The GitHub nightly path has no Codex dependency and publishes runtime status separately from human-reviewed release notes.

## Verified for this release

- Python compile for changed/new Python files: PASS.
- Core regression set: 149 tests PASS; exact installer test list: 194 tests PASS.
- Archive dry run: PASS; 214 lineage files hash-verified, v84 memory preserved, no source file deleted.
- Research-core dry run: PASS.
- v117 acceptance dry run: `PASS_CODE_CONTRACT_AWAITING_RUNTIME_PROOF` — explicitly not a full Windows/operational proof.

## Current runtime state

- Runtime release observed: `v90_8_10_116`.
- ML autopilot: `QUICK_RUNNING` · profile `quick` · phase `CONTEXT_LOAD` · symbol `BTCUSDT` · coins `0/5`.
- Stage truth source: `LIVE_STAGE_HEARTBEAT`.
- Live trading: `No` · real-capital flag: `0` · automatic promotion: `disabled`.
- Snapshot observed: `2026-09-04T00:43:25.149915Z`.

## Still open / not yet proven

- P0 open: existing FeatureCaches are not yet incrementally extended only with new candles; this remains explicitly unresolved.
- A Windows long run must prove that QUICK starts only through Local ML and that Research Forward does not create a second training start.
- A real QUICK completion followed by an autonomous BALANCED start must be observed prospectively.
- History-sync runtime and import volume must be measured on Windows against the previous double-scan behavior.
- OpenAI daily counting/reset, web due-state and `UNCHANGED_CONTEXT_SKIPPED` must be confirmed in real scheduler runs.
- Code PASS alone does not close an item: `PROVEN_CLOSED` requires current runtime/browser/ledger evidence.

## Technical evidence

Detailed hashes, public register entries, verification limits and historical artifacts remain available separately. They are evidence, not a substitute for the development summary above.

See [Current status](../CURRENT_STATUS.md), [Test results](../docs/verification/TEST_RESULTS.md), [Roadmap](../docs/progress/ROADMAP.md) and the [Evidence summary](../evidence/EVIDENCE_SUMMARY.md).
<!-- AUTO_VALUES_END -->
