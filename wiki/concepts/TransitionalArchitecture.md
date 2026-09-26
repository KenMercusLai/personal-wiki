---
title: "Transitional Architecture"
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
[[TransitionalArchitecture]] is the temporary architecture used while a legacy system is being incrementally replaced and old and new components must interoperate before the target architecture is complete.

## Current Synthesis
The Legacy Mimic source treats transitional architecture as the normal condition of serious legacy displacement. The old world and new world cannot be separated cleanly from day one; replacement work has to preserve business continuity while changing system boundaries. Temporary adapters, interceptors, replicas, and compatibility layers create options for sequencing the migration.

The key discipline is to keep the transition visible as transition. In the logistics example, the event interceptor and metrics mimic are useful precisely because they let Sales, Business Performance, and Logistics move at different times. They should not endure in the target architecture once those legacy dependencies are gone.

The aggregator example shows that temporary architecture exists whichever direction a migration takes. Leaving reporting in legacy needs mimic feeds from newly displaced upstream systems; replacing it first needs intercepted events, source repositories, facades, parallel operation, and progressive redirection until the old aggregator and its remaining paths can be retired.

The worked storefront example makes the lifecycle concrete. An event-router seam enables selective traffic movement; an event transformer protects the new event model; database adapters and reporting mimics keep legacy processes alive. Each component disappears when its specific dependency is removed, so the target is reached through multiple safe decommissioning points rather than one final cutover. The architecture is justified when earlier value and lower migration risk outweigh its build-and-removal cost.

## Key Claims
- Incremental replacement usually needs temporary structures between legacy and new systems.
- Transitional components preserve business processes while capability boundaries move.
- The transition architecture can create sequencing options for extracting part of a system before the rest is replaced.
- Temporary compatibility components need explicit retirement expectations.
- Removal conditions should be tied to the dependency each temporary component satisfies.
- Enduring integration to external systems should be separated from transitional legacy compatibility.

## Evidence
- Migration boundary: [[blog-ian-cartwright-rob-horn-james-lewis-martinfowler-com-legacy-mimic]] says incremental replacement prevents clean isolation between old and new worlds.
- Sequencing: [[blog-ian-cartwright-rob-horn-james-lewis-martinfowler-com-legacy-mimic]] says seams discovered through legacy and target architecture analysis allow the problem to be broken into parts.
- Example architecture: [[blog-ian-cartwright-rob-horn-james-lewis-martinfowler-com-legacy-mimic]] shows logistics extracted while sales and business performance remain in the legacy system.
- Retirement expectation: [[blog-ian-cartwright-rob-horn-james-lewis-martinfowler-com-legacy-mimic]] says the example mimics are not part of the target architecture.
- Bidirectional sequencing: [[blog-ian-cartwright-rob-horn-james-lewis-martinfowler-com-divert-the-flow]] says both early and late aggregator replacement require temporary components and integrations.
- Operational controls: [[blog-ian-cartwright-rob-horn-james-lewis-martinfowler-com-divert-the-flow]] recommends parallel running, staged user diversion, feed monitoring, and output tolerances.
- Value test: [[blog-ian-cartwright-rob-horn-james-lewis-martinfowler-com-transitional-architecture]] compares earlier time-to-value and reduced displacement risk with temporary construction and removal cost.
- Dependency-ordered retirement: [[blog-ian-cartwright-rob-horn-james-lewis-martinfowler-com-transitional-architecture]] shows middleware, routing, transformation, reporting-mimic, and database-adapter components removed at different milestones.

## Counterevidence & Qualifications
The sources provide practitioner patterns rather than comparative migration outcomes or a full governance model. A transition design can become accidental permanence unless teams track temporary ownership, the dependency each component satisfies, validation criteria, and removal conditions; removability itself may require additional up-front work.

## What Changed
- Added explicit cost-benefit criteria based on time-to-value, migration risk, and temporary construction cost.
- Added dependency-ordered decommissioning from the storefront evolution example.

## Related Concepts
- [[LegacyDisplacement]] - transitional architecture is the operating model for incremental displacement.
- [[LegacyMimic]] - a common temporary component inside transition architecture.
- [[ExtractValueStreams]] - one sequencing approach that creates temporary old/new coexistence.
- [[EventInterception]] - one transitional mechanism for feeding new capabilities from legacy activity.
- [[AntiCorruptionLayer]] - can be enduring when it protects a target model from an external system.
- [[DivertTheFlow]] - uses a changing set of temporary feeds while an aggregator moves first.
- [[ParallelRunning]] - validates old/new coexistence during the transition.
- [[RevertToSource]] - can replace an indirect legacy feed during migration.
