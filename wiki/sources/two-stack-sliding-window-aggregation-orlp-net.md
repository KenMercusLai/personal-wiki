---
title: "Two-Stack Sliding-Window Aggregation"
type: source
tags: [algorithms, data-structures, streaming, aggregation, numerical-computing]
date: 2026-10-02
source_file: "/mnt/ken_personal_wiki/Articles/Two-Stack Sliding-Window Aggregation | orlp.net.md"
---

## Summary
The article presents a two-stack queue that maintains an arbitrary [[AssociativeAggregation|associative aggregate]] over a dynamically growing or shrinking window. It provides constant-time evaluation, amortized constant-time insertion and removal, and linear memory in the maximum window size without requiring an inverse operation. Because every aggregate is rebuilt only from current window elements, the method also prevents departed `NaN`, infinity, or rounding error from contaminating all later floating-point results.

## Key Claims
- Inverse-based rolling updates work for some exact aggregates but fail for non-invertible summaries such as minima, quantiles, and approximate distinct counts.
- The aggregation interface can separate input values, intermediate aggregate state, and finalized output through `empty`, `unit`, `combine`, and `finalize` operations.
- One stack stores newly pushed values and their forward aggregate; the other stores reverse-order cumulative aggregates for older values.
- Combining the older stack's current cumulative aggregate with the newer stack's aggregate evaluates the entire ordered window in constant time.
- When the older stack empties, transferring and cumulatively aggregating the newer stack costs linear time for that operation but amortized constant time per element.
- The structure uses linear memory and does not require a fixed-size window or a fixed push-pop schedule.
- Floating-point addition is not truly associative, but rebuilding from only current elements bounds contamination and long-term drift to the active window.

## Key Quotes
> “Each aggregate is strictly a combination of the elements in the window, and none outside the window.” — on error containment.

## Connections
- [[SlidingWindowAggregation]] — the two-stack queue maintains a current aggregate as elements enter and leave an ordered window.
- [[AssociativeAggregation]] — associativity, rather than invertibility, is the algebraic requirement that permits regrouping across the two stacks.
- [[AmortizedAnalysis]] — occasional full-stack transfers cost linear time but distribute to constant work per element across an operation sequence.
- [[FunctionalProgramming]] — the `empty`, `unit`, `combine`, and `finalize` interface separates values, aggregate state, composition, and output.
- [[TimeSeriesDatabase]] — rolling summaries over recent observations are a common temporal workload, although storage and query semantics add further concerns.

## Contradictions
- Floating-point addition violates the exact associativity assumed by the proof, so the algorithm offers useful numerical containment rather than equality under every regrouping.
- Amortized constant time does not provide a worst-case latency bound for each operation; workloads with strict tail-latency requirements may need a more complex worst-case constant-time algorithm.
- The article is an explanatory practitioner account and code sketch, not a benchmark, formal proof, or comparison across implementations and aggregate types.
