---
title: "Audience Targeting"
type: concept
tags: [advertising, data, user-profiling, segmentation]
sources:
  - blog-wulc-zen-yang-yong-shu-ju-dong-cha-ni-de-yong-hu
  - building-lyfts-marketing-automation-platform-lyft-engineering
last_updated: 2026-09-15
knowledge_schema: synthesis-v1
---

## Definition
[[AudienceTargeting]] is the practice of converting user, context, advertiser, and ad information into labels or scores that let an advertising system identify useful audiences for campaigns or models.

## Current Synthesis
The sources treat audience targeting as a demand-shaped description and action problem. Raw behavior logs are too disorderly to use directly, so systems create labels; however, the label set should be driven by advertiser needs and downstream optimization rather than by an abstract wish to describe users completely. Lyft adds the campaign-operations side: high-value user segments, audiences, creatives, incentives, and regional context become levers that an automation platform can identify, test, and deploy across acquisition channels.

## Key Claims
- Audience targeting transforms raw user behavior into demand-relevant labels rather than neutral biographies of users.
- User profiles and audience targeting overlap, but profiling emphasizes interpretability while targeting emphasizes optimization and effect.
- Targeting can label user attributes, media context, user-advertiser relationships, and ad attributes.
- Label systems are used both to sell traffic to advertisers and to provide features for estimation modules such as CTR prediction.
- Good tag design starts from an industry and its customer decision process, then creates labels for meaningful decision stages.
- Targeting effectiveness should be tested empirically, such as by checking whether narrower tagged audiences show higher CTR on a Reach/CTR curve.
- At acquisition-platform scale, targeting becomes one of several deployable levers alongside bids, budgets, creatives, incentives, and channel strategy.

## Evidence
- Demand-shaped description: [[blog-wulc-zen-yang-yong-shu-ju-dong-cha-ni-de-yong-hu]] says users should not be described by assumption, but labeled according to demand-side needs.
- Profiling versus targeting: [[blog-wulc-zen-yang-yong-shu-ju-dong-cha-ni-de-yong-hu]] and its inspected comparison diagram distinguish interpretable user profiling from optimizable audience targeting.
- Label dimensions: [[blog-wulc-zen-yang-yong-shu-ju-dong-cha-ni-de-yong-hu]] identifies user, context, user-advertiser, and ad dimensions, with examples such as demographics, region, behavior, keywords, topics, channels, and advertiser-specific user states.
- System uses: [[blog-wulc-zen-yang-yong-shu-ju-dong-cha-ni-de-yong-hu]] says labels support advertiser-facing traffic sale and model-feature construction for estimation modules.
- Taxonomy qualification: [[blog-wulc-zen-yang-yong-shu-ju-dong-cha-ni-de-yong-hu]] contrasts Yahoo-style structured categories with BlueKai-style demand-driven categories such as intent, B2B, past purchase, geo/demo, lifestyle, and financial estimates.
- Decision-process design: [[blog-wulc-zen-yang-yong-shu-ju-dong-cha-ni-de-yong-hu]] uses the automobile-purchase path of budget, use case, and brand as an example of industry-specific labels.
- Evaluation curve: [[blog-wulc-zen-yang-yong-shu-ju-dong-cha-ni-de-yong-hu]] uses an inspected Reach/CTR chart to argue that lower reach should usually correspond to higher CTR if a targeting label is effective.
- Acquisition levers: [[building-lyfts-marketing-automation-platform-lyft-engineering]] lists audiences, high-value user segments, incentives, creatives, and campaign strategies among the decisions Lyft wanted to automate.
- Funnel placement: [[building-lyfts-marketing-automation-platform-lyft-engineering]] and its inspected funnel diagram place acquisition at the top of the onboarding funnel across awareness, consideration, and install/sign-up channels.

## Counterevidence & Qualifications
The Wulc source is an advertising-oriented 2017 overview and does not evaluate later privacy regulation, cookie loss, fairness, user consent, data minimization, or modern platform changes. The Lyft source is a company engineering account that mentions segmentation and audiences as automation levers but does not publish details of its targeting features, model inputs, privacy boundaries, or segment performance.

## What Changed
- Added Lyft's Symphony as a case where targeting outputs become operational levers in an automated acquisition platform.
- Added the inspected funnel diagram as evidence that targeting decisions sit within a broader onboarding and channel system.

## Related Concepts
- [[BehavioralTargeting]] - behavioral targeting is the source's main method for assigning audience labels from historical actions.
- [[BehavioralData]] - supplies the raw action traces that targeting converts into labels.
- [[DataMonetization]] - targeting raises the value of advertising traffic by improving advertiser fit.
- [[ProgrammaticAdvertising]] - uses audience labels and advertiser-specific user states in automated bidding.
- [[ProductUserSegmentation]] - both divide users into meaningful groups, but audience targeting is optimized for advertising outcomes.
- [[MarketingAttribution]] - complements targeting by measuring whether targeted marketing produced downstream value.
- [[MarketingOperations]] - turns targeting labels and audience choices into campaign execution.
- [[CustomerLifetimeValue]] - expected value can define which targeted users or segments are worth acquiring.
