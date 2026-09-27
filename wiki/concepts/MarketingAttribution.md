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
  - content-is-eating-the-world-contentlys-ceo-on-winning-at-marketings-new-hotness-first-round-review
  - dev-tool-marketing-for-early-stage-startups-what-weve-learned
  - does-sponsoring-daring-fireball-actually-work-john-saddington
last_updated: 2026-09-27
knowledge_schema: synthesis-v1
---

## Definition
[[MarketingAttribution]] is the practice of assigning credit for customer outcomes across marketing touchpoints so teams can judge whether spending produced useful demand, while recognizing that the credit rules themselves can be incomplete, uncertain, or manipulated.

## Current Synthesis
The sources frame attribution as growth infrastructure for deciding whether marketing effort produces valuable outcomes. Multi-touch SaaS journeys make simple first-click, last-click, and linear models fragile; offline awareness, sponsorships, and developer-tool advertising expose meaningful influence that clicks miss; and Lyft shows how performance data can feed LTV forecasts, budget allocation, and channel bidders. PostHog makes the blind spot concrete: a person can discover the product on Hacker News, later search its name, click a Google ad, and cause the ad to receive credit for demand it did not originate. The Desk case adds the inverse problem: a paid placement may coincide with immediate proceeds and a wider halo through platform rank, reviews, testimonials, and awards, but those later effects cannot all be causally assigned to the sponsor. Optional free-text discovery questions, before-and-after baselines, engagement evidence, and downstream outcomes can fill gaps without becoming controlled counterfactuals. Attribution therefore requires deeper outcomes, mixed signals, telemetry integrity, source transparency, and resistance to both strategic manipulation and causal overstatement.

## Key Claims
- Attribution turns marketing from preference debates into measurable budget decisions.
- Multi-touch journeys make simplistic first-click and last-click models incomplete even when every participant is honest.
- Useful systems connect touchpoints to deep business outcomes rather than stopping at clicks, installs, signups, or trials.
- Implementation is technical and organizational because teams must trust data, definitions, and resulting budget changes.
- Offline, brand, sponsorship, word-of-mouth, developer, and content influence may need baselines, self-reported discovery, engagement, platform rank, press, subscriber, sales, or CRM evidence alongside click data, without treating correlation as causation.
- Automated attribution can drive LTV forecasting, allocation, and bidding but inherits data-quality and model risks.
- Attribution rules are attack surfaces: actors can fabricate or time events to seize credit and payment without adding marketing value.

## Evidence
- Multi-touch measurement: [[attribution-marketing-creating-a-growth-engine-at-salesforce-zendesk-and-slack-for-entrepreneurs]] shows why first-click, last-click, and linear models can misprice display, social, content, search, trial, and later revenue touchpoints.
- Deep outcomes and adoption: [[attribution-marketing-creating-a-growth-engine-at-salesforce-zendesk-and-slack-for-entrepreneurs]] recommends tracking leads, opportunities, deals, expansion, retention, and satisfaction while educating teams early enough to trust the system.
- Hard-to-observe influence: [[billboards-for-small-businesses-costs-advice-and-thinking-twice]] reports billboard awareness without clear sales lift, while [[burning-money-on-paid-ads-for-a-dev-tool-what-weve-learned-posthog]] uses self-reported signup and demo answers to supplement missing click influence.
- Last-touch mirage: [[dev-tool-marketing-for-early-stage-startups-what-weve-learned]] shows how Hacker News can create awareness before a later branded search and Google-ad click receives apparent credit; it reports that roughly 10% of signups answer an optional free-text discovery question.
- Automated feedback: [[building-lyfts-marketing-automation-platform-lyft-engineering]] feeds performance data and expected LTV into budget allocation and channel-specific bidding.
- Adversarial last-click capture: [[android-apps-with-more-than-2-billion-total-downloads-are-committing-ad-fraud]] explains how Cheetah and Kika apps allegedly injected late clicks or flooded likely installs to win bounties for demand they did not create.
- Integrity and concealment: [[android-apps-with-more-than-2-billion-total-downloads-are-committing-ad-fraud]] says claims were dispersed through more than 20 networks and sometimes hidden behind false app names or obscured sub-publishers.
- Content evidence ladder: [[content-is-eating-the-world-contentlys-ceo-on-winning-at-marketings-new-hotness-first-round-review]] moves from impressions to dwell time, scroll depth, return visits, referrals, subscriptions, downloads, sales remarks, and reader-to-customer matching.
- Sponsorship response and halo: [[does-sponsoring-daring-fireball-actually-work-john-saddington]] compares first-week proceeds with the preceding week and separately reports App Store rank, review demand, testimonials, and Apple recognition, while acknowledging that the placement's contribution to the award cannot be isolated.
- Repeatability check: [[does-sponsoring-daring-fireball-actually-work-john-saddington]] says the second Daring Fireball campaign was less successful despite a similar product-publication pairing.

## Counterevidence & Qualifications
The sources favor measurement discipline but acknowledge word of mouth, dark social, offline exposure, customer delight, sponsorship halo, developer ad exposure without clicks, forecast uncertainty, and organizational cost. Algorithmic systems require infrastructure, integrations, monitoring, and human feedback, while anecdotes, self-reports, and before-and-after comparisons are not controlled tests. A voluntary response from roughly one in ten signups can reveal otherwise invisible channels but remains incomplete, recall-sensitive, hard to standardize, and vulnerable to selection bias. Contently's reader-customer overlap likewise does not isolate causation. Saddington's campaign figures use ambiguous net-profit language and sit inside a feedback system involving App Store rank, reviews, press, seasonal demand, Hacker News, and Apple recognition. The fraud source is a disputed 2018 investigation without a complete published forensic dataset. The combined lesson is neither that every startup needs a full attribution stack nor that attribution is unusable, but that credit estimates depend on model fitness, mixed evidence, trustworthy event provenance, explicit uncertainty, and careful causal language.

## What Changed
- Added direct sponsorship as a case where immediate response and a wider distribution halo require different evidence.
- Added repeat-campaign variance and platform-feedback effects as limits on before-and-after attribution.

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
- [[ContentLedAcquisition]] - content programs need engagement and downstream evidence beyond traffic counts.
- [[DeveloperMarketing]] - technical audiences expose click-attribution blind spots and motivate direct discovery questions.
- [[DirectSponsorship]] - a known placement can generate measurable response plus harder-to-isolate secondary distribution.
