---
title: "Distributed SQLite"
type: concept
tags: [sqlite, distributed-databases, replication, consistency]
sources:
  - twelve-years-distributed-sqlite
last_updated: 2026-10-25
knowledge_schema: synthesis-v1
---

## Definition
[[DistributedSQLite]] is the family of architectures that add replication, recovery, multi-node availability, or multi-writer convergence around or within [[SQLite]].

## Current Synthesis
Distributed SQLite is not a single protocol. The source identifies three broad approaches that optimize for different failure and coordination requirements. Consensus systems such as [[Rqlite]] and dqlite order writes through a leader and majority so a cluster can continue without waiting to restore a failed node. Streaming systems such as Litestream retain one writer and copy WAL changes to object storage for inexpensive disaster recovery. Merge-based systems such as cr-sqlite use CRDTs so multiple writers can diverge and later converge without a leader.

Packaging forms a second axis. A system may be a self-operated server, an embedded library, a filesystem or platform feature, a database-engine fork, or a managed edge service. Moving from an embedded file to any of these forms can answer SQLite's single-machine availability limits, but it also adds protocol, routing, restore, conflict, platform, or vendor dependencies. Architecture choice should therefore begin with the required recovery delay, consistency, write topology, and operating model.

## Key Claims
- Consensus, WAL streaming, and merge-based replication solve materially different problems.
- Consensus systems trade minority-partition write availability for one strongly ordered replicated history.
- WAL streaming can preserve SQLite's single-writer simplicity while reducing disaster-recovery cost, but recovery is not continuous cluster availability.
- CRDT-based replication permits divergent writers and later convergence, fitting local-first use cases but weakening immediate consistency.
- Server, embedded-library, filesystem, engine-fork, and managed-platform packaging create distinct operational and ownership boundaries.
- Commercial value in the recounted history concentrated in managed platforms even though the underlying category developed in open source.

## Evidence
- Consensus corner: [[twelve-years-distributed-sqlite]] describes rqlite's leader and majority protocol, dqlite's embedded form, and SQLite Cloud's Raft-based service.
- Streaming corner: [[twelve-years-distributed-sqlite]] says Litestream copies WAL changes to S3 for recovery without maintaining a consensus cluster.
- Merge corner: [[twelve-years-distributed-sqlite]] says cr-sqlite adds CRDTs so writers can diverge and merge without a leader.
- Packaging diversity: [[twelve-years-distributed-sqlite]] contrasts servers, libraries, filesystem replication, forks, and managed edge databases.
- Category history: [[twelve-years-distributed-sqlite]] traces projects from rqlite, Bedrock, and ActorDB through dqlite, Litestream, LiteFS, cr-sqlite, libSQL, SQLite Cloud, D1, and Durable Objects.
- Commercialization: [[twelve-years-distributed-sqlite]] argues that venture funding and acquisitions followed platform services more than free self-operated projects.

## Counterevidence & Qualifications
The three-corner model is the author's synthesis, not an exhaustive taxonomy: hybrid systems can combine log shipping, consensus, read replicas, leases, engine changes, and platform-specific recovery. The source offers no comparative benchmarks, failure tests, formal consistency analysis, adoption counts, cost model, or independent verification of chronology and priority. “Distributed SQLite” can also obscure whether SQLite itself remains unmodified, is forked, or merely supplies a storage layer inside a larger system.

## What Changed
- Created a requirements-centered taxonomy of consensus, streaming, and merge-based SQLite replication.
- Separated replication mechanism from packaging and commercial operating model.

## Related Concepts
- [[SQLite]] - embedded database engine around which the category is built.
- [[SQLiteProductionTradeoffs]] - single-node constraints create demand for distributed extensions, whose machinery changes the simplicity tradeoff.
- [[DistributedConsensus]] - provides ordered majority agreement for the consensus corner.
- [[ReplicatedLog]] - records one ordered write history for consensus replicas.
- [[LocalFirstSoftware]] - motivates offline and divergent-writer convergence in the merge corner.
- [[CloudHighAvailability]] - availability and recovery requirements determine whether replication is needed.
