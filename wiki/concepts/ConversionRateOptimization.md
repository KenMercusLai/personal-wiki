---
title: "Conversion Rate Optimization"
type: concept
tags: [product, experimentation, metrics, fundraising]
sources:
  - a-first-peek-behind-the-scenes-of-hillary-clintons-technology-operation
last_updated: 2026-09-13
knowledge_schema: synthesis-v1
---

## Definition
[[ConversionRateOptimization]] is the practice of changing a product flow, measuring user behavior, and using experiment results to increase the share of users who complete a desired action.

## Current Synthesis
The Clinton campaign source shows conversion optimization in a high-pressure fundraising context. The donation team did not only add payment features; it simplified an account and saved-card flow after donation, reused the donor's email address, detected account state, and removed an extra click. The visible result was a large measured increase in saved-card opt-in, and the follow-up reporting graph suggests the winning experiment carried into production behavior.

## Key Claims
- Conversion optimization can target operational efficiency, not only top-line acquisition.
- Removing account confusion and repeated data entry can materially change completion rates.
- A/B test wins are stronger when the metric improvement appears after full rollout, not only inside the experiment.
- Campaign fundraising products can apply the same experimentation discipline as commercial products.
- Conversion metrics need interpretation because some test lifts fail to appear in later reporting.

## Evidence
- Donation context: [[a-first-peek-behind-the-scenes-of-hillary-clintons-technology-operation]] says the web donation platform processed more than 1 million donations and ran around 80 A/B tests.
- Fee efficiency: [[a-first-peek-behind-the-scenes-of-hillary-clintons-technology-operation]] says ACH support was added partly to reduce credit-card fees.
- Flow simplification: [[a-first-peek-behind-the-scenes-of-hillary-clintons-technology-operation]] describes using the donor's submitted email, detecting account status, and removing a click in the saved-card path.
- Experiment result: [[a-first-peek-behind-the-scenes-of-hillary-clintons-technology-operation]] reports a 238.8% saved-card opt-in increase at 99% confidence.
- Production validation: [[a-first-peek-behind-the-scenes-of-hillary-clintons-technology-operation]] shows a saved-card opt-in graph with a spike after the winning flow was deployed to all visitors.

## Counterevidence & Qualifications
The source reports campaign-internal results and screenshots rather than raw experiment data. It also notes a common problem: some A/B test improvements do not later appear in regular reports after rollout. The concept therefore depends on both experimental evidence and post-deployment monitoring.

## What Changed
- Created the concept from the Clinton campaign donation-platform example.

## Related Concepts
- [[ProductMetricLadder]] - conversion metrics can act as short-cycle proxies for larger fundraising goals.
- [[CustomerLedProductDevelopment]] - user confusion in a flow can reveal product improvement opportunities.
- [[OfficialCampaignTechnology]] - the campaign's staffed technology team owned the fundraising product surface.
- [[BehavioralData]] - optimization depends on measured user actions.
