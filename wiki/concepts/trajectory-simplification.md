---
title: "轨迹抽稀"
description: "轨迹抽稀是在保持运动路径整体形状的前提下删除重复、静止或近似共线的轨迹点，以降低传输、存储和渲染成本。"
type: "concept"
updated: "2026-09-01"
source_keys: ["matianjiangxin-douglas-peucker-trajectory-simplification"]
---

轨迹抽稀是一种对经纬度轨迹点序列做压缩的处理方式，目标是在路径形状基本不变的前提下移除冗余点。来源：[《轨迹抽稀之道格拉斯-普克算法 | 码田匠心》]({{< relref "/wiki/sources/matianjiangxin-douglas-peucker-trajectory-simplification.md" >}})。

在车辆轨迹展示场景中，终端按固定频率上传位置点时，一辆活跃车辆每天可能产生大量轨迹数据。并非所有点都同等重要：静止状态上传的重复点、近似重合的点，以及长直线路段中的中间点，都可以在不明显改变路线观感的情况下删除。

轨迹抽稀的工程意义是把地图展示、接口响应、网络传输和存储成本从原始点数中解耦出来。点数越少，前端渲染和数据传输越轻；但阈值过大时，拐角和局部细节会被过度平滑。因此抽稀策略需要在压缩率和路径保真度之间取舍。

## 相关算法

- [Ramer-Douglas-Peucker 算法]({{< relref "/wiki/concepts/ramer-douglas-peucker-algorithm.md" >}})通过首尾弦线、最大垂距和递归分割来保留轨迹中的关键形状点。
