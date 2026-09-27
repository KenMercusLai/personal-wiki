---
title: "DAU/MAU"
type: concept
tags: [product-metrics, engagement, retention]
sources:
  - dau-mau-is-an-important-metric-to-measure-engagement-but-heres-where-it-fails-at-andrewchen
last_updated: 2026-09-26
knowledge_schema: synthesis-v1
---

## Definition
[[DAUMAU]] is the ratio of daily active users to monthly active users, expressed as a percentage, used to estimate how much of a product's monthly audience returns on a typical day.

## Current Synthesis
DAU/MAU is most informative when the product's intended value has a daily cadence. A high ratio can reveal strong habitual use in communication or social products, but the same benchmark can misclassify valuable travel, recruiting, enterprise, mobility, or commerce products whose demand is naturally episodic. Frequency must therefore be interpreted alongside retention, monetization, transaction value, accumulated data or content, and the behavior of consistently active cohorts.

The ratio is also sensitive to intervention design. Reactivation messages can grow MAU faster than DAU and lower DAU/MAU even while absolute usage rises. Teams should treat the ratio as one rung in a [[ProductMetricLadder]], define “active” around meaningful product value, segment users and cohorts, and test whether frequency increases with network size or accumulated product investment rather than optimizing the aggregate percentage in isolation.

## Key Claims
- DAU/MAU measures daily reach within the monthly active population, not value per interaction or durable retention by itself.
- The metric fits products with naturally daily behavior better than episodic or weekly categories.
- A low ratio can coexist with high transaction value, monetization, or uniquely valuable data.
- Growth in MAU can mechanically reduce the ratio when DAU grows more slowly, so a falling ratio does not necessarily mean less total engagement.
- Hardcore-user cohorts and frequency correlated with network, content, or saved value can reveal product strength hidden by the aggregate ratio.
- Metric choice should follow product cadence and business model rather than borrowed cross-category benchmarks.

## Evidence
Daily-use fit:
- [[dau-mau-is-an-important-metric-to-measure-engagement-but-heres-where-it-fails-at-andrewchen]] says Facebook popularized the ratio and historically exceeded 50%, while communication combines high frequency with high retention.

Episodic-value boundary:
- [[dau-mau-is-an-important-metric-to-measure-engagement-but-heres-where-it-fails-at-andrewchen]] uses Uber, LinkedIn, Airbnb, Booking, enterprise software, and infrequent commerce to show that valuable interactions need not happen daily.

Ratio mechanics and alternatives:
- [[dau-mau-is-an-important-metric-to-measure-engagement-but-heres-where-it-fails-at-andrewchen]] argues that notifications may increase MAU faster than DAU and recommends examining hardcore users plus usage changes associated with network size or accumulated content.

## Counterevidence & Qualifications
The source gives practitioner benchmarks and examples without a comparative dataset, a stable definition of “active,” cohort distributions, or causal tests. DAU/MAU can vary with seasonality, time zones, audience growth, bots, notification campaigns, category, and measurement windows. A high ratio can also coexist with churn or compulsive low-value use, while a low ratio may hide strong weekly or event-driven retention. The article's repeated chart reference resolves to unrelated HTML rather than an inspectable chart, so its Flurry comparison is not independently recoverable from the supplied source assets.

## What Changed
- Established DAU/MAU as a cadence-dependent engagement metric rather than a universal product-quality or product-market-fit score.
- Added cohort behavior, network or content accumulation, transaction value, monetization, and retention as complementary evidence.

## Related Concepts
- [[ProductMetricLadder]] - places DAU/MAU beside longer-horizon outcomes and category-appropriate countermetrics.
- [[ProductMarketFit]] - daily frequency can support fit evidence but should not define it across categories.
- [[ProductLedRetention]] - repeated value and hardcore cohort behavior help interpret the ratio.
- [[NetworkEffects]] - usage that rises with network size may explain improving cohort frequency.
- [[ProductStickiness]] - daily return can indicate habit, but stickiness can also arise at weekly or episodic cadences.
