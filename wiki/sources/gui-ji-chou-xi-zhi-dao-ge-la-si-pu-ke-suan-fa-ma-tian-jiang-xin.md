---
title: "轨迹抽稀之道格拉斯-普克算法 | 码田匠心"
type: source
tags: [algorithm, gis, trajectory, map]
date: 2026-03-31
source_file: /mnt/ken_personal_wiki/Articles/轨迹抽稀之道格拉斯-普克算法 码田匠心.md
---

## Summary
This article explains [[TrajectorySimplification]] for vehicle-track display using the [[RamerDouglasPeuckerAlgorithm]]. [[MaTianJiangXin]] motivates the technique with a practical GIS problem: frequent vehicle uploads can create thousands of coordinate points per day, slowing API responses and frontend rendering. The article then shows how an epsilon threshold controls point retention, with an 812-point sample compressed to 35 points at epsilon 0.001 while preserving the broad path shape.

## Key Claims
- Vehicle trajectory displays can become slow when each vehicle uploads frequent GPS points, making [[TrajectorySimplification]] useful for storage, transfer, and rendering cost.
- Many trajectory points are redundant because stopped vehicles can emit repeated points and straight-line segments can often be represented by endpoints.
- The [[RamerDouglasPeuckerAlgorithm]] recursively compares each segment's farthest intermediate point against an [[EpsilonTolerance]] threshold.
- If the maximum perpendicular distance is below epsilon, intermediate points can be discarded and the segment can be approximated by a straight line.
- If the maximum distance meets or exceeds epsilon, the farthest point splits the curve and the same procedure runs on both subsegments.
- Larger epsilon values retain fewer points and may introduce visible corner differences, so the threshold is a compression-versus-fidelity control.
- The article's [[MapTrajectoryRendering]] example shows that point reduction can substantially reduce frontend rendering cost while keeping the route visually recognizable.

## Key Quotes
> "这样的过程我们称之为抽稀" - on removing redundant points while preserving the broad trajectory.

> "仅用4%的点就可以展示大致路径" - on the article's strongest compression example.

## Connections
- [[TrajectorySimplification]] - the article's central applied problem.
- [[RamerDouglasPeuckerAlgorithm]] - the simplification method explained step by step.
- [[EpsilonTolerance]] - the threshold that controls point retention and path fidelity.
- [[MapTrajectoryRendering]] - the practical display context for the algorithm.
- [[MaTianJiangXin]] - the source account credited by the article title.
- [[BaiduMaps]] - the map platform used in the trajectory drawing example.

## Contradictions
- No direct contradictions with existing wiki content. This source extends the technology thread from protocols and AI infrastructure into GIS-style data reduction for interactive rendering.
