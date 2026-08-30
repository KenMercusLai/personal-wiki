---
title: "地理轨迹简化的容差选择"
description: "简化阈值必须与坐标系、距离单位、地图比例和业务允许误差共同定义。"
type: "concept"
updated: "2026-08-30"
source_keys: ["matianjiangxin-douglas-peucker-trajectory-simplification"]
featured: false
---

## 容差不是无单位旋钮

在[RDP曲线简化]({{< relref "/wiki/concepts/ramer-douglas-peucker-algorithm.md" >}})中，`epsilon`表示点到近似线段的允许距离。若直接使用经纬度，它的单位是角度，无法在不同纬度和范围下稳定代表相同米数。

## 选择方法

1. 明确展示、存储、传输或分析任务允许的空间误差。
2. 选择适合区域的投影坐标或测地距离，以米表达阈值。
3. 在真实轨迹上比较保留点数、最大偏差、关键转角和渲染性能。
4. 对停留、时间、速度和道路拓扑另设保留规则，不让纯几何算法覆盖业务语义。
5. 按地图缩放级别生成多级简化结果时，保持原始轨迹可恢复。

## 来源

- [《轨迹抽稀之道格拉斯-普克算法》]({{< relref "/wiki/sources/matianjiangxin-douglas-peucker-trajectory-simplification.md" >}})
