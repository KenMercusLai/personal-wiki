---
title: "API Backward Compatibility"
type: concept
tags: [api, reliability, software-engineering, platform]
sources:
  - cs183c-session-11-patrick-collison-stripe-blitzscaling-class-notes-and-essays-medium
last_updated: 2026-09-25
knowledge_schema: synthesis-v1
---

## Definition
[[APIBackwardCompatibility]] is the practice of evolving an API while preserving the behavior expected by clients on supported older versions and giving the remaining users of deprecated versions a controlled migration path.

## Current Synthesis
The Stripe account treats compatibility as the bridge between infrastructure innovation and customer reliability. A translation layer lets customers remain on recent API versions while the provider changes the underlying product; very old versions can then be retired through a narrow, explicit migration rather than a surprise breaking change. This is a source-scoped operating pattern, not comparative proof that translation layers are always cheaper or safer than long-lived versions, feature negotiation, or coordinated client upgrades.

## Key Claims
- Infrastructure providers must treat compatibility as part of reliability because customer systems depend on stable behavior.
- A translation layer can decouple internal product evolution from the API version a customer uses.
- Deprecation becomes safer when the provider identifies the remaining users and coordinates migration directly.
- Compatibility mechanisms create their own maintenance and testing burden and therefore need an explicit support boundary.

## Evidence
- Translation layer: [[cs183c-session-11-patrick-collison-stripe-blitzscaling-class-notes-and-essays-medium]] says Stripe built a layer that kept customers on any recent API version working.
- Narrow deprecation: [[cs183c-session-11-patrick-collison-stripe-blitzscaling-class-notes-and-essays-medium]] says Stripe approached the three remaining users of a 2010 API version before retiring it.
- Reliability objective: [[cs183c-session-11-patrick-collison-stripe-blitzscaling-class-notes-and-essays-medium]] frames version handling as a way to add capabilities without becoming unreliable.

## Counterevidence & Qualifications
The interview gives no architecture, defect rate, compatibility-test strategy, support cost, migration duration, or customer account of the deprecation. The three-user example shows a tractable tail, not what works when an old contract has thousands of clients or legal and safety constraints.

## What Changed
- Created the concept from Stripe's translation-layer and direct-deprecation example.

## Related Concepts
- [[SystemReliability]] - stable API behavior is one layer of service dependability.
- [[APIEcosystemGovernance]] - version and deprecation policy shape developer trust in a platform.
- [[DeveloperExperience]] - predictable upgrades reduce integration and maintenance friction.
- [[AntiCorruptionLayer]] - translation layers isolate one interface model from another.
