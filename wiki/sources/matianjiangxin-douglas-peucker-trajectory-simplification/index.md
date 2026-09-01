---
title: "轨迹抽稀之道格拉斯-普克算法 | 码田匠心"
description: "码田匠心用车辆轨迹点压缩场景说明 Douglas-Peucker 算法如何按距离阈值保留关键点，从而降低轨迹传输、存储与渲染成本。"
type: "source"
updated: "2026-09-01"
source_key: "matianjiangxin-douglas-peucker-trajectory-simplification"
image_status: "not_selected"
source_url: "https://zulu.wang/posts/2020/09/08/ramer-douglas-peucker-algorithm.html"
---

## 摘要

这篇文章以车辆轨迹展示为例说明轨迹抽稀的工程价值。车辆按约每 5 秒上传一个经纬度点时，活跃车辆一天可能产生约 1 万个轨迹点；如果全部返回给接口和前端地图渲染，会增加传输、存储和页面绘制成本。

文章把轨迹抽稀定义为在保持轨迹曲线整体形状基本不变的前提下，剔除重复点、静止状态点或近似位于同一直线上的冗余点。Douglas-Peucker 算法是其中一种实现方式：它用首尾点连成的弦近似曲线，并根据中间点到弦的最大距离和阈值 `epsilon` 的比较结果决定是否继续分割。

## 算法逻辑

Douglas-Peucker 算法先连接一段轨迹的首尾点 `A` 和 `B`，把直线 `AB` 作为该曲线段的弦；然后遍历中间所有点，找到距离直线 `AB` 最远的点 `C`，并记录最大距离 `maxDistance`。

如果 `maxDistance < epsilon`，算法认为直线 `AB` 足以近似这段曲线，于是舍弃首尾之间的中间点。如果 `maxDistance >= epsilon`，算法保留点 `C`，并把原曲线分成 `AC` 与 `CB` 两段递归处理。所有片段处理完成后，保留下来的分割点按原顺序连成折线，作为原始轨迹的近似路径。

## 测试结果

文章用 812 个轨迹点做测试，并逐步增大 `epsilon`。当 `epsilon` 为 `0.000001` 时保留 676 个点，为 `0.00001` 时保留 569 个点，为 `0.0001` 时保留 250 个点，为 `0.001` 时只保留 35 个点。作者观察到 `epsilon = 0.001` 时部分拐角会有差异，但整体路径仍较平滑，只用约 4% 的点即可展示大致路径，显著降低传输和存储成本。

## 相关知识

- [轨迹抽稀]({{< relref "/wiki/concepts/trajectory-simplification.md" >}})
- [Ramer-Douglas-Peucker 算法]({{< relref "/wiki/concepts/ramer-douglas-peucker-algorithm.md" >}})
