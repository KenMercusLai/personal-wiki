---
title: "Modular Monolith"
type: concept
tags: [software-architecture, modularity, monolith, domain-boundaries]
sources:
  - deconstructing-the-monolith-shopify-engineering
last_updated: 2026-09-27
knowledge_schema: synthesis-v1
---

## Definition
A [[ModularMonolith]] is one application and deployment unit whose internal business domains have explicit, respected boundaries, owned data, and narrow public interfaces.

## Current Synthesis
Shopify's case separates two decisions that architecture debates often collapse: how modular the code is and how many units are deployed. A system can be a tightly coupled monolith, a modular monolith, well-bounded microservices, or a distributed big ball of mud. Keeping one repository, pipeline, database, and in-process call path can preserve operational simplicity, but only if internal dependencies are visible and constrained.

The migration path in the source is incremental in governance even though its initial file move was a big-bang pull request. Shopify first used developer pain to justify the work, mapped code to business domains, reorganized files, defined component ownership and public APIs, measured cross-boundary calls and data associations, and planned stronger enforcement. The goal was not perfect isolation immediately; it was to make coupling legible and steadily removable while retaining one deployment unit.

## Key Claims
- Modularity is independent from the number of deployment units.
- One deployment can preserve repository, pipeline, database, and in-process-call simplicity.
- Business-domain organization reduces search and onboarding context compared with purely technical-layer organization.
- Public interfaces and data ownership are necessary for components to be more than folders.
- Dynamic and static dependency evidence can turn boundary quality into measurable work.
- Architecture should evolve when observed coupling costs exceed the current design's simplicity benefits.

## Evidence
- Architectural distinction: [[deconstructing-the-monolith-shopify-engineering]] includes Simon Brown's matrix with modularity on one axis and deployment-unit count on the other.
- Monolith benefits: [[deconstructing-the-monolith-shopify-engineering]] lists one repository, pipeline, database, infrastructure set, and direct calls as sources of lower overhead.
- Domain reorganization: [[deconstructing-the-monolith-shopify-engineering]] shows Shopify moving from models/controllers/jobs folders toward apps, billing, checkouts, taxes, and other components.
- Boundary contract: [[deconstructing-the-monolith-shopify-engineering]] says each component should expose a public API and exclusively own associated data.
- Measurement: [[deconstructing-the-monolith-shopify-engineering]] describes [[Wedge]] using CI call graphs, associations, and inheritance data to score isolation.
- Changeability: [[deconstructing-the-monolith-shopify-engineering]] reports that dependency isolation enabled replacement of a legacy tax engine.

## Counterevidence & Qualifications
The source is one company's 2019 progress report, and the program was incomplete: full isolation, inheritance analysis, score trends, and runtime enforcement were still future work. Its claim is not that a modular monolith always dominates microservices. Independently deployed services can provide autonomy and scaling benefits when boundaries are understood and the organization can bear their operational cost; a small uncomplicated monolith may need no formal modularity yet.

## What Changed
- Established deployment count and modularity as separate architecture dimensions.
- Identified measurement and staged enforcement as the bridge from folder organization to respected boundaries.

## Related Concepts
- [[CDComponentization]] - component extraction can improve ownership, feedback speed, and changeability without requiring separate deployment.
- [[MicroserviceOperationalOverhead]] - a modular monolith retains boundaries while avoiding some distributed-system costs.
- [[BoundedContext]] - domain context helps define meaningful component boundaries.
- [[DistributedSystemRestraint]] - delayed distribution preserves learning until service boundaries and operational need are clearer.
- [[MonolithConsolidation]] - consolidation also reduces deployment units, but usually by reversing prior service proliferation.
- [[DomainModelDrivenData]] - component data ownership should follow domain meaning rather than arbitrary table splits.
