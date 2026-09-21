# Project direction

AlgoSphere started as a trading-analysis and automation project, but the long-term goal is broader than running a single strategy or model.

The project is being developed toward a configurable quantitative research and trading-analysis system for crypto markets that can work across a broad coin universe and improve its decisions through measured evidence rather than by blindly retraining or changing parameters.

## What the system is meant to do

Over time, AlgoSphere should be able to:

- monitor a configurable universe of crypto markets
- understand market structure, regime and state across several time horizons
- compare multiple strategy families instead of assuming one approach works everywhere
- train and validate machine-learning models against preserved Rule baselines
- track Decisions → Trades → Outcomes consistently
- learn from profitable, losing and NO_TRADE decisions
- identify which approaches work by coin, side, market state and horizon
- re-evaluate strategies and models when enough new evidence exists
- preserve failed and negative experiments instead of hiding them
- move research forward only when the evidence supports it

The intended research lifecycle is:

HYPOTHESIS → QUICK → ROBUST_OOS → CHALLENGER → PAPER → CHAMPION

A later model should not become active simply because it is newer. Promotion is meant to depend on reproducible evidence, robustness and controlled comparison.

## Configurable, not tied to a handful of coins

The coins visible in current runtime or research reports are working populations, not the intended product limit.

The long-term direction is a configurable coin universe: as many supported markets as can be processed reliably within data, compute, liquidity, quality and exchange constraints.

Different coins may require different strategies, thresholds, horizons or no trade at all.

The goal is therefore not:

> find one model that trades everything

but rather:

> learn what works, where, under which conditions — and when the best decision is not to trade.

## Learning without uncontrolled self-modification

“Self-improving” in AlgoSphere does not mean allowing the system to rewrite or promote itself without evidence.

The intended loop is controlled:

new evidence → evaluation → learning delta → revalidation → lifecycle decision

Research automation may become increasingly autonomous, while runtime permissions, promotion rules, release boundaries and any future real-capital execution remain explicitly governed.

## Analysis, training and execution are separate concerns

AlgoSphere is intended to become useful as:

1. a market-analysis environment,
2. an ML and strategy research/training system,
3. a Paper/Shadow validation environment,
4. later, a controlled execution system where the evidence and safety contract support it.

These stages are intentionally separated so that a successful analysis or training run is never mistaken for live-readiness.

## Public project boundary

This GitHub repository documents the public research record, status, evidence, methodology and selected verification tooling.

The private application/runtime source, credentials, market databases, trained model bundles and proprietary strategy parameters are not published here.

That separation is deliberate: the public repository is meant to make the work understandable and auditable without publishing the operational trading system itself.