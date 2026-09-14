---
title: "有价值的数据应该如何交易"
type: source
tags: [data-trading, advertising, adtech, privacy]
date: 2017-06-16
source_file: /mnt/ken_personal_wiki/Articles/Blog - wulc - 有价值的数据应该如何交易.md
---

## Summary
[[Wulc]] summarizes a Zhihu Live on which user behavior data is valuable, how [[DataManagementPlatform]] businesses package and trade advertising labels, and why data trading raises privacy constraints. The article and inspected diagrams distinguish first-party, second-party, and third-party data; compare first-party and third-party DMP business models; and show DMP, ADX, and DSP systems using real-time bidding paths to attach label data to ad impressions.

## Key Claims
- Behavior data has a value-density gradient: conversion and cart actions are highest intent, search and clicks are also valuable, page views and shares are weaker, and forced ad exposure is nearly worthless or even harmful.
- User identifiers are foundational because behavior traces need to be tied to a user before they can support targeting, with cookies, IDFA, Android ID, IMEI, and fingerprinting carrying different persistence and policy tradeoffs.
- First-party and second-party data sit with advertisers and ad platforms, while third-party data comes from outside providers that do not directly participate in the ad transaction.
- First-party DMPs process advertiser-owned data into requested labels without reselling the advertiser's raw data unless separately authorized.
- Third-party DMPs collect data from multiple data providers, apply their own label logic, and sell label data through ADX/DSP channels, sharing revenue back to providers.
- DMP-to-DSP data trading usually rides through ADX infrastructure so label data can be attached to real-time bid requests without every DMP and DSP needing a direct integration.
- Impression-based data pricing may underprice data by raising traffic prices through broader bidder participation, while limited label sales would require auction-style allocation.

## Key Quotes
> "数据有价值密度之分" - on why high-intent behavior can matter more than raw volume.

> "用户ID，也就是用户标示，是最重要的数据" - on identity resolution as the precondition for usable behavior data.

> "目前对于这个领域相关的研究课题是差分隐私" - on differential privacy as a response to sparse behavior-data reidentification.

## Connections
- [[Wulc]] - author and summarizer of the Zhihu Live.
- [[DataManagementPlatform]] - central institution for processing and trading first-party or third-party advertising labels.
- [[DataMonetization]] - data value is realized through label products, improved targeting, and impression-linked payments.
- [[ProgrammaticAdvertising]] - ADX and DSP infrastructure provides the trading path for DMP labels.
- [[BehavioralData]] - decision, active, semi-active, passive, and social-relation signals are ranked by intent strength.
- [[BehavioralTargeting]] - high-value actions and user IDs become the evidence layer for audience labels.
- [[LocationDataPrivacy]] - the source's privacy section generalizes the reidentification and consent concerns already visible in location-data cases.

## Contradictions
- No direct contradictions found. The source deepens earlier Wulc advertising-data notes by adding DMP business models, data-trading pricing concerns, and explicit privacy constraints around PII, opt-out, retention, sparse-data reidentification, and differential privacy.
