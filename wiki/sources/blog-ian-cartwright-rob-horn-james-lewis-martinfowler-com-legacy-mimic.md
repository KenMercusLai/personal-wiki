---
title: "Legacy Mimic"
type: source
tags: [legacy-displacement, architecture, migration, transitional-architecture]
date: 2026-09-14
source_file: "/mnt/ken_personal_wiki/Articles/Blog - Ian Cartwright, Rob Horn, James Lewis (martinfowler.com) - Legacy Mimic.md"
---

## Summary
Ian Cartwright, Rob Horn, and James Lewis describe [[LegacyMimic]] as a transitional architecture pattern for incremental legacy replacement. When new systems cannot be cleanly isolated from old ones, a new component may need to conform to legacy interfaces, events, schemas, or semantics so unreplaced legacy processes continue working while a capability is displaced.

## Key Claims
- Incremental replacement often requires the new world to satisfy existing implicit contracts rather than immediately impose a clean target architecture.
- A [[LegacyMimic]] can provide a legacy-shaped interface over a new implementation or consume legacy interfaces used by unreplaced systems.
- Mimics commonly use services, adapters, translators, and facades, and often realize [[AntiCorruptionLayer]] forces.
- [[LegacyMimic]] is transitional: unlike an enduring [[AntiCorruptionLayer]] around an external partner, it should disappear after displacement is complete.
- [[EventInterception]] can be a service-providing mimic when it consumes legacy events while forwarding work into a new system.
- Metrics replication into a legacy reporting database can be a service-consuming mimic when it conforms to legacy schema and semantics.

## Key Quotes
> "keep the lights on" - reason the new system may need to support legacy interactions during transition

> "Both of these components will not endure within the target architecture of the system" - qualification that the example mimics are transitional

## Connections
- [[IanCartwright]] - coauthor of the article.
- [[RobHorn]] - coauthor of the article.
- [[JamesLewis]] - coauthor of the article.
- [[LegacyMimic]] - central legacy-displacement pattern explained by the source.
- [[TransitionalArchitecture]] - migration context in which temporary components keep old and new systems cooperating.
- [[LegacyDisplacement]] - broader modernization problem of replacing legacy capabilities incrementally.
- [[AntiCorruptionLayer]] - related adapter pattern that protects a model from external or legacy semantics.
- [[EventInterception]] - example service-providing mimic used to feed sales events into a new logistics system.
- [[ExtractValueStreams]] - sequencing approach used in the example to move logistics out of a monolith.
- [[CapabilityOrientedIntegration]] - related idea that implementation complexity can be hidden behind fit-for-purpose interfaces.

## Visual Evidence
- The first inspected diagram shows a monolithic legacy system supporting Sales, Logistics, and Business Performance, plus a separate Logistics Partner System.
- The second inspected diagram shows Logistics extracted into a New Logistics System while Sales and Business Performance remain with the legacy system. An Event Interceptor sends legacy sales activity to the new logistics capability, a Legacy Mimic writes back toward the legacy reporting database, and an Anti-Corruption Layer mediates calls to the Logistics Partner System.
- The inspected sequence diagram distinguishes a service-providing mimic, labeled Event Interceptor Mimic, from a service-consuming mimic, labeled Metrics Mimic. The sequence records a sale in the legacy database, publishes and consumes a sale message, processes the sale in the new logistics system, uses the new-world ACL to dispatch to the partner system, and updates legacy metrics back into the legacy database.

## Contradictions
- No direct contradiction found. The source complements [[CapabilityOrientedIntegration]] by showing that clean target boundaries may require temporary legacy-shaped adapters during displacement.
