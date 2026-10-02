---
title: "Microservice Data Boundaries"
type: concept
tags: [microservices, data, software-architecture, domain-driven-design]
sources:
  - christian-posta-the-hardest-part-about-microservices-your-data
  - real-world-engineering-challenges-8-breaking-up-a-monolith
  - sean-kelly-microservices-please-dont
last_updated: 2026-10-02
knowledge_schema: synthesis-v1
---

## Definition
[[MicroserviceDataBoundaries]] are the domain, ownership, transaction, and integration boundaries that determine how data is modeled, stored, changed, and reconciled across microservices.

## Current Synthesis
Posta frames data boundaries as the hardest part of microservices because they force teams to give up the safety and convenience of one shared ACID database without replacing it with simplistic rules. The article's claim is not merely "one database per service." It says services need explicit domain meanings, small transactional boundaries, and communication mechanisms that accept distributed-system limits.

The inspected diagrams make the progression concrete. One diagram separates Admin, Orders/Booking, and Search behind REST APIs with MySQL or Elasticsearch stores and an anti-corruption boundary near Search. Later diagrams show why putting Flight, Customers, Planes, and Booking into one transaction boundary is too broad, and how Booking, SeatAvailability, and Flights can become independent transactional units. The final architecture sketch uses data capture and event handlers feeding a distributed replicated event log, turning cross-service consistency into event processing rather than shared writes.

Khan Academy supplies a production ownership rule during gradual decomposition: exactly one service could write each piece of data, and every other service had to call that owner. This did not eliminate cross-service workflows or shared infrastructure, but it made responsibility for state change traceable while fields moved incrementally out of the monolith.

Kelly adds a readiness gate before those boundaries become remote. A team should understand its domain dependencies and trace each request's reads, writes, ordering constraints, failure points, and recovery paths before turning a local workflow into a distributed transaction. Internal modules can expose uncertain boundaries for learning without immediately committing the system to remote coordination.

## Key Claims
- Microservice boundaries should follow explicit domain models rather than physical database convenience.
- Data splitting removes single-database conveniences, so teams must deliberately replace ACID assumptions with boundary-aware consistency design.
- Terms such as Customer, Account, Booking, or Book can have different valid meanings in different contexts.
- Transactional boundaries should be smaller than broad object graphs when business invariants do not require one atomic update.
- Cross-boundary workflows require explicit call ordering, partial-failure, compensation, and recovery design.
- One-database-per-service is a heuristic, not an absolute rule.
- Single-writer ownership can clarify change provenance during incremental service extraction even when reads and workflows still cross boundaries.

## Evidence
- Domain-first data: [[christian-posta-the-hardest-part-about-microservices-your-data]] says the data model should be driven by the domain model rather than the other way around.
- Context ambiguity: [[christian-posta-the-hardest-part-about-microservices-your-data]] uses the "book" example to show that data meaning depends on who is asking and in what context.
- Diagram evidence: [[christian-posta-the-hardest-part-about-microservices-your-data]] shows Admin, Orders/Booking, and Search as separate service areas with distinct stores and an anti-corruption boundary.
- Oversized transaction warning: [[christian-posta-the-hardest-part-about-microservices-your-data]] argues that a Flight aggregate containing customers, planes, bookings, and schedules creates unnecessary transaction conflicts.
- Boundary tradeoff: [[christian-posta-the-hardest-part-about-microservices-your-data]] says shared databases can be acceptable when the same team owns the processes and autonomy is not undermined.
- Production ownership rule: [[real-world-engineering-challenges-8-breaking-up-a-monolith]] says Khan Academy allowed only one service to write a given piece of data and required other services to call its API.
- Residual coupling: [[real-world-engineering-challenges-8-breaking-up-a-monolith]] reports that shared Redis use, cache expiry, and cross-service data flows still required system-level management.
- Readiness gate: [[sean-kelly-microservices-please-dont]] says teams should understand domain boundaries and request workflows before distributing them.
- Recovery obligation: [[sean-kelly-microservices-please-dont]] identifies ordering, parallelism, application errors, network errors, and partial writes as transaction-specific design problems.

## Counterevidence & Qualifications
The sources do not claim every system should become microservices or event-sourced. Posta explicitly warns against copying Netflix-style visible outcomes without the process and says enterprises must balance domain complexity, scale, and organizational change. His diagrams are conceptual rather than a production reference architecture. Khan Academy's rule comes from one large migration and does not specify database topology, transaction protocol, availability behavior, or how ownership disputes were resolved; one logical writer can still depend on shared physical infrastructure. Kelly's discussion names distributed-transaction questions but supplies no protocol, measured implementation, or proof that internal modules will reveal every eventual network boundary.

## What Changed
- Added domain and request-path comprehension as a gate before local boundaries become distributed transactions.
- Made partial failure, call ordering, compensation, and recovery explicit parts of boundary design.

## Related Concepts
- [[BoundedContext]] - domain boundaries are the article's starting point for data ownership.
- [[AggregateTransactionBoundary]] - transactional boundaries refine data ownership into atomic business-invariant units.
- [[EventDrivenConsistency]] - event propagation reconciles state across boundaries.
- [[EventLogAsSystemOfRecord]] - persistent logs generalize the event-driven approach into replayable system history.
- [[AntiCorruptionLayer]] - protects one bounded model from another model's assumptions.
- [[MicroserviceOperationalOverhead]] - service boundaries also carry testing, deployment, and operations cost.
- [[DistributedSystemRestraint]] - boundary decisions should match team and operational readiness.
- [[IncrementalMonolithMigration]] - ownership must become explicit as writes move out of a monolith.
