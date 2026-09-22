# Architecture overview

This is a public, high-level view of how AlgoSphere is intended to fit together. It describes the research architecture without publishing private application code, proprietary strategy parameters or deployment details.

## The main loop

```text
Market data
   ↓
Market context / state / structure
   ↓
Research candidates
   ↓
Decision lanes
   ↓
Paper / Shadow / Research outcomes
   ↓
Canonical Memory
   ↓
Learning Delta
   ↓
Revalidation / lifecycle
   ↺
```

The important part is the loop: a later decision should be able to trace back to the evidence that influenced it.

## 1. Market inputs

AlgoSphere works with market information across several horizons.

Public documentation distinguishes between:

- execution truth used for outcome measurement
- context/features used for analysis
- broader market context such as BTC/ETH, structure, volatility and news where relevant

The project avoids treating future information as if it were available at decision time.

## 2. Market understanding

Before a strategy or model is judged, AlgoSphere tries to describe the environment it is operating in.

Public examples stay intentionally broad: regime, structure, volatility and transition context. Exact indicators, thresholds, feature definitions and combinations are private.


The goal is not to assume that one strategy works equally well in every market state.

## 3. Rule and ML research

Rule evidence is preserved separately from ML research performance. Exact selector design, feature sets and scoring logic are private.

That matters because ML should have to demonstrate value against a real baseline rather than replacing a working rule system by default.

The public lifecycle is:

`HYPOTHESIS → QUICK → ROBUST_OOS → CHALLENGER → PAPER → CHAMPION`

A candidate can fail, remain inconclusive or be preserved without promotion.

## 4. Decision lanes

AlgoSphere intentionally separates different decision populations.

Public documentation separates simulated, research and counterfactual populations. Exact lane names, routing rules and eligibility logic are private.


These lanes are not silently mixed because their decisions may be produced under different contracts.

## 5. Canonical Memory

Canonical Memory is the common evidence layer linking decisions, outcomes and learning. Exact schema, identity fields and joins are private.

It preserves enough identity and provenance for later causal analysis without publishing internal schema or field names.


## 6. Learning and adaptation

AlgoSphere's intended learning loop is controlled rather than self-modifying without limits:

`new evidence → evaluation → revalidation → lifecycle decision`

Learning may influence future strategy selection, but promotion and execution permissions remain governed separately.

## 7. Paper / Shadow before Live

Paper and Shadow paths are used to collect prospective evidence without treating research success as live-readiness.

A technical PASS is not the same as:

- scientific uplift
- robust profitability
- release readiness
- live execution safety

Those require different evidence.

## 8. Demo and later execution

Demo / Packaging / Release is a separate workstream.

A future Connected Demo is still not Live trading, and a future public/client package must have its own:

- permission boundaries
- approved model package
- configuration handling
- reconnect/recovery behavior
- integrity/update/rollback path
- credential protection

Live-readiness remains later work behind controlled simulation and stability proof. Exact venue/account rollout order is private.

## Why the architecture is built this way

The project is trying to answer a harder question than “can a model predict price?”

It is trying to learn:

> what works, where, under which conditions, with what evidence — and when not trading is the better decision.

That requires preserving failed experiments, separating populations and making the learning path auditable.

See also: [Project Direction](PROJECT_DIRECTION.md) · [Current Status](../../CURRENT_STATUS.md) · [Evidence Summary](../../evidence/EVIDENCE_SUMMARY.md)
