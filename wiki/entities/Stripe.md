---
title: "Stripe"
type: entity
tags: [payments, saas, infrastructure]
sources:
  - yi-ge-du-li-chuang-zao-zhe-de-wu-nian
  - 16-lessons-on-scaling-from-eric-schmidt-reid-hoffman-marissa-mayer-brian-chesky-diane-greene-jeff-weiner-and-more
  - cs183c-session-11-patrick-collison-stripe-blitzscaling-class-notes-and-essays-medium
last_updated: 2026-09-25
knowledge_schema: synthesis-v1
---

## Overview
[[Stripe]] appears in the wiki as developer-oriented payment infrastructure, a modular service for small software businesses, and a case in startup organization and scaling.

## Current Profile
In the independent-creator source, Stripe is part of the financial infrastructure that made [[BootstrappedSaaS]] practical for a non-U.S. creator. The CS183C material adds the company's origin in a developer pain point, early adoption through [[YCombinator]], and a wider infrastructure thesis: Stripe sought to make accepting and coordinating internet payments as accessible as provisioning a server. The same account presents slow early hiring, engineering-led product work, direct partnership-building, backward-compatible API evolution, and formal written communication as the organization grew.

## Key Characteristics
- Provides programmable payment infrastructure for SaaS businesses and multi-party marketplaces.
- Grew from a private developer prototype distributed through friends and Y Combinator companies.
- Offers developer experience through documentation, API design, and compatibility across versions.
- Fits a lightweight service stack that lets small companies rent financial capability instead of building it.
- Requires country-specific eligibility and may request identity, tax, or business verification.
- Serves as a scaling example for patient early hiring and engineering-led product decisions.
- Illustrates the move toward explicit writing, broadcast communication, and delegated leadership under growth.

## Evidence
- Payment selection: [[yi-ge-du-li-chuang-zao-zhe-de-wu-nian]] says Hawstein chose Stripe after researching overseas payment providers.
- Eligibility workaround: [[yi-ge-du-li-chuang-zao-zhe-de-wu-nian]] describes using a U.S. bank account and EIN because Stripe did not support mainland China registration.
- Developer experience: [[yi-ge-du-li-chuang-zao-zhe-de-wu-nian]] praises Stripe's documentation and API design.
- Verification and company update: [[yi-ge-du-li-chuang-zao-zhe-de-wu-nian]] describes submitting IRS documentation and later changing tax, business, and bank details after company formation.
- Early hiring: [[16-lessons-on-scaling-from-eric-schmidt-reid-hoffman-marissa-mayer-brian-chesky-diane-greene-jeff-weiner-and-more]] says Stripe took six months to hire its first two people and then hired only a few more in the next six months.
- Work trials: [[16-lessons-on-scaling-from-eric-schmidt-reid-hoffman-marissa-mayer-brian-chesky-diane-greene-jeff-weiner-and-more]] describes Stripe using week-long candidate trials.
- Communication at scale: [[16-lessons-on-scaling-from-eric-schmidt-reid-hoffman-marissa-mayer-brian-chesky-diane-greene-jeff-weiner-and-more]] cites [[PatrickCollison]] on needing formal broadcast communication after 150 employees.
- Origin and early distribution: [[cs183c-session-11-patrick-collison-stripe-blitzscaling-class-notes-and-essays-medium]] describes the `/dev/payments` prototype and says many of its first 20–30 users were Y Combinator companies or friends of alumni.
- Product expansion: [[cs183c-session-11-patrick-collison-stripe-blitzscaling-class-notes-and-essays-medium]] distinguishes simple person-to-person payments from Connect's coordination of marketplace flows such as charges, payouts, refunds, and tips.
- Partnerships and operations: [[cs183c-session-11-patrick-collison-stripe-blitzscaling-class-notes-and-essays-medium]] says the founders initially created processor accounts manually and that an early non-engineering hire helped secure a Wells Fargo relationship.
- Compatibility: [[cs183c-session-11-patrick-collison-stripe-blitzscaling-class-notes-and-essays-medium]] describes a translation layer for recent API versions and direct outreach to the last three users of a 2010 version before deprecation.

## Qualifications
The independent-creator source recommends Stripe from one author's experience but warns that access and risk control are strict. The CS183C accounts are founder and class-note retrospectives from 2015; their scale figures, product structure, and organization description are historical, company-favorable, and not independently benchmarked.

## What Changed
- Added Stripe's founding problem, YC distribution, marketplace-payment expansion, partnership work, and API compatibility model.
- Broadened the organization profile from hiring and communication to engineering-led product judgment and delegated leadership.

## Relationships
- [[BootstrappedSaaS]] - Stripe enabled subscription payment collection.
- [[MicroCompany]] - Stripe is one of the modular services that reduce solo-company operating burden.
- [[Hawstein]] - Hawstein used Stripe for his overseas SaaS business.
- [[PatrickCollison]] - Stripe founder whose scaling lessons appear in the source.
- [[JohnCollison]] - co-founder who built the early prototype with Patrick.
- [[StartupHiringAtScale]] - Stripe is an example of slow early hiring.
- [[ScalingCommunication]] - Stripe is used for the post-150 broadcast communication threshold.
- [[APIBackwardCompatibility]] - Stripe uses version translation and direct migration to protect integrations.
- [[YCombinator]] - community source for many of the first prototype users.
