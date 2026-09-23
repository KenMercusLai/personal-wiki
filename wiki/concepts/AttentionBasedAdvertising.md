---
title: "Attention-Based Advertising"
type: concept
tags: [advertising, attention, privacy, browsers, cryptocurrency]
sources:
  - your-next-browser-will-pay-you-by-daniel-colin-james
last_updated: 2026-09-23
knowledge_schema: synthesis-v1
---

## Definition
[[AttentionBasedAdvertising]] is the source's proposed advertising model in which a user agent measures attention locally, matches optional ads without exporting personal data, and shares advertising value directly with users and publishers.

## Current Synthesis
The Brave/BAT proposal moves ad selection and attention measurement from a large third-party tracking chain into the browser. The intended trade is explicit: users opt in and receive BAT, publishers receive a defined share or voluntary contributions, and advertisers receive more accurate matching, analytics, and lower fraud. This bundles privacy architecture, revenue allocation, cryptocurrency settlement, and browser distribution into one incentive system. Its appeal comes from aligning stakeholders who are dissatisfied with conventional ad technology, but the source documents a design thesis and marketing forecast rather than mature evidence that the incentives, privacy boundary, or token economics work at scale.

## Key Claims
- Optional participation makes the advertising exchange more explicit than default third-party tracking.
- On-device matching can in principle use browser context while limiting disclosure of personal data to advertisers or the platform.
- Paying users recognizes attention as an input with economic value rather than treating it as free inventory.
- Direct publisher allocation and voluntary contributions aim to preserve content funding despite default ad blocking.
- Fewer intermediaries and local measurement are expected to improve advertiser return and reduce fraud.
- A browser can seed the market because it sits between users, publishers, content, and ad delivery.
- Token settlement is meant to make the model portable into other attention-heavy applications.

## Evidence
- Opt-in and privacy design: [[your-next-browser-will-pay-you-by-daniel-colin-james]] says Brave Ads are optional and that matching and attention monitoring remain on-device.
- User and publisher allocation: [[your-next-browser-will-pay-you-by-daniel-colin-james]] specifies proposed revenue shares and lets users contribute earned BAT to sites and creators.
- Advertiser proposition: [[your-next-browser-will-pay-you-by-daniel-colin-james]] promises better targeting, detailed effectiveness analytics, and less fraud.
- Architecture diagram: [[your-next-browser-will-pay-you-by-daniel-colin-james]] visually connects the user, advertiser, and publisher around BAT while placing user data behind an anonymity shield.
- Expansion forecast: [[your-next-browser-will-pay-you-by-daniel-colin-james]] imagines the model extending to messaging, games, podcasts, and streaming.

## Counterevidence & Qualifications
The only source is a commissioned 2018 advocacy article whose author owned BAT. It does not show audited revenue flows, privacy analysis, advertiser lift, publisher income, user retention, fraud reduction, token volatility, regulatory treatment, or the later outcome of its adoption forecast. Local targeting can reduce data disclosure, but the source does not specify the full threat model, analytics boundary, verification mechanism, or how advertisers can validate attention without recreating surveillance or fraud risks.

## What Changed
- Created the concept to capture Brave's combined local-targeting, user-reward, publisher-payment, and token-settlement design.

## Related Concepts
- [[WebAdEconomics]] - incumbent funding model the proposal seeks to restructure.
- [[AdBlocking]] - default rejection of conventional inventory creates the opening for an opt-in replacement.
- [[BehavioralTargeting]] - browser-local preference matching is presented as a privacy-preserving alternative to server-side profiling.
- [[ProgrammaticAdvertising]] - the proposal aims to remove much of the intermediary delivery chain.
- [[BasicAttentionToken]] - token used to settle and redistribute attention value.
- [[Brave]] - browser implementation and distribution channel for the model.
