---
title: "Microservice Data Boundaries"
type: concept
tags: [microservices, data, software-architecture, domain-driven-design]
sources:
  - christian-posta-the-hardest-part-about-microservices-your-data
last_updated: 2026-09-15
knowledge_schema: synthesis-v1
---

## Definition
[[MicroserviceDataBoundaries]] are the domain, ownership, transaction, and integration boundaries that determine how data is modeled, stored, changed, and reconciled across microservices.

## Current Synthesis
Posta frames data boundaries as the hardest part of microservices because they force teams to give up the safety and convenience of one shared ACID database without replacing it with simplistic rules. The article's claim is not merely "one database per service." It says services need explicit domain meanings, small transactional boundaries, and communication mechanisms that accept distributed-system limits.

The inspected diagrams make the progression concrete. One diagram separates Admin, Orders/Booking, and Search behind REST APIs with MySQL or Elasticsearch stores and an anti-corruption boundary near Search. Later diagrams show why putting Flight, Customers, Planes, and Booking into one transaction boundary is too broad, and how Booking, SeatAvailability, and Flights can become independent transactional units. The final architecture sketch uses data capture and event handlers feeding a distributed replicated event log, turning cross-service consistency into event processing rather than shared writes.

## Key Claims
- Microservice boundaries should follow explicit domain models rather than physical database convenience.
- Data splitting removes single-database conveniences, so teams must deliberately replace ACID assumptions with boundary-aware consistency design.
- Terms such as Customer, Account, Booking, or Book can have different valid meanings in different contexts.
- Transactional boundaries should be smaller than broad object graphs when business invariants do not require one atomic update.
- Integration across boundaries should be designed as distributed consistency work, not hidden behind synchronous RPC abstractions.
- One-database-per-service is a heuristic, not an absolute rule.

## Evidence
- Domain-first data: [[christian-posta-the-hardest-part-about-microservices-your-data]] says the data model should be driven by the domain model rather than the other way around.
- Context ambiguity: [[christian-posta-the-hardest-part-about-microservices-your-data]] uses the "book" example to show that data meaning depends on who is asking and in what context.
- Diagram evidence: [[christian-posta-the-hardest-part-about-microservices-your-data]] shows Admin, Orders/Booking, and Search as separate service areas with distinct stores and an anti-corruption boundary.
- Oversized transaction warning: [[christian-posta-the-hardest-part-about-microservices-your-data]] argues that a Flight aggregate containing customers, planes, bookings, and schedules creates unnecessary transaction conflicts.
- Boundary tradeoff: [[christian-posta-the-hardest-part-about-microservices-your-data]] says shared databases can be acceptable when the same team owns the processes and autonomy is not undermined.

## Counterevidence & Qualifications
The source does not claim every system should become microservices or event-sourced. It explicitly warns against copying Netflix-style visible outcomes without the process and says enterprises must balance domain complexity, scale, and organizational change. The diagrams are conceptual rather than a production reference architecture.

## What Changed
- Created the concept from Posta's article on domain, transaction, and data boundaries in microservices.

## Related Concepts
- [[BoundedContext]] - domain boundaries are the article's starting point for data ownership.
- [[AggregateTransactionBoundary]] - transactional boundaries refine data ownership into atomic business-invariant units.
- [[EventDrivenConsistency]] - event propagation reconciles state across boundaries.
- [[EventLogAsSystemOfRecord]] - persistent logs generalize the event-driven approach into replayable system history.
- [[AntiCorruptionLayer]] - protects one bounded model from another model's assumptions.
- [[MicroserviceOperationalOverhead]] - service boundaries also carry testing, deployment, and operations cost.
- [[DistributedSystemRestraint]] - boundary decisions should match team and operational readiness.
