---
title: "Data Durability"
type: concept
tags: [distributed-systems, databases, reliability]
sources:
  - distributed-architecture-concepts-i-learned-while-building-a-large-payments-system
last_updated: 2026-09-27
knowledge_schema: synthesis-v1
---

## Definition
[[DataDurability]] is the guarantee that data acknowledged as successfully stored remains recoverable across subsequent crashes, node loss, or storage corruption within an explicitly defined failure model.

## Current Synthesis
For payments, durability protects the historical fact that a transaction completed. The source moves the requirement from a single machine to the cluster: replicating records across nodes allows a surviving copy to serve or restore data after one node fails.

Durability must still be stated precisely. Replication helps only when acknowledgements, replica placement, failure independence, repair, backup, and recovery procedures match the promised failure scope. It is distinct from availability, which asks whether the system can respond now, and from consistency, which asks what state concurrent readers and writers observe.

## Key Claims
- Successfully acknowledged payment records should remain recoverable after component failure.
- Cluster-level durability requires more than the survival of one machine's local storage.
- Replication can preserve a record when one node loses its copy.
- Durability, availability, and consistency protect different system properties.
- A durability claim is meaningful only with an explicit failure and acknowledgement model.

## Evidence
- Payment invariant: [[distributed-architecture-concepts-i-learned-while-building-a-large-payments-system]] says completed transactions could not be lost and therefore required cluster-level durability.
- Replication mechanism: [[distributed-architecture-concepts-i-learned-while-building-a-large-payments-system]] names replication as the usual way to keep data available after node failure.
- Visual failure model: [[distributed-architecture-concepts-i-learned-while-building-a-large-payments-system]] retains a three-step diagram in which one of two record copies survives a storage-node failure and returns the data.

## Counterevidence & Qualifications
The source does not specify write acknowledgement thresholds, replica geography, correlated failures, repair windows, backup and restore, accidental deletion, ransomware, or empirical durability rates. Its examples of Cassandra, MongoDB, HDFS, and DynamoDB show configurable options, not equivalent guarantees. The retained diagram illustrates one-node survival but cannot establish complete cluster-level durability.

## What Changed
- Created the concept from the payment system's no-loss requirement and replicated single-node failure model.

## Related Concepts
- [[DurableMessaging]] - applies persistence and replication to in-flight work rather than database records.
- [[IdempotentPaymentProcessing]] - depends on retained operation state to recognize retries after failures.
- [[DistributedPaymentArchitecture]] - combines durable state with selective consistency and delivery guarantees.
- [[CloudHighAvailability]] - focuses on continued service through infrastructure failure rather than preservation alone.
