---
title: "Clarity Metrics"
type: concept
tags: [metrics, product-analytics, operations, customer-behavior]
sources:
  - im-sorry-but-those-are-vanity-metrics-first-round-review
last_updated: 2026-10-02
knowledge_schema: synthesis-v1
---

## Definition
[[ClarityMetrics]] are operational measures chosen to predict or explain valuable customer behavior over time and to give a team a concrete lever for improving service, engagement, retention, or reliability.

## Current Synthesis
[[LloydTabb]] contrasts clarity metrics with [[VanityMetrics]] that mainly support external comparison. A useful clarity metric is close enough to an operational mechanism to guide action: pickup delay for a ride, active engagement rather than software downloads, source-linked acquisition payback rather than click volume, repeat purchasing rather than basket size, or failures to deliver a department's promise. The measure need not capture a subjective outcome directly; it can be an inexpensive proxy, provided its relationship to later behavior is repeatedly checked.

The framework combines quantitative sequence with qualitative diagnosis. Chronological event streams reveal clusters, gaps, conversion paths, and drop-off, while outliers tell teams whom to call and what experience to investigate. Failure rates make broken promises visible across departments, and poison rates narrow attention to first experiences associated with permanent abandonment and lost referral. Metric usefulness therefore comes from prediction, actionability, temporal context, and continued contact with customers rather than from size or presentational appeal.

## Key Claims
- A clarity metric should guide an operational decision and connect plausibly to later customer behavior.
- Early service events can be more useful than aggregate usage because they expose the mechanism shaping repeat behavior.
- Time-ordered event streams preserve behavioral context that isolated transaction tables and averages can hide.
- Failure rates should be defined at the level of each department's promise and revised when the product or process changes.
- Poison rates identify severe first experiences whose cost includes both abandonment and foregone referral.
- Outlier analysis should lead to customer contact because behavioral data alone cannot explain intent, confusion, or sentiment.
- A proxy remains useful only while its relationship to the intended customer and business outcome is monitored.

## Evidence
- Service proxy design: [[im-sorry-but-those-are-vanity-metrics-first-round-review]] proposes glass fill level as a cheap restaurant-service signal and ride pickup time as a predictor of reuse.
- Accountability example: [[im-sorry-but-those-are-vanity-metrics-first-round-review]] reports that LiveOps contractor attendance predicted agent performance better than call duration or upselling and informed call routing.
- Software engagement: [[im-sorry-but-those-are-vanity-metrics-first-round-review]] says Looker initially tracked active minutes and contacted unusual active or inactive customers to interpret the pattern.
- Temporal analysis: [[im-sorry-but-those-are-vanity-metrics-first-round-review]] recommends unified event streams and active five-minute blocks to reveal sequences, clusters, inactivity, and drop-off.
- Failure and poison rates: [[im-sorry-but-those-are-vanity-metrics-first-round-review]] defines failures as undelivered promises and poison as first experiences associated with customers never returning.
- Loyalty mechanism: [[im-sorry-but-those-are-vanity-metrics-first-round-review]] treats repeat purchase and reliable delivery as stronger ecommerce operating signals than order value alone.

## Counterevidence & Qualifications
The framework comes from one favorable practitioner interview and selected anecdotes, not comparative validation. A predictive proxy is not automatically causal: reliable agents may attend more consistently without attendance interventions improving service, and active minutes can represent confusion or an idle browser rather than value. Failure and poison rates depend on event definitions, observation windows, segmentation, and counterfactual behavior; apparent abandonment may have unrelated causes. Direct calls add mechanism and sentiment but introduce selection, interviewer, recall, and social-desirability bias. Teams should therefore combine operational proxies with cohort analysis, qualitative research, guardrail metrics, and experiments suited to the decision rather than treating “clarity” as an intrinsic property of a number.

## What Changed
- Created the concept from Tabb's framework linking operational proxies, time-ordered behavior, direct customer contact, and failure analysis.

## Related Concepts
- [[VanityMetrics]] - contrasting measures useful mainly for display, comparison, or top-of-funnel description.
- [[ProductMetricLadder]] - places actionable short-cycle proxies beneath slower business outcomes.
- [[BehavioralData]] - supplies the observed events from which operational proxies are constructed.
- [[MarketingAttribution]] - connects acquisition signals to later customer and economic outcomes.
- [[CustomerLifetimeValue]] - downstream value that acquisition and retention proxies attempt to anticipate.
- [[UnitEconomics]] - tests whether observed behavior produces sustainable customer- or transaction-level value.
