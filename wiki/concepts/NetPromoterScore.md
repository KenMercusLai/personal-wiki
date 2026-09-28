---
title: "Net Promoter Score"
type: concept
tags: [product-management, metrics, customer-loyalty]
sources:
  - a-practitioners-guide-to-net-promoter-score-at-andrewchen
  - attribution-marketing-creating-a-growth-engine-at-salesforce-zendesk-and-slack-for-entrepreneurs
  - credit-karmas-ceo-built-a-sexy-brand-in-an-unsexy-category-with-no-pr-firm-and-a-tiny-budget-heres-how-first-round-review
  - four-promises-a-brand-makes-to-its-customers-lightspeed-venture-partners-medium
last_updated: 2026-09-28
knowledge_schema: synthesis-v1
---

## Definition
[[NetPromoterScore]] is a customer-loyalty metric calculated from a recommendation-likelihood survey by subtracting the percentage of detractors from the percentage of promoters.

## Current Synthesis
The sources treat Net Promoter Score as a useful but fragile product-management and customer-satisfaction signal. Its basic calculation is simple: ask how likely a customer is to recommend the company, classify scores of 9-10 as promoters, 7-8 as passives, and 0-6 as detractors, then subtract detractor share from promoter share. The practical value comes from the surrounding program: open-ended comments, representative sampling, consistent methodology, behavior correlation, quarterly analysis, and roadmap follow-through. The Slack attribution source adds that NPS can also become one input to [[MarketingAttribution]] when a company wants to understand how brand, offline, word-of-mouth, product, and lifecycle touches contribute to satisfaction and recommendation.

The [[CreditKarma]] case extends NPS from general measurement into advocate discovery: high scores, sharing, referrals, and unsolicited public defense can identify promoters whose feedback may inform product work. Taussig further proposes NPS as a proxy for [[BrandEquity]] because its recommendation question approximates referability. Both extensions reinforce that the score should sit beside behavioral signals such as return frequency, sharing, referrals, and unsubscribes rather than being treated as a complete measure of brand or a causal growth lever by itself.

## Key Claims
- NPS is calculated by separating promoters, passives, and detractors from a 0-10 recommendation-likelihood question.
- The metric becomes actionable when teams ask why the respondent gave that score.
- Sampling and collection channels can bias results toward more engaged customers unless the sample reflects the broader user base.
- NPS should be compared across surveys only when methodology remains consistent.
- Verbatim analysis and product-behavior correlation can translate scores into product priorities.
- NPS is a lagging and sampled measure, so it should complement rather than replace operational metrics and strategy.
- NPS can be used relationally or transactionally, help locate likely advocates, and serve as a narrow referability signal for brand equity, but scores need behavioral corroboration and do not directly measure delivery across product, price, channel, and marketing.

## Evidence
- Calculation: [[a-practitioners-guide-to-net-promoter-score-at-andrewchen]] describes promoters as 9-10, passives as 7-8, detractors as 0-6, and NPS as promoter percentage minus detractor percentage; the inspected diagram shows the same grouping and subtraction formula.
- Actionability: [[a-practitioners-guide-to-net-promoter-score-at-andrewchen]] says the open-ended "why" question turns NPS from past-performance score into improvement input.
- Sampling bias: [[a-practitioners-guide-to-net-promoter-score-at-andrewchen]] warns that email and in-product prompts can overrepresent engaged users and that engagement and customer tenure correlated with NPS results.
- Methodology sensitivity: [[a-practitioners-guide-to-net-promoter-score-at-andrewchen]] says question order, competitor lists, and sampling approach affect comparability.
- Product learning: [[a-practitioners-guide-to-net-promoter-score-at-andrewchen]] describes categorizing promoter and detractor comments and correlating product actions with higher NPS to infer activation behaviors.
- Operational limits: [[a-practitioners-guide-to-net-promoter-score-at-andrewchen]] says NPS is too infrequent for day-to-day operations, carries margin-of-error limits, and is not a replacement for strategy.
- Attribution input: [[attribution-marketing-creating-a-growth-engine-at-salesforce-zendesk-and-slack-for-entrepreneurs]] says [[Slack]] tracks NPS at both relational and transactional levels and feeds satisfaction data into its attribution model.
- Advocate discovery: [[credit-karmas-ceo-built-a-sexy-brand-in-an-unsexy-category-with-no-pr-firm-and-a-tiny-budget-heres-how-first-round-review]] combines NPS with sharing, referrals, forum advocacy, return behavior, and unsubscribes to identify and understand promoters.
- Product loop: [[credit-karmas-ceo-built-a-sexy-brand-in-an-unsexy-category-with-no-pr-firm-and-a-tiny-budget-heres-how-first-round-review]] says [[CreditKarma]] asked Reddit advocates what they needed and built Direct Dispute in response to report-inaccuracy complaints.
- Brand-equity proxy: [[four-promises-a-brand-makes-to-its-customers-lightspeed-venture-partners-medium]] uses NPS as a measure of customers' tendency to recommend and connects referability to accumulated belief in brand promises.

## Counterevidence & Qualifications
The sources are practitioner guidance, company retrospectives, and an investor essay rather than universal measurement proof. NPS can be biased by response channels, sampling, customer tenure, engagement, seasonality, methodology changes, and the difficulty of linking satisfaction to specific prior touchpoints. Credit Karma's quoted claim that category NPS leaders grow twice as fast and Taussig's claim that high-NPS companies tend to remain market-share leaders do not include underlying studies or establish causation. Recommendation intent also captures only one aspect of brand equity and may diverge from actual referral. NPS is too slow for A/B tests or daily management and should be paired with acquisition, engagement, monetization, referral, retention, attribution, customer-experience, and other operational evidence.

## What Changed
- Created the concept page for NPS as a customer-loyalty metric and product-learning program.
- Added Slack's relational and transactional NPS usage as an attribution and satisfaction signal.
- Added NPS as one input to advocate discovery and product feedback, qualified by behavioral corroboration and unverified causal growth claims.
- Added referability as a narrow brand-equity use while rejecting NPS as a complete or causal measure of brand strength.

## Related Concepts
- [[ProductMetricLadder]] - NPS can be a slow business-level metric that needs shorter-cycle proxy metrics.
- [[CustomerLedProductDevelopment]] - open-ended NPS comments provide structured customer voice for product decisions.
- [[ViralLoops]] - the source connects customer recommendation strength with word-of-mouth virality.
- [[ProductMarketFit]] - strong loyalty and recommendation intent can indicate product pull but do not replace broader market validation.
- [[StatisticalModelThinking]] - NPS interpretation depends on sample size, bias, margin of error, and comparability assumptions.
- [[MarketingAttribution]] - NPS can become a downstream satisfaction and recommendation input in attribution models.
- [[DeepFunnelMetrics]] - NPS is one deeper customer outcome beyond signup or lead creation.
- [[BrandEquity]] - NPS approximates stated referability but not the full set of beliefs created by customer experience.
