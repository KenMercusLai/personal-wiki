---
title: "Epsilon Tolerance"
type: concept
tags: [algorithm, geometry, threshold, gis]
sources:
  - gui-ji-chou-xi-zhi-dao-ge-la-si-pu-ke-suan-fa-ma-tian-jiang-xin
last_updated: 2026-09-11
knowledge_schema: synthesis-v1
---

## Definition
[[EpsilonTolerance]] is the distance threshold used by a simplification algorithm to decide whether deviation from an approximate segment is acceptable.

## Current Synthesis
In the source's Ramer-Douglas-Peucker explanation, epsilon is the main control knob for compression and fidelity. The algorithm measures the farthest intermediate point's distance from the chord joining the segment endpoints. If that maximum distance is smaller than epsilon, the segment is simplified; if it is greater than or equal to epsilon, the farthest point is retained and recursion continues.

The test table makes epsilon's effect concrete. Small epsilon values keep most of the original points, while larger values rapidly reduce the point count. The source treats a high-compression setting as acceptable when the route remains visually smooth enough for display, even if some corners differ slightly.

## Key Claims
- Epsilon defines the maximum tolerated deviation between the original curve and the simplified segment.
- Smaller epsilon values preserve more detail and retain more points.
- Larger epsilon values increase compression but can visibly alter corners or fine-grained shape.
- The threshold is application-specific because acceptable error depends on the display or analysis purpose.
- In the source's sample, epsilon 0.001 retains only 35 of 812 points while preserving the broad route.

## Evidence
- Decision rule: [[gui-ji-chou-xi-zhi-dao-ge-la-si-pu-ke-suan-fa-ma-tian-jiang-xin]] uses epsilon to decide whether the farthest point's distance is low enough to discard all intermediate points.
- Point-count results: [[gui-ji-chou-xi-zhi-dao-ge-la-si-pu-ke-suan-fa-ma-tian-jiang-xin]] lists retained point counts of 676, 569, 250, and 35 as epsilon rises from 0.000001 to 0.001.
- Fidelity tradeoff: [[gui-ji-chou-xi-zhi-dao-ge-la-si-pu-ke-suan-fa-ma-tian-jiang-xin]] says epsilon 0.001 causes some corner differences but keeps the overall trajectory relatively smooth.

## Counterevidence & Qualifications
The source reports epsilon values in coordinate units without discussing map projection, latitude-dependent distance distortion, or how to choose a tolerance from a pixel budget or meter-level error budget.

## What Changed
- Created a threshold concept page for simplification tolerance in the Ramer-Douglas-Peucker workflow.

## Related Concepts
- [[RamerDouglasPeuckerAlgorithm]] - epsilon is the algorithm's recursive stop-or-split threshold.
- [[TrajectorySimplification]] - epsilon controls how aggressively a trajectory is simplified.
- [[MapTrajectoryRendering]] - visual rendering needs determine the acceptable tolerance.
