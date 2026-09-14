---
title: "Behavioral Targeting"
type: concept
tags: [advertising, behavioral-data, targeting, user-profiling]
sources:
  - blog-wulc-zen-yang-yong-shu-ju-dong-cha-ni-de-yong-hu
  - blog-wulc-you-jia-zhi-de-shu-ju-ying-gai-ru-he-jiao-yi
last_updated: 2026-09-15
knowledge_schema: synthesis-v1
---

## Definition
[[BehavioralTargeting]] is audience targeting that assigns user labels or scores from historical behavior such as browsing, search, ad exposure, ad clicks, sharing, and conversion events.

## Current Synthesis
The sources frame behavioral targeting as a scalable, time-sensitive feature extraction problem whose input behaviors have different value density. A user's actions are mapped to labels by analyzing the content objects behind those actions: pages, ads, search results, product categories, and conversion items. Those labels are then weighted because different behaviors carry different intent strength, and they are accumulated with sliding windows or time decay because user intent often expires quickly. The result is a per-user score for each label, compared against thresholds and evaluated by whether the selected audience produces higher CTR at lower reach.

## Key Claims
- Behavioral targeting converts user actions into labels by analyzing the content, ad, query, or product object touched by the action.
- Browsing and ad-click behavior can be labeled through keyword extraction, manual labeling, classification, or topic modeling over associated text.
- Search behavior needs special handling: general search can infer labels from search-result content, while vertical search can reuse domain categories from sites such as ecommerce, travel, or automobile platforms.
- Different behaviors require different weights because purchase, cart, search, click, view, share, and ad-exposure events express different levels of intent.
- Behavior labels must handle recency because the path from attention to purchase is often short-lived.
- Session logs organized by user ID make targeting a local computation that can scale through MapReduce-style processing.
- Target scores become operational only after thresholds define who belongs to a label audience.

## Evidence
- Behavior-to-label process: [[blog-wulc-zen-yang-yong-shu-ju-dong-cha-ni-de-yong-hu]] shows browsing, search, and ad-click inputs flowing into label scores for education, travel, and sports examples.
- Content extraction methods: [[blog-wulc-zen-yang-yong-shu-ju-dong-cha-ni-de-yong-hu]] diagrams behavior types leading through content, ad landing pages, descriptions, search results, query outputs, product categories, and conversion items into keywords or labels.
- Search distinction: [[blog-wulc-zen-yang-yong-shu-ju-dong-cha-ni-de-yong-hu]] distinguishes general search, which needs result-content extraction, from vertical search, which can often reuse existing domain classifications.
- Weighting model: [[blog-wulc-zen-yang-yong-shu-ju-dong-cha-ni-de-yong-hu]] uses a Poisson-frequency model where a tag's normalized click count depends on a weighted sum of raw behavior statistics.
- Intent hierarchy: [[blog-wulc-you-jia-zhi-de-shu-ju-ying-gai-ru-he-jiao-yi]] ranks conversion/pre-conversion, search and clicks, sharing and page views, and forced ad exposure by decreasing targeting value.
- Recency handling: [[blog-wulc-zen-yang-yong-shu-ju-dong-cha-ni-de-yong-hu]] compares sliding-window accumulation with time decay and says time decay is usually more computationally efficient.
- Session-log organization: [[blog-wulc-zen-yang-yong-shu-ju-dong-cha-ni-de-yong-hu]] describes combining behavior logs into user-keyed session logs for local targeting computation.
- Threshold evaluation: [[blog-wulc-zen-yang-yong-shu-ju-dong-cha-ni-de-yong-hu]] says a user receives scores over all labels and enters a target audience when the score exceeds the chosen threshold.

## Counterevidence & Qualifications
The sources emphasize practical advertising utility and scalability, and the newer data-trading source explicitly notes PII, opt-out, retention, and reidentification concerns. They still do not cover privacy rights, consent management, identity resolution errors, cross-device ambiguity, adversarial behavior, or whether higher CTR translates into durable business value. Their modeling details should be treated as an introductory 2017 account rather than a current production adtech recipe.

## What Changed
- Added the value-density hierarchy of behavior signals to the existing behavior-to-label pipeline.

## Related Concepts
- [[AudienceTargeting]] - behavioral targeting is a method for building audience labels.
- [[BehavioralData]] - provides the event traces that behavioral targeting consumes.
- [[DataMonetization]] - behavior-derived labels make traffic more valuable to advertisers.
- [[DataManagementPlatform]] - may package behavior-derived labels for trading.
- [[ProgrammaticAdvertising]] - can consume behavioral labels for bidding, retargeting, and look-alike audiences.
- [[MarketingAttribution]] - evaluates downstream impact beyond immediate targeting and CTR.
- [[LocationDataPrivacy]] - related because behavioral and scene inference can expose sensitive user states.
