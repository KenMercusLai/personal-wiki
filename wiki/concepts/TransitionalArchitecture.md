---
title: "Transitional Architecture"
type: concept
tags: [software-architecture, migration, legacy-systems]
sources:
  - blog-ian-cartwright-rob-horn-james-lewis-martinfowler-com-legacy-mimic
last_updated: 2026-09-14
knowledge_schema: synthesis-v1
---

## Definition
[[TransitionalArchitecture]] is the temporary architecture used while a legacy system is being incrementally replaced and old and new components must interoperate before the target architecture is complete.

## Current Synthesis
The Legacy Mimic source treats transitional architecture as the normal condition of serious legacy displacement. The old world and new world cannot be separated cleanly from day one; replacement work has to preserve business continuity while changing system boundaries. Temporary adapters, interceptors, replicas, and compatibility layers create options for sequencing the migration.

The key discipline is to keep the transition visible as transition. In the logistics example, the event interceptor and metrics mimic are useful precisely because they let Sales, Business Performance, and Logistics move at different times. They should not endure in the target architecture once those legacy dependencies are gone.

## Key Claims
- Incremental replacement usually needs temporary structures between legacy and new systems.
- Transitional components preserve business processes while capability boundaries move.
- The transition architecture can create sequencing options for extracting part of a system before the rest is replaced.
- Temporary compatibility components need explicit retirement expectations.
- Enduring integration to external systems should be separated from transitional legacy compatibility.

## Evidence
- Migration boundary: [[blog-ian-cartwright-rob-horn-james-lewis-martinfowler-com-legacy-mimic]] says incremental replacement prevents clean isolation between old and new worlds.
- Sequencing: [[blog-ian-cartwright-rob-horn-james-lewis-martinfowler-com-legacy-mimic]] says seams discovered through legacy and target architecture analysis allow the problem to be broken into parts.
- Example architecture: [[blog-ian-cartwright-rob-horn-james-lewis-martinfowler-com-legacy-mimic]] shows logistics extracted while sales and business performance remain in the legacy system.
- Retirement expectation: [[blog-ian-cartwright-rob-horn-james-lewis-martinfowler-com-legacy-mimic]] says the example mimics are not part of the target architecture.

## Counterevidence & Qualifications
The source does not provide a full governance model for retiring transitional components. A transition design can become accidental permanence unless teams track which components are temporary, what dependency they satisfy, and what condition removes them.

## What Changed
- Created the concept from the source's explanation of temporary architecture during legacy displacement.

## Related Concepts
- [[LegacyDisplacement]] - transitional architecture is the operating model for incremental displacement.
- [[LegacyMimic]] - a common temporary component inside transition architecture.
- [[ExtractValueStreams]] - one sequencing approach that creates temporary old/new coexistence.
- [[EventInterception]] - one transitional mechanism for feeding new capabilities from legacy activity.
- [[AntiCorruptionLayer]] - can be enduring when it protects a target model from an external system.
