---
title: "Microservices - Please, don't"
type: source
tags: [microservices, monolith, software-architecture, distributed-systems]
date: 2016-09-14
source_file: "/mnt/ken_personal_wiki/Articles/Sean Kelly - Microservices Please don't.md"
---

## Summary
[[SeanKelly]] argues that microservices are not inherently bad, but that adopting them before a team understands its domain, workflows, failure modes, monitoring, and business case can replace local code problems with distributed-system and organizational problems. He recommends first creating well-defined internal service modules inside a monolith, then extracting independently deployed services only when a demonstrated need justifies network, transaction, testing, deployment, and coordination costs.

## Key Claims
- A network boundary does not create clean code; explicit internal modules can establish domain ownership and dependencies without adding remote failure modes.
- Distributed workflows require decisions about call ordering, partial failure, compensation, and recovery, so transactions spanning services are not automatically simpler than local transactions.
- Reported microservice performance gains can conflate service decomposition with rewrites in faster languages, while network calls add latency and I/O that co-resident calls avoid.
- Many services increase local-development setup, integration-test scope, system comprehension, cross-team coordination, and the risk that ownership fragments into “not my problem” behavior.
- Horizontal scaling does not require microservices: one monolithic codebase can run separate API, front-end, and background-worker clusters tuned and scaled for different workloads.
- Microservices become more credible when domain boundaries and request paths are understood, failures and recovery are observable, and the organization can demonstrate technical and business value.
- A [[ModularMonolith]] can preserve a later extraction path by modeling internal services before committing to distributed deployment.

## Key Quotes
> "You don't need to introduce a network boundary as an excuse to write better code" - on separating code quality from deployment topology.

> "When you're ready as an engineering organization" - on the central adoption gate.

## Connections
- [[SeanKelly]] - author drawing on experience with a legacy-monolith decomposition effort.
- [[MicroserviceOperationalOverhead]] - network calls, local environments, integration tests, and cross-team work expand the cost of service proliferation.
- [[ModularMonolith]] - internal service modules are presented as a lower-cost precursor and alternative to distributed services.
- [[MicroserviceDataBoundaries]] - domain understanding and distributed transaction recovery are prerequisites for safe service boundaries.
- [[DistributedSystemRestraint]] - the article recommends delaying distribution until technical, organizational, and business evidence justifies it.
- [[ServiceObservability]] - monitoring request paths and failures is part of microservice readiness.

## Contradictions
- The article qualifies microservice benefits rather than denying them: it accepts independent workload scaling and eventual extraction where domain knowledge, operational readiness, and demonstrated value support the move.
- Its claim that a monolith can be scaled outward challenges arguments that microservices are required for horizontal scaling, but does not establish that monoliths provide equivalent fault isolation, release autonomy, placement, or team independence.
- This is a 2016 practitioner argument adapted from a talk. It provides no measured latency, delivery, incident, staffing, or business outcomes, and several conclusions rely on the author's experience rather than a comparative study.
