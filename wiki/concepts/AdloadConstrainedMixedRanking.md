---
title: "Adload-Constrained Mixed Ranking"
type: concept
tags: [advertising, mixed-ranking, constrained-optimization, beam-search]
sources:
  - adload-constrained-mix-ranking-value-maximization
last_updated: 2026-10-07
knowledge_schema: synthesis-v1
---

## Definition
[[AdloadConstrainedMixedRanking]] jointly chooses whether a feed request should contain ads and where those ads should appear so that aggregate advertising-plus-recommendation value is maximized without exceeding an application- or session-level ad-exposure limit.

## Current Synthesis
The source treats adload as a shared capacity constraint rather than an independent per-request rule. Each request can take one of several exposure strategies, whose incremental value is the mixed list's utility above the no-ad baseline and whose weight is its ad count. Because both quantities change with the placement strategy, the aggregate problem is a dynamic knapsack. A lightweight application layer greedily ranks requests by value per ad exposure and derives a marginal threshold. The request layer then searches templates by maximizing incremental value minus that threshold times ad count, converting an otherwise cross-request effect into a local score.

The placement search preserves the internal order of recommendation and ad queues, expands one recommendation or ad slot at a time, prunes top-slot and minimum-gap violations, and retains only the best beam. The architecture is useful because it joins global adload, local layout rules, organic utility, and commercial utility in one decision. It is approximate: greedy knapsack selection need not be optimal, threshold pricing can misestimate displaced requests, utility scales require calibration, and a stale threshold needs faster refresh or pacing when traffic changes.

## Key Claims
- Adload couples requests, so request-local insertion value alone cannot determine the globally best allocation.
- Incremental request value must compare the mixed list with its no-ad baseline, including both commercial gain and changed recommendation utility.
- Strategy-dependent value and ad count turn fixed-capacity allocation into a dynamic-knapsack problem.
- A value-per-ad threshold can approximate the opportunity cost of aggregate capacity and make request-level search locally computable.
- Order-preserving beam search can enforce top-ad-slot and minimum-gap constraints while limiting combinatorial growth.
- Threshold freshness, utility-scale calibration, and approximation error are first-class operating concerns rather than post-processing details.

## Evidence
- Aggregate objective: [[adload-constrained-mix-ranking-value-maximization]] and its formulation image maximize advertising plus monetized recommendation utility across a request sequence under monetization-rate, top-slot, and gap constraints.
- Dynamic request representation: [[adload-constrained-mix-ranking-value-maximization]] defines value relative to a no-ad list and weight as ad exposures, then shows why strategy-dependent quantities form a dynamic knapsack.
- Hierarchical decomposition: [[adload-constrained-mix-ranking-value-maximization]] derives the application threshold and the local `value - threshold × ad count` objective from the estimated displacement of marginal requests.
- Constrained search: [[adload-constrained-mix-ranking-value-maximization]] shows beam expansion over two ranked queues, constraint pruning, top-`B` retention, and the final threshold-gated no-ad fallback.
- Operational control: [[adload-constrained-mix-ranking-value-maximization]] warns that a daily threshold can miss a changing adload target and proposes faster updates or a real-time pacer.

## Counterevidence & Qualifications
The evidence is one secondary technical article interpreting one paper, not a reproduced implementation or benchmark. Greedy density ranking is not generally optimal for knapsack, and using the current cutoff as the marginal value of displaced capacity may be inaccurate when traffic or request weights are irregular. The utility tradeoff coefficient, score normalization, position discount, beam size, constraints, and pacing gains all require empirical calibration. Preserving upstream ad order supports auction assumptions only while the eCPM and charging model remain correct; context-aware re-estimation may change the valid order and make prediction depend on the layout being searched.

## What Changed
- Established adload as a cross-request capacity problem rather than an independent insertion cap.
- Connected a global marginal-capacity threshold to request-local beam-search scoring.
- Made no-ad baseline value, order preservation, constraint pruning, and threshold freshness explicit parts of mixed-ranking design.

## Related Concepts
- [[MixedRankingGovernance]] - supplies the broader value-alignment, incentive, and system-stability boundary around local ranking optimization.
- [[ScoreShading]] - uses aggregate constraints and adaptive control to alter local mixed-ranking decisions.
- [[MultiChannelAdOptimization]] - similarly decomposes a global advertising objective into local bidding and allocation controls.
- [[ProgrammaticAdvertising]] - supplies eCPM ordering and auction-mechanism assumptions for the ad queue.
- [[Adtech]] - contains the delivery, prediction, measurement, and optimization infrastructure needed to operate the ranking system.
- [[MarketingIncrementality]] - provides a stricter outcome standard than attributed ad value alone.
