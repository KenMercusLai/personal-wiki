---
title: "Legacy Displacement"
type: concept
tags: [software-architecture, migration, legacy-systems]
sources:
  - blog-ian-cartwright-rob-horn-james-lewis-martinfowler-com-legacy-mimic
  - blog-ian-cartwright-rob-horn-james-lewis-martinfowler-com-divert-the-flow
  - blog-ian-cartwright-rob-horn-james-lewis-martinfowler-com-transitional-architecture
last_updated: 2026-09-25
knowledge_schema: synthesis-v1
---

## Definition
[[LegacyDisplacement]] is the incremental replacement of legacy-system capabilities with new systems while business processes continue to operate across old and new components.

## Current Synthesis
The source presents displacement as a sequencing problem rather than a single cutover. Teams examine existing technical architecture, target architecture, current business processes, and desired processes to find exploitable seams. Those seams let a replacement effort move one capability at a time while compatibility components keep adjacent legacy processes alive.

In the example, Logistics is separated from a legacy system that also supports Sales and Business Performance. That split creates a need for [[EventInterception]] so sales events reach the new logistics system, and for [[LegacyMimic]] behavior so legacy reporting still receives logistics metrics.

The aggregator example makes sequencing costs explicit. Teams can displace upstream capabilities first and keep feeding a legacy [[CriticalAggregator]] through mimics, or use [[DivertTheFlow]] to replace the aggregator early and progressively redirect it toward authoritative sources. Both choices require transitional components, but they place compatibility burden and early user value in different parts of the program.

The storefront evolution adds traffic and responsibility as controllable migration dimensions. A router first creates a seam, selected product traffic moves through a new storefront manager, and the legacy middleware is retired once the new path handles all traffic. Later components remove the remaining routing, reporting, and database dependencies in turn, with the same seam providing a practical rollback path during gradual adoption.

## Key Claims
- Legacy replacement can be decomposed by finding seams between business capabilities and system interactions.
- Sequencing choices create temporary integration obligations between old and new worlds.
- Extracting a value stream can move a capability out of a monolith before all related processes are replaced.
- Compatibility components are migration enablers, not the final architecture.
- Cross-cutting capabilities should be sequenced by comparing the cost of early replacement with the cumulative cost of preserving their legacy contracts.
- Migration can improve data completeness and timeliness when replacement systems reconnect to ultimate sources.
- Traffic can move gradually across a seam so failures affect a bounded subset and serious problems can be rolled back.

## Evidence
- Seam discovery: [[blog-ian-cartwright-rob-horn-james-lewis-martinfowler-com-legacy-mimic]] says legacy architecture, target architecture, and business-process analysis reveal seams that break the problem into parts.
- Logistics example: [[blog-ian-cartwright-rob-horn-james-lewis-martinfowler-com-legacy-mimic]] shows Sales, Logistics, and Business Performance initially supported by one legacy system.
- Extracted capability: [[blog-ian-cartwright-rob-horn-james-lewis-martinfowler-com-legacy-mimic]] shows Logistics moved into a new system while Sales and Business Performance remain legacy.
- Compatibility need: [[blog-ian-cartwright-rob-horn-james-lewis-martinfowler-com-legacy-mimic]] uses event interception and metrics replication as transition supports.
- Aggregator choice: [[blog-ian-cartwright-rob-horn-james-lewis-martinfowler-com-divert-the-flow]] contrasts early aggregator replacement with updating legacy feeds after each upstream displacement.
- Operational path: [[blog-ian-cartwright-rob-horn-james-lewis-martinfowler-com-divert-the-flow]] joins iterative delivery, parallel validation, staged cutover, and monitoring.
- Traffic migration: [[blog-ian-cartwright-rob-horn-james-lewis-martinfowler-com-transitional-architecture]] routes an increasing share of products through the storefront manager until the integration middleware has no remaining traffic.
- Responsibility migration: [[blog-ian-cartwright-rob-horn-james-lewis-martinfowler-com-transitional-architecture]] removes each bridge only after routing, reporting, or sale-processing ownership has moved.

## Counterevidence & Qualifications
The sources are practitioner pattern guidance rather than comparative migration evidence. They support incremental displacement but do not establish that every replacement should use the same seams, traffic strategy, value-stream sequence, or aggregator-first approach; the balance depends on criticality, coupling, knowledge, rollback feasibility, and transition cost.

## What Changed
- Added progressive traffic routing, bounded failure impact, and dependency-ordered component retirement.

## Related Concepts
- [[TransitionalArchitecture]] - displacement requires an architecture for the old/new coexistence period.
- [[LegacyMimic]] - compatibility pattern that supports displacement sequencing.
- [[ExtractValueStreams]] - sequencing method illustrated by extracting Logistics.
- [[EventInterception]] - migration mechanism for feeding new systems from legacy events.
- [[CapabilityOrientedIntegration]] - related boundary discipline for hiding source-system complexity.
- [[DivertTheFlow]] - sequencing strategy that replaces a cross-cutting aggregator early.
- [[CriticalAggregator]] - dependency hub whose placement can constrain the migration sequence.
- [[RevertToSource]] - improves data paths while legacy intermediaries are displaced.
