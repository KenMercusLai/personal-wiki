---
title: "Replicated Log"
type: concept
tags: [distributed-systems, consensus, replication, state-machines]
sources:
  - unmesh-joshi-replicated-log
  - ren-yi-gui-mo-de-git
last_updated: 2026-10-09
knowledge_schema: synthesis-v1
---

## Definition
[[ReplicatedLog]] is a durable ordered sequence of state changes used to make replicas reconstruct or apply one coherent history, commonly through agreement among nodes or through one authoritative log shared by derived replicas.

## Current Synthesis
Consensus on isolated requests does not by itself keep replicas synchronized because non-commutative requests can produce different final states when applied in different orders. The replicated-log pattern makes order part of the agreement: every node maintains the same write-ahead log, each entry carries the request and consensus state needed for coordination, and replicas execute committed entries sequentially.

The log therefore connects agreement to deterministic state evolution. It turns a sequence of separately proposed changes into one cluster-wide history, allowing nodes that crash or become disconnected to preserve a common ordering boundary when they participate in the replicated state.

Continuity adds a different authority model. Instead of making every local Git repository a voting member of one replicated log, it stores push records and an index in S3-compatible object storage, serializes index changes through atomic compare-and-swap, and treats local repositories as caches that can replay or follow the log. UDP gossip accelerates delivery but is not required for correctness because a read checks the authoritative index and catches up first when necessary. This is log-backed replication, but the source does not establish that Continuity implements a classical consensus-replicated log.

## Key Claims
- Replicas must agree on request order as well as on the requests themselves.
- Each node maintains a write-ahead log containing user requests and consensus-related state.
- Consensus is constructed over log entries so replicas converge on one ordered history.
- Sequential execution of the common log makes every replica apply the same operations in the same order.
- The pattern is intended to preserve shared state despite node crashes and disconnections.
- A durable authoritative log can also support replaceable replicas that verify and replay history instead of participating in consensus for every entry.
- Log compaction must preserve reconstructibility while bounding replay and lookup costs.

## Evidence
- Ordering requirement: [[unmesh-joshi-replicated-log]] explains that replicas can reach different final states if they execute individually agreed requests in different orders.
- Log structure: [[unmesh-joshi-replicated-log]] says every node maintains a write-ahead log whose entries store both a user request and the state needed for consensus.
- State convergence: [[unmesh-joshi-replicated-log]] connects agreement over the complete log with sequential execution and identical replica state.
- Authoritative-log variant: [[ren-yi-gui-mo-de-git]] describes push records and a CAS-updated index in object storage as the source from which local Git repositories catch up or rebuild.
- Correctness boundary: [[ren-yi-gui-mo-de-git]] says gossip may be lost because replicas validate their WAL index ETag against S3 before serving reads.
- Compaction: [[ren-yi-gui-mo-de-git]] describes propagating primary-produced Git repacks through the WAL so followers can apply the same maintenance result.

## Counterevidence & Qualifications
The Unmesh Joshi source is a concise pattern description, not a complete replication protocol. It does not specify how log positions are proposed or committed, how leaders or quorums operate, whether execution must be deterministic, how lagging or newly joined replicas catch up, how snapshots and log compaction work, or what consistency and liveness guarantees hold. [[Paxos]] is related consensus material in the wiki, but that source does not require or describe a particular consensus algorithm for implementing the log. Cursor's Continuity account is first-party and likewise omits a formal protocol or proof; its “no consensus” claim relocates ordering into object-store CAS and therefore depends on external storage semantics rather than eliminating coordination assumptions.

## What Changed
- Added the distinction between a consensus-replicated log and derived replicas following one externally authoritative log.
- Added read-time freshness validation, cache reconstruction, and compaction propagation from the Continuity case.

## Related Concepts
- [[DistributedConsensus]] - a replicated log applies consensus to successive ordered log positions.
- [[Paxos]] - a related protocol family for safely choosing values, without being prescribed by this source as the log implementation.
- [[SystemReliability]] - replicated ordering aims to preserve consistent state across crashes and disconnections.
- [[DistributedProgramming]] - replicated logs address ordering and shared-state coordination across independent nodes.
- [[Continuity]] - uses an object-store WAL as durable authority for rebuildable local Git repositories.
- [[GitHostingArchitecture]] - applies ordered logs to Git push durability, visibility, replica catch-up, and repacking.
