---
title: "Audience Targeting"
type: concept
tags: [advertising, data, user-profiling, segmentation]
sources:
  - blog-wulc-zen-yang-yong-shu-ju-dong-cha-ni-de-yong-hu
last_updated: 2026-09-15
knowledge_schema: synthesis-v1
---

## Definition
[[AudienceTargeting]] is the practice of converting user, context, advertiser, and ad information into labels or scores that let an advertising system identify useful audiences for campaigns or models.

## Current Synthesis
The source treats audience targeting as a demand-shaped description problem. Raw behavior logs are too disorderly to use directly, so systems create labels; however, the label set should be driven by advertiser needs and downstream optimization rather than by an abstract wish to describe users completely. User profiles and targeting labels overlap, but their emphasis differs: user profiles favor interpretable attributes such as demographics, lifestyle, occupation, and income, while targeting can favor less interpretable but more effective labels for prediction, traffic sale, and campaign optimization.

## Key Claims
- Audience targeting transforms raw user behavior into demand-relevant labels rather than neutral biographies of users.
- User profiles and audience targeting overlap, but profiling emphasizes interpretability while targeting emphasizes optimization and effect.
- Targeting can label user attributes, media context, user-advertiser relationships, and ad attributes.
- Label systems are used both to sell traffic to advertisers and to provide features for estimation modules such as CTR prediction.
- Demand-driven, non-structured tag systems can outperform tidy taxonomies when advertiser needs are specific.
- Good tag design starts from an industry and its customer decision process, then creates labels for meaningful decision stages.
- Targeting effectiveness should be tested empirically, such as by checking whether narrower tagged audiences show higher CTR on a Reach/CTR curve.

## Evidence
- Demand-shaped description: [[blog-wulc-zen-yang-yong-shu-ju-dong-cha-ni-de-yong-hu]] says users should not be described by assumption, but labeled according to demand-side needs.
- Profiling versus targeting: [[blog-wulc-zen-yang-yong-shu-ju-dong-cha-ni-de-yong-hu]] and its inspected comparison diagram distinguish interpretable user profiling from optimizable audience targeting.
- Label dimensions: [[blog-wulc-zen-yang-yong-shu-ju-dong-cha-ni-de-yong-hu]] identifies user, context, user-advertiser, and ad dimensions, with examples such as demographics, region, behavior, keywords, topics, channels, and advertiser-specific user states.
- System uses: [[blog-wulc-zen-yang-yong-shu-ju-dong-cha-ni-de-yong-hu]] says labels support advertiser-facing traffic sale and model-feature construction for estimation modules.
- Taxonomy qualification: [[blog-wulc-zen-yang-yong-shu-ju-dong-cha-ni-de-yong-hu]] contrasts Yahoo-style structured categories with BlueKai-style demand-driven categories such as intent, B2B, past purchase, geo/demo, lifestyle, and financial estimates.
- Decision-process design: [[blog-wulc-zen-yang-yong-shu-ju-dong-cha-ni-de-yong-hu]] uses the automobile-purchase path of budget, use case, and brand as an example of industry-specific labels.
- Evaluation curve: [[blog-wulc-zen-yang-yong-shu-ju-dong-cha-ni-de-yong-hu]] uses an inspected Reach/CTR chart to argue that lower reach should usually correspond to higher CTR if a targeting label is effective.

## Counterevidence & Qualifications
The source is an advertising-oriented 2017 overview and does not evaluate later privacy regulation, cookie loss, fairness, user consent, data minimization, or modern platform changes. It presents advertiser effectiveness as the main criterion, so its framework should be paired with privacy and trust considerations before being treated as a complete user-data strategy.

## What Changed
- Created the concept to capture the wiki's tag-system and evaluation layer for advertising user insight.

## Related Concepts
- [[BehavioralTargeting]] - behavioral targeting is the source's main method for assigning audience labels from historical actions.
- [[BehavioralData]] - supplies the raw action traces that targeting converts into labels.
- [[DataMonetization]] - targeting raises the value of advertising traffic by improving advertiser fit.
- [[ProgrammaticAdvertising]] - uses audience labels and advertiser-specific user states in automated bidding.
- [[ProductUserSegmentation]] - both divide users into meaningful groups, but audience targeting is optimized for advertising outcomes.
- [[MarketingAttribution]] - complements targeting by measuring whether targeted marketing produced downstream value.
