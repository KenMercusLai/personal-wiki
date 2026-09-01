---
title: "Trajectory simplification"
description: "Reducing the number of points in a recorded path while preserving the route's useful shape."
type: "concept"
updated: "2026-09-02"
source_keys: ["ramer-douglas-peucker-algorithm"]
---

Trajectory simplification reduces dense movement traces to fewer coordinates while keeping the visible route close to the original. In vehicle tracking, this can reduce API payload size, storage, and browser rendering work when location samples arrive frequently and many points are repeated or lie along nearly straight segments.

The article [轨迹抽稀之道格拉斯-普克算法]({{< relref "/wiki/sources/ramer-douglas-peucker-algorithm.md" >}}) frames simplification as an acceptable tradeoff when the retained points preserve the route's overall curve. Its example begins with 812 trajectory points and shows that higher tolerance values can sharply reduce the point count, with 35 points still preserving the broad path at the largest tested tolerance.
