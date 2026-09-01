---
title: "Ramer-Douglas-Peucker 算法"
description: "Ramer-Douglas-Peucker 算法通过递归寻找曲线点到首尾弦线的最大距离，并用 epsilon 阈值决定是否保留分割点，从而把曲线近似为更少的点。"
type: "concept"
updated: "2026-09-01"
source_keys: ["matianjiangxin-douglas-peucker-trajectory-simplification"]
---

Ramer-Douglas-Peucker 算法是一种曲线简化算法，也常用于轨迹抽稀。来源：[《轨迹抽稀之道格拉斯-普克算法 | 码田匠心》]({{< relref "/wiki/sources/matianjiangxin-douglas-peucker-trajectory-simplification.md" >}})。

算法处理一段曲线时，先用首尾两点连成直线，把这条直线作为原曲线段的近似弦。随后遍历首尾之间的点，找到距离这条弦最远的点，并把这个距离与阈值 `epsilon` 比较。

如果最大距离小于 `epsilon`，首尾之间的点会被舍弃，这段曲线由首尾直线近似表示。如果最大距离大于或等于 `epsilon`，距离最大的点会被保留，并把曲线分成两段继续递归处理。递归结束后，保留下来的点按原顺序连接，形成点数更少的近似折线。

## 工程取舍

- 较小的 `epsilon` 会保留更多点，路径细节更接近原始轨迹，但压缩率较低。
- 较大的 `epsilon` 会显著减少点数，降低传输、存储和渲染成本，但可能让拐角或局部变化变得更平滑。
- 对车辆轨迹这类地图展示场景，合适的阈值取决于前端视觉效果、地图比例尺和业务对路径细节的要求。
