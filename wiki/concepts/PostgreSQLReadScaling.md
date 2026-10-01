---
title: "PostgreSQL Read Scaling"
type: concept
tags: [postgresql, databases, replication, scaling]
sources:
  - openai-scaling-postgresql-to-power-800-million-chatgpt-users
last_updated: 2026-10-01
knowledge_schema: synthesis-v1
---

## Definition
[[PostgreSQLReadScaling]] is the use of replicas, routing, locality, workload separation, and capacity controls to grow a PostgreSQL system whose demand is dominated by reads while retaining a single write primary.

## Current Synthesis
OpenAI's case shows that a single writer can coexist with very large read throughput when read traffic is aggressively removed from the primary. Nearly 50 replicas distribute reads across regions, PgBouncer is co-located with clients and replicas, multiple replicas per region keep failure headroom, and the primary uses a synchronized hot standby for failover.

The pattern has a hard workload boundary. All writes and transaction-coupled reads still converge on one primary, while MVCC makes heavy updates create row-version, scan, index, bloat, and vacuum costs. OpenAI therefore treats replication as read scaling rather than general database scaling: shardable write-heavy workloads move to a sharded store, unnecessary and bursty writes are suppressed, and new tables are not admitted to the legacy deployment.

Replica fan-out is itself finite. Direct WAL shipping from the primary to every replica consumes CPU and network capacity and can destabilize lag. Cascading replication moves that fan-out to intermediate replicas, potentially raising the ceiling, but it also makes failover topology more complex and remained under test in the source.

## Key Claims
- Read replicas can extend a single-primary PostgreSQL system when the workload is predominantly read-heavy.
- Regional co-location reduces client latency and connection occupancy, while per-region redundancy absorbs individual replica loss.
- A hot standby shortens primary recovery, and replica-served reads can preserve partial service when writes fail.
- Read replication does not remove the single-writer bottleneck or PostgreSQL MVCC costs under heavy updates.
- Direct WAL fan-out eventually pressures the primary; cascading replication exchanges that pressure for topology and failover complexity.
- Sustainable scaling depends on moving unsuitable workloads away rather than treating replicas as a cure for every access pattern.

## Evidence
- Production scale: [[openai-scaling-postgresql-to-power-800-million-chatgpt-users]] reports millions of QPS, nearly 50 regional replicas, near-zero lag, low double-digit millisecond p99 client latency, and five-nines availability.
- Writer protection: [[openai-scaling-postgresql-to-power-800-million-chatgpt-users]] describes offloading reads, optimizing transaction-coupled reads, suppressing unnecessary writes, and rate-limiting backfills.
- Failure behavior: [[openai-scaling-postgresql-to-power-800-million-chatgpt-users]] uses an HA hot standby for the primary and multiple replicas with regional headroom.
- Workload boundary: [[openai-scaling-postgresql-to-power-800-million-chatgpt-users]] moves shardable write-heavy workloads to sharded systems and disallows new tables in the current PostgreSQL deployment.
- Replication ceiling: [[openai-scaling-postgresql-to-power-800-million-chatgpt-users]] identifies direct WAL fan-out as a scaling limit and cascading replication as a still-unproven next step.

## Counterevidence & Qualifications
This is one first-party production account rather than a reproducible benchmark. It does not disclose query mix, dataset size, instance types, cost, consistency requirements, replica-routing details, lag distributions, or failover measurements. The reported outcome therefore supports a workload-qualified pattern, not a universal claim that one PostgreSQL primary can serve any system of similar user count. Cascading replication is prospective in the source, and preserving replica reads during primary failure still leaves writes and transaction-dependent requests unavailable.

## What Changed
- Created the concept to distinguish read-replica scale from write scalability.
- Added regional locality, failure headroom, and partial read-only continuity as parts of the pattern.
- Added direct versus cascading WAL fan-out as a capacity-versus-operational-complexity tradeoff.

## Related Concepts
- [[DatabaseEngineeringTradeoffs]] - workload mix determines whether replication extends the architecture or hides an approaching write limit.
- [[SystemReliability]] - hot standby, regional redundancy, headroom, and partial degradation shape failure behavior.
- [[DatabaseOverloadProtection]] - replicas remain viable only when sudden load and pathological work are bounded.
- [[DynamicContentCaching]] - successful cache hits remove read demand before it reaches replicas.
- [[ReplicatedLog]] - PostgreSQL WAL carries ordered changes from the primary toward replicas.
