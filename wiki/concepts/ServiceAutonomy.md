---
title: "Service Autonomy"
type: concept
tags: [microservices, software-architecture, coupling, service-boundaries]
sources:
  - jimmy-bogard-my-microservices-faq
last_updated: 2026-10-01
knowledge_schema: synthesis-v1
---

## Definition
[[ServiceAutonomy]] is the degree to which a software boundary can be owned, built, deployed, run, secured, changed, and recovered independently while controlling its information and honoring explicit external contracts.

## Current Synthesis
Bogard makes autonomy the defining property of a service and microservice size a consequence rather than an input. The smallest viable service boundary depends on the domain, people, technology, and business goals. If a unit cannot run without coordinated behavior from neighboring units, or if its communication protocol forces lockstep availability and change, it may be a module inside a larger service even when separately deployed.

Autonomy is multidimensional rather than binary. Independent deployment is insufficient without operational responsibility, information ownership, access protection, failure containment, and contracts that can evolve without exposing internal state directly. Conversely, one application and database need not be a harmful monolith when its model is cohesive and meets the organization's business and operational needs.

## Key Claims
- Service size should be derived from the smallest boundary that can preserve meaningful autonomy in context.
- Independent deployment is necessary but not sufficient; a service must also run, protect information, handle failure, and meet operational objectives independently.
- Technology and topology labels do not prove autonomy: containers, languages, protocols, repositories, and databases are supporting choices.
- Process, temporal, data, and change coupling can reveal that separately deployed units belong to one larger service boundary.
- External events and contracts should be designed independently from internal state representations so each can evolve for its own reasons.
- Microservices are justified when finer autonomous boundaries address a demonstrated delivery constraint and the wider value stream can support the resulting service count.

## Evidence
- Defining boundary: [[jimmy-bogard-my-microservices-faq]] defines a microservice as a service designed toward the smallest autonomous boundary.
- Operational responsibility: [[jimmy-bogard-my-microservices-faq]] requires independent ownership, build, deployment, operation, security, information protection, and failure handling.
- Coupling test: [[jimmy-bogard-my-microservices-faq]] uses RPC-only communication and repository changes forced across services as signs that autonomy has been lost.
- Contract separation: [[jimmy-bogard-my-microservices-faq]] warns that directly exposing internal event-sourced changes couples public subscribers to an internal model.
- Adoption gate: [[jimmy-bogard-my-microservices-faq]] asks whether service size is actually bottlenecking delivery before treating microservices as a suitable response.

## Counterevidence & Qualifications
The source offers a coherent practitioner definition rather than an empirical autonomy metric. Some systems can tolerate synchronous dependencies, coordinated releases, shared data, or a monorepo while retaining enough independent ownership for their goals. Strictly classifying every RPC-dependent unit as a module may understate degrees of autonomy, graceful degradation, or the difference between ordinary dependency and mandatory lockstep operation.

## What Changed
- Established autonomy as a multidimensional service-boundary test rather than a synonym for separate deployment.
- Distinguished defining architecture properties from enabling technologies and repository topology.
- Added delivery-value-stream need and organizational capacity as adoption gates.

## Related Concepts
- [[MicroservicePlatformEngineering]] - supplies shared controls that can make independently operated services repeatable and safe.
- [[MicroserviceDataBoundaries]] - gives autonomy an information-ownership and transaction boundary.
- [[MicroserviceOperationalOverhead]] - increases as more autonomous units acquire separate operational obligations.
- [[ModularMonolith]] - can preserve domain modularity when independent runtime operation is unnecessary or too costly.
- [[EventDrivenConsistency]] - coordinates independently owned state through durable facts rather than shared transactions.
- [[DistributedSystemRestraint]] - delays distribution until autonomy benefits justify its coordination and operating cost.
