---
title: "Customer Acquisition Cost"
type: concept
tags: [saas, metrics, unit-economics]
sources:
  - a-comprehensive-data-guide-to-why-you-shouldnt-discount
  - acquisition-is-easy-retention-is-hard-product-habits
  - billboards-for-small-businesses-costs-advice-and-thinking-twice
  - burning-money-on-paid-ads-for-a-dev-tool-what-weve-learned-posthog
last_updated: 2026-09-15
knowledge_schema: synthesis-v1
---

## Definition
[[CustomerAcquisitionCost]] is the amount spent to acquire a customer, usually evaluated against the recurring revenue and time needed to recover that spend.

## Current Synthesis
The sources treat CAC as meaningful only when paired with retention quality, channel fit, customer value, and conversion validity. The discounting source uses CAC recovery to show why a lower contract price can harm SaaS economics even when it increases signups: a 20% discount on a $500 monthly customer who costs $6,000 to acquire reduces the monthly revenue available for payback, extending recovery by about three months before considering the higher churn risk of discounted customers. The Product Habits source adds a market-level warning: acquisition tools and distribution may be easier to access, but competition, saturated channels, and weak-fit lead chasing can make CAC rise while retention becomes harder. The billboard source adds a fixed-media version of the same discipline: broad awareness only makes sense when the business can tolerate a high acquisition cost and plausibly convert a broad audience. PostHog adds a digital version of the same risk: cheap reported CPA can be a trap when bots or irrelevant conversions make the apparent customer count low quality.

## Key Claims
- CAC must be evaluated against actual realized subscription revenue, not only customer count.
- Discounts can lengthen CAC recovery by lowering monthly revenue per customer.
- Higher churn among discounted customers compounds CAC risk because the company may never recover acquisition spend.
- Easier acquisition channels do not guarantee cheaper or healthier acquisition when markets saturate.
- CAC risk increases when marketing attracts customers who are likely to churn.
- Expensive offline awareness channels require enough customer value, audience breadth, and attribution confidence to justify their fixed cost.
- Low apparent CPA can be misleading when a channel produces bots, irrelevant signups, or weak-fit conversions.

## Evidence
- Recovery example: [[a-comprehensive-data-guide-to-why-you-shouldnt-discount]] compares a $500/month customer with $6,000 CAC under minimal versus aggressive discounting.
- Discount effect: [[a-comprehensive-data-guide-to-why-you-shouldnt-discount]] says a 20% discount can extend CAC recovery by three months.
- Churn compounding: [[a-comprehensive-data-guide-to-why-you-shouldnt-discount]] argues that discounted customers churn more often, worsening the payback problem.
- Market saturation: [[acquisition-is-easy-retention-is-hard-product-habits]] reports the SaaSFest claim that CAC is steadily increasing as competition and demands rise.
- Lead quality: [[acquisition-is-easy-retention-is-hard-product-habits]] warns that cheap distribution can waste time and money on customers who are going to churn.
- Billboard threshold: [[billboards-for-small-businesses-costs-advice-and-thinking-twice]] says billboards may make sense for a business willing to spend roughly $1,000 to gain a customer, especially for high-ticket or mass-market offers.
- False cheapness: [[burning-money-on-paid-ads-for-a-dev-tool-what-weve-learned-posthog]] warns against being seduced by Google Display's low reported CPA because PostHog saw bots and irrelevant conversions.

## Counterevidence & Qualifications
The sources supply strategic and illustrative CAC arguments rather than a complete model for every business. Actual payback depends on gross margin, contract length, expansion revenue, onboarding cost, sales compensation, channel saturation, conversion quality, bot filtering, physical placement quality, and whether lower prices or broader acquisition campaigns change retention enough to offset their apparent conversion gains.

## What Changed
- Added PostHog's warning that low reported CPA can be false cheapness when conversions are bots or weak-fit traffic.

## Related Concepts
- [[SaaSDiscounting]] - discounts reduce the revenue available to recover CAC.
- [[CustomerLifetimeValue]] - CAC becomes meaningful when compared with long-term customer value.
- [[SaaSPricing]] - pricing choices affect payback timing.
- [[SaaSMarketing]] - acquisition channels create CAC that must be recovered through retention.
- [[SaaSRetention]] - retention determines whether acquired customers repay CAC.
- [[BillboardAdvertising]] - billboard spend should be tested against customer value and acquisition-cost tolerance.
- [[DeveloperToolPaidAdvertising]] - developer-tool ad channels should be judged by conversion quality, not only CPA.
