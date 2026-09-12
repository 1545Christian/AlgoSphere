# Current public status

Publication date: **2026-09-12**.

This page is a human-reviewed correction of the public state after the automatic nightly narrative carried older September 5/6 development text forward for several days. Runtime observations, implementation reports and acceptance proofs are kept separate.

## Current research state

AlgoSphere remains a research system. Live trading and automatic real-capital promotion are disabled.

The most important recent change is the rebuild of the OpenAI research path. Earlier OpenAI comparison data was re-audited and several issues were found: mixed Spot/Futures context, stale per-coin inputs, an historical exit-time interpretation problem and overly permissive immediate-entry assumptions in the comparison logic.

The prospective OpenAI path has therefore been rebuilt as an **AI-only Bitget Futures path** with explicit request snapshots, causal timing and a single active economic contract of **100 USDT with 12 bps costs**.

## OpenAI / canonical outcome correction

The earlier 87-trade OpenAI control window produced about **+43.49 USDT** under the old 12-bps calculation. Rebuilding the same control set against the intended Bitget Futures price basis changed the result to about **+27.07 USDT**.

The continuation did not confirm the early curve:

- control window: 87 trades, about **+27.07 USDT** after Futures correction
- continuation: 672 trades, about **-116.50 USDT**
- combined evaluated set: 759 trades, about **-89.43 USDT**
- open OpenAI cases at the September 10 rebuild snapshot: 25

The positive start was concentrated: three ENA trades contributed about **+28.68 USDT**, while the remaining 84 control trades were slightly negative in aggregate.

This does **not** prove one single selection-rule change caused the later losses. The audit did show materially stale input context in part of the continuation and a strong side asymmetry: later Long signals were the main source of loss, while Shorts remained positive overall.

## Canonical outcome base

The active canonical contract is now **100 USDT / 12 bps**.

Latest rebuild report:

- **81,283 outcomes migrated**
- active X9/50-USDT outcomes: **0**
- duplicates: **0**
- checked orphan references: **0**
- **327 outcomes remain `UNPROVEN`** rather than being forced into valid history

Missing evidence remains missing evidence.

## OpenAI AI-only Paper path

The prospective implementation now follows these boundaries:

- Bitget Futures 1m only for reference, entry and exit prices
- fresh 1m / 5m / 15m / 1h context before each OpenAI request
- no local-ML direction in the OpenAI request
- no Spot fallback
- no X9 logic in the active OpenAI outcome path
- entry only after the OpenAI response exists and its structured Futures condition is satisfied
- newer coin evaluations supersede older pending ideas to prevent delayed "zombie entries"
- NO_TRADE, expired, invalidated and superseded predictions remain available for learning without inventing trades or PnL
- request cadence and daily API limit unchanged
- response limit increased from 2,200 to 3,200 tokens to reduce incomplete responses without increasing request frequency

The implementation report records **28 targeted tests passed**, Futures preflight **PASS**, active X9 outcomes **0**, local-ML fields in the OpenAI request **0**, and test-triggered API calls **0**.

The supervisor automatically reloaded the changed process. A natural prospective AI-only case had not yet occurred at the time of the acceptance report, so the end-to-end forward proof remains open.

## Timing clarification

The previously discussed "30 minutes" referred to stale **input context**, not to proven fills occurring 30 minutes after an OpenAI response.

Observed signal-to-fill gaps in the normal runtime paths were much smaller:

- Paper: up to about 85 seconds
- Watch: up to about 86 seconds
- Research Forward: up to about 88 seconds

Where response availability could be proven for historical OpenAI comparison rows, the answer arrived roughly 16–33 seconds after the stored prediction timestamp. Those rows were historical comparison trades, not real executed orders.

## What remains open

1. Observe the first natural AI-only prospective cases end to end.
2. Keep the request snapshot immutable from prompt through outcome memory.
3. Rebuild or leave `UNPROVEN` legacy OpenAI rows whose context or exit evidence cannot be proven.
4. Keep historical reference comparison strictly separated from prospective Paper execution.
5. Continue the research lifecycle as **HYPOTHESIS → QUICK → ROBUST_OOS → CHALLENGER → PAPER → CHAMPION**. Candidate remains eligibility/artifact metadata rather than a separate operational stage.
6. Preserve rule-edge when ML rejects: a valid rule artifact must not be deleted merely because ML says no.
7. Repair the nightly publisher's source-selection layer so recent engineering work is not replaced by an older narrative.
8. Runtime context gate evidence still requires resolution before any live-readiness claim.

## Publication note

The daily GitHub upload itself has been running on schedule. The recent defect was in the **automatic narrative/source selection**, not the upload scheduler. This status intentionally records both improvements and corrections instead of treating every implementation report as an end-to-end PASS.

[Latest English update](updates/2026-09-12-public-status.md) · [Latest German update](updates/2026-09-12-public-status_DE.md) · [Roadmap](docs/progress/ROADMAP.md) · [Completed engineering work](docs/progress/COMPLETED_WORK.md) · [Tests](docs/verification/TEST_RESULTS.md)
