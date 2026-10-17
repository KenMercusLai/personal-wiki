---
title: "Disaggregated Transactional Database"
type: concept
tags: [databases, distributed-systems, storage, compute, transactions]
sources:
  - p4385-pandis
last_updated: 2026-10-18
knowledge_schema: synthesis-v1
---

## Definition
[[DisaggregatedTransactionalDatabase]] separates transactional execution from durable log replication, page materialization, and persistent storage so each layer can scale, fail, and recover independently.

## Current Synthesis
Lakebase demonstrates a four-part form. PostgreSQL computes execute transactions and cache working pages; Safekeepers quorum-replicate WAL and fence writers by term; Pageservers consume committed WAL and reconstruct versioned pages; object storage preserves logs, layers, indexes, and snapshots. Distinct LSN frontiers make the handoffs explicit and bound what is committed, locally recoverable, remotely recoverable, or visible to a reader.

Separation enables disposable compute, read replicas, fast recovery, branching, storage sharding, and analytical engines outside the primary. It also turns the local I/O path into a distributed protocol: performance depends on cache residency, WAL and page-service lag, backpressure, placement, cross-zone redundancy, and the recovery of each layer.

## Key Claims
- WAL durability can be separated from page materialization without weakening the transaction boundary when quorum and LSN invariants are explicit.
- Compute-local caching preserves a fast common read path while shared storage makes compute replaceable.
- Independent page services can shard, compact, reconstruct historical versions, and recover outside PostgreSQL compute.
- Disaggregation enables compute elasticity and failure replacement without copying the complete database first.
- Shared versioned storage can serve multiple execution engines, but format compatibility and snapshot semantics remain required.
- Additional services and network boundaries replace local simplicity with placement, lag, backpressure, and failover coordination.

## Evidence
Durability boundary:
- [[p4385-pandis]] commits WAL after a Safekeeper quorum flush and uses term-based leader election to reject stale writers.

Read boundary:
- [[p4385-pandis]] serves local-cache misses through `GetPage@LSN`, reconstructing a page from image and delta layers while using a not-modified-since LSN to avoid unnecessary waits.

Recovery and availability:
- [[p4385-pandis]] reports warm replacement computes, cross-zone Safekeepers, Pageserver hot standbys, object-store snapshots, and automatic placement repair.

Multi-engine access:
- [[p4385-pandis]] lets Spark write PostgreSQL-compatible pages and Lakehouse//RT read consistent page snapshots outside the primary.

## Counterevidence & Qualifications
Lakebase is one implementation and its evidence is first-party. A quorum-flushed record can precede object-store backup, so the durability argument also depends on Safekeeper redundancy and timely repair. Cache misses, Pageserver lag, remote downloads, compaction, and metadata coordination create latency and recovery tails absent from an all-local model. “Open” PostgreSQL pages are versioned physical structures, not a universal analytical interchange format, and the paper does not fully quantify multi-tenant interference or correlated regional failure.

## What Changed
- Established an explicit four-layer model joining compute, quorum WAL, page services, and object storage.

## Related Concepts
- [[ObjectStorageNativeDatabase]] - supplies the durable remote substrate while disaggregation adds independent log and page services.
- [[DatabaseBranching]] - uses retained versioned pages and logs to fork state cheaply.
- [[PostgreSQLReadScaling]] - read replicas consume shared durability while maintaining their own caches.
- [[DistributedConsensus]] - Safekeeper quorum and terms establish one accepted WAL leader.
- [[SystemReliability]] - failover behavior depends on distinct compute, log, page, and object-store recovery paths.
