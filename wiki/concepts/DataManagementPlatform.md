---
title: "Data Management Platform"
type: concept
tags: [advertising, adtech, data, targeting]
sources:
  - blog-wulc-you-jia-zhi-de-shu-ju-ying-gai-ru-he-jiao-yi
last_updated: 2026-09-15
knowledge_schema: synthesis-v1
---

## Definition
[[DataManagementPlatform]] is advertising data infrastructure that collects or receives user data, processes it into audience labels, and makes those labels usable for site operations or ad buying.

## Current Synthesis
The source presents DMPs as the institutional layer between raw behavior data and tradable advertising labels. A first-party DMP works for an advertiser or data owner: it receives first-party data, may combine it with permitted third-party or public-market data, and produces the user labels the advertiser needs for operations or ad placement without reselling the advertiser's data by default. A third-party DMP works for smaller data providers that lack processing or sales capability: it collects raw data from multiple providers, applies its own labeling logic, sells label data toward DSP demand through ADX infrastructure, and shares revenue back to providers.

## Key Claims
- DMPs create value by turning raw user data into advertiser-usable labels rather than by merely moving files.
- First-party DMPs are service providers for advertiser-owned data and should not resell that data without agreement.
- Third-party DMPs aggregate data from providers that have data but not enough processing, sales, or advertiser-demand access.
- DMP label products reach advertisers indirectly because advertisers often delegate targeting execution to DSPs.
- ADX infrastructure lowers integration cost by carrying label data alongside real-time bidding requests.
- DMP pricing creates a market-design problem: unlimited impression-based sales may raise traffic prices while muting the apparent price of data.

## Evidence
- Label creation: [[blog-wulc-you-jia-zhi-de-shu-ju-ying-gai-ru-he-jiao-yi]] describes DMPs as collecting first-party or provider data and processing it into user labels.
- First-party boundary: [[blog-wulc-you-jia-zhi-de-shu-ju-ying-gai-ru-he-jiao-yi]] says first-party DMPs process first-party data but cannot use or sell it unless the advertiser agrees.
- Third-party aggregation: [[blog-wulc-you-jia-zhi-de-shu-ju-ying-gai-ru-he-jiao-yi]] diagrams data providers sending raw data to a third-party DMP, which then sells label data and shares revenue.
- DSP connection: [[blog-wulc-you-jia-zhi-de-shu-ju-ying-gai-ru-he-jiao-yi]] says advertisers often rely on DSPs for targeting, so data transactions occur between DMPs and DSPs.
- ADX routing: [[blog-wulc-you-jia-zhi-de-shu-ju-ying-gai-ru-he-jiao-yi]] diagrams DMP data flowing to ADX and then to several DSPs with bid requests and attached data.
- Pricing qualification: [[blog-wulc-you-jia-zhi-de-shu-ju-ying-gai-ru-he-jiao-yi]] argues that paying by actual ad impressions can indirectly lift traffic prices and understate data's value.

## Counterevidence & Qualifications
The source is a 2017 advertising-market explanation rather than a current compliance or product architecture guide. It discusses privacy principles such as avoiding PII, opt-out, retention limits, sparse-data reidentification, and differential privacy, but it does not cover later regulatory changes, cookie deprecation, clean rooms, consent-management infrastructure, or modern mobile identifier limits in depth.

## What Changed
- Created the concept to capture the DMP business and infrastructure layer behind advertising data trading.

## Related Concepts
- [[DataMonetization]] - DMPs are one institutional mechanism for monetizing audience data.
- [[ProgrammaticAdvertising]] - DMP labels are delivered into DSP and ADX bidding workflows.
- [[BehavioralData]] - raw user actions are the main evidence that DMPs process into labels.
- [[BehavioralTargeting]] - DMP labels often depend on behavior-derived intent and category scores.
- [[AudienceTargeting]] - DMP label products are demand-facing audience segments.
- [[LocationDataPrivacy]] - DMP use of behavioral and identity data raises privacy and reidentification risks similar to sensitive movement data.
