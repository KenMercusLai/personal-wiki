---
title: "Associative Aggregation"
type: concept
tags: [algorithms, algebra, streaming, data-processing]
sources:
  - two-stack-sliding-window-aggregation-orlp-net
last_updated: 2026-10-07
knowledge_schema: synthesis-v1
---

## Definition
[[AssociativeAggregation]] summarizes values through an identity, a value-to-state conversion, an associative state-combination operation, and an optional final conversion from aggregate state to output.

## Current Synthesis
Separating `Value`, `Agg`, and `Out` makes aggregation more general than repeatedly applying an operator to one type. A string can become a probabilistic distinct-count sketch, sketches can combine, and the final sketch can yield an integer estimate. A mean can similarly maintain a `(sum, count)` state and divide only when finalized.

Associativity allows an ordered sequence to be split into groups and those group aggregates to be recombined without changing the mathematical result. It does not require commutativity: regrouping must preserve left-to-right operand order. Nor does it require an inverse, which is why cumulative partial aggregates can support removal indirectly even for minima, quantiles, sketches, and other summaries that cannot subtract a departing input.

## Key Claims
- Input values, intermediate aggregate state, and finalized output may be different types.
- An identity and associative `combine` permit empty-state handling and hierarchical regrouping.
- Associativity changes grouping, not operand order, and therefore does not imply commutativity.
- Invertibility is unnecessary when a data structure retains sufficient partial aggregates.
- The same interface can express exact, approximate, scalar, and structured summaries.
- Numerical implementations may only approximate the algebraic law assumed by the abstract algorithm.

## Evidence
- Typed interface: [[two-stack-sliding-window-aggregation-orlp-net]] defines separate `empty`, `unit`, `combine`, and `finalize` functions over `Value`, `Agg`, and `Out` types.
- Structured state: [[two-stack-sliding-window-aggregation-orlp-net]] represents a mean with a sum-count pair rather than treating the intermediate state as the final scalar output.
- Approximate state: [[two-stack-sliding-window-aggregation-orlp-net]] uses strings, HyperLogLog sketches, and an integer estimate to illustrate three distinct types.
- Regrouping: [[two-stack-sliding-window-aggregation-orlp-net]] combines reverse cumulative state with a forward aggregate while retaining sequence order.
- Algebraic boundary: [[two-stack-sliding-window-aggregation-orlp-net]] explicitly notes that floating-point addition is not exactly associative despite remaining practically useful.

## Counterevidence & Qualifications
The source gives an interface sketch rather than a formal algebraic specification. It does not state all identity laws, serialization requirements, mutation rules, or error bounds for approximate summaries. Some aggregates have expensive or state-size-dependent combination costs, so treating `combine` as constant time can hide important complexity. Floating-point arithmetic, nondeterministic sketches, order-sensitive approximations, and mutable aggregate objects may violate assumptions needed for reproducible regrouping.

## What Changed
- Created a typed aggregation model separating source values, combinable state, and finalized output.
- Clarified that associativity permits regrouping without granting commutativity or invertibility.
- Added approximate and numerically inexact aggregates as qualified implementations of the abstraction.

## Related Concepts
- [[SlidingWindowAggregation]] - uses retained partial states to maintain an associative aggregate as an ordered window changes.
- [[FunctionalProgramming]] - explicit pure-style conversion and combination functions expose state transitions and composition boundaries.
- [[TimeSeriesDatabase]] - temporal engines apply aggregation over time and label dimensions, subject to alignment and domain semantics.
- [[VectorizedArrayOperations]] - reductions over arrays are another execution form for associative operations, with numerical ordering caveats.
