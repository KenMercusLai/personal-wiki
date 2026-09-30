---
title: "Traffic Unitization"
type: concept
tags: [distributed-systems, routing, sharding, active-active]
sources:
  - kaito-gao-dong-yi-di-duo-huo-kan-zhe-pian-jiu-gou-le
last_updated: 2026-10-01
knowledge_schema: synthesis-v1
---

## Definition
[[TrafficUnitization]] is the partitioning and routing of related users, business capabilities, or geographic workloads to a designated site so their normal read-write path forms a local operational loop while other sites remain able to assume ownership during failure.

## Current Synthesis
In Kaito's cross-city active-active pattern, unitization prevents the conflict that unrestricted multi-primary writes would create. A routing layer assigns a stable cohort to one site; applications use local storage; an ownership check near storage catches misrouted writes; and asynchronous replication distributes the resulting state to other sites. The method moves conflict prevention to traffic admission instead of asking replication middleware to infer a total order from imperfect clocks after concurrent writes occur.

The partition key has architectural consequences. Business-type partitioning can keep tightly dependent services together but may create uneven load or cross-unit calls. User-hash partitioning can balance stable cohorts but must define how shared records, account changes, and rebalancing work. Geographic partitioning can improve proximity for location-bound services but needs policy for travel, border cases, global actors, and regional capacity. The invariant is more important than the specific key: related operations should have one active owner and a local closure under normal conditions.

Failover complicates that invariant. Moving a unit requires routing convergence, a decision about replication lag and admissible data loss, fencing of the old owner, adequate capacity at the destination, and a safe failback plan. Data that cannot be partitioned or cannot tolerate delayed convergence may need a single writer or a stronger coordination model, so unitization should prioritize core workloads that fit its consistency boundary rather than forcing every service into active-active operation.

## Key Claims
- Stable traffic ownership prevents many cross-site write conflicts before they reach storage.
- A unit should contain related operations and dependencies so normal work completes without synchronous cross-site calls.
- Business capability, user hash, and geography are alternative partition keys with different locality, balance, and ownership tradeoffs.
- Storage-side ownership validation is a safety backstop when routing bugs or user movement violate the intended assignment.
- Unit failover requires routing, fencing, replication-lag, capacity, and failback controls; replication alone is insufficient.
- Strongly consistent global data may remain outside the unitized multi-writer path.

## Evidence
- Routing invariant: [[kaito-gao-dong-yi-di-duo-huo-kan-zhe-pian-jiu-gou-le]] says one user's related requests should complete inside one data center without cross-site access.
- Partition alternatives: [[kaito-gao-dong-yi-di-duo-huo-kan-zhe-pian-jiu-gou-le]] illustrates business-type, user-hash, and geographic routing.
- Dependency locality: [[kaito-gao-dong-yi-di-duo-huo-kan-zhe-pian-jiu-gou-le]] recommends placing mutually dependent services, such as ordering and payment, in the same active unit.
- Defense in depth: [[kaito-gao-dong-yi-di-duo-huo-kan-zhe-pian-jiu-gou-le]] calls for storage-access middleware to verify data ownership if a routing bug lets a user drift between sites.
- Scope boundary: [[kaito-gao-dong-yi-di-duo-huo-kan-zhe-pian-jiu-gou-le]] excludes global configuration and inventory-like strongly consistent data from the proposed dual-active write path.

## Counterevidence & Qualifications
The source offers diagrams and practitioner reasoning but no measured routing accuracy, rebalancing procedure, conflict rate, failover time, capacity model, or production outcome. User-level ownership does not automatically contain records shared by many users, workflows spanning business units, or globally scarce resources. Hash examples based on user ranges simplify real consistent-hashing and migration concerns. Geography can conflict with travel, residency, compliance, or uneven demand. Correct unitization therefore depends on domain boundaries, explicit ownership metadata, fencing, observability, reconciliation, and disaster exercises that the article names only at a high level.

## What Changed
- Created the concept from Kaito's three routing patterns and local read-write closure invariant.

## Related Concepts
- [[MultiSiteHighAvailability]] - unitization is the traffic and ownership layer of the source's cross-city active-active design.
- [[EventDrivenConsistency]] - asynchronous cross-unit state propagation needs durable delivery, idempotency, and repair.
- [[AggregateTransactionBoundary]] - both concepts seek a boundary inside which related state changes remain coherent.
- [[DistributedConsensus]] - stronger agreement may be required for global state that cannot be safely assigned to one unit.
- [[NetworkLoadBalancing]] - load balancing distributes requests, while unitization adds stable domain-aware ownership and locality.
