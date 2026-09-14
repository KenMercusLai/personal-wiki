---
title: "Channel API"
type: concept
tags: [api, architecture, integration, b2b]
sources:
  - blog-brandon-byars-martinfowler-com-you-cant-buy-integration
last_updated: 2026-09-14
knowledge_schema: synthesis-v1
---

## Definition
[[ChannelAPI]] is an API shaped for a specific channel, consumer group, or partner context while hiding broader downstream system complexity behind a cleaner interface.

## Current Synthesis
Byars prefers "channel API" as a broader and clearer name than "experience API" or "backend for frontend." The pattern is useful when a consumer needs a tailored surface that can evolve at a different pace from core capabilities, narrow the exposed attack surface, or absorb partner-specific integration formats.

In the article's B2B integration case, channel APIs let organizations keep a common external or channel-specific interface while using integration DSLs as inexpensive adapters for partner FTP, EDI, EBCDIC, file, or legacy-system differences. In the telecom example, a web eCommerce channel API calls capability APIs for plans, eligibility, ordering, and provisioning so the web team does not inherit call-center or billing-system abstractions.

## Key Claims
- Channel APIs optimize an interface for a specific consumer context rather than mirror underlying systems.
- Channel APIs can evolve independently from underlying capability implementations.
- Narrow channel-specific surfaces can reduce consumer complexity and security exposure.
- Integration DSLs can be useful behind channel APIs as partner or system adapters.
- Channel APIs should still avoid becoming ETL workflows dressed as APIs.

## Evidence
- Naming and scope: [[blog-brandon-byars-martinfowler-com-you-cant-buy-integration]] says "channel API" better covers B2B and non-frontend concerns than "experience API" or "backend for frontend."
- Evolution rate: [[blog-brandon-byars-martinfowler-com-you-cant-buy-integration]] says channel-specific APIs allow channels to evolve at different rates from underlying capabilities.
- B2B adapter diagram: [[blog-brandon-byars-martinfowler-com-you-cant-buy-integration]] shows partner-side DSL adapters feeding a common channel API.
- Telecom diagram: [[blog-brandon-byars-martinfowler-com-you-cant-buy-integration]] shows web eCommerce calling a web channel API, which calls clean plan, eligibility, ordering, and provisioning APIs.
- ETL warning: [[blog-brandon-byars-martinfowler-com-you-cant-buy-integration]] warns that system/process/experience layers can become extract-transform-load in API clothing when implementation concerns dominate.

## Counterevidence & Qualifications
The article supports the channel API pattern but warns against treating it as another rigid layer in a vendor architecture. If the channel API merely forwards source-system leakage or encodes implementation-driven ETL steps, it loses the consumer-centered benefit the pattern is meant to provide.

## What Changed
- Created the concept from Byars's preferred framing for consumer- or partner-specific API surfaces.

## Related Concepts
- [[CapabilityOrientedIntegration]] - channel APIs should sit over clean capability interfaces.
- [[IntegrationDSL]] - DSLs can act as adapters behind a channel API.
- [[IntegrationStrategy]] - channel API design is one strategy for preserving agility while serving varied consumers.
- [[APIErrorHandling]] - channel APIs also need failure contracts that consumers can recover from.
- [[ProductUserSegmentation]] - channel APIs express different needs for different consumer segments.
