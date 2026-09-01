---
title: "Ramer-Douglas-Peucker algorithm"
description: "A recursive line simplification algorithm that keeps points whose distance from a chord exceeds a tolerance."
type: "entity"
updated: "2026-09-02"
source_keys: ["ramer-douglas-peucker-algorithm"]
entity_kind: "algorithm"
---

The Ramer-Douglas-Peucker algorithm simplifies a polyline by recursively comparing intermediate points against the straight line between a segment's endpoints. If the farthest point is within the tolerance `epsilon`, the segment can be represented by its endpoints; otherwise that farthest point is retained and the same test is applied to the two resulting subsegments.

In [轨迹抽稀之道格拉斯-普克算法]({{< relref "/wiki/sources/ramer-douglas-peucker-algorithm.md" >}}), the algorithm is used to thin vehicle GPS trajectories before display. The source's 812-point example shows the practical control `epsilon` gives over compression: increasing the tolerance reduces retained points, but excessive tolerance can slightly distort corners.
