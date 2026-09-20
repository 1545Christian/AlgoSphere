# Current public status

Publication date: **2026-09-21**. Human-reviewed.

No major AlgoSphere development work was continued on September 20. This document consolidates the latest verified state and removes stale blockers from the public status.

## Operating boundary

- Live trading: **No**
- Real capital: **0**
- Automatic promotion: **No**
- Demo release: **Not ready**
- Elite / UTA: **Deferred**
- Paper / Shadow research: active
- Training: operator-controlled; no broad automatic training
- Safety boundary: fail-closed

## Runtime / Research Forward

The latest Research Forward restart proof confirms that the current scientific overlay is bound before engine creation.

- runtime composition hashes: **35/35 PASS**
- Research Forward hash proof: **PASS**
- strategies: **170 / 170**
- duplicates: **0**
- CURRENT control path unchanged
- WebUI: **90.8.10.199**

The same proof showed CURRENT 19 settled / -2.05 USDT and CONTEXT_V2 13 settled / -0.79 USDT.

This does **not** prove V2 is better. The new event population around that proof was still dominated by NO_CURRENT_SETUP, so selector-ranking uplift is not yet established.

## Canonical Memory / Learning

The current Canonical Memory core and new-write contract are now treated as **PROVEN_CLOSED**.

Current-path guarantees include stable provenance and identity, machine/human/AI-readable evidence, no parallel truth path, Decision → Outcome → Learning linkage and Before → Delta → After traceability.

The earlier SQLite-lock status is no longer the final state: the scoped Exact-only backfill was later committed and targeted mapping/state repair completed where exact evidence existed.

Verified historical repair included:

- PAPER/CURRENT 17/17 Outcome → Contribution → Delta chains repaired
- exact-recoverable state fields repaired for 1,483 PAPER/CURRENT rows
- exact-recoverable state fields repaired for 10 PAPER/CONTEXT_V2 rows
- targeted integrity check: PASS

Legacy gaps intentionally remain where exact evidence does not exist:

- 1,739 UNVERSIONED rows
- 74 no-evidence legacy gaps

Those values are not synthesized. PAPER/CONTEXT_V2 still did not have a comparable settled outcome population at that checkpoint.

## CONTEXT_V2 selector

The existing CONTEXT_V2 selector consumes Canonical Learning Delta evidence in addition to market-state/context-fit. Matching is variant-safe by coin, side, strategy family and market state. CURRENT remains the control path.

Technical connection: proven. Trading improvement: **INSUFFICIENT_EVIDENCE**.

## Market Intelligence / training

The latest important training result remains the ENA full-history one-coin pilot:

- Rule and ML compared on the same OOS folds
- RULE_VS_ML = DEGRADED
- candidate_eligible = false
- no Challenger promotion
- no automatic promotion
- Rule evidence preserved

The Robustness Gate remains required before any later Challenger claim. Broad multi-coin training remains deferred.

## Research handoff

The Research → standardized memory projection now preserves compact Candidate / Rule / Nested-Fold / Contract evidence that had previously been dropped before the Canonical Memory boundary.

The future projection is structurally tested. Current proof state: **AWAITING_REAL_RUN**. No additional training run should be started only to prove this connection.

## Storage / database

The local database had grown to roughly 62 GB, with research_runs contributing roughly 35 GB.

The future snapshot writer was corrected so decoded canonical fields are no longer stored together with duplicate physical *_json aliases. Representative evidence indicates about **49% smaller future large snapshots**.

A Future Summary Identity contract was also added for future runs, including summary hash, schema version, evidence/archive pointers, artifact/checkpoint/canonical-evidence status and retention metadata.

Existing 569 historical runs were not rewritten.

Legacy compaction is **not authorized** yet:

- 0 runs currently proven eligible for automatic compaction
- 173 resumable
- 394 missing required evidence
- 2 unknown

No historical DELETE / VACUUM / migration is authorized from this status.

## WebUI

The Research / Trade Like Che UI is materially improved: CURRENT / CONTEXT_V2 separation, stable variant/filter/scroll state, compact shared table contract, long text via tooltips, and the same served build across local IP and configured aliases at proof time.

The full product-style information architecture is still not considered finished. Large-history pagination/virtualization and further reduction of dense page regions remain open.

## OpenAI AI-only

The AI-only lane remains independent: OpenAI is the final trading decision layer inside that lane.

The current request contract includes multi-timeframe context, BTC/ETH context, news, structure/support-resistance, learning memory and current OpenAI position context. Open positions are monitored locally and should not trigger repeated paid calls merely because they remain open.

Still open: compact single-plan request forward proof, causal decision-quality evidence and trusted cost reporting. Profitability is **not proven** and the older positive PnL interpretation must not be used as profit evidence.

## Demo / Packaging / Release

Demo and distribution remain **OPEN / BLOCKED**.

Before a public/client demo can be called ready, the project still needs:

- Offline Demo / Connected Demo isolation
- no accidental Training / OpenAI-paid / Live / real-capital activation
- approved and signed model-bundle contract
- Bitget Demo/Testnet end-to-end proof
- Decision → Entry → Exit → Outcome → reconnect/recovery proof
- product-ready client/WebUI surface
- installer / update / rollback / configuration / logs
- local-PC vs remote WebUI/server operating-model decision
- later server/webspace deployment contract
- secure credentials
- explicit read-only permissions where intended
- release integrity
- license / terms / disclaimer
- distribution-profile isolation

Important boundaries: Demo Connected ≠ Live; Bitget read-only ≠ trading permission; LAST_APPROVED_MODEL_BUNDLE ≠ latest trained model.

Normal Futures live readiness remains later work behind Demo/stability proof. Elite / UTA remains deferred beyond stable Normal Futures.

## What remains scientifically open

The central research question is unchanged: **more infrastructure works, but durable predictive / trading uplift is not yet demonstrated.**

Not yet proven: ENA ML uplift, CONTEXT_V2 selector uplift, OpenAI decision quality, and a newly completed Learning → Challenger → Paper → Champion cycle.

## Current priorities

1. Keep prospective CURRENT / CONTEXT_V2 evidence collection clean and variant-safe.
2. Wait for a natural Research/QUICK handoff to prove the future compact evidence projection.
3. Continue model-quality investigation before broader training.
4. Keep historical unknowns explicit.
5. Keep legacy storage compaction blocked until retention safety is proven.
6. Continue WebUI simplification.
7. Keep Demo/Packaging/Release separate from Live readiness.
8. Do not reopen Elite/UTA before Normal Futures is stable.

## Safety boundary

LIVE=false · REAL_CAPITAL=0 · automatic promotion disabled · Demo not ready.

No documentation update authorizes live trading, real-capital execution, automatic promotion or release readiness.

See the [September 21 update](updates/2026-09-21-public-status.md), [roadmap](docs/progress/ROADMAP.md), [completed work](docs/progress/COMPLETED_WORK.md) and [test results](docs/verification/TEST_RESULTS.md).