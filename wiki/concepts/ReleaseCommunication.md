---
title: "Release Communication"
type: concept
tags: [product-communication, release-notes, mobile-apps, feature-adoption]
sources:
  - its-time-to-get-rid-of-traditional-release-notes-colm-doyle-medium
last_updated: 2026-09-30
knowledge_schema: synthesis-v1
---

## Definition
[[ReleaseCommunication]] is the practice of explaining product changes to the users who can encounter them through channels and timing suited to their actual experience.

## Current Synthesis
The source separates build documentation from feature introduction. In consumer mobile software, a shipped binary may expose different capabilities by feature flag, account entitlement, server state, or user behavior, so one App Store note cannot reliably describe every person's next session. Auto-updating further weakens the store page as the only communication surface.

The proposed alternative is contextual in-product communication: introduce a feature near the place and moment it can be used, and connect the message to measurable response and feedback. This is best understood as channel specialization rather than a case for deleting all release records. Public notes, technical changelogs, support documentation, audit trails, and in-app guidance can serve different audiences and obligations.

## Key Claims
- Release communication should correspond to the experience available to a particular user rather than assuming every installed build behaves identically.
- App Store notes are a weak primary feature-introduction surface when updates happen automatically or users do not revisit the store listing.
- Contextual in-app guidance can connect an explanation directly to the relevant feature and next action.
- Instrumented prompts can create feedback and response data, but those measures do not automatically establish comprehension or value.
- Consumer feature communication does not replace versioned documentation needed by developers, support teams, regulated environments, or users who need a durable record.

## Evidence
- Experience variability: [[its-time-to-get-rid-of-traditional-release-notes-colm-doyle-medium]] identifies APIs, feature flags, paid entitlements, and different usage patterns as reasons users of the same mobile build may see different capabilities.
- Store-channel weakness: [[its-time-to-get-rid-of-traditional-release-notes-colm-doyle-medium]] argues that auto-updates and unformatted store text reduce the reach and explanatory value of traditional notes.
- Contextual alternative: [[its-time-to-get-rid-of-traditional-release-notes-colm-doyle-medium]] recommends in-app tutorials or notifications and illustrates a callout, a personalized feature card, and a direct action.
- Measurement boundary: [[its-time-to-get-rid-of-traditional-release-notes-colm-doyle-medium]] says in-app communication permits conversion measurement and feedback, but reports no outcomes.
- Scope boundary: [[its-time-to-get-rid-of-traditional-release-notes-colm-doyle-medium]] explicitly limits its argument to consumer-facing software rather than APIs and SDKs.

## Counterevidence & Qualifications
The evidence is one brief 2016 practitioner essay with no readership, experiment, adoption, satisfaction, or support data. Platform behavior, update controls, notification norms, and accessibility expectations may differ across products and over time. In-app messages can interrupt users, miss people who do not reach the relevant surface, or optimize clicks instead of understanding. Feature flags make communication targetable but also create operational complexity and a stronger need for accurate internal and external records. The source therefore supports moving feature introduction closer to use, not treating documentation as valueless.

## What Changed
- Created a distinction between durable change records and contextual feature introduction.
- Added user-specific exposure and auto-update behavior as channel-selection constraints.
- Preserved APIs, SDKs, support, compliance, accessibility, and audit needs as limits on replacing release notes.

## Related Concepts
- [[ContinuousDelivery]] - frequent delivery and feature flags weaken the assumption that one binary maps to one uniform user-visible release.
- [[DeploymentReleaseSeparation]] - activation timing can differ from artifact installation, changing when communication is relevant.
- [[ProductUserSegmentation]] - entitlements and exposure rules determine which audience can encounter a change.
- [[ConversionRateOptimization]] - instrumented prompts can measure a desired response while requiring interpretation beyond clicks.
- [[MobilePlatformDiscovery]] - App Store visibility and auto-update behavior shape whether users encounter release metadata.
- [[ProductLedRetention]] - clear feature discovery can support continued value when it helps users reach relevant capabilities.
