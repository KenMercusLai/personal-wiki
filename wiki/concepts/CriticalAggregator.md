---
title: "Critical Aggregator"
type: concept
tags: [software-architecture, legacy-systems, reporting, data]
sources:
  - blog-ian-cartwright-rob-horn-james-lewis-martinfowler-com-divert-the-flow
last_updated: 2026-09-25
knowledge_schema: synthesis-v1
---

## Definition
[[CriticalAggregator]] is a cross-cutting capability that combines data from multiple systems into reports, metrics, calculations, or other outputs vital to operating a business.

## Current Synthesis
An aggregator becomes a legacy-migration bottleneck when its business importance, broad user base, opaque calculations, and invasive upstream connections make teams afraid to disturb it. Upstream systems then remain coupled to its schemas, workarounds, and update frequency even after their own implementations change.

The source presents two sequencing choices. [[DivertTheFlow]] replaces the aggregator early and progressively improves its sources; leaving it until last requires [[LegacyMimic]] feeds from each displaced upstream capability. Either route needs deliberate transition architecture and output validation.

## Key Claims
- Criticality comes from the business reliance on aggregated outputs, not merely the component's technical size.
- Many upstream dependencies make the aggregator a cross-cutting migration constraint.
- Apparent data sources may be intermediate legacy systems rather than ultimate origins.
- Lost calculation knowledge and off-system manual work can be as important as code dependencies.
- Early replacement and late replacement create different, explicit transition costs.

## Evidence
- Coupling problem: [[blog-ian-cartwright-rob-horn-james-lewis-martinfowler-com-divert-the-flow]] describes legacy critical aggregators as invasive implementations that freeze themselves and upstream systems in place.
- Dependency map: [[blog-ian-cartwright-rob-horn-james-lewis-martinfowler-com-divert-the-flow]] says mapping must cover upstream and downstream systems, data items, cadence, and discarded data.
- Knowledge risk: [[blog-ian-cartwright-rob-horn-james-lewis-martinfowler-com-divert-the-flow]] recounts a financial calculation whose undocumented spreadsheet lineage could no longer be recovered.
- Visual evidence: [[blog-ian-cartwright-rob-horn-james-lewis-martinfowler-com-divert-the-flow]] shows legacy reporting consuming five internal systems fed indirectly by warehouse and till sources.

## Counterevidence & Qualifications
The source uses reporting and data warehouses as the main examples, so it does not establish that every shared service is a Critical Aggregator or should be replaced early. Criticality, coupling, replacement cost, regulatory obligations, and tolerance for parallel operation must be assessed in the specific business context.

## What Changed
- Created the concept from the source's reporting and data-warehouse examples.

## Related Concepts
- [[DivertTheFlow]] - strategy for replacing the aggregator before its upstream systems.
- [[LegacyMimic]] - supplies the legacy aggregator when upstream systems move first.
- [[RevertToSource]] - traces aggregated data back to ultimate origins.
- [[ParallelRunning]] - compares old and replacement aggregator outputs.
- [[TransitionalArchitecture]] - coordinates temporary dependencies during replacement.
