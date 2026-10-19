---
title: "Database Partitioning"
type: concept
tags: [database, partitioning, distributed-systems, scalability]
sources:
  - rethink-greptimedb-partition
last_updated: 2026-10-19
knowledge_schema: synthesis-v1
---

## Definition
[[DatabasePartitioning]] divides a logical dataset into smaller ownership or execution units so storage, retention, routing, and compute load can be placed and managed separately.

## Current Synthesis
Partitioning is not one scaling mechanism. A time boundary can make history effectively unbounded and TTL deletion cheap, yet active time-series writes and reads remain concentrated in the newest slices. Horizontal throughput requires another dimension—such as primary-key ranges—that can distribute simultaneously active data and its associated work.

The partition unit must also match the resource being controlled. GreptimeDB's Region combined data ownership with read and write routing, mutable state, file catalogs, caches, metadata, compaction, schema alteration, and lifecycle transitions. That initially simplified implementation but coupled unrelated bottlenecks and turned repartitioning from a mapping change into a multi-stage operational procedure.

An object store as durable source of truth removes some physical movement from ownership changes, but it does not remove coordination. Metadata, flushing, file reassignment, online-write continuity, cache warming, rollback, historical recompaction, and paused-task recovery still make repartitioning expensive. Moving stateless write preparation to elastic Frontend nodes narrows Regions toward file registration and query-serving ownership, while introducing write-latency, visibility, failure, and cold-cache tradeoffs.

The resulting direction is query-led and finer-grained: independent multidimensional key ranges can be inferred from predicates and observed data bounds, while immutable files may eventually be sufficient physical scheduling units. The fully automatic endpoint remains aspirational because the proposal lacks a complete feedback loop and lightweight state transitions.

## Key Claims
- Time partitioning primarily addresses retained history and lifecycle deletion; it does not necessarily distribute a time-series system's active load.
- A useful horizontal partition separates concurrently active primary-key ranges and the compute load associated with them.
- Combining routing, ownership, mutable state, files, caches, metadata, and maintenance in one partition creates coupled bottlenecks and costly repartitioning.
- Shared object storage can avoid physical file movement during ownership changes, but metadata, state, cache, recovery, and background work remain real coordination costs.
- Stateless write preparation can scale independently from partition ownership, allowing partition policy to focus more directly on query placement.
- Multidimensional ranges preserve independent pruning across key columns and can support workload-derived hotspot detection without one fixed lexicographic priority.

## Evidence
Purpose and load separation:
- [[rethink-greptimedb-partition]] contrasts Prometheus-style time Blocks with timestamp-plus-key partitioning and explains why only the latter distributes currently active load.

Abstraction weight and repartitioning:
- [[rethink-greptimedb-partition]] enumerates Region responsibilities and depicts a state machine spanning worker lifecycle, role changes, staging, editing, truncation, dropping, and recovery; it also reports five metadata groups plus flushing, file reassignment, rollback, online writes, and later recompaction during repartitioning.

Write-path separation:
- [[rethink-greptimedb-partition]] describes Frontend-side validation, encoding, file construction, and object-store upload followed by Region-side file registration, together with its latency and cache implications.

Query-led multidimensional placement:
- [[rethink-greptimedb-partition]] shows independent ranges over two columns and proposes deriving hotspots from filter predicates and observed min/max values.

## Counterevidence & Qualifications
The evidence is one GreptimeDB-affiliated practitioner's retrospective rather than a controlled comparison of partitioning strategies. No measurements establish repartitioning cost, batch-write improvement, added latency, cache hit effects, hotspot-detection accuracy, stability of automatic rule changes, or superiority to consistent hashing or one-dimensional ranges. Independent multidimensional ranges may also produce long rule lists and overlapping operational concerns that the article does not quantify. The file-as-partition model is explicitly personal speculation outside the GreptimeDB roadmap, and the described no-intervention partitioner lacks a complete query-load feedback loop.

## What Changed
- Distinguished capacity and TTL partitioning from partitioning that distributes active compute load.
- Made abstraction weight and repartitioning cost part of partition-design evaluation.
- Added query-led multidimensional ranges and file-granularity scheduling as qualified design directions.

## Related Concepts
- [[TimeSeriesDatabase]] - concentrated recent activity makes time-only partitioning insufficient for horizontal throughput.
- [[ObjectStorageNativeDatabase]] - shared durable objects reduce data-movement needs while retaining metadata and cache coordination.
- [[DatabaseEngineeringTradeoffs]] - partition granularity couples latency, locality, operability, and failure behavior.
- [[StorageArchitectureEvolvability]] - stable separation of foreground ownership from background work determines how cheaply partition policy can change.
- [[DatabaseOverloadProtection]] - partition and placement choices affect hotspot isolation and how overload propagates.
