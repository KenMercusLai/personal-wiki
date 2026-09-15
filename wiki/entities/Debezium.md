---
title: "Debezium"
type: entity
tags: [change-data-capture, data-integration, event-streaming]
sources:
  - christian-posta-the-hardest-part-about-microservices-your-data
last_updated: 2026-09-15
knowledge_schema: synthesis-v1
---

## Overview
[[Debezium]] appears in the wiki as a change-data-capture tool that can stream database changes into an event log for microservice consistency.

## Current Profile
Posta names Debezium as part of a path for teams that continue writing to an ACID database but want to publish durable events without distributed transactions. In that model, Debezium captures database changes and feeds a persistent replicated log such as Kafka, where event processors can derive domain events or downstream projections.

## Key Characteristics
- Provides change data capture from ordinary databases in the source's architecture.
- Helps bridge ACID database writes into event streams.
- Is an implementation option for event-driven consistency, not a modeling substitute.

## Evidence
- CDC role: [[christian-posta-the-hardest-part-about-microservices-your-data]] names Debezium as a way to stream database changes to a persistent replicated log.
- Event processing role: [[christian-posta-the-hardest-part-about-microservices-your-data]] says events may then be deduced through an event processor or stream processor.

## Qualifications
The source only mentions Debezium briefly. It does not evaluate setup, connector support, schema evolution, or operational failure modes.

## What Changed
- Created the entity page for Debezium from Posta's event-stream implementation discussion.

## Relationships
- [[ApacheKafka]] - Debezium is paired with Kafka-like replicated logs in the source.
- [[EventDrivenConsistency]] - CDC can publish facts after local database transactions.
- [[EventLogAsSystemOfRecord]] - CDC can feed the event history used by projections.
