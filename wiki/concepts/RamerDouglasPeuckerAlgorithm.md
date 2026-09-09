---
title: "Ramer-Douglas-Peucker Algorithm"
type: concept
tags: [geometry, algorithms, compression]
sources:
  - guiji-chouxi-douglas-peucker-suanfa
last_updated: 2026-09-09
knowledge_schema: synthesis-v1
---

## Definition

The Ramer-Douglas-Peucker algorithm approximates a polyline with fewer points by recursively retaining points whose perpendicular distance from a segment meets or exceeds an error tolerance, epsilon.

## Current Synthesis

The algorithm is a split-and-merge form of geometric simplification. It starts with a segment joining the first and last points, finds the intermediate point with the largest distance from that segment, and either removes all intermediate points or splits at the farthest point and recurses. Its output therefore depends on both the input geometry and the meaning of distance in the chosen coordinate system.

## Key Claims

- The first and last points of each recursively processed segment are retained as its approximation boundary.
- The farthest intermediate point determines whether a segment can be represented by a single chord or must be split.
- Increasing epsilon generally removes more points while allowing larger geometric deviation from the original polyline.
- Applying the method directly to longitude and latitude requires an explicit distance model because angular coordinates are not automatically planar metric coordinates.

## Evidence

- Algorithm mechanism - [[guiji-chouxi-douglas-peucker-suanfa]] describes the chord, farthest-point test, epsilon comparison, and recursive split.
- Threshold behavior - [[guiji-chouxi-douglas-peucker-suanfa]] reports progressively fewer retained points as epsilon rises across four runs.
- Coordinate qualification - [[guiji-chouxi-douglas-peucker-suanfa]] supplies decimal epsilon values for geographic coordinates but does not state the projection or distance formula.

## Counterevidence & Qualifications

The current corpus contains one tutorial and one empirical trajectory example. It does not independently verify the implementation, establish a universal compression ratio, compare iterative and recursive variants, or measure time complexity and runtime performance.

## What Changed

- Established the algorithm's recursive farthest-point decision rule.
- Added the epsilon-versus-fidelity tradeoff and the coordinate-system qualification.

## Related Concepts

- [[TrajectorySimplification]] - Ramer-Douglas-Peucker is one algorithmic method for reducing the point count of a trajectory or polyline.
