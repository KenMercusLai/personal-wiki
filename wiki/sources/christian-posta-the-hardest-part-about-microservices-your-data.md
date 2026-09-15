---
title: "The Hardest Part About Microservices: Your Data"
type: source
tags: [microservices, data, domain-driven-design, distributed-systems]
date: 2026-03-02
source_file: /mnt/ken_personal_wiki/Articles/Christian Posta - The Hardest Part About Microservices Your Data.md
---

## Summary
[[ChristianPosta]] argues that the hard part of [[MicroserviceDataBoundaries]] is not choosing Spring Boot, Docker, REST, or one-database-per-service rules, but identifying domain meanings, transactional boundaries, and consistency mechanisms. The article connects Domain-Driven Design, bounded contexts, aggregates, event-driven communication, CQRS, and event logs into a practical model for splitting data without pretending distributed systems behave like one ACID database. Its diagrams reinforce the progression from context boundaries, to oversized transactions, to smaller aggregate transactions, to data capture feeding a replicated event log.

## Key Claims
- Microservices are primarily about boundaries and autonomy, so data models should follow explicit domain models rather than shared-database convenience.
- Bounded contexts let the same term, such as "book," mean different things in different business contexts without forcing one universal data model.
- Transactional boundaries should be the smallest units needed to protect true business invariants, often around one aggregate rather than a broad object graph.
- Cross-boundary consistency should usually be communicated with immutable events instead of synchronous point-to-point calls or two-phase commit across services.
- The article's inspected diagrams show Search, Booking, Admin, and Ticketing split by domain and transaction boundaries, with anti-corruption boundaries and separate stores where appropriate.
- Persistent event logs can make databases, caches, and indexes materialized views over historical events, improving auditability, replay, testing, and migration.
- Rules such as "every microservice owns one database" are tradeoffs, not laws; a shared database can be acceptable when one team owns the participating processes and autonomy is preserved.

## Key Quotes
> "Context is king." - on why data meaning must be modeled inside explicit business contexts.

> "There are no hard and fast rules, only tradeoffs." - on copying Netflix or applying microservice rules mechanically.

## Connections
- [[ChristianPosta]] - author of the article.
- [[MicroserviceDataBoundaries]] - central problem: splitting data around domain, transaction, and integration boundaries.
- [[BoundedContext]] - DDD boundary used to make domain meanings explicit.
- [[AggregateTransactionBoundary]] - smallest atomic unit for true business invariants.
- [[EventDrivenConsistency]] - cross-boundary consistency model based on immutable events.
- [[EventLogAsSystemOfRecord]] - "turn the database inside out" view of event logs and materialized views.
- [[AntiCorruptionLayer]] - the first inspected diagram shows an anti-corruption boundary between Search and the rest of the system.
- [[ApacheKafka]] - named as a persistent replicated log option for streaming database changes.
- [[Debezium]] - named as a database-change capture tool that can feed event streams.
- [[ApacheCamel]] - named as an integration and transformation tool for ticketing-system interaction.
- [[ApacheSamza]] - named through Martin Kleppmann's "turning the database inside out" reference.
- [[MicroserviceOperationalOverhead]] - related caution: service boundaries carry operational cost beyond data-model purity.
- [[DistributedSystemRestraint]] - related caution: distributed design must match organizational and operational readiness.

## Contradictions
- No direct contradictions found. The source qualifies both pro-microservice and anti-microservice material in the wiki: it accepts service autonomy as valuable, but says the decisive work is domain modeling, transactional boundaries, and consistency design rather than service count or tool choice.
