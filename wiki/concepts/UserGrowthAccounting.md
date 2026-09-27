---
title: "User Growth Accounting"
type: concept
tags: [growth, retention, metrics, product-management]
sources:
  - diligence-at-social-capital-part-1-accounting-for-user-growth
last_updated: 2026-09-27
knowledge_schema: synthesis-v1
---

## Definition
[[UserGrowthAccounting]] is a period-over-period decomposition of active users into new, retained, resurrected, and churned groups so a team can distinguish durable growth from acquisition that merely replaces departing users.

## Current Synthesis
The framework starts with two identities: current active users equal new plus retained plus resurrected users, and prior-period active users equal retained plus churned users. Subtraction yields net growth as new plus resurrected minus churned. That decomposition makes a rising MAU line diagnostically useful: teams can see whether retention is improving, whether resurrection campaigns add users without later churn, and whether acquisition is compensating for a weak product base. The accompanying quick ratio divides new plus resurrected users by churned users; a value above one means inflow exceeds loss, but the same net growth can still be more or less attractive depending on the underlying retention burden.

## Key Claims
- Active-user growth should be decomposed because topline MAU cannot reveal how many users repeatedly receive value.
- New, retained, resurrected, and churned users form a complete period-over-period accounting when “active” and the comparison window are consistently defined.
- The user-growth quick ratio measures inflow against churn and must exceed one for the active-user base to grow.
- Two products can have identical net MAU growth while one has materially better retention and a stronger base for future acquisition.
- Retention improvement usually deserves priority over accelerating acquisition when most acquired users soon churn.
- Measurement cadence should match natural product frequency; a rolling 28-day window can reduce calendar noise, while weekly or daily views require sufficiently frequent use.

## Evidence
- Accounting identity: [[diligence-at-social-capital-part-1-accounting-for-user-growth]] defines current MAU as new plus retained plus resurrected users and prior MAU as retained plus churned users.
- Growth equation: [[diligence-at-social-capital-part-1-accounting-for-user-growth]] derives net MAU change as new plus resurrected minus churned.
- Inflow-to-loss test: [[diligence-at-social-capital-part-1-accounting-for-user-growth]] defines the user-growth quick ratio as `(new + resurrected) / churned` and explains that growth requires a value above one.
- Hidden dynamics: [[diligence-at-social-capital-part-1-accounting-for-user-growth]] uses two fictional decompositions with the same roughly 12% monthly MAU growth but different retention and quick-ratio profiles.
- Investment and operating implication: [[diligence-at-social-capital-part-1-accounting-for-user-growth]] prefers the higher-retention case and recommends fixing churn before pushing harder on referrals or paid acquisition.
- Cadence choice: [[diligence-at-social-capital-part-1-accounting-for-user-growth]] describes rolling 28-day, weekly, daily, and sub-daily variants tied to product frequency.

## Counterevidence & Qualifications
The framework comes from one 2015 investor-practitioner article and uses fictional examples rather than comparative outcome data. Results depend on the definition of “active,” identity resolution, observation window, seasonality, cohort mix, and whether resurrection is durable. A ratio above one establishes net active-user growth, not product-market fit, monetization, unit economics, causal product improvement, or a healthy acquisition cost. Monthly accounting can also misread valuable but naturally episodic products, while shorter windows can amplify churn mechanically when the product is not meant to be used that often.

## What Changed
- Created the concept and its core accounting identities.
- Added the user-growth quick ratio as an inflow-to-churn diagnostic.
- Distinguished identical topline growth from the retention quality underneath it.

## Related Concepts
- [[ProductMarketFit]] - user-growth decomposition supplies one traction diagnostic but does not by itself prove fit.
- [[ProductLedRetention]] - retention quality determines whether acquisition compounds or continually replaces churn.
- [[VanityMetrics]] - cumulative registrations and unexamined MAU can hide weak recurring value.
- [[ProductMetricLadder]] - activity definitions and measurement windows should reflect the user behavior a product is meant to create.
- [[DAUMAU]] - frequency ratio that complements growth decomposition but also depends on natural product cadence.
- [[CustomerAcquisitionCost]] - aggressive acquisition is harder to justify when churn destroys acquired-user value.
