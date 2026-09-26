---
title: "Event Interception"
type: concept
tags: [software-architecture, events, migration]
sources:
  - blog-ian-cartwright-rob-horn-james-lewis-martinfowler-com-legacy-mimic
  - blog-ian-cartwright-rob-horn-james-lewis-martinfowler-com-divert-the-flow
  - blog-ian-cartwright-rob-horn-james-lewis-martinfowler-com-transitional-architecture
last_updated: 2026-09-25
knowledge_schema: synthesis-v1
---

## Definition
[[EventInterception]] is a migration mechanism where activity from a legacy system is captured from an existing event stream or interface so a new system can react without requiring the legacy producer to know about the replacement.

## Current Synthesis
The source presents event interception as a concrete service-providing [[LegacyMimic]]. In the logistics example, the legacy sales flow records a sale and publishes a sale message. An event interceptor consumes that legacy-shaped message and passes the sale to the new logistics system for processing, allowing Logistics to be extracted without rewriting the sales process first.

The Divert the Flow source gives the mechanism a second role: an extracted [[CriticalAggregator]] may initially intercept activity from legacy systems while direct [[RevertToSource]] feeds are introduced. Event interception is therefore one bridge in a changing data-sourcing plan, not necessarily the replacement's final ingestion boundary.

In the storefront example, interception begins even earlier as a technical seam: an event router is inserted between the legacy queue and middleware before behavior changes. That route then supports selective traffic diversion, message transformation into a clean business event, gradual adoption, and rollback. The router and transformer are removed when the asset disposal router becomes the authoritative event producer.

## Key Claims
- Event interception can let a new capability subscribe to legacy activity during migration.
- It is service-providing mimic behavior when the interceptor conforms to the legacy event interface.
- The mechanism helps decouple extraction sequencing: the event producer can remain legacy while the consumer moves to the new world.
- Interceptors used this way are transitional and should disappear when the old event dependency is retired.
- An aggregator migration can combine intercepted events with direct source feeds and reduce interception as upstream systems move.
- A router can establish a seam before replacement behavior exists, then support progressive traffic migration and rollback.

## Evidence
- Example role: [[blog-ian-cartwright-rob-horn-james-lewis-martinfowler-com-legacy-mimic]] says the Event Interceptor is a service-providing mimic because it conforms to legacy event consumption.
- Visual evidence: [[blog-ian-cartwright-rob-horn-james-lewis-martinfowler-com-legacy-mimic]] shows a legacy sales message consumed by an Event Interceptor Mimic, which then processes the sale through the new logistics system.
- Sequencing: [[blog-ian-cartwright-rob-horn-james-lewis-martinfowler-com-legacy-mimic]] uses event interception after choosing to extract the Logistics capability.
- Aggregator use: [[blog-ian-cartwright-rob-horn-james-lewis-martinfowler-com-divert-the-flow]] proposes event interception as one way to feed a replacement aggregator from existing legacy systems.
- Router seam: [[blog-ian-cartwright-rob-horn-james-lewis-martinfowler-com-transitional-architecture]] inserts an event router into the queue path as the first enabling step.
- Retirement: [[blog-ian-cartwright-rob-horn-james-lewis-martinfowler-com-transitional-architecture]] removes the router and transformer after the asset disposal router emits target-format business events directly.

## Counterevidence & Qualifications
The sources give pattern examples, not a general event-architecture taxonomy. Interception can introduce duplication, ordering, replay, schema, latency, routing-state, and ownership questions that are outside their scope; direct production or sourcing is preferable once a stable authoritative boundary exists.

## What Changed
- Added interception as a pre-behavior routing seam for gradual traffic migration, rollback, and later removal.

## Related Concepts
- [[LegacyMimic]] - event interception is the article's service-providing mimic example.
- [[ExtractValueStreams]] - extraction of Logistics creates the need for intercepted sales events.
- [[TransitionalArchitecture]] - event interception is temporary old/new bridgework.
- [[LegacyDisplacement]] - intercepted events support incremental replacement.
- [[AntiCorruptionLayer]] - both adapt across model or interface boundaries.
- [[DivertTheFlow]] - uses interception while redirecting a new aggregator's inputs.
- [[RevertToSource]] - complementary option for bypassing legacy intermediaries.
- [[CriticalAggregator]] - replacement consumer that may temporarily receive intercepted events.
