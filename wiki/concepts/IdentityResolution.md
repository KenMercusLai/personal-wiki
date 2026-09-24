---
title: "Identity Resolution"
type: concept
tags: [identity, advertising, privacy, adtech]
sources:
  - a-comprehensive-guide-to-digital-marketing-and-analytics
last_updated: 2026-09-24
knowledge_schema: synthesis-v1
---

## Definition
[[IdentityResolution]] is the process of connecting multiple device, browser, cookie, or partner identifiers to a more durable person-level identity.

## Current Synthesis
The source describes a third-party advertising model in which an identity provider places or recognizes cookies across digital partners, observes the same identifier at a partner where a visitor supplies personally identifiable information, and then links the wider cookie history to that record. The resulting continuity can improve audience recognition after individual cookies change or disappear, but it converts pseudonymous browsing traces into directly attributable profiles and therefore raises a stronger privacy, consent, security, and purpose-limitation boundary than ordinary campaign measurement.

## Key Claims
- Identity resolution joins fragmented browser or partner identifiers into one person-level view.
- A deterministic link can arise when a visitor supplies personally identifiable information at one participating service.
- Partner coverage lets an identity provider propagate that link across previously pseudonymous activity.
- Durable identity can improve targeting continuity beyond the lifespan of any one cookie.
- The same durability materially increases surveillance, misuse, breach, and governance risk.

## Evidence
- Cross-partner recognition: [[a-comprehensive-guide-to-digital-marketing-and-analytics]] and its retained flow diagram show an identity-resolution company recognizing one cookie across multiple digital partners.
- PII linkage: [[a-comprehensive-guide-to-digital-marketing-and-analytics]] shows a participating service connecting that cookie to submitted personal information.
- Continuity objective: [[a-comprehensive-guide-to-digital-marketing-and-analytics]] contrasts frequently deleted cookies with person-level information that is intended to remain stable.

## Counterevidence & Qualifications
The source is a conceptual 2018 account built around third-party cookies. It does not cover later browser restrictions, consent frameworks, privacy regulation, mobile identifier limits, data clean rooms, probabilistic matching error, user access and deletion rights, or governance controls. Its description explains the mechanism but does not establish accuracy, legitimacy, or acceptable use.

## What Changed
- Created the concept from the source's inspected identity-linkage diagram and privacy warning.

## Related Concepts
- [[AudienceTargeting]] - consumes identity-linked attributes to construct deployable audience segments.
- [[DataManagementPlatform]] - may aggregate and activate identifiers and associated audience data.
- [[ProgrammaticAdvertising]] - uses resolved audience signals during automated media buying.
- [[BehavioralData]] - supplies the activity traces joined to an identity.
- [[LocationDataPrivacy]] - shares the risk that seemingly indirect traces can identify and profile a person.
