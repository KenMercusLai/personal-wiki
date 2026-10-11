---
title: "Ramer-Douglas-Peucker Algorithm"
type: concept
tags: [algorithm, geometry, gis, compression]
sources:
  - gui-ji-chou-xi-zhi-dao-ge-la-si-pu-ke-suan-fa-ma-tian-jiang-xin
  - tzf-de-chun-ji-geng-xin-ringsaturn
last_updated: 2026-10-11
knowledge_schema: synthesis-v1
---

## Definition
[[RamerDouglasPeuckerAlgorithm]] is a recursive curve-simplification algorithm that approximates a polyline with fewer points by preserving endpoints and recursively retaining intermediate points whose distance from the current segment exceeds a chosen tolerance.

## Current Synthesis
The sources present the algorithm as a practical answer to excessive geometric detail. A trajectory can contain many repeated or nearly collinear GPS coordinates; rendering and transferring all of them is often unnecessary when the visual path can be preserved by a much smaller representative set. The tzf case adds a different use: reducing polygon boundaries distributed for coordinate-to-time-zone lookup.

The algorithm's core decision is geometric. It connects the first and last points of a segment, finds the intermediate point farthest from that chord, and compares that distance with [[EpsilonTolerance]]. If the distance is small enough, the segment is replaced by the chord; otherwise the farthest point becomes a split point and the process repeats on each side.

That local geometric rule does not preserve relationships between separate inputs. When neighboring polygons independently simplify what began as a common boundary, they may retain different points and introduce gaps or overlaps. [[TopologyAwarePolygonSimplification]] therefore identifies shared edges first, simplifies the common chain once, and reuses the result on both sides.

## Key Claims
- The algorithm reduces a curve or trajectory to a smaller point sequence while preserving its broad shape.
- It treats the first and last points of the current segment as mandatory anchors.
- It uses the farthest intermediate point from the segment chord as the deciding point.
- [[EpsilonTolerance]] controls whether intermediate points are discarded or retained as split points.
- Recursive splitting continues until all retained segments satisfy the tolerance threshold.
- Higher epsilon values can produce much stronger compression with visible fidelity loss at corners.
- Independent application does not by itself preserve adjacency or coverage topology across polygons.

## Evidence
- Shape-preserving reduction: [[gui-ji-chou-xi-zhi-dao-ge-la-si-pu-ke-suan-fa-ma-tian-jiang-xin]] defines thinning as removing redundant points while keeping the trajectory curve broadly unchanged.
- Segment anchors and farthest point: [[gui-ji-chou-xi-zhi-dao-ge-la-si-pu-ke-suan-fa-ma-tian-jiang-xin]] describes connecting the first and last points, scanning all intermediate points, and finding the maximum distance point.
- Tolerance decision: [[gui-ji-chou-xi-zhi-dao-ge-la-si-pu-ke-suan-fa-ma-tian-jiang-xin]] explains that distances below epsilon allow the middle points to be dropped, while distances above or equal to epsilon trigger subdivision.
- Compression behavior: [[gui-ji-chou-xi-zhi-dao-ge-la-si-pu-ke-suan-fa-ma-tian-jiang-xin]] reports reductions from 812 original trajectory points to 676, 569, 250, and 35 points as epsilon increases.
- Polygon-set failure: [[tzf-de-chun-ji-geng-xin-ringsaturn]] shows independently simplified neighboring time-zone boundaries diverging into gaps and overlaps.
- Topology-aware wrapper: [[tzf-de-chun-ji-geng-xin-ringsaturn]] identifies shared reverse-directed edges and replaces both polygon sides with one simplified boundary.

## Counterevidence & Qualifications
The trajectory source demonstrates the algorithm visually and operationally but does not discuss coordinate-system effects, distance formulas on a sphere, GPS noise, topology preservation, or worst-case runtime. The tzf source directly demonstrates the topology limitation but does not fully specify tolerance selection, invalid-geometry handling, holes, self-intersection, antimeridian behavior, or the complete production algorithm. RDP therefore controls geometric approximation, not all validity, topology, or application-accuracy requirements.

## What Changed
- Added the distinction between simplifying one curve and preserving shared topology across a polygon set.
- Added tzf's shared-edge preprocessing as a wrapper around independent geometric simplification.

## Related Concepts
- [[TrajectorySimplification]] - Ramer-Douglas-Peucker is the source's chosen simplification method.
- [[EpsilonTolerance]] - epsilon is the algorithm's fidelity threshold.
- [[MapTrajectoryRendering]] - the article applies the algorithm to frontend trajectory display.
- [[TopologyAwarePolygonSimplification]] - adds shared-boundary invariants that RDP alone does not preserve.
