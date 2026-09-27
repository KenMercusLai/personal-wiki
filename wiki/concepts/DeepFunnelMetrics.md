---
title: "Deep Funnel Metrics"
type: concept
tags: [marketing, saas, metrics]
sources:
  - attribution-marketing-creating-a-growth-engine-at-salesforce-zendesk-and-slack-for-entrepreneurs
  - designing-for-personalization-the-story-of-optimizelys-homepage-optimizely-blog
last_updated: 2026-09-27
knowledge_schema: synthesis-v1
---

## Definition
[[DeepFunnelMetrics]] are downstream customer and revenue measures used to judge marketing impact beyond early clicks, forms, signups, or trials.

## Current Synthesis
The sources argue that marketing and product experiments become more actionable when measurement follows prospects through the business funnel. Trial signup, account creation, or form completion is too shallow if the real goal is durable SaaS growth. Teams should connect acquisition and web-experience changes to engagement, lead quality, qualified opportunities, sales velocity, signed contracts, annual contract value, expansion revenue, retention, activity, satisfaction, and recommendation signals where those outcomes define the business. The Optimizely homepage case makes the tradeoff concrete: a new design could lower immediate lead conversion yet still be preferable if visitors became better informed and generated fewer, better-qualified opportunities.

## Key Claims
- Marketing attribution should not stop at trial signup or form completion.
- Data warehouse integration is needed to connect touches to later business outcomes.
- Long-term core metrics reduce the risk of optimizing short-term vanity outcomes.
- B2B SaaS journeys may require tracking many touches over months before the first meaningful action.
- Team-based products may need account-level or team-level metrics rather than only individual-user tracking.
- Existing-customer and lifecycle marketing can be measured against retention, growth, satisfaction, and expansion.
- A lower immediate conversion rate can be acceptable when qualification, engagement, or sales progression improves enough to create more business value.

## Evidence
- Funnel depth: [[attribution-marketing-creating-a-growth-engine-at-salesforce-zendesk-and-slack-for-entrepreneurs]] says attribution should follow users from trial through lead, opportunity, signed deal, and expansion revenue.
- Metric caution: [[attribution-marketing-creating-a-growth-engine-at-salesforce-zendesk-and-slack-for-entrepreneurs]] warns that tying marketing value to short-term metrics can create wrong incentives.
- Zendesk case: [[attribution-marketing-creating-a-growth-engine-at-salesforce-zendesk-and-slack-for-entrepreneurs]] says Zendesk connected content and channel exposure to lead creation, sales velocity, deal size, and revenue growth.
- Slack case: [[attribution-marketing-creating-a-growth-engine-at-salesforce-zendesk-and-slack-for-entrepreneurs]] says Slack tracked team size, average ARR per seat, activity across teams, expansion ARR, brand recall, sentiment, share of voice, and NPS.
- Lifecycle scope: [[attribution-marketing-creating-a-growth-engine-at-salesforce-zendesk-and-slack-for-entrepreneurs]] says attribution can value touchpoints after acquisition in customer success, usage, satisfaction, retention, and growth.
- Lead-quality failure: [[designing-for-personalization-the-story-of-optimizelys-homepage-optimizely-blog]] says Optimizely's conversion-focused homepage produced many unqualified accounts with incomplete lead data and weak progression to sales conversations and opportunities.
- Redesign scorecard: [[designing-for-personalization-the-story-of-optimizelys-homepage-optimizely-blog]] proposes engagement, lead conversion, accounts created, lead qualification, and sales velocity as complementary measures.

## Counterevidence & Qualifications
Deep metrics are slower and harder to attribute than clicks or forms. They can also mix marketing influence with sales execution, product quality, customer success, pricing, and market fit. The sources recommend them because they align with core business value, not because they eliminate attribution uncertainty. Optimizely's article reports a planned test rather than results, and changing page structure and personalization together would make it difficult to isolate which mechanism caused any downstream effect.

## What Changed
- Created deep funnel metrics as the downstream outcome layer for attribution and SaaS marketing measurement.
- Added homepage redesign and personalization as cases where lead quality and sales velocity can outweigh raw conversion volume.

## Related Concepts
- [[MarketingAttribution]] - attribution needs deep funnel outcomes to judge spend quality.
- [[CustomerAcquisitionCost]] - CAC quality depends on downstream conversion and value.
- [[CustomerLifetimeValue]] - lifecycle and expansion value should inform channel evaluation.
- [[SaaSRetention]] - retention is a downstream outcome that acquisition metrics can miss.
- [[NetPromoterScore]] - one satisfaction and recommendation signal used in deeper measurement.
- [[ProductMetricLadder]] - deep outcomes often need faster proxy metrics for day-to-day steering.
- [[WebsitePersonalization]] - personalized modules should be evaluated by downstream customer quality as well as clicks and forms.
- [[AccountBasedMarketing]] - targeted acquisition shifts attention from lead quantity toward account fit and sales progression.
