---
title: "Event Interception"
type: concept
tags: [software-architecture, events, migration]
sources:
  - blog-ian-cartwright-rob-horn-james-lewis-martinfowler-com-legacy-mimic
last_updated: 2026-09-14
knowledge_schema: synthesis-v1
---

## Definition
[[EventInterception]] is a migration mechanism where activity from a legacy system is captured from an existing event stream or interface so a new system can react without requiring the legacy producer to know about the replacement.

## Current Synthesis
The source presents event interception as a concrete service-providing [[LegacyMimic]]. In the logistics example, the legacy sales flow records a sale and publishes a sale message. An event interceptor consumes that legacy-shaped message and passes the sale to the new logistics system for processing, allowing Logistics to be extracted without rewriting the sales process first.

## Key Claims
- Event interception can let a new capability subscribe to legacy activity during migration.
- It is service-providing mimic behavior when the interceptor conforms to the legacy event interface.
- The mechanism helps decouple extraction sequencing: the event producer can remain legacy while the consumer moves to the new world.
- Interceptors used this way are transitional and should disappear when the old event dependency is retired.

## Evidence
- Example role: [[blog-ian-cartwright-rob-horn-james-lewis-martinfowler-com-legacy-mimic]] says the Event Interceptor is a service-providing mimic because it conforms to legacy event consumption.
- Visual evidence: [[blog-ian-cartwright-rob-horn-james-lewis-martinfowler-com-legacy-mimic]] shows a legacy sales message consumed by an Event Interceptor Mimic, which then processes the sale through the new logistics system.
- Sequencing: [[blog-ian-cartwright-rob-horn-james-lewis-martinfowler-com-legacy-mimic]] uses event interception after choosing to extract the Logistics capability.

## Counterevidence & Qualifications
The source gives a pattern example, not a general event-architecture taxonomy. Event interception can introduce duplication, ordering, replay, schema, and ownership questions that are outside this article's scope.

## What Changed
- Created the concept from the article's logistics transition example.

## Related Concepts
- [[LegacyMimic]] - event interception is the article's service-providing mimic example.
- [[ExtractValueStreams]] - extraction of Logistics creates the need for intercepted sales events.
- [[TransitionalArchitecture]] - event interception is temporary old/new bridgework.
- [[LegacyDisplacement]] - intercepted events support incremental replacement.
- [[AntiCorruptionLayer]] - both adapt across model or interface boundaries.
