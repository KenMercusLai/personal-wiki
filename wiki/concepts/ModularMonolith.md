---
title: "Modular Monolith"
type: concept
tags: [software-architecture, modularity, monolith, domain-boundaries]
sources:
  - deconstructing-the-monolith-shopify-engineering
  - jimmy-bogard-my-microservices-faq
  - kubernetes-maybe-a-few-bashpython-scripts-is-enough
  - sean-kelly-microservices-please-dont
last_updated: 2026-10-02
knowledge_schema: synthesis-v1
---

## Definition
A [[ModularMonolith]] is one application and deployment unit whose internal business domains have explicit, respected boundaries, owned data, and narrow public interfaces.

## Current Synthesis
Shopify's case separates two decisions that architecture debates often collapse: how modular the code is and how many units are deployed. A system can be a tightly coupled monolith, a modular monolith, well-bounded microservices, or a distributed big ball of mud. Keeping one repository, pipeline, database, and in-process call path can preserve operational simplicity, but only if internal dependencies are visible and constrained.

Bogard adds a semantic test for the label "monolith." One application and database are not intrinsically harmful when the model is cohesive and the system meets its business and operational needs. The failure condition is competing domains whose terms, information models, and interfaces interfere so strongly that change becomes difficult. A modular monolith is therefore not merely a microservice architecture waiting to be split; it can be the appropriate boundary when internal cohesion is stronger than the case for independent runtime operation.

The migration path in the source is incremental in governance even though its initial file move was a big-bang pull request. Shopify first used developer pain to justify the work, mapped code to business domains, reorganized files, defined component ownership and public APIs, measured cross-boundary calls and data associations, and planned stronger enforcement. The goal was not perfect isolation immediately; it was to make coupling legible and steadily removable while retaining one deployment unit.

The Binary Igor essay adds an infrastructure consequence rather than another boundary mechanism. When a cohesive system remains one deployment unit, or only a few services, it may not need dynamic scheduling, automatic horizontal scaling, service discovery across a large fleet, or granular team isolation. The application shape can therefore reduce the justification for Kubernetes, while leaving reliable deployment, rollback, networking, backups, observability, and reproducibility as requirements that another platform or bounded automation must still meet.

Kelly adds an extraction strategy: organize a monolith around internal services that own limited domain responsibilities and make dependencies explicit, then move a boundary onto the network only after a concrete need emerges. This treats modularity as useful design work in its own right while retaining an option—not an obligation—to extract a service after domain and workflow knowledge improve.

## Key Claims
- Modularity and domain cohesion are independent from the number of deployment units.
- A single application or database is not automatically a harmful monolith.
- One deployment can preserve repository, pipeline, database, in-process-call, and infrastructure simplicity.
- Business-domain organization reduces search and onboarding context compared with purely technical-layer organization.
- Public interfaces and data ownership are necessary for components to be more than folders.
- Dynamic and static dependency evidence can turn boundary quality into measurable work.
- Internal service modules can preserve an extraction option without paying distributed-system costs before a concrete need appears.

## Evidence
- Cohesion test: [[jimmy-bogard-my-microservices-faq]] says one application and database may be appropriate when its model is cohesive and meets business and operational needs.
- Negative monolith definition: [[jimmy-bogard-my-microservices-faq]] locates the problem in competing domains whose terms, information design, interfaces, and changes interfere.
- Architectural distinction: [[deconstructing-the-monolith-shopify-engineering]] includes Simon Brown's matrix with modularity on one axis and deployment-unit count on the other.
- Monolith benefits: [[deconstructing-the-monolith-shopify-engineering]] lists one repository, pipeline, database, infrastructure set, and direct calls as sources of lower overhead.
- Domain reorganization: [[deconstructing-the-monolith-shopify-engineering]] shows Shopify moving from models/controllers/jobs folders toward apps, billing, checkouts, taxes, and other components.
- Boundary contract: [[deconstructing-the-monolith-shopify-engineering]] says each component should expose a public API and exclusively own associated data.
- Measurement: [[deconstructing-the-monolith-shopify-engineering]] describes [[Wedge]] using CI call graphs, associations, and inheritance data to score isolation.
- Changeability: [[deconstructing-the-monolith-shopify-engineering]] reports that dependency isolation enabled replacement of a legacy tax engine.
- Infrastructure consequence: [[kubernetes-maybe-a-few-bashpython-scripts-is-enough]] argues that one or a few deployment units reduce the need for dynamic orchestration and can fit managed containers or a small reproducible VM-and-container platform.
- Extraction option: [[sean-kelly-microservices-please-dont]] recommends domain-owning internal services first and independent network services only when a demonstrated need arises.
- Workload scaling: [[sean-kelly-microservices-please-dont]] says one codebase can still run separately tuned API, front-end, and background-job clusters.

## Counterevidence & Qualifications
Shopify is one company's 2019 progress report, and the program was incomplete: full isolation, inheritance analysis, score trends, and runtime enforcement were still future work. Bogard's FAQ, Kelly's article, and the infrastructure essay are practitioner arguments without comparative evidence. None proves that a modular monolith always dominates microservices or that one deployment removes operational requirements. Kelly's internal-service recommendation also depends on discipline: modules without enforced interfaces can remain a coupled monolith. Independently operated services can provide autonomy, scaling, placement, and fault-containment benefits when boundaries are understood and the organization can bear their operational cost; a small cohesive application may need no formal modularity yet.

## What Changed
- Added internal domain services as design work that is valuable before, and may remove the need for, network extraction.
- Added independently tuned workload clusters as a scaling option that does not require separate service codebases.

## Related Concepts
- [[ServiceAutonomy]] - determines whether an internal boundary should also become an independently operated service.
- [[CDComponentization]] - component extraction can improve ownership, feedback speed, and changeability without requiring separate deployment.
- [[MicroserviceOperationalOverhead]] - a modular monolith retains boundaries while avoiding some distributed-system costs.
- [[BoundedContext]] - domain context helps define meaningful component boundaries.
- [[DistributedSystemRestraint]] - delayed distribution preserves learning until service boundaries and operational need are clearer.
- [[MonolithConsolidation]] - consolidation also reduces deployment units, but usually by reversing prior service proliferation.
- [[DomainModelDrivenData]] - component data ownership should follow domain meaning rather than arbitrary table splits.
- [[Kubernetes]] - orchestration whose benefits are less compelling when a cohesive system has few predictable deployment units.
- [[InfrastructureAsCode]] - simple topology still needs reproducible provisioning and recovery.
