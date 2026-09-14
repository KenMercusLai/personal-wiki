---
title: "Anti-Corruption Layer"
type: concept
tags: [software-architecture, domain-driven-design, integration]
sources:
  - blog-ian-cartwright-rob-horn-james-lewis-martinfowler-com-legacy-mimic
last_updated: 2026-09-14
knowledge_schema: synthesis-v1
---

## Definition
[[AntiCorruptionLayer]] is an isolating translation layer that lets a system interact with another model or interface without allowing that external model to compromise its own domain model.

## Current Synthesis
The Legacy Mimic source uses Eric Evans's Domain-Driven Design pattern to explain the forces behind legacy mimics. Both patterns use services, adapters, translators, and facades to bridge model boundaries. The difference is lifecycle and intent: a [[LegacyMimic]] temporarily conforms to legacy expectations during displacement, while an anti-corruption layer can be an enduring target-architecture boundary.

The logistics example makes the distinction explicit. The event interceptor and metrics mimic are temporary legacy-compatibility components. The new logistics system's anti-corruption layer toward the external Logistics Partner System is expected to endure because it protects the new logistics domain model from the partner system's model.

## Key Claims
- Anti-corruption layers translate between models while protecting a system's own domain language.
- Legacy mimics often realize anti-corruption-layer mechanics during migration.
- The same adapter mechanisms can be transitional or enduring depending on the dependency they mediate.
- External partner integration can justify a permanent anti-corruption layer even after legacy displacement ends.

## Evidence
- Pattern relationship: [[blog-ian-cartwright-rob-horn-james-lewis-martinfowler-com-legacy-mimic]] says a Legacy Mimic often realizes the anti-corruption layer pattern from Domain-Driven Design.
- Mechanisms: [[blog-ian-cartwright-rob-horn-james-lewis-martinfowler-com-legacy-mimic]] says both patterns commonly use services, adapters, translators, and facades.
- Enduring boundary: [[blog-ian-cartwright-rob-horn-james-lewis-martinfowler-com-legacy-mimic]] says the logistics partner ACL endures because the new logistics model should not be compromised by the external partner's model.
- Visual evidence: [[blog-ian-cartwright-rob-horn-james-lewis-martinfowler-com-legacy-mimic]] shows a New World ACL between the New Logistics System and the external Logistics Partner System.

## Counterevidence & Qualifications
This page is currently grounded only in the Legacy Mimic article's summary of the pattern, not in Evans's full Domain-Driven Design treatment. The source uses the anti-corruption layer mostly as a contrast against transitional mimic components.

## What Changed
- Created the concept from the article's comparison between Legacy Mimic and enduring external-system translation.

## Related Concepts
- [[LegacyMimic]] - shares translation mechanics but is explicitly transitional.
- [[TransitionalArchitecture]] - temporary layers should be distinguished from enduring model-protection layers.
- [[CapabilityOrientedIntegration]] - both protect consumers from source-system details.
- [[IntegrationStrategy]] - anti-corruption layers are one way to contain integration complexity.
- [[LegacyDisplacement]] - displacement may use anti-corruption mechanics to bridge old and new systems.
