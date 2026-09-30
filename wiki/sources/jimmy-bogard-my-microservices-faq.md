---
title: "My Microservices FAQ"
type: source
tags: [microservices, software-architecture, service-autonomy, coupling]
date: 2018-02-15
source_file: "/mnt/ken_personal_wiki/Articles/Jimmy Bogard - My Microservices FAQ.md"
---

## Summary
[[JimmyBogard]] defines a microservice as the smallest contextually viable [[ServiceAutonomy|autonomous service boundary]], not as a container, language, repository layout, or communication technology. A service must be independently owned, built, deployed, and run; protect and control its information; expose contracts; and contain failure without corrupting that information. The FAQ uses that test to distinguish services from modules, cohesive single applications from monoliths, and independent communication from coupling disguised as distribution.

## Key Claims
- Microservice size is not a fixed code, team, or deployment measure; it is the smallest boundary that can still preserve service autonomy in a particular domain, organization, technology stack, and business context.
- Containers, programming languages, REST, messaging, streams, queues, and repository layouts may enable an architecture but do not determine whether software is a microservice.
- A single application and database are not automatically a monolith; the negative condition is the coupling of competing domain models until terms, information design, interfaces, and changes interfere with one another.
- A unit is too small to be a service when it cannot run independently and is better understood as a module, function, or data store.
- Synchronous RPC-only communication can create process and temporal coupling strong enough that nominal services are really modules inside a larger service boundary.
- External contracts should not directly expose internal state changes because internal representations and public obligations evolve for different reasons and at different rates.
- Microservices are worth considering when insufficiently small service boundaries are a demonstrated bottleneck in the software-delivery value stream, not merely because the style is fashionable.

## Key Quotes
> "A microservice is a service with a design focus towards the smallest autonomous boundary." - Bogard's central definition.

> "Repository boundaries are (somewhat) orthogonal to service boundaries." - on separating source-control organization from runtime autonomy.

## Connections
- [[JimmyBogard]] - author presenting the FAQ as contextual architecture guidance rather than a technology prescription.
- [[ServiceAutonomy]] - the defining test for whether a software unit is a service and how small it can safely become.
- [[MicroservicePlatformEngineering]] - shared platform capabilities may remove technical barriers to autonomous operation but do not create autonomy by themselves.
- [[ModularMonolith]] - a cohesive single application can preserve domain boundaries without becoming independently deployed services.
- [[MicroserviceDataBoundaries]] - information ownership and protection are necessary parts of an autonomous service boundary.
- [[EventDrivenConsistency]] - one possible inter-service coordination approach, preferred by Bogard but explicitly not universal.
- [[MicroserviceOperationalOverhead]] - smaller autonomous boundaries usually produce more services and affect the entire delivery chain.
- [[DevOpsCulture]] - microservice adoption generally requires broader ownership and production responsibility, though tooling and job titles are insufficient.

## Contradictions
- The source qualifies technology-centered microservice accounts: containers, REST, asynchronous messaging, and separate repositories can support independent services, but none proves that the resulting units can operate autonomously.
- It sharpens rather than contradicts [[ModularMonolith]]: one application is not a harmful monolith when its model remains cohesive and it meets business and operational needs.
- The FAQ is a concise 2018 practitioner definition, not an empirical comparison. It supplies no measurements, implementation case, migration costs, or operational outcomes, and its claim that RPC-only units cease to be services depends on how strictly autonomy is interpreted.
