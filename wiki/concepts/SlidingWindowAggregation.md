---
title: "Sliding-Window Aggregation"
type: concept
tags: [algorithms, data-structures, streaming, numerical-computing]
sources:
  - two-stack-sliding-window-aggregation-orlp-net
last_updated: 2026-10-07
knowledge_schema: synthesis-v1
---

## Definition
[[SlidingWindowAggregation]] maintains a summary over an ordered set whose oldest elements can leave while new elements enter, without recomputing the whole active window after every change.

## Current Synthesis
The two-stack method extends efficient rolling computation beyond aggregates with usable inverses. A newer stack stores incoming values plus their aggregate in arrival order. An older stack stores cumulative aggregates in reverse removal order. Evaluation combines the older cumulative state with the newer aggregate, preserving operand order even when `combine` is associative but not commutative.

When the older stack is empty during a removal, all newer values move across in reverse order while cumulative aggregates are built. That transfer makes one operation linear in the number moved, but each element crosses stacks only once, so insertion and removal are amortized constant time. Evaluation remains constant time and storage remains linear in the maximum active window. The window may grow or shrink arbitrarily rather than having a fixed width.

The numerical benefit is containment rather than exactness. Floating-point addition is not associative, so regrouping can change rounding. Nevertheless, every maintained state is composed only from active elements: a departed `NaN`, infinity, outlier, or earlier rounding contribution cannot poison all later windows as it can in a subtractive rolling sum.

## Key Claims
- A two-stack queue supports associative window aggregates without requiring an inverse operation.
- Operand order is preserved, so the aggregation need not be commutative.
- Evaluation is constant time, while insertion and removal are amortized constant time.
- Memory use is linear in the maximum number of active elements.
- Pushes and removals may occur in arbitrary proportions, allowing variable-size windows.
- Rebuilding aggregate state from active elements contains exceptional values and numerical drift to windows that still contain their causes.

## Evidence
- Data-structure invariant: [[two-stack-sliding-window-aggregation-orlp-net]] describes a newer-value stack with one forward aggregate and an older stack of reverse cumulative aggregates.
- Complexity: [[two-stack-sliding-window-aggregation-orlp-net]] explains that a linear transfer occurs only after the previous transferred batch has been removed, bounding total work per element.
- Generality: [[two-stack-sliding-window-aggregation-orlp-net]] gives minima, quantiles, means, and HyperLogLog-style approximate distinct counts as aggregates expressible without inverses.
- Dynamic windows: [[two-stack-sliding-window-aggregation-orlp-net]] states that callers may vary pushes and removals between evaluations rather than maintaining a fixed width.
- Numerical containment: [[two-stack-sliding-window-aggregation-orlp-net]] contrasts active-window-only recomputation with a subtractive rolling sum whose `NaN` or rounding error can persist after the originating value leaves.

## Counterevidence & Qualifications
The complexity guarantee is amortized, so a transfer can still create a latency spike proportional to the current stack size. Correctness depends on an associative `combine`, a valid identity, and order-consistent `unit` and `finalize` functions. Floating-point arithmetic violates exact associativity, and compensated summation reduces but does not eliminate rounding sensitivity. The source supplies illustrative Python rather than a formal proof, benchmark, production implementation, concurrency model, or analysis of aggregate-state copying costs; large sketches may make each nominal combine materially expensive.

## What Changed
- Created a general model for inverse-free rolling aggregation using a two-stack queue.
- Added active-window-only state as a containment mechanism for exceptional floating-point values and accumulated error.
- Distinguished amortized throughput from worst-case per-operation latency.

## Related Concepts
- [[AssociativeAggregation]] - supplies the algebraic interface and regrouping property used across the two stacks.
- [[AmortizedAnalysis]] - explains why occasional full transfers still yield constant average work per element.
- [[TimeSeriesDatabase]] - temporal queries often compute rolling summaries, though database execution adds storage, alignment, and query-planning concerns.
- [[AlgorithmicComplexityVulnerabilities]] - highlights why an amortized bound may be insufficient when an adversary or latency budget can target the expensive operation.
