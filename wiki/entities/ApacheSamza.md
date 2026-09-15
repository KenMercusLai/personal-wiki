---
title: "Apache Samza"
type: entity
tags: [stream-processing, event-streaming, data-architecture]
sources:
  - christian-posta-the-hardest-part-about-microservices-your-data
last_updated: 2026-09-15
knowledge_schema: synthesis-v1
---

## Overview
[[ApacheSamza]] appears in the wiki through Posta's reference to Martin Kleppmann's "Turning the database inside-out with Apache Samza" as background for event-log-centered data architecture.

## Current Profile
The source uses Samza as a pointer to the inside-out database idea: persistent streams can be treated as the basis for deriving current-state databases, caches, and indexes. The inspected image is a title-style graphic reading "Turning the DB inside-out with samza," so its evidentiary value is mainly confirming the reference context rather than adding independent architecture details.

## Key Characteristics
- Serves as the named stream-processing technology in the inside-out database reference.
- Is connected to persistent event streams and materialized views.
- Is not independently analyzed beyond the reference.

## Evidence
- Reference: [[christian-posta-the-hardest-part-about-microservices-your-data]] points to Martin Kleppmann's Samza talk/blog post for more information on turning the database inside out.
- Image evidence: [[christian-posta-the-hardest-part-about-microservices-your-data]] includes an inspected title graphic for "Turning the DB inside-out with samza."

## Qualifications
The source does not explain Samza's architecture, APIs, deployment model, or tradeoffs. The page should be expanded only if a Samza-specific source is ingested.

## What Changed
- Created the entity page for Apache Samza from Posta's inside-out database reference.

## Relationships
- [[EventLogAsSystemOfRecord]] - Samza is named in the source's reference for event-log-centered data architecture.
- [[EventDrivenConsistency]] - stream processing is one way to consume and derive from event streams.
