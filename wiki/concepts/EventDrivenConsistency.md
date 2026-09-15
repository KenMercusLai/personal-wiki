---
title: "Event-Driven Consistency"
type: concept
tags: [distributed-systems, microservices, events, consistency]
sources:
  - christian-posta-the-hardest-part-about-microservices-your-data
last_updated: 2026-09-15
knowledge_schema: synthesis-v1
---

## Definition
[[EventDrivenConsistency]] is a distributed consistency strategy where services publish immutable domain events after local transactions and other bounded contexts consume those events to update their own state over time.

## Current Synthesis
Posta presents event-driven consistency as the practical answer to reconciling small transactional boundaries across unreliable networks. Instead of treating REST, SOAP, RPC frameworks, or two-phase commit as ways to preserve single-database thinking across services, the article accepts that distributed systems cannot promise timely knowledge everywhere. Services publish facts about what happened, and peers decide how to store, derive, or act on those facts.

The article gives several implementation paths. Aggregates can emit domain events directly; a dedicated event store can act as both database and pub-sub topic; or an ordinary ACID database can be paired with change data capture into a replicated log such as Kafka through Debezium. The core principle is stable across implementations: immutable events communicate consistency across boundaries without forcing every service into the same transaction.

## Key Claims
- Cross-boundary consistency should not usually depend on distributed transactions or synchronous point-to-point calls.
- Immutable events communicate facts across bounded contexts while preserving service autonomy.
- Event consumers need idempotency and their own decision logic because they observe other systems with delay.
- Event-driven consistency enables services to choose local storage and schema evolution independently.
- CQRS becomes more natural after write and read concerns are separated by events.
- Event-driven approaches improve flexibility but increase debugging, operations, and CAP-related design burden.

## Evidence
- Distributed-system limit: [[christian-posta-the-hardest-part-about-microservices-your-data]] cites unreliable asynchronous networks and warns against hiding the network behind frameworks.
- Event recommendation: [[christian-posta-the-hardest-part-about-microservices-your-data]] says boundaries should use events to communicate consistency.
- Booking-to-ticketing example: [[christian-posta-the-hardest-part-about-microservices-your-data]] says Booking can publish `NewBookingCreated` and Ticketing can consume it.
- Implementation options: [[christian-posta-the-hardest-part-about-microservices-your-data]] names domain events, event stores, Kafka, and Debezium as possible ways to publish changes.
- Diagram evidence: [[christian-posta-the-hardest-part-about-microservices-your-data]] shows data capture and event handlers around Admin, Orders/Booking, and Search services feeding a distributed replicated event log.
- Tradeoff list: [[christian-posta-the-hardest-part-about-microservices-your-data]] lists scalability, flexibility, and independent schemas as advantages, while naming debugging and operational difficulty as disadvantages.

## Counterevidence & Qualifications
The source explicitly says this model is more complicated and harder to debug and operate. It does not present events as a free replacement for transactions; events move consistency work into modeling, idempotency, ordering, observability, and operations.

## What Changed
- Created the concept from Posta's event-based cross-boundary consistency model.

## Related Concepts
- [[MessagePassing]] - event-driven consistency is a domain-event form of message-based coordination.
- [[AggregateTransactionBoundary]] - local aggregate transactions produce events that other contexts consume.
- [[EventLogAsSystemOfRecord]] - persistent logs extend event-driven consistency into replayable state derivation.
- [[TaskQueueDesign]] - delivery, ordering, retry, and idempotency concerns overlap with queue design.
- [[DistributedProgramming]] - event propagation is a distributed-programming communication pattern.
- [[SystemReliability]] - event-based systems require operational visibility and failure handling.
