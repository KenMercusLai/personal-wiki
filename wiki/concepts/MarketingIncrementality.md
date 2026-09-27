---
title: "Marketing Incrementality"
type: concept
tags: [marketing, experimentation, measurement, advertising]
sources:
  - engineering-to-improve-marketing-effectiveness-part-1
last_updated: 2026-09-27
knowledge_schema: synthesis-v1
---

## Definition
[[MarketingIncrementality]] is the counterfactual effect of marketing: the outcomes caused by an intervention beyond what would have happened without it.

## Current Synthesis
The Netflix source treats incrementality as the objective that should govern paid media. Advertising someone who was already likely to subscribe can look successful under ordinary conversion attribution without changing the outcome. The operating goal is therefore to learn which audiences remain undecided and which spend changes their behavior, then balance demand creation with acquisition activity across markets.

This principle makes experimentation more than campaign reporting: spend should produce evidence about causal lift as well as immediate outcomes. The source states the objective but does not disclose the experiment designs, estimators, targeting features, uncertainty, or measured lift used to implement it.

## Key Claims
- Observed post-ad conversion is not sufficient evidence that advertising caused the conversion.
- Incremental targeting seeks people whose decisions can still be changed rather than people likely to act anyway.
- Paid-media efficiency depends on causal lift, not only attributed response or low delivery cost.
- Market-level demand creation and acquisition activity should be balanced rather than optimized in isolation.
- Repeated experiments can turn campaign spending into learning when their counterfactuals and outcome measures are credible.

## Evidence
- Counterfactual objective: [[engineering-to-improve-marketing-effectiveness-part-1]] says Netflix would prefer not to advertise to cohorts likely to subscribe anyway.
- Audience focus: [[engineering-to-improve-marketing-effectiveness-part-1]] identifies people who have not made up their minds as the primary marketing target.
- Learning loop: [[engineering-to-improve-marketing-effectiveness-part-1]] describes every marketing dollar as an opportunity to learn and places measurement and optimization within the AdTech charter.
- Market balance: [[engineering-to-improve-marketing-effectiveness-part-1]] says demand creation and acquisition should be kept in an appropriate proportion by market.

## Counterevidence & Qualifications
The source is a first-party strategy account, not a methods paper or results report. It provides no holdout design, randomization unit, time horizon, statistical uncertainty, spillover treatment, privacy analysis, or measured incremental subscriptions. Some advertising may have brand, information, or long-horizon effects that short experiments miss, while attempts to identify “persuadable” people can introduce targeting, fairness, and privacy concerns.

## What Changed
- Created a counterfactual definition that separates causal marketing lift from attributed conversion.
- Preserved the source's market-balancing and learning objectives while making its missing measurement detail explicit.

## Related Concepts
- [[MarketingAttribution]] - assigns credit to observed touchpoints, while incrementality asks whether those touchpoints changed the outcome.
- [[MarketingOperations]] - supplies the systems and operating process needed to run and act on experiments.
- [[AudienceTargeting]] - selects cohorts, including those judged more likely to respond incrementally.
- [[CustomerAcquisitionCost]] - becomes more decision-useful when calculated against incremental rather than merely attributed acquisition.
- [[AATesting]] - calibrates experiment pipelines and interpretation before causal lifts are trusted.
