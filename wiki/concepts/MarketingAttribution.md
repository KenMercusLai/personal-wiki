---
title: "Marketing Attribution"
type: concept
tags: [marketing, analytics, growth]
sources:
  - attribution-marketing-creating-a-growth-engine-at-salesforce-zendesk-and-slack-for-entrepreneurs
  - billboards-for-small-businesses-costs-advice-and-thinking-twice
  - building-lyfts-marketing-automation-platform-lyft-engineering
  - burning-money-on-paid-ads-for-a-dev-tool-what-weve-learned-posthog
  - android-apps-with-more-than-2-billion-total-downloads-are-committing-ad-fraud
last_updated: 2026-09-25
knowledge_schema: synthesis-v1
---

## Definition
[[MarketingAttribution]] is the practice of assigning credit for customer outcomes across marketing touchpoints so teams can judge whether spending produced useful demand, while recognizing that the credit rules themselves can be incomplete, uncertain, or manipulated.

## Current Synthesis
The sources frame attribution as growth infrastructure for deciding whether marketing effort produces valuable outcomes. Multi-touch SaaS journeys make simple first-click, last-click, and linear models fragile; offline awareness and developer-tool advertising expose meaningful influence that clicks miss; and Lyft shows how performance data can feed LTV forecasts, budget allocation, and channel bidders. The Android investigation adds an adversarial boundary: when an install bounty is paid to the last recorded click, software already on the device can inject a late click or flood speculative clicks and receive credit without creating demand. Attribution therefore requires not only better models and deeper outcomes but also telemetry integrity, anomaly detection, source transparency, and resistance to strategic manipulation.

## Key Claims
- Attribution turns marketing from preference debates into measurable budget decisions.
- Multi-touch journeys make simplistic first-click and last-click models incomplete even when every participant is honest.
- Useful systems connect touchpoints to deep business outcomes rather than stopping at clicks, installs, signups, or trials.
- Implementation is technical and organizational because teams must trust data, definitions, and resulting budget changes.
- Offline, brand, word-of-mouth, and developer influence may need qualitative or self-reported evidence alongside click data.
- Automated attribution can drive LTV forecasting, allocation, and bidding but inherits data-quality and model risks.
- Attribution rules are attack surfaces: actors can fabricate or time events to seize credit and payment without adding marketing value.

## Evidence
- Multi-touch measurement: [[attribution-marketing-creating-a-growth-engine-at-salesforce-zendesk-and-slack-for-entrepreneurs]] shows why first-click, last-click, and linear models can misprice display, social, content, search, trial, and later revenue touchpoints.
- Deep outcomes and adoption: [[attribution-marketing-creating-a-growth-engine-at-salesforce-zendesk-and-slack-for-entrepreneurs]] recommends tracking leads, opportunities, deals, expansion, retention, and satisfaction while educating teams early enough to trust the system.
- Hard-to-observe influence: [[billboards-for-small-businesses-costs-advice-and-thinking-twice]] reports billboard awareness without clear sales lift, while [[burning-money-on-paid-ads-for-a-dev-tool-what-weve-learned-posthog]] uses self-reported signup and demo answers to supplement missing click influence.
- Automated feedback: [[building-lyfts-marketing-automation-platform-lyft-engineering]] feeds performance data and expected LTV into budget allocation and channel-specific bidding.
- Adversarial last-click capture: [[android-apps-with-more-than-2-billion-total-downloads-are-committing-ad-fraud]] explains how Cheetah and Kika apps allegedly injected late clicks or flooded likely installs to win bounties for demand they did not create.
- Integrity and concealment: [[android-apps-with-more-than-2-billion-total-downloads-are-committing-ad-fraud]] says claims were dispersed through more than 20 networks and sometimes hidden behind false app names or obscured sub-publishers.

## Counterevidence & Qualifications
The sources favor measurement discipline but acknowledge word of mouth, dark social, offline exposure, customer delight, developer ad exposure without clicks, forecast uncertainty, and organizational cost. Algorithmic systems require infrastructure, integrations, monitoring, and human feedback, while anecdotes and self-reports are not controlled tests. The fraud source is a disputed 2018 investigation: Cheetah denied proprietary SDK involvement, Kika denied intent, Google initially said it had not confirmed fraud, and the article does not publish a complete forensic dataset. The combined lesson is neither that every startup needs a full attribution stack nor that attribution is unusable, but that credit estimates depend on both model fitness and trustworthy event provenance.

## What Changed
- Added deliberate event manipulation as a failure mode distinct from ordinary attribution uncertainty or missing touchpoints.
- Reframed trustworthy telemetry, provenance, and anomaly detection as prerequisites for attribution-driven spending.

## Related Concepts
- [[AlgorithmicAttribution]] - data-driven multi-touch credit assignment that still depends on valid input events.
- [[AppInstallAttributionFraud]] - deliberate fabrication or timing of mobile events to capture unearned credit.
- [[MarketingOperations]] - organizational and technical owner of tracking, integrations, and measurement trust.
- [[DeepFunnelMetrics]] - downstream outcomes that make attribution more useful than click or signup counts alone.
- [[CustomerAcquisitionCost]] - spending metric whose apparent value can be corrupted by false attribution.
- [[CustomerLifetimeValue]] - downstream value target used to compare acquisition channels and allocate budgets.
- [[BillboardAdvertising]] - offline channel exposing the gap between awareness and attributable demand.
- [[DeveloperToolPaidAdvertising]] - technical-buyer advertising that exposes limits of direct click measurement.
- [[IdentityResolution]] - linkage layer connecting devices, events, clicks, installs, and customers.
