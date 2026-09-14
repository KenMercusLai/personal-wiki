---
title: "Legacy Displacement"
type: concept
tags: [software-architecture, migration, legacy-systems]
sources:
  - blog-ian-cartwright-rob-horn-james-lewis-martinfowler-com-legacy-mimic
last_updated: 2026-09-14
knowledge_schema: synthesis-v1
---

## Definition
[[LegacyDisplacement]] is the incremental replacement of legacy-system capabilities with new systems while business processes continue to operate across old and new components.

## Current Synthesis
The source presents displacement as a sequencing problem rather than a single cutover. Teams examine existing technical architecture, target architecture, current business processes, and desired processes to find exploitable seams. Those seams let a replacement effort move one capability at a time while compatibility components keep adjacent legacy processes alive.

In the example, Logistics is separated from a legacy system that also supports Sales and Business Performance. That split creates a need for [[EventInterception]] so sales events reach the new logistics system, and for [[LegacyMimic]] behavior so legacy reporting still receives logistics metrics.

## Key Claims
- Legacy replacement can be decomposed by finding seams between business capabilities and system interactions.
- Sequencing choices create temporary integration obligations between old and new worlds.
- Extracting a value stream can move a capability out of a monolith before all related processes are replaced.
- Compatibility components are migration enablers, not the final architecture.

## Evidence
- Seam discovery: [[blog-ian-cartwright-rob-horn-james-lewis-martinfowler-com-legacy-mimic]] says legacy architecture, target architecture, and business-process analysis reveal seams that break the problem into parts.
- Logistics example: [[blog-ian-cartwright-rob-horn-james-lewis-martinfowler-com-legacy-mimic]] shows Sales, Logistics, and Business Performance initially supported by one legacy system.
- Extracted capability: [[blog-ian-cartwright-rob-horn-james-lewis-martinfowler-com-legacy-mimic]] shows Logistics moved into a new system while Sales and Business Performance remain legacy.
- Compatibility need: [[blog-ian-cartwright-rob-horn-james-lewis-martinfowler-com-legacy-mimic]] uses event interception and metrics replication as transition supports.

## Counterevidence & Qualifications
The source focuses on one displacement pattern page, so it does not compare all possible modernization strategies. It supports incremental displacement but does not claim every legacy replacement should be decomposed through the same seams or value-stream sequence.

## What Changed
- Created the concept from the article's framing of incremental replacement and seam-based sequencing.

## Related Concepts
- [[TransitionalArchitecture]] - displacement requires an architecture for the old/new coexistence period.
- [[LegacyMimic]] - compatibility pattern that supports displacement sequencing.
- [[ExtractValueStreams]] - sequencing method illustrated by extracting Logistics.
- [[EventInterception]] - migration mechanism for feeding new systems from legacy events.
- [[CapabilityOrientedIntegration]] - related boundary discipline for hiding source-system complexity.
