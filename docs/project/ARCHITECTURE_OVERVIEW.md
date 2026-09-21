# Architecture overview

This is a public, high-level view of how AlgoSphere is intended to fit together. It describes the research architecture without publishing private application code, proprietary strategy parameters or deployment details.

## The main loop

```text
Market data
   ↓
Market context / state / structure
   ↓
Strategy & model candidates
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

- execution truth used for entries/exits
- context/features used for analysis
- broader market context such as BTC/ETH, structure, volatility and news where relevant

The project avoids treating future information as if it were available at decision time.

## 2. Market understanding

Before a strategy or model is judged, AlgoSphere tries to describe the environment it is operating in.

Examples include:

- range vs trend behavior
- directional state
- transition / volatility expansion / shock conditions
- support/resistance and structural context
- multi-timeframe alignment

The goal is not to assume that one strategy works equally well in every market state.

## 3. Rule and ML research

Rule evidence is preserved separately from ML-selector performance.

That matters because ML should have to demonstrate value against a real baseline rather than replacing a working rule system by default.

The public lifecycle is:

`HYPOTHESIS → QUICK → ROBUST_OOS → CHALLENGER → PAPER → CHAMPION`

A candidate can fail, remain inconclusive or be preserved without promotion.

## 4. Decision lanes

AlgoSphere intentionally separates different decision populations.

Examples in the current public documentation include:

- Paper
- Research Watch / Forward
- Trade Like Che CURRENT
- Trade Like Che CONTEXT_V2 Shadow
- OpenAI AI-only
- Counterfactual evidence

These lanes are not silently mixed because their decisions may be produced under different contracts.

## 5. Canonical Memory

Canonical Memory is the common evidence layer that links:

`Decision → Trade / NO_TRADE → Outcome → Learning`

It is designed to preserve identity and provenance so later analysis can ask:

- which decision produced this outcome?
- which strategy, side and market state were involved?
- what happened after entry?
- what evidence was learned?
- did later selection actually change?

## 6. Learning and adaptation

AlgoSphere's intended learning loop is controlled rather than self-modifying without limits:

`new evidence → evaluation → Learning Delta → revalidation → lifecycle decision`

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
- approved model bundle
- configuration handling
- reconnect/recovery behavior
- integrity/update/rollback path
- credential protection

Normal Futures live-readiness remains later work, and Elite/UTA is deferred beyond stable Normal Futures.

## Why the architecture is built this way

The project is trying to answer a harder question than “can a model predict price?”

It is trying to learn:

> what works, where, under which conditions, with what evidence — and when not trading is the better decision.

That requires preserving failed experiments, separating populations and making the learning path auditable.

See also: [Project Direction](PROJECT_DIRECTION.md) · [Current Status](../../CURRENT_STATUS.md) · [Evidence Summary](../../evidence/EVIDENCE_SUMMARY.md)
