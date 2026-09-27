---
title: "The Opportunities Microservices Provide at Uber Engineering"
type: source
tags: [microservices, software-architecture, reliability, uber]
date: 2016-04-20
source_file: "/mnt/ken_personal_wiki/Articles/Emily Reinhold - The Opportunities Microservices Provide at Uber Engineering.md"
---

## Summary
[[EmilyReinhold]] uses [[Tincup]], [[Uber]]'s currency and exchange-rate service, to describe how a rapidly growing organization tried to make microservice ownership repeatable. The account combines design review, application and persistence separation, globally replicated data, asynchronous I/O, service discovery, typed interfaces, load testing, container isolation, and controlled disruption into a [[MicroservicePlatformEngineering]] approach. Its strongest lesson is conditional: service autonomy depends on shared governance and operational guardrails, while consumer migration and early testing remain substantial work.

## Key Claims
- New-service RFCs can improve designs, expose duplicate work, and create collaboration opportunities before implementation begins.
- Tincup separated application logic into an MVCS service layer so persistence could change without rewriting the business rules.
- Replacing PostgreSQL with Uber's globally replicated UDR datastore supported the company's all-active, multi-data-center goal for currency and exchange-rate data.
- Tornado's non-blocking I/O reduced the risk that a degraded dependency would starve synchronous workers and spread failure to callers.
- TChannel over Hyperbahn supplied name-based service discovery, unhealthy-host removal, rate limiting, and circuit breaking, while Thrift supplied strict, backward-compatible service contracts.
- Hailstorm load tests, uContainer resource isolation, and uDestroy failure injection moved capacity and resilience testing into the production-readiness process.
- Consumer migration remained slow; Uber recommended examples and hands-on support, while using a small service to learn the new stack and investing early in unit, integration, and load tests.

## Key Quotes
> "Migrating consumers is a long, slow process, so make it as easy as you can." - on the coordination cost after a service is built

> "Load test as early and often as you can." - on discovering capacity limits before launch

## Connections
- [[EmilyReinhold]] - author of the Uber Engineering account.
- [[Uber]] - organization migrating a monolith toward several hundred microservices.
- [[Tincup]] - currency and exchange-rate service used as the implementation case.
- [[MicroservicePlatformEngineering]] - shared governance, networking, contracts, testing, isolation, and resilience controls that make service ownership repeatable.
- [[MicroserviceOperationalOverhead]] - the source shows both the migration cost and the platform investment used to contain service proliferation.
- [[ChaosEngineering]] - uDestroy deliberately disrupted services so teams could find resilience gaps.
- [[MicroserviceDataBoundaries]] - MVCS and UDR separated business logic from persistence and supported a globally available data boundary.
- [[SystemReliability]] - asynchronous I/O, routing, circuit breaking, load testing, containers, and failure injection form a layered reliability approach.

## Contradictions
- The source qualifies warnings against microservice proliferation by showing a large organization investing in governance and platform capabilities to make hundreds of services operable; it does not show that the same architecture is appropriate for smaller teams.
- This is a first-party 2016 implementation account. It supplies no comparative delivery metrics, incident rates, load-test results, migration duration, operating cost, or evidence that every named control worked as intended at fleet scale.
- The article's Thrift guidance treats backward compatibility as non-breaking additions until consumers migrate, but it does not cover schema-evolution edge cases, semantic compatibility, version negotiation, or deprecation enforcement.
