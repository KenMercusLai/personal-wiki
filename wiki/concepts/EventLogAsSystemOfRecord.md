---
title: "Event Log as System of Record"
type: concept
tags: [event-sourcing, distributed-systems, data-architecture, microservices]
sources:
  - christian-posta-the-hardest-part-about-microservices-your-data
last_updated: 2026-09-15
knowledge_schema: synthesis-v1
---

## Definition
[[EventLogAsSystemOfRecord]] is a data architecture where the durable event stream is treated as the historical record, while databases, caches, and indexes are materialized views over that stream.

## Current Synthesis
Posta describes "turning the database inside out" as the logical extreme of event-driven microservices. Instead of treating a database table as the true record and events as a side effect, the event log stores what happened over time, and current state is derived by folding over those events.

This model changes what databases are for. A relational database, cache, search index, or specialized store becomes a current-state projection that can be rebuilt, tested, migrated, or compared by replaying history. The inspected Samza image is mostly a title slide, but the surrounding section makes the architectural claim: persistent streams make audit, replay, schema evolution, and database migration more tractable when the event history is the durable source.

## Key Claims
- A persistent event log can become the durable historical record of a system.
- Databases, caches, and indexes can be treated as materialized views over events.
- Replaying past events enables audit logging, migration, schema-change testing, and behavioral comparison.
- Current-state databases remain useful but are not necessarily the deepest record.
- This approach extends event-driven consistency but increases the need for robust event design and operations.

## Evidence
- Core model: [[christian-posta-the-hardest-part-about-microservices-your-data]] asks whether databases, caches, and indexes are materialized views of a persistent stream of events.
- Replay benefits: [[christian-posta-the-hardest-part-about-microservices-your-data]] says past events can be replayed to test new application versions and rebuild new databases.
- Audit benefit: [[christian-posta-the-hardest-part-about-microservices-your-data]] says event persistence provides audit logging.
- Migration benefit: [[christian-posta-the-hardest-part-about-microservices-your-data]] says replay can support database versioning, upgrades, and moves to new database technology.
- Reference context: [[christian-posta-the-hardest-part-about-microservices-your-data]] points to Martin Kleppmann's Apache Samza talk/blog post as more information on the inside-out database idea.

## Counterevidence & Qualifications
The source presents the model as a powerful extension, not a universal default. Replaying events only helps when event meanings are durable enough, ordering and idempotency are handled, and operators can manage the complexity of logs, processors, and projections.

## What Changed
- Created the concept from Posta's "turn the database inside out" section.

## Related Concepts
- [[EventDrivenConsistency]] - event-log systems extend event-based cross-boundary consistency.
- [[MicroserviceDataBoundaries]] - persistent events are one way to reconcile data split across services.
- [[ApacheKafka]] - Kafka is one named persistent replicated log option in the source.
- [[ApacheSamza]] - Samza is named through the inside-out database reference.
- [[Debezium]] - change data capture can bridge conventional databases into event logs.
- [[DatabaseConsolidation]] - event-log architectures are an alternative to treating a single database as the simplifying center.
