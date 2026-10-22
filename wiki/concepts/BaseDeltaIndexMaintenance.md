---
title: "Base-Delta Index Maintenance"
type: concept
tags: [indexing, databases, mutable-data, consistency]
sources:
  - psql-bm25s
last_updated: 2026-10-22
knowledge_schema: synthesis-v1
---

## Definition
[[BaseDeltaIndexMaintenance]] separates a read-optimized base index from a small append-oriented delta of recent writes, updates, and deletions, then periodically folds the delta into a replacement base.

## Current Synthesis
The design moves expensive global optimization out of ordinary writes. Queries normally use the base, while a realtime path reads the base and delta together or waits for pending maintenance, and an eventual path serves the base with bounded temporary staleness. Background folding produces a new optimized base and retires the previous one.

The pattern exchanges one monolithic mutable structure for coordination among base versions, delta state, readers, and the fold process. Its value depends on fold cost, delta growth, concurrency, crash semantics, write amplification, storage overhead, and whether the application's freshness contract tolerates the eventual path.

## Key Claims
- Foreground writes remain bounded because they append to the delta instead of rebuilding the optimized base.
- Background folding amortizes optimization across accumulated mutations.
- Realtime reads combine or synchronize with recent changes to preserve committed-result freshness.
- Eventual reads reduce coordination cost by accepting brief ranking staleness.
- Safe replacement requires the old base to remain valid until readers can move to the new base.

## Evidence
Write path and fold:
- [[psql-bm25s]] describes recent writes, updates, and tombstones entering a delta that background maintenance folds into a new optimized BM25 base.

Freshness choices:
- [[psql-bm25s]] distinguishes realtime reads over current committed state from faster eventual reads that may briefly observe stale rankings.

Operational boundary:
- [[psql-bm25s]] requires the design to coexist with PostgreSQL WAL, crash recovery, physical replication, and predictable foreground operations.

## Counterevidence & Qualifications
The article explains the architecture but does not publish mutation throughput, fold duration, write amplification, delta-size bounds, concurrent-reader behavior, storage peaks, crash-point tests, replication lag, or freshness-delay distributions. Base-plus-delta is therefore a design pattern demonstrated by the authors' implementation claim, not evidence that every mutable index should use the same structure or expose the same consistency modes.

## What Changed
- Added base-plus-delta maintenance as a way to separate optimized query layout from bounded foreground mutation.
- Made read freshness an explicit application choice between realtime and eventual modes.

## Related Concepts
- [[PsqlBm25s]] - concrete PostgreSQL BM25 implementation using this maintenance pattern.
- [[BM25]] - ranking data represented in the optimized base and recent delta.
- [[PostgreSQL]] - supplies the transactional, WAL, recovery, and replication environment.
- [[RebuildableDerivedIndex]] - related pattern that treats an index as recoverable derived state rather than the only durable copy.
- [[EventDrivenConsistency]] - related consistency pattern in which asynchronously applied changes create temporary visibility lag.
