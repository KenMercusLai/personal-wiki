---
title: "Data-Intensive Systems"
type: concept
tags: [databases, distributed-systems, reliability, data-processing]
sources:
  - laisky-reading-notes-on-designing-data-intensive-applications
last_updated: 2026-10-01
knowledge_schema: synthesis-v1
---

## Definition
[[DataIntensiveSystems]] are applications whose central engineering difficulty lies in storing, retrieving, moving, transforming, and coordinating data reliably at the required scale.

## Current Synthesis
The source frames data-system design as a set of coupled choices rather than a search for one universally best database or architecture. Reliability asks which faults the service can tolerate, scalability asks how load and resource needs change, and maintainability asks whether people can understand and evolve the system. Latency distributions, service objectives, failure models, and operational complexity therefore matter alongside average throughput.

Data representation and storage should follow access patterns. Documents improve locality but become awkward for dense many-to-many relationships; relational systems make references and joins explicit; graph systems make variable-depth traversal natural. LSM trees, B-trees, row storage, column storage, materialized views, in-memory engines, and warehouses each optimize different mixes of write rate, read latency, range access, compression, analysis, and update cost.

Distribution adds new tradeoffs rather than merely more capacity. Replication can improve locality, availability, and read throughput while introducing lag and conflict. Partitioning spreads load while creating routing and hotspot problems. Transactions, isolation, linearizability, causal order, consensus, and atomic commit address different correctness boundaries and impose different coordination or availability costs.

Batch and stream processing extend the same reasoning to derived data. Immutable input, deterministic transformation, replay, durable logs, idempotent effects, and explicit ordering make recovery tractable. Streaming additionally requires decisions about backpressure, partition ordering, event time, windows, joins against changing reference data, and what delivery guarantee is actually achieved end to end.

## Key Claims
- Reliability, scalability, and maintainability must be evaluated together and against an explicit workload and failure model.
- Data models and storage engines exchange locality, relationship flexibility, write cost, read cost, compression, and operational complexity.
- Replication and partitioning improve some combinations of availability, locality, and throughput while adding lag, conflict, routing, and coordination costs.
- Transaction isolation, linearizability, causal consistency, consensus, and atomic commit protect different correctness boundaries and should not be treated as synonyms.
- Immutable logs, deterministic transformations, replay, and idempotent effects are reusable recovery mechanisms across databases, batch jobs, and streams.
- End-to-end processing guarantees depend on how storage, messaging, consumer state, ordering, retries, and external side effects compose.

## Evidence
System qualities:
- [[laisky-reading-notes-on-designing-data-intensive-applications]] defines reliability, scalability, and maintainability and recommends latency distributions and service objectives rather than one fixed response-time number.

Models and storage:
- [[laisky-reading-notes-on-designing-data-intensive-applications]] compares relational, document, and graph relationships, then contrasts LSM trees, B-trees, indexes, warehouses, and columnar execution.

Distribution and correctness:
- [[laisky-reading-notes-on-designing-data-intensive-applications]] connects replication, partitioning, transactions, clocks, leases, fencing, linearizability, causal consistency, consensus, and atomic commit.

Derived data:
- [[laisky-reading-notes-on-designing-data-intensive-applications]] describes immutable batch inputs, durable partitioned logs, CDC, backpressure, event-time windows, stream joins, and delivery semantics.

## Counterevidence & Qualifications
The source is one reader's compressed notes on a broad book, not a protocol specification, benchmark, product comparison, or empirical survey. Many statements omit version, workload, configuration, and failure-model detail, and several product examples can age. The listed tradeoffs are a design-question map; they do not determine which architecture is correct without application invariants, measurements, operational capability, and current primary documentation.

## What Changed
- Created an umbrella concept linking the wiki's database, distribution, transaction, and data-processing threads.

## Related Concepts
- [[DatabaseEngineeringTradeoffs]] - narrows the system-wide framework to database behavior and operational choices.
- [[DatabaseTransactionIsolation]] - protects transaction invariants against concurrency anomalies.
- [[DistributedConsensus]] - coordinates ordered state despite partial failure and inconsistent local views.
- [[DataDurability]] - asks whether acknowledged state survives the promised failure scope.
- [[DurableMessaging]] - applies persistence, replication, and replay to in-flight work.
- [[SystemReliability]] - broadens dependability beyond data mechanisms into code, operations, change, and recovery.
