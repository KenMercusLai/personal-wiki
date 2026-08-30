---
title: "Ramer–Douglas–Peucker曲线简化"
description: "递归保留偏离首尾弦超过容差的最远点，以更少顶点近似有序折线。"
type: "concept"
updated: "2026-08-30"
source_keys: ["matianjiangxin-douglas-peucker-trajectory-simplification"]
featured: true
---

## 定义

Ramer–Douglas–Peucker（RDP）算法用较少的顶点近似一条有序折线。它连接当前区段的首尾点，找到距离该线段最远的中间点：距离超过容差则保留并递归分割，否则删除全部中间点。

## 性质

- 容差越大，通常保留点越少。
- 保留首尾点和被判定为显著偏离的转折点。
- 结果依赖距离定义、[坐标系和容差单位]({{< relref "/wiki/concepts/geospatial-simplification-tolerance.md" >}})。
- 它控制几何偏离，不保持时间间隔、速度峰值、停留点或道路拓扑。
- 朴素递归实现最坏复杂度可达`O(n²)`。

## 来源

- [《轨迹抽稀之道格拉斯-普克算法》]({{< relref "/wiki/sources/matianjiangxin-douglas-peucker-trajectory-simplification.md" >}})
