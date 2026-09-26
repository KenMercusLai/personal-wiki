---
title: "Revert to Source"
type: concept
tags: [software-architecture, migration, data, provenance]
sources:
  - blog-ian-cartwright-rob-horn-james-lewis-martinfowler-com-divert-the-flow
last_updated: 2026-09-25
knowledge_schema: synthesis-v1
---

## Definition
[[RevertToSource]] is a migration approach that obtains data from its ultimate originating system rather than preserving an indirect feed through a legacy intermediary that has become the apparent source of truth.

## Current Synthesis
The source uses sales data to distinguish provenance from convenience: a mainframe may hold the records used by reporting while in-store tills are the ultimate origin. Feeding a replacement aggregator from the origin can improve format, completeness, and timeliness while reducing dependency on the legacy estate.

Reverting to source begins with a context map of systems, flows, cadence, consumers, and data discarded along the current route. It can coexist with [[EventInterception]] while a migration is incomplete; the goal is not doctrinal direct access but a progressive reduction in legacy mediation.

## Key Claims
- An operationally convenient legacy store is not necessarily the ultimate source of data.
- Source mapping must include flow direction, frequency, transformations, consumers, and discarded fields.
- Moving closer to the origin can improve timeliness and recover data lost by legacy representations.
- Direct-source feeds still need explicit ownership, contracts, quality controls, and monitoring.

## Evidence
- Provenance example: [[blog-ian-cartwright-rob-horn-james-lewis-martinfowler-com-divert-the-flow]] distinguishes a mainframe holding sales information from the tills where sales originate.
- Lost data: [[blog-ian-cartwright-rob-horn-james-lewis-martinfowler-com-divert-the-flow]] says legacy bottlenecks often discard useful source-system data that could not be represented.
- Mixed transition: [[blog-ian-cartwright-rob-horn-james-lewis-martinfowler-com-divert-the-flow]] says new aggregators commonly combine event interception and revert-to-source feeds.
- Visual evidence: [[blog-ian-cartwright-rob-horn-james-lewis-martinfowler-com-divert-the-flow]] shows warehouse and till data redirected into stock and sales repositories outside the legacy reporting path.

## Counterevidence & Qualifications
The source does not define when direct access would improperly couple an aggregator to a transactional system or overload an operational source. “Ultimate” can also be ambiguous after transformations, corrections, and stewardship. A well-owned repository or event contract may be the safer boundary even when the raw event originates elsewhere.

## What Changed
- Created the concept from the source's provenance and data-flow guidance.

## Related Concepts
- [[DivertTheFlow]] - uses source redirection to loosen an aggregator from legacy systems.
- [[CriticalAggregator]] - consumer whose indirect feeds are being reconsidered.
- [[EventInterception]] - complementary transition mechanism when direct sourcing is unavailable.
- [[TransitionalArchitecture]] - governs coexistence between direct and legacy feeds.
- [[LegacyDisplacement]] - broader program in which source ownership changes.
