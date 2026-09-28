---
title: "Identity Resolution"
type: concept
tags: [identity, advertising, privacy, adtech]
sources:
  - a-comprehensive-guide-to-digital-marketing-and-analytics
  - google-data-collection-research-digital-content-next
last_updated: 2026-09-28
knowledge_schema: synthesis-v1
---

## Definition
[[IdentityResolution]] is the process of connecting multiple device, browser, cookie, or partner identifiers to a more durable person-level identity.

## Current Synthesis
The sources describe two routes from pseudonymous activity to a person. In the third-party advertising model, an identity provider recognizes cookies across digital partners and links the wider history when one partner receives personally identifiable information. In Google's vertically integrated model, an Android device can send device identifiers and a browser can present a DoubleClick cookie, while a signed-in Google application supplies the durable account boundary that joins them. The resulting continuity can improve recognition after individual identifiers change or disappear, but it converts passive browsing, application, and device traces into directly attributable profiles and therefore raises a stronger privacy, consent, security, and purpose-limitation boundary than ordinary campaign measurement.

## Key Claims
- Identity resolution joins fragmented browser or partner identifiers into one person-level view.
- A deterministic link can arise when a visitor supplies personally identifiable information at one participating service.
- Partner coverage lets an identity provider propagate that link across previously pseudonymous activity.
- A platform controlling devices, applications, accounts, and advertising infrastructure can resolve identity without relying only on an independent third-party broker.
- Durable identity can improve targeting continuity beyond the lifespan of any one cookie.
- The same durability materially increases surveillance, misuse, breach, and governance risk.

## Evidence
- Cross-partner recognition: [[a-comprehensive-guide-to-digital-marketing-and-analytics]] and its retained flow diagram show an identity-resolution company recognizing one cookie across multiple digital partners.
- PII linkage: [[a-comprehensive-guide-to-digital-marketing-and-analytics]] shows a participating service connecting that cookie to submitted personal information.
- Continuity objective: [[a-comprehensive-guide-to-digital-marketing-and-analytics]] contrasts frequently deleted cookies with person-level information that is intended to remain stable.
- Device-to-account linkage: [[google-data-collection-research-digital-content-next]] says Android can pass device-level identification to Google servers, allowing an advertising identifier to be associated with a Google identity.
- Cookie-to-account linkage: [[google-data-collection-research-digital-content-next]] says a DoubleClick cookie from third-party browsing can be associated with a Google account when a Google application is used in the same browser.

## Counterevidence & Qualifications
Both sources are conceptual or research-summary accounts from 2018. They do not cover later browser restrictions, consent frameworks, privacy regulation, mobile identifier limits, data clean rooms, probabilistic matching error, user access and deletion rights, or current Google controls. Their descriptions explain plausible mechanisms but do not independently establish every join's accuracy, prevalence, legitimacy, retention, or use.

## What Changed
- Expanded identity resolution from cross-partner cookie matching to vertically integrated device, browser, advertising, and signed-in account linkage.
- Added passive platform signals as inputs while preserving uncertainty about prevalence, retention, and downstream use.

## Related Concepts
- [[AudienceTargeting]] - consumes identity-linked attributes to construct deployable audience segments.
- [[DataManagementPlatform]] - may aggregate and activate identifiers and associated audience data.
- [[ProgrammaticAdvertising]] - uses resolved audience signals during automated media buying.
- [[BehavioralData]] - supplies the activity traces joined to an identity.
- [[LocationDataPrivacy]] - shares the risk that seemingly indirect traces can identify and profile a person.
