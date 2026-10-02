---
title: "I’m Sorry, But Those Are Vanity Metrics"
type: source
tags: [metrics, product-analytics, customer-behavior, data-culture]
date: 2017-04-04
source_file: "/mnt/ken_personal_wiki/Articles/I’m Sorry, But Those Are Vanity Metrics - First Round Review.md"
---

## Summary
[[FirstRoundReview]] interviews [[LloydTabb]] about separating outward-facing [[VanityMetrics]] from operational [[ClarityMetrics]] that help teams improve customer behavior and business quality. Tabb recommends time-ordered event streams, behavior-linked attribution, direct investigation of outliers, and department-specific failure and poison rates, using [[Looker]], [[LiveOps]], ride sharing, advertising, software, marketplaces, and ecommerce as practitioner examples. The sole embedded image is a decorative photograph of Tabb speaking at a Looker-branded event and adds no evidence beyond identity and setting, so it was omitted.

## Key Claims
- Vanity metrics such as users, downloads, impressions, and revenue growth can support external comparison, fundraising, and partnerships without explaining how to improve the business.
- Clarity metrics should be inexpensive to observe, hard to misinterpret, operationally actionable, and predictive of valuable behavior over time.
- Service businesses should seek early proxies for customer experience: pickup time can predict repeat ride-sharing use, while LiveOps treated contractor attendance as a proxy for accountability and routed more calls to reliable agents.
- Advertising and ecommerce measurement should link acquisition source and cost to later behavior, purchases, retention, and payback rather than stop at impressions or click-through rates.
- User activity should be organized as chronological event streams so teams can inspect clusters, gaps, drop-off, and changing behavior rather than isolate transactions in separate tables.
- Software companies should distinguish accounts or downloads from active engagement, then contact unusual active or inactive users to understand the qualitative mechanism behind the data.
- Department-specific failure rates expose broken promises, while poison rates identify first experiences severe enough to drive customers away and suppress future referral.
- Ecommerce loyalty depends on repeat purchase and reliable logistics more than one-time basket size, and data fluency must extend beyond a central analytics team for operational metrics to guide daily work.

## Key Quotes
> "Vanity metrics aren’t useless. They have their use case, but are points of comparison for other people to evaluate you." - Tabb on preserving a bounded external role for surface measures.

> "Data can’t reveal how people feel." - Tabb on pairing event-stream analysis with direct customer conversations.

## Connections
- [[LloydTabb]] - interview subject and source of the vanity-versus-clarity framework.
- [[Looker]] - company where Tabb used active engagement and customer-outlier calls as operating signals.
- [[LiveOps]] - call-center case where contractor attendance reportedly predicted agent performance better than call length or upselling.
- [[VanityMetrics]] - aggregate measures can impress outsiders while obscuring retention, service quality, or unit economics.
- [[ClarityMetrics]] - source-specific name for actionable leading indicators tied to individual behavior over time.
- [[ProductMetricLadder]] - adds early behavioral proxies, failure measures, and qualitative investigation beneath a small external or executive scoreboard.
- [[MarketingAttribution]] - argues for linking impressions and clicks through acquisition, purchase, and lifetime value.
- [[UnitEconomics]] - acquisition cost, payback time, retention, and repeat behavior qualify apparently strong user or transaction growth.
- [[CustomerLifetimeValue]] - depends on source-linked acquisition quality and behavior after signup, not only top-of-funnel volume.

## Contradictions
- No direct contradiction was found. The article strengthens existing warnings about surface metrics while explicitly preserving their use for external comparison, fundraising, awareness, and partnerships.
- The examples are Tabb's practitioner anecdotes rather than disclosed datasets or controlled studies. The source gives no definitions, cohort windows, sample sizes, confidence estimates, or independent validation for the claimed predictive relationships or revenue effects.
- Attendance, pickup time, active minutes, repeat purchase, and poison rates can themselves become vanity or gaming targets if definitions are weak, context changes, or teams optimize the proxy rather than the customer outcome.
- The critique of A/B testing is too broad to establish that direct interviews or event-stream inspection generally outperform well-designed experiments. Its mistaken-click example instead shows why immediate click-through needs downstream countermetrics and causal interpretation.
