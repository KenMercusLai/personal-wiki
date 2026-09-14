---
title: "Capability-Oriented Integration"
type: concept
tags: [architecture, api, integration, enterprise-architecture]
sources:
  - blog-brandon-byars-martinfowler-com-you-cant-buy-integration
last_updated: 2026-09-14
knowledge_schema: synthesis-v1
---

## Definition
[[CapabilityOrientedIntegration]] is an integration design posture that exposes stable business capabilities through clean interfaces instead of exposing the quirks or names of underlying systems.

## Current Synthesis
The Byars source argues that modern digital integration should focus on capabilities rather than systems. API consumers usually want to create an order, evaluate eligibility, retrieve plans, or provision service; they should not need to know whether data comes from SAP, Salesforce, a mainframe, or another system of record.

Capability-oriented integration accepts that implementation may become more complex so the interface can become simpler. Transformations, orchestration, caching, and legacy containment are not eliminated; they are moved behind a capability boundary where a knowledgeable team can evolve them without forcing every consumer to relearn downstream system details.

## Key Claims
- APIs should be designed from the consumer's perspective rather than the source system's structure.
- Clean capability interfaces hide implementation details, including source systems and programming languages.
- Legacy complexity should be adapted behind the interface instead of exported to every new consumer.
- Capability interfaces must evolve with users over time, making integration a programming-over-time problem.
- Diagrams should make capability boundaries visible rather than foregrounding integration tools or implementation languages.

## Evidence
- Consumer perspective: [[blog-brandon-byars-martinfowler-com-you-cant-buy-integration]] says users do not need an SAP API; they need access to capabilities such as order management.
- Complexity hiding: [[blog-brandon-byars-martinfowler-com-you-cant-buy-integration]] compares clean integration interfaces to simple product interfaces backed by complex implementation.
- Legacy adaptation: [[blog-brandon-byars-martinfowler-com-you-cant-buy-integration]] describes a telecom eCommerce API redesigned around plans, eligibility, ordering, and provisioning instead of call-center transaction and billing-system details.
- Diagram evidence: [[blog-brandon-byars-martinfowler-com-you-cant-buy-integration]] shows a web channel API calling capability APIs rather than exposing downstream system mechanics.
- User evolution: [[blog-brandon-byars-martinfowler-com-you-cant-buy-integration]] warns that APIs which fail to evolve with users become point-in-time integrations in API clothing.

## Counterevidence & Qualifications
Capability abstraction can require more up-front architectural skill and implementation work than direct system integration. Systems of record, ERPs, and legacy billing platforms may resist clean boundaries, and some internal or administrative use cases may still need system-specific APIs. The source's recommendation is a strategic default, not a claim that every technical endpoint must hide every implementation detail.

## What Changed
- Created the concept from Byars's principle to abstract the capability rather than the system.

## Related Concepts
- [[IntegrationStrategy]] - capability orientation is the strategic center of the article.
- [[ChannelAPI]] - channel APIs adapt capability interfaces to a specific consumer or partner context.
- [[APIErrorHandling]] - API design includes recoverable failure interfaces, not just happy-path capability calls.
- [[ProductManagement]] - the article treats APIs as products designed around user needs.
- [[TechnologyStackComplexity]] - capability boundaries contain complexity created by multiple systems.
