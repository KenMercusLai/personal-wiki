---
title: "Divert the Flow"
type: concept
tags: [software-architecture, migration, legacy-systems, data]
sources:
  - blog-ian-cartwright-rob-horn-james-lewis-martinfowler-com-divert-the-flow
last_updated: 2026-09-25
knowledge_schema: synthesis-v1
---

## Definition
[[DivertTheFlow]] is a legacy-displacement strategy that replaces a tightly coupled cross-cutting capability, especially a [[CriticalAggregator]], before its upstream systems and progressively redirects the replacement toward decoupled and more authoritative data sources.

## Current Synthesis
The pattern reverses the common instinct to leave a dependency-heavy aggregator until last. A new implementation is placed outside the legacy boundary, initially fed through a mixture of [[EventInterception]], legacy facades, and [[RevertToSource]]. Once users trust its outputs, the legacy implementation can be disabled and upstream capabilities can move without continuing to satisfy its formats, workarounds, and update frequencies.

The migration is iterative rather than a clean switch. Teams map ultimate sources and consumers, rebuild valuable outputs in slices, reconcile old and new results, cut users over in cohorts, and monitor feeds and output tolerances. As upstream systems move, the new aggregator's remaining legacy dependencies should decline.

## Key Claims
- Replacing a critical aggregator early can remove a dependency bottleneck that would otherwise constrain every upstream migration.
- Initial data feeds may combine intercepted legacy activity, direct source access, repositories, and temporary facades.
- The useful target is current user value and trustworthy outputs, not automatic feature parity with accumulated reports.
- Output disagreement must be investigated with known inputs and worked examples because legacy behavior may itself be wrong.
- Transitional dependencies need monitoring and an explicit path toward removal.

## Evidence
- Sequencing rationale: [[blog-ian-cartwright-rob-horn-james-lewis-martinfowler-com-divert-the-flow]] contrasts early aggregator replacement with leaving it until last and maintaining mimic feeds.
- Data sourcing: [[blog-ian-cartwright-rob-horn-james-lewis-martinfowler-com-divert-the-flow]] recommends combining event interception with direct access to ultimate source systems.
- Delivery path: [[blog-ian-cartwright-rob-horn-james-lewis-martinfowler-com-divert-the-flow]] recommends report-by-report slices, production-like delivery, beta feedback, parallel running, and staged cutover.
- Visual evidence: [[blog-ian-cartwright-rob-horn-james-lewis-martinfowler-com-divert-the-flow]] shows reporting moved outside the legacy boundary and fed through stock and sales repositories while legacy paths are phased out.

## Counterevidence & Qualifications
The pattern is practitioner guidance rather than comparative outcome research. Moving a critical aggregator first can be expensive when its calculations, users, workarounds, or provenance are poorly understood, and the source does not supply a general decision threshold. A new aggregator can reproduce legacy coupling under new names unless temporary feeds, ownership, and retirement conditions remain explicit.

## What Changed
- Created the concept from the source's early-aggregator displacement strategy and inspected before/after diagrams.

## Related Concepts
- [[CriticalAggregator]] - primary cross-cutting capability targeted by the strategy.
- [[LegacyDisplacement]] - broader modernization process that the strategy sequences.
- [[TransitionalArchitecture]] - contains the temporary feeds and facades needed during diversion.
- [[LegacyMimic]] - alternative support when the old aggregator is deliberately left in place.
- [[RevertToSource]] - replaces indirect legacy feeds with data from ultimate origins.
- [[ParallelRunning]] - validates replacement outputs before and after cutover.
