---
title: "Replicated Log"
type: concept
tags: [distributed-systems, consensus, replication, state-machines]
sources:
  - unmesh-joshi-replicated-log
last_updated: 2026-09-23
knowledge_schema: synthesis-v1
---

## Definition
[[ReplicatedLog]] is a shared, ordered sequence of state-change requests on which multiple cluster nodes reach agreement before executing those requests in the same order.

## Current Synthesis
Consensus on isolated requests does not by itself keep replicas synchronized because non-commutative requests can produce different final states when applied in different orders. The replicated-log pattern makes order part of the agreement: every node maintains the same write-ahead log, each entry carries the request and consensus state needed for coordination, and replicas execute committed entries sequentially.

The log therefore connects agreement to deterministic state evolution. It turns a sequence of separately proposed changes into one cluster-wide history, allowing nodes that crash or become disconnected to preserve a common ordering boundary when they participate in the replicated state.

## Key Claims
- Replicas must agree on request order as well as on the requests themselves.
- Each node maintains a write-ahead log containing user requests and consensus-related state.
- Consensus is constructed over log entries so replicas converge on one ordered history.
- Sequential execution of the common log makes every replica apply the same operations in the same order.
- The pattern is intended to preserve shared state despite node crashes and disconnections.

## Evidence
- Ordering requirement: [[unmesh-joshi-replicated-log]] explains that replicas can reach different final states if they execute individually agreed requests in different orders.
- Log structure: [[unmesh-joshi-replicated-log]] says every node maintains a write-ahead log whose entries store both a user request and the state needed for consensus.
- State convergence: [[unmesh-joshi-replicated-log]] connects agreement over the complete log with sequential execution and identical replica state.

## Counterevidence & Qualifications
The source is a concise pattern description, not a complete replication protocol. It does not specify how log positions are proposed or committed, how leaders or quorums operate, whether execution must be deterministic, how lagging or newly joined replicas catch up, how snapshots and log compaction work, or what consistency and liveness guarantees hold. [[Paxos]] is related consensus material in the wiki, but this source does not require or describe a particular consensus algorithm for implementing the log.

## What Changed
- Created the concept to distinguish agreement on requests from agreement on their execution order.
- Added the common write-ahead log as the mechanism connecting consensus to replicated state convergence.

## Related Concepts
- [[DistributedConsensus]] - a replicated log applies consensus to successive ordered log positions.
- [[Paxos]] - a related protocol family for safely choosing values, without being prescribed by this source as the log implementation.
- [[SystemReliability]] - replicated ordering aims to preserve consistent state across crashes and disconnections.
- [[DistributedProgramming]] - replicated logs address ordering and shared-state coordination across independent nodes.
