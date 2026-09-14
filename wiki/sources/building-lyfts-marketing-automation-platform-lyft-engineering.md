---
title: "Building Lyft's Marketing Automation Platform"
type: source
tags: [marketing-automation, growth, machine-learning, advertising]
date: 2019-06-07
source_file: "/mnt/ken_personal_wiki/Articles/Building Lyft’s Marketing Automation Platform - Lyft Engineering.md"
---

## Summary
[[Lyft]] describes Symphony, a [[MarketingOperations]] platform that automates acquisition decisions across regions, channels, bids, budgets, creatives, incentives, and audiences. The system combines [[CustomerLifetimeValue]] forecasting, budget allocation, and channel-specific bidders so marketing teams can shift from repeated manual operations toward experimentation and human-in-the-loop learning. The inspected lead image is a decorative Lyft automation illustration, while the funnel diagram is evidence-bearing: it shows acquisition at the top of the onboarding funnel, spread across awareness, consideration, and install/sign-up channels before later user-journey stages.

## Key Claims
- Acquisition at Lyft required thousands of daily campaign decisions across markets, making manual bid, budget, creative, incentive, and audience management expensive and hard to scale.
- Symphony turns a business objective into future-user-value prediction, budget allocation, and deployed channel bids for new-user acquisition.
- The architecture has three main parts: an LTV forecaster, a budget allocator, and bidders that translate allocations into channel-specific API actions.
- [[CustomerLifetimeValue]] forecasting lets the system judge acquisition channels by expected user value while accounting for Lyft's two-sided marketplace.
- The budget allocator uses Thompson Sampling-style exploration over spend/LTV curves so budget decisions can learn from uncertain campaign performance rather than only exploiting current estimates.
- Bidders encode channel-specific levers, recency weighting, seasonality, partner constraints, and API integrations for search, display, social, referrals, and job-board channels.
- Long-term marketing automation depends on human feedback because models degrade when the automation engine receives poor human input.

## Key Quotes
> "build a marketing automation platform" - statement of the platform goal.

> "human-in-the-loop" - description of the long-term operating model.

## Connections
- [[Lyft]] - company and marketplace context for Symphony.
- [[MarketingOperations]] - Symphony automates and monitors the operational layer behind paid acquisition.
- [[MarketingAttribution]] - marketing performance data and LTV feedback determine where budgets should move.
- [[CustomerLifetimeValue]] - forecast target used to compare acquisition channel efficiency.
- [[AudienceTargeting]] - user segments, audiences, and campaign targets are among the levers Symphony automates.
- [[ReinforcementLearning]] - the source frames marketing performance data as feedback for a learning system.
- [[ContextualBandits]] - related online-learning family for exploration/exploitation, though the source specifically describes Thompson Sampling for budget allocation.

## Contradictions
- No direct contradiction found. The source complements existing attribution and targeting pages by showing a later-stage marketplace case where measurement, LTV forecasting, and bidding are automated into a production marketing platform.
