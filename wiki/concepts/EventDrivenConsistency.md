---
title: "Event-Driven Consistency"
type: concept
tags: [distributed-systems, microservices, events, consistency]
sources:
  - christian-posta-the-hardest-part-about-microservices-your-data
  - kikcat-dian-shang-xi-tong-de-gao-bing-fa-ku-cun-kou-jian
last_updated: 2026-09-23
knowledge_schema: synthesis-v1
---

## Definition
[[EventDrivenConsistency]] is a distributed consistency strategy where services record durable state-change events around local transactions and other bounded contexts consume those events to update projections or authoritative state over time.

## Current Synthesis
Posta presents event-driven consistency as the practical answer to reconciling small transactional boundaries across unreliable networks. Instead of using REST, RPC, or two-phase commit to reproduce one-database assumptions across services, each bounded context commits what it knows locally and communicates immutable facts. Aggregates can emit domain events directly, a dedicated event store can be both database and pub-sub topic, or change data capture can move ACID database changes into a replicated log.

Kikcat's inventory design makes the operational obligations concrete. Redis accepts the latency-critical stock deduction, each `order_item` becomes a stock-change event, and a consumer applies the deduction to the goods database; replenishment writes the durable goods change and a stock event that refreshes Redis. This decouples order responsiveness from database write latency and avoids one cross-service atomic commit, but it does not make consistency automatic.

The inventory case adds the missing recovery boundary: consumers must be idempotent, unsynchronized items and events must remain discoverable, stale snapshots must reject new writes, and a coordinator must drain pending changes before rebuilding Redis and restoring service. If the order fails after Redis deduction and even the local failure ledger is lost, periodic reconciliation is still required. Event-driven consistency is therefore a protocol of durable evidence, replay, freshness, and repair rather than merely publishing messages.

## Key Claims
- Cross-boundary consistency should not usually depend on distributed transactions or synchronous point-to-point calls.
- Immutable events communicate facts across bounded contexts while preserving service autonomy.
- Event consumers need idempotency, retryable evidence, and their own decision logic because they observe other systems with delay.
- Event-driven consistency enables services to choose local storage and schema evolution independently.
- A low-latency projection must fail closed when its event position or freshness is not trustworthy.
- Recovery requires draining or replaying pending events before a derived snapshot is declared ready.
- Event-driven approaches improve flexibility but move atomicity work into durability, ordering, reconciliation, observability, and operations.

## Evidence
- Boundary and implementation choices: [[christian-posta-the-hardest-part-about-microservices-your-data]] recommends events across bounded contexts and names aggregate events, event stores, Kafka, Debezium, and change data capture as implementation paths.
- Cross-service examples: [[christian-posta-the-hardest-part-about-microservices-your-data]] uses Booking and Ticketing, while [[kikcat-dian-shang-xi-tong-de-gao-bing-fa-ku-cun-kou-jian]] turns order items and replenishments into stock events spanning Redis, order storage, and the goods database.
- Idempotency and projection freshness: [[kikcat-dian-shang-xi-tong-de-gao-bing-fa-ku-cun-kou-jian]] calls for Lua-backed idempotent consumption and rejects inventory writes while the Redis snapshot is stale.
- Recovery and reconciliation: [[kikcat-dian-shang-xi-tong-de-gao-bing-fa-ku-cun-kou-jian]] drains unsynced order items and stock events before rebuilding Redis and uses local-ledger or periodic reconciliation for failed order creation.
- Architectural tradeoff: [[christian-posta-the-hardest-part-about-microservices-your-data]] lists scalability, flexibility, and independent schemas alongside debugging and operational costs; [[kikcat-dian-shang-xi-tong-de-gao-bing-fa-ku-cun-kou-jian]] adds deliberate unavailability and residual over- or underselling risk.

## Counterevidence & Qualifications
Neither source presents events as a free replacement for transactions. Posta explicitly names the debugging and operational burden; Kikcat shows that event sourcing does not by itself prevent overselling or underselling when Redis fails, a process pauses, a failure record is lost, or reconciliation has not completed. Claims of “guaranteed consistency” must therefore be read as conditional on durable capture, idempotent application, correct fencing, replay, and repair.

## What Changed
- Added a concrete inventory state-machine example spanning synchronous Redis decisions and asynchronous durable application.
- Made stale-projection rejection, coordinator recovery, and reconciliation explicit parts of the consistency model.
- Narrowed any guarantee claim to the full durability, idempotency, fencing, and repair protocol.

## Related Concepts
- [[MessagePassing]] - event-driven consistency is a domain-event form of message-based coordination.
- [[AggregateTransactionBoundary]] - local aggregate transactions produce events that other contexts consume.
- [[EventLogAsSystemOfRecord]] - persistent logs extend event-driven consistency into replayable state derivation.
- [[TaskQueueDesign]] - delivery, ordering, retry, and idempotency concerns overlap with queue design.
- [[DistributedProgramming]] - event propagation is a distributed-programming communication pattern.
- [[SystemReliability]] - event-based systems require operational visibility and failure handling.
- [[HighConcurrencyInventoryDeduction]] - demonstrates event-driven consistency under a latency-sensitive inventory invariant.
- [[TwoPhaseCommit]] - provides stronger atomic coordination when delayed reconciliation is unacceptable.
