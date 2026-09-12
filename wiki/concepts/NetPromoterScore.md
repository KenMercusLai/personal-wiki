---
title: "Net Promoter Score"
type: concept
tags: [product-management, metrics, customer-loyalty]
sources:
  - a-practitioners-guide-to-net-promoter-score-at-andrewchen
last_updated: 2026-09-13
knowledge_schema: synthesis-v1
---

## Definition
[[NetPromoterScore]] is a customer-loyalty metric calculated from a recommendation-likelihood survey by subtracting the percentage of detractors from the percentage of promoters.

## Current Synthesis
The source treats Net Promoter Score as a useful but fragile product-management signal. Its basic calculation is simple: ask how likely a customer is to recommend the company, classify scores of 9-10 as promoters, 7-8 as passives, and 0-6 as detractors, then subtract detractor share from promoter share. The practical value comes from the surrounding program: open-ended comments, representative sampling, consistent methodology, behavior correlation, quarterly analysis, and roadmap follow-through. NPS is strongest as a loyalty and customer-voice input, not as a day-to-day operating dashboard or replacement for product strategy.

## Key Claims
- NPS is calculated by separating promoters, passives, and detractors from a 0-10 recommendation-likelihood question.
- The metric becomes actionable when teams ask why the respondent gave that score.
- Sampling and collection channels can bias results toward more engaged customers unless the sample reflects the broader user base.
- NPS should be compared across surveys only when methodology remains consistent.
- Verbatim analysis and product-behavior correlation can translate scores into product priorities.
- NPS is a lagging and sampled measure, so it should complement rather than replace operational metrics and strategy.

## Evidence
- Calculation: [[a-practitioners-guide-to-net-promoter-score-at-andrewchen]] describes promoters as 9-10, passives as 7-8, detractors as 0-6, and NPS as promoter percentage minus detractor percentage; the inspected diagram shows the same grouping and subtraction formula.
- Actionability: [[a-practitioners-guide-to-net-promoter-score-at-andrewchen]] says the open-ended "why" question turns NPS from past-performance score into improvement input.
- Sampling bias: [[a-practitioners-guide-to-net-promoter-score-at-andrewchen]] warns that email and in-product prompts can overrepresent engaged users and that engagement and customer tenure correlated with NPS results.
- Methodology sensitivity: [[a-practitioners-guide-to-net-promoter-score-at-andrewchen]] says question order, competitor lists, and sampling approach affect comparability.
- Product learning: [[a-practitioners-guide-to-net-promoter-score-at-andrewchen]] describes categorizing promoter and detractor comments and correlating product actions with higher NPS to infer activation behaviors.
- Operational limits: [[a-practitioners-guide-to-net-promoter-score-at-andrewchen]] says NPS is too infrequent for day-to-day operations, carries margin-of-error limits, and is not a replacement for strategy.

## Counterevidence & Qualifications
The source is practitioner guidance from one LinkedIn context rather than a universal measurement proof. NPS can be biased by response channels, sampling, customer tenure, engagement, seasonality, and methodology changes. It is also too slow for A/B tests or daily management and should be paired with acquisition, engagement, monetization, and other operational dashboards.

## What Changed
- Created the concept page for NPS as a customer-loyalty metric and product-learning program.

## Related Concepts
- [[ProductMetricLadder]] - NPS can be a slow business-level metric that needs shorter-cycle proxy metrics.
- [[CustomerLedProductDevelopment]] - open-ended NPS comments provide structured customer voice for product decisions.
- [[ViralLoops]] - the source connects customer recommendation strength with word-of-mouth virality.
- [[ProductMarketFit]] - strong loyalty and recommendation intent can indicate product pull but do not replace broader market validation.
- [[StatisticalModelThinking]] - NPS interpretation depends on sample size, bias, margin of error, and comparability assumptions.
