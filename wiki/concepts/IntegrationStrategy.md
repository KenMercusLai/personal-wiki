---
title: "Integration Strategy"
type: concept
tags: [architecture, integration, enterprise-architecture, api]
sources:
  - blog-brandon-byars-martinfowler-com-you-cant-buy-integration
last_updated: 2026-09-14
knowledge_schema: synthesis-v1
---

## Definition
[[IntegrationStrategy]] is the architectural discipline of deciding how systems, teams, and external parties expose and consume business capabilities through durable interfaces.

## Current Synthesis
The Byars source argues that integration strategy is often weakened by a category mistake: buying an integration platform is mistaken for buying integration. Commercial products can reduce some implementation effort, but the strategic work is creating clean interfaces that let business capabilities evolve without every consumer absorbing downstream system complexity.

The article reframes integration as an agility problem. Point-to-point or point-in-time connections can be quick locally, yet they leave an organization with many brittle lines between systems. A stronger integration strategy invests in API products, capability boundaries, testing, observability, and programming-over-time practices that may slow initial delivery but increase long-term change speed.

## Key Claims
- Integration cannot be outsourced to a product because the hard part is shaping capability interfaces and evolution paths.
- Tool mandates can turn architectural strategy into vendor product strategy.
- The hidden cost of integration often lives in the lines between application boxes, not only in the boxes themselves.
- Strategic integration optimizes organizational agility over time rather than first-connection speed alone.
- General-purpose languages are usually better for interface evolution because they support diffing, modularity, testing, observability, security tooling, and larger ecosystems.

## Evidence
- Category error: [[blog-brandon-byars-martinfowler-com-you-cant-buy-integration]] says integration products are programming environments for building integrations, not products that solve the business integration problem directly.
- Hidden cost: [[blog-brandon-byars-martinfowler-com-you-cant-buy-integration]] uses architecture diagrams to show integration lines becoming a primary cost driver over time.
- Vendor strategy risk: [[blog-brandon-byars-martinfowler-com-you-cant-buy-integration]] warns architects not to let a vendor's product strategy become their architectural strategy.
- Programming-over-time: [[blog-brandon-byars-martinfowler-com-you-cant-buy-integration]] argues general-purpose languages handle change history, modularity, parallel work, test loops, ecosystem tooling, and operations better than low-code integration runtimes.
- Agility payoff: [[blog-brandon-byars-martinfowler-com-you-cant-buy-integration]] uses the digital-capabilities-over-time figure to argue that clean interfaces can become an accelerator for digital transformation.

## Counterevidence & Qualifications
The source does not claim integration products have no value. It explicitly supports buying middleware infrastructure, API gateways, workflow tools, connectors, analytics databases, and container orchestration when they are bounded to implementation concerns. The argument is strongest for complex, evolving enterprise interfaces; slow-moving partner integrations or simple workflows may justify more direct use of integration DSLs.

## What Changed
- Created the concept from Byars's distinction between buying integration tools and designing integration architecture.

## Related Concepts
- [[CapabilityOrientedIntegration]] - names the capability-interface orientation Byars recommends.
- [[IntegrationDSL]] - commercial tool category that can support but should not own integration strategy.
- [[SourceDiagramIsomorphism]] - low-code tool structure that affects programming-over-time concerns.
- [[ChannelAPI]] - channel-specific interface pattern used to protect consumers from downstream complexity.
- [[TechnologyStackComplexity]] - integration lines multiply operational and reasoning burden across systems.
- [[DeveloperExperience]] - integration strategy depends on tools being diffable, testable, observable, and maintainable.
