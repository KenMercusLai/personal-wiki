---
title: "Stripe"
type: entity
tags: [payments, saas, infrastructure]
sources:
  - yi-ge-du-li-chuang-zao-zhe-de-wu-nian
  - 16-lessons-on-scaling-from-eric-schmidt-reid-hoffman-marissa-mayer-brian-chesky-diane-greene-jeff-weiner-and-more
last_updated: 2026-09-12
knowledge_schema: synthesis-v1
---

## Overview
[[Stripe]] appears in the wiki as both SaaS payment infrastructure and a startup scaling example.

## Current Profile
In the independent-creator source, Stripe is part of the financial infrastructure that made [[BootstrappedSaaS]] practical for a non-U.S. independent creator. The CS183C source adds Stripe as an organization example: [[PatrickCollison]] describes slow early hiring, week-long trials, and the communication shift that occurred after the company grew past roughly 150 employees.

## Key Characteristics
- Provides payment infrastructure for overseas SaaS subscriptions.
- Requires country-specific account eligibility and identity or tax information.
- Offers strong developer experience through documentation and API design.
- Can request additional verification as revenue grows.
- Fits the author's broader lightweight infrastructure stack for one-person SaaS.
- Serves as a scaling example for slow early hiring before organizational growth.
- Illustrates the need for formal broadcast communication past roughly 150 employees.

## Evidence
- Payment selection: [[yi-ge-du-li-chuang-zao-zhe-de-wu-nian]] says Hawstein chose Stripe after researching overseas payment providers.
- Eligibility workaround: [[yi-ge-du-li-chuang-zao-zhe-de-wu-nian]] describes using a U.S. bank account and EIN because Stripe did not support mainland China registration.
- Developer experience: [[yi-ge-du-li-chuang-zao-zhe-de-wu-nian]] praises Stripe's documentation and API design.
- Verification and company update: [[yi-ge-du-li-chuang-zao-zhe-de-wu-nian]] describes submitting IRS documentation and later changing tax, business, and bank details after company formation.
- Early hiring: [[16-lessons-on-scaling-from-eric-schmidt-reid-hoffman-marissa-mayer-brian-chesky-diane-greene-jeff-weiner-and-more]] says Stripe took six months to hire its first two people and then hired only a few more in the next six months.
- Work trials: [[16-lessons-on-scaling-from-eric-schmidt-reid-hoffman-marissa-mayer-brian-chesky-diane-greene-jeff-weiner-and-more]] describes Stripe using week-long candidate trials.
- Communication at scale: [[16-lessons-on-scaling-from-eric-schmidt-reid-hoffman-marissa-mayer-brian-chesky-diane-greene-jeff-weiner-and-more]] cites [[PatrickCollison]] on needing formal broadcast communication after 150 employees.

## Qualifications
The independent-creator source recommends Stripe from one author's experience but warns that risk control is strict. The CS183C source uses Stripe as an operating anecdote rather than a full account of the company's hiring process or organizational design.

## What Changed
- Added Stripe's role as a startup scaling example for slow early hiring and post-150 communication.

## Relationships
- [[BootstrappedSaaS]] - Stripe enabled subscription payment collection.
- [[MicroCompany]] - Stripe is one of the modular services that reduce solo-company operating burden.
- [[Hawstein]] - Hawstein used Stripe for his overseas SaaS business.
- [[PatrickCollison]] - Stripe founder whose scaling lessons appear in the source.
- [[StartupHiringAtScale]] - Stripe is an example of slow early hiring.
- [[ScalingCommunication]] - Stripe is used for the post-150 broadcast communication threshold.
