---
title: "Durable Messaging"
type: concept
tags: [distributed-systems, messaging, reliability]
sources:
  - distributed-architecture-concepts-i-learned-while-building-a-large-payments-system
last_updated: 2026-09-27
knowledge_schema: synthesis-v1
---

## Definition
[[DurableMessaging]] is the persistence and replication of accepted messages so that producer, broker, node, or consumer failure does not silently erase work that the system has committed to process.

## Current Synthesis
The payments case treats a payment-intent message as critical state rather than transient transport. The message must remain available after a processing failure and after a queue node goes offline, which motivates persistent storage and replication across the messaging cluster.

The team chose Kafka with at-least-once delivery rather than claiming exactly-once end-to-end execution. That trade preserves work by allowing redelivery, then relies on [[IdempotentPaymentProcessing]] to stop duplicates from becoming duplicate charges or refunds. Durable transport and correct effects are therefore separate guarantees that must be composed.

## Key Claims
- Acknowledged payment-intent messages must survive processing and broker-node failures.
- Persistence protects queued work across restart; replication can preserve it when one storage copy fails.
- At-least-once delivery favors avoiding silent loss while permitting duplicate delivery.
- Consumer idempotency is required when a redelivered message can trigger a financial effect.
- Broker durability alone does not prove end-to-end losslessness or exactly-once business outcomes.

## Evidence
- Payment requirement: [[distributed-architecture-concepts-i-learned-while-building-a-large-payments-system]] identifies payment-initiation messages as work the system could not afford to lose.
- Delivery choice: [[distributed-architecture-concepts-i-learned-while-building-a-large-payments-system]] reports a Kafka-based lossless cluster configured around durable, at-least-once delivery.
- Visual failure model: [[distributed-architecture-concepts-i-learned-while-building-a-large-payments-system]] retains a diagram in which a message written to two queue nodes remains deliverable after one node fails.

## Counterevidence & Qualifications
The source does not document producer acknowledgements, replication factor, in-sync replica policy, retention, consumer commits, poison messages, ordering, backpressure, disaster recovery, or measured message-loss rates. Its diagram demonstrates an intended single-node failure model, not a proof against correlated failures. The phrase “every message needed to be delivered once” conflicts with the stated at-least-once design and is interpreted as a no-loss business requirement rather than a literal transport guarantee.

## What Changed
- Created the concept while separating durable transport, at-least-once delivery, and exactly-once business effects.

## Related Concepts
- [[IdempotentPaymentProcessing]] - neutralizes the duplicate deliveries permitted by at-least-once messaging.
- [[DataDurability]] - applies the analogous survival requirement to stored transaction state.
- [[DistributedPaymentArchitecture]] - composes messaging durability with consistency and payment invariants.
- [[EventLogAsSystemOfRecord]] - represents the stronger pattern in which a durable event stream becomes canonical state.
