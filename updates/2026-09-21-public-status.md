# Public status update — 2026-09-21

Deutsch: [Öffentliches Status-Update](./2026-09-21-public-status_DE.md)

> **Late September 21 update:** the newest internal handoff moved the state forward again. WebUI browser acceptance is now at **90.8.10.239** for B37/B38/B39 PASS. The current Memory writer is PASS, but global/historical Memory trust remains open because of existing chain/join gaps. A small OpenAI exact-repair is blocked by target-set drift (3 authorized / 4 discovered) and the still-unproven writer-free maintenance state. The new OpenAI paper-loop patch has **49 focused tests PASS** but is not yet runtime-active; the earlier approximately **+43.49 USDT** interpretation is still unreconciled. **Bitget Demo/Testnet has not started and remains M2 BLOCKED_BY_M1.**

## Why this update exists

No major AlgoSphere development work was continued on September 20. This update reconciles the latest verified state across the project threads so the public documentation does not carry stale blockers forward or imply that unfinished work is complete.

## Runtime and Research Forward

The latest Research Forward restart proof is stronger than the earlier code-only checks. The current scientific overlay is bound before engine creation and the active process has a composition/hash receipt.

- runtime composition hashes: **35/35 PASS**
- Research Forward process: live
- strategies: **170 expected / 170 active / 0 duplicates**
- CURRENT control path: unchanged
- WebUI at that proof: **90.8.10.199**
- CURRENT and CONTEXT_V2 remain visibly separated

A snapshot from that proof showed CURRENT 19 settled / -2.05 USDT and CONTEXT_V2 13 settled / -0.79 USDT.

Those numbers are not evidence that V2 is better. Many new events around that proof were still NO_CURRENT_SETUP, so a causal selector-ranking improvement was not demonstrated.

## Canonical Memory and learning

The Canonical Memory core and the current new-write contract have now been reported **PROVEN_CLOSED** for the current path: provenance, machine/human/AI readability, no-parallel-truth rules and Learning Delta before/after evidence are in place.

That does not mean all historical data is repaired. Still separate and open:

- historical PAPER/CURRENT Contribution/Delta population mismatch
- historical state/version gaps
- PAPER/CONTEXT_V2 still lacks a comparable executed-outcome population
- historical exact-only repair/backfill remains a separate legacy-data task
- some new Research handoffs still need natural forward proof

**Current contract closed does not mean historical archive fully normalized.**

## CONTEXT_V2 learning

The existing CONTEXT_V2 selector now consumes Canonical Learning Delta evidence instead of relying only on market-state/context-fit. CURRENT remains the control path.

The connection is technically implemented and tested. A meaningful trading improvement remains **INSUFFICIENT_EVIDENCE** until natural multi-candidate / settled evidence exists.

## Market Intelligence and training

The ENA full-history one-coin pilot remains the latest important training result:

- RULE_VS_ML = DEGRADED
- candidate_eligible = false
- no Challenger promotion
- no automatic promotion
- Rule evidence preserved

The Robustness Gate remains the required evidence layer before any later Challenger claim. Broad multi-coin training is still deferred.

## Research evidence handoff

The Research → standardized memory handoff was repaired future-only so compact Candidate / Rule / Nested-Fold / Contract evidence is no longer dropped before the Canonical Memory boundary.

The fix is structurally tested, but FUTURE_RESEARCH_HANDOFF_PROVEN remains **AWAITING_REAL_RUN**. No extra training run should be started only to prove it.

## Storage / database

The local database had grown to roughly 62 GB, with research_runs contributing roughly 35 GB.

The active-strategy snapshots are mostly unique, so classic content deduplication is not the solution. The future writer was corrected so decoded canonical values are no longer stored together with duplicate physical *_json aliases.

Representative evidence indicates roughly **49% smaller future large snapshots**. Historical rows were not deleted, migrated or vacuumed.

Retention/compaction remains a separate later task because checkpoint, completion-marker and artifact-reference coverage must remain safe enough to preserve scientific evidence.

## WebUI

The Trade Like Che / Research views are substantially clearer: CURRENT and CONTEXT_V2 are separated, filter/variant/scroll state survives refresh, long fields use tooltips, and local IP plus configured aliases served the same accepted build.

The broader product-style information architecture is still not treated as finished. Large histories still need cleaner pagination/virtualization and some pages remain too dense.

## OpenAI AI-only

The AI-only path remains independent: OpenAI is the final trading decision layer inside that lane and the local code is not supposed to re-decide the trade after a valid AI plan.

The input contract now includes the intended multi-timeframe context, BTC/ETH context, news, market structure/support-resistance, learning memory and current OpenAI position context.

Open positions are monitored locally and should not cause periodic duplicate paid calls merely because they remain open.

The compact single-plan request path still needs normal forward proof, and OpenAI decision quality / profitability remains **not proven**. The older positive PnL interpretation must not be used as profit evidence.

## Demo / Packaging / Release

Demo and distribution are **not finished** and are explicitly tracked as their own release area.

Current status: **OPEN / BLOCKED**

Still required before a public/client demo can be called ready:

- strict isolation between Offline Demo and Connected Demo
- no accidental Training, OpenAI paid calls, Live trading or real-capital activation
- approved/signed model-bundle contract instead of "latest model"
- Demo/Testnet end-to-end proof
- Decision → Entry → Exit → Outcome → reconnect/recovery proof
- product-ready WebUI/client surface
- installer / update / rollback / config / log handling
- decision on local-PC vs remote WebUI/server operating model
- later server/webspace deployment contract
- secure credential handling
- explicit read-only exchange permissions where applicable
- release integrity, licensing/terms/disclaimer and distribution-profile isolation

**Demo Connected ≠ Live.**
**Bitget read-only access ≠ trading permission.**
**LAST_APPROVED_MODEL_BUNDLE ≠ latest trained model.**

Normal Futures live-readiness remains later work behind Demo/stability proof, and Elite/UTA remains deferred beyond stable Normal Futures.

## What is still scientifically open

More infrastructure is working, but durable predictive/trading uplift is still not demonstrated:

- ENA ML did not beat its preserved Rule baseline
- V2 selector benefit is not yet proven by enough natural candidate/outcome evidence
- OpenAI quality is not yet proven by enough settled causal outcomes
- a newly promoted Challenger/Champion cycle is not yet demonstrated

## Public safety boundary

- Live trading: **disabled**
- Real capital: **0**
- Automatic promotion: **disabled**
- Demo release: **not ready**
- Elite/UTA: **deferred**

No documentation update authorizes live trading, real-capital execution, automatic model promotion or release readiness.

[Current status](../CURRENT_STATUS.md) · [Roadmap](../docs/progress/ROADMAP.md) · [Documented work](../docs/progress/COMPLETED_WORK.md) · [Test results](../docs/verification/TEST_RESULTS.md)