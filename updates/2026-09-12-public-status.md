# Public status update — 2026-09-12

Deutsch: [Öffentliches Status-Update](./2026-09-12-public-status_DE.md)

## Summary

The last few days were mainly about correcting the data and evidence path around OpenAI research, not about trying to make an old equity curve look better.

The important result is that several assumptions from the earlier OpenAI comparison were too optimistic or technically incomplete. We found mixed Spot/Futures inputs, stale per-coin context, an historical exit-time interpretation problem and an execution model that could treat a directional OpenAI answer as an immediate trade even when the text itself asked for confirmation or a pullback.

Those findings changed the direction of the work. The active OpenAI paper path has now been rebuilt as a prospective **AI-only Futures path** with explicit snapshots, causal timing and a single canonical 100-USDT / 12-bps contract. The historical comparison remains useful as a research reference, but it is no longer treated as unquestioned performance truth.

## What changed between September 8 and September 11

### Research / Forward warm-up and outcome visibility

A warm-up problem in the Research path was corrected so the system uses a sufficiently long history before evaluating setups. After that repair, fresh cycles and outcomes became visible again instead of the earlier misleading zero-result state.

This matters because a research system must distinguish between "no setup existed" and "the pipeline never had enough data to evaluate one".

### Canonical outcome rebuild: from an intermediate 50-USDT cleanup to the active 100-USDT truth

An intermediate 50-USDT normalization was completed first to remove duplicates, inconsistent cost handling and unproven rows from the historical outcome base.

The active contract has since been superseded by a **canonical 100-USDT basis with 12 bps global costs**. The latest rebuild migrated **81,283 outcomes**. Active X9/50-USDT outcomes, duplicates and checked orphan references are reported as **0**. **327 outcomes remain explicitly UNPROVEN** instead of being silently converted into valid results.

This is intentional: missing evidence stays missing evidence.

### OpenAI historical comparison was rechecked against Futures prices

The earlier OpenAI control window consisted of 87 historical comparison trades. Under the old 12-bps calculation it produced about **+43.49 USDT**.

When the same control set was rebuilt against the intended **Bitget Futures** price basis, the result changed to about **+27.07 USDT**.

The following continuation did not confirm the early curve:

- control window: 87 trades, about **+27.07 USDT** after Futures correction
- continuation: 672 trades, about **-116.50 USDT**
- combined evaluated set: 759 trades, about **-89.43 USDT**

As of the rebuild snapshot on September 10, 25 OpenAI cases were still open.

The early positive result was also highly concentrated: three ENA trades contributed about **+28.68 USDT**, while the other 84 control trades were slightly negative in aggregate.

The continuation showed a clear side asymmetry. Shorts remained positive overall, while later Long signals were the main source of loss. This is evidence of changed outcome quality, but not proof that a single new selection rule caused it.

### The "30-minute" issue was clarified

A previous description could be read as if trades were being filled 30 minutes after an OpenAI response. That was not what the audit showed.

The confirmed problem was **stale input context**: a fresh overall analysis cycle could reuse an older per-coin prediction. In the audited continuation, older source context was strongly associated with worse results.

For the normal runtime paths, observed signal-to-fill gaps were much smaller:

- Paper: up to about 85 seconds
- Watch: up to about 86 seconds
- Research Forward: up to about 88 seconds

For the historical OpenAI comparison, the stored comparison entry was tied to the original prediction timestamp; where response availability could be proven, the answer arrived roughly 16–33 seconds later. Those rows were historical comparison trades, not real executed orders.

### OpenAI request snapshots are now bound to what the model actually saw

The code was changed so the evidence chain preserves the actual request context instead of reconstructing it later from newer market data.

The intended binding now includes:

- the exact market context used for the request,
- Futures reference price,
- request start and response time,
- the decision context that Paper/Watch used,
- and later settlement against the original evidence rather than a substituted lookup.

A later writer must not silently fill missing price evidence or replace the original context.

### The AI-only OpenAI Paper path was rebuilt

The prospective OpenAI path has now been separated from local ML direction and legacy context.

The active implementation is designed around these rules:

- **Bitget Futures 1m only** for reference, entry and exit pricing,
- fresh 1m / 5m / 15m / 1h context before each OpenAI request,
- no local-ML direction inserted into the OpenAI request,
- no Spot-price fallback,
- no X9 logic in the active OpenAI outcome path,
- entry only after the OpenAI response exists and its structured Futures condition is satisfied,
- newer evaluations supersede older pending ideas so "zombie entries" cannot appear later,
- NO_TRADE, expired, invalidated and superseded predictions remain available for learning without inventing trades or PnL,
- the active economic contract remains **100 USDT with 12 bps costs**.

The API cadence and daily usage limit were kept unchanged. The response limit was increased from 2,200 to 3,200 tokens to reduce incomplete responses without increasing request frequency.

### Verification of the new prospective path

The implementation report records:

- **28 targeted tests passed**,
- Futures preflight: **PASS**,
- active X9 outcomes in this path: **0**,
- local-ML fields in the OpenAI request: **0**,
- API calls triggered by the test run: **0**.

The supervisor automatically reloaded the changed process. At the time of the acceptance report, the first natural new AI-only case had not yet occurred, so the prospective end-to-end runtime proof is still pending.

That boundary is important: implementation and tests are positive evidence, but they are not the same as a natural forward result.

## What remains open

The current priorities are now clearer:

1. Observe the first natural AI-only prospective cases end to end.
2. Keep the request snapshot immutable from prompt to outcome memory.
3. Rebuild or mark legacy OpenAI rows whose historical context or exit evidence cannot be proven.
4. Keep historical reference results separate from prospective Paper execution.
5. Continue the broader Factory → QUICK → ROBUST_OOS → CHALLENGER → PAPER → CHAMPION lifecycle work without bypassing evidence gates.
6. Repair the public nightly publisher's source-selection layer so recent engineering work is not replaced by an older September 5 narrative.

## Public-status correction

The GitHub nightly upload itself has been running on schedule during the last days. The weak point was the **automatic narrative selection**: the daily files kept carrying older September 5/6 development text forward even though newer work existed locally.

This September 12 update is therefore a human-reviewed correction of the public narrative. It does not retroactively turn old results into PASS. It records what changed, what was disproven, what was repaired and what still needs natural runtime evidence.

## Safety boundary

AlgoSphere remains a research system. Live trading and automatic real-capital promotion remain disabled. Historical and paper results are research evidence, not a promise of future performance.

[Current status](../CURRENT_STATUS.md) · [Roadmap](../docs/progress/ROADMAP.md) · [Completed engineering work](../docs/progress/COMPLETED_WORK.md) · [Tests](../docs/verification/TEST_RESULTS.md)
