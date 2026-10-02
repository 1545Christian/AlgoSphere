# MIOIQ public status update — 2026-10-01

Deutsch: [Öffentliches Status-Update](./2026-10-01-public-status_DE.md)

This update summarizes reviewed progress since the September 28 public update. It intentionally stays at public, reconstruction-resistant level.

## What moved

### Demo access moved from design to a proven registration path

The invite-approval and first-time Demo registration path has now been exercised end to end in the reviewed local product flow.

That closes this **specific access path**. It does not close the broader Demo product.

Still open are connected venue authentication, execution/recovery end to end, release/distribution readiness and broader multi-user/product acceptance.

### The product model is clearer

Demo is no longer treated as a separate product world.

The current direction is one product with role/account-gated capabilities and fail-closed permissions. Demo, Paper and later connected execution remain different operating scopes inside that product rather than independent applications.

### Runtime and restart work progressed, but autonomy is not closed

Startup/restart handling and dependency boundaries received further engineering work.

The reviewed state is still partial: source and scoped runtime receipts exist, but durable autonomous lifecycle behavior is not yet treated as globally proven.

### WebUI truth checks became more precise

Several filtering, identity and same-snapshot contracts were tightened and tested.

At the same time, a current browser/session/build mismatch exposed why older UI passes cannot be reused as present-day acceptance. Full current WebUI acceptance therefore remains open.

A separate performance investigation also narrowed one previously suspected data-reader bottleneck, but current end-to-end UI timing still needs fresh measurement.

### Paper V2 adoption is visible in the running research path

The current Paper V2 context path has been observed in runtime and natural simulated activity continued through it.

This is an engineering/adoption result only. It is **not** evidence that V2 is better than V1, and no performance-uplift claim is being made.

### Memory / learning integration continued

The current memory path was re-adopted in runtime and natural evidence continued through the reviewed learning path.

Historical identity conflicts and the human-readable Brain/read-projection remain separate open work. Existing evidence is not being rewritten to make those gaps disappear.

### Storage work advanced without pretending logical cleanup is physical shrink

Additional bounded compaction work reduced logical duplication while preserving references.

A controlled pause/resume maintenance path was demonstrated for a scoped window.

The physical database file has **not** been proven durably reduced by the latest logical batches. Retention, remaining legacy references and physical space recovery remain open.

### Multi-venue contracts moved closer to executable readiness

Execution-intent, journaling and isolation contracts advanced, including offline isolation work between simulated and Demo-oriented paths.

This remains pre-execution engineering. No connected private Demo account read, connected Demo order cycle or production-ready multi-venue claim is being made.

### Release/distribution remains an explicit blocker

The current release manifest and moved documentation/source paths are not yet reconciled into a reproducible current installer/update/rollback proof.

That work stays open rather than being hidden behind successful component tests.

## What did not change

- Live trading remains disabled.
- Real capital remains 0.
- Automatic promotion remains disabled.
- Connected Demo/Testnet execution end to end is not proven.
- External AI-analysis profitability is not proven.
- V2 superiority over V1 is not proven.
- Infrastructure progress is not trading edge.

## Current focus

**Research → Evidence → Validation → Controlled Execution**

The project continues to prefer scoped proof over broad claims: source code is not runtime proof, a component PASS is not product acceptance, and a working registration path is not connected Demo readiness.

GitHub: https://github.com/1545Christian/MIOIQ  
Telegram: https://t.me/+BXzjABr9iQpjMTgy

Research & engineering only. No trading signals or investment advice.
