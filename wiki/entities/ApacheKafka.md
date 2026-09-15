---
title: "Apache Kafka"
type: entity
tags: [event-streaming, distributed-systems, infrastructure]
sources:
  - christian-posta-the-hardest-part-about-microservices-your-data
last_updated: 2026-09-15
knowledge_schema: synthesis-v1
---

## Overview
[[ApacheKafka]] appears in the wiki as a persistent replicated log option for propagating database changes and events across microservice boundaries.

## Current Profile
Posta mentions Kafka as one implementation path for event-driven microservice consistency. Instead of making every service participate in a distributed transaction, a conventional ACID database can be paired with change data capture and streamed into a persistent replicated log. Kafka is the named log substrate in that option.

## Key Characteristics
- Represents a persistent replicated log in the source's architecture options.
- Supports event propagation from database changes into downstream processors.
- Is positioned as one implementation choice, not the essence of microservices.

## Evidence
- Event-log option: [[christian-posta-the-hardest-part-about-microservices-your-data]] names Kafka as a persistent, replicated log for streamed database changes.
- Change-data-capture context: [[christian-posta-the-hardest-part-about-microservices-your-data]] pairs Kafka with Debezium and event processors.

## Qualifications
The source does not analyze Kafka internals, operational tradeoffs, ecosystem, or alternatives. It uses Kafka as an example of an event-log substrate.

## What Changed
- Created the entity page for Kafka from Posta's event-driven consistency implementation discussion.

## Relationships
- [[EventDrivenConsistency]] - Kafka can carry events between bounded contexts.
- [[EventLogAsSystemOfRecord]] - Kafka is one possible replicated log substrate.
- [[Debezium]] - Debezium is named as the change-data-capture bridge into Kafka-style logs.
