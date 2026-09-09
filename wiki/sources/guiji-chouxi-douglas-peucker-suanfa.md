---
title: "轨迹抽稀之道格拉斯-普克算法"
description: "用道格拉斯-普克算法按几何误差阈值压缩车辆轨迹点的实现思路与案例。"
type: "source"
updated: "2026-09-09"
source_key: "guiji-chouxi-douglas-peucker-suanfa"
author: "码田匠心"
source_date: "2020-09-08"
source_url: "https://zulu.wang/posts/2020/09/08/ramer-douglas-peucker-algorithm.html"
source_file: "Articles/轨迹抽稀之道格拉斯-普克算法 码田匠心.md"
featured: false
---

## Summary

文章以车辆每 5 秒上报一个轨迹点、活跃车辆一天可能产生约一万个点的场景说明轨迹抽稀的必要性，并介绍用道格拉斯-普克算法减少接口传输、存储和前端渲染负担的方法。算法以首尾点连线为弦，寻找距离该直线最远的中间点；最大距离小于阈值 epsilon 时舍弃中间点，否则在最远点处分段递归。

## Key Claims

- 轨迹中的重复点和近似共线点通常可以删除，而不显著改变路径的整体形状。
- epsilon 控制压缩率与几何保真度：阈值越大，保留点越少，拐角处的偏差风险越高。
- 文中 812 个轨迹点的案例在 epsilon 从 0.000001 增至 0.001 时，保留点数依次为 676、569、250 和 35。
- 在该案例中，epsilon 为 0.001 时仅保留约 4% 的点，作者认为路径整体仍较平滑且与原路径差异不大。

## Algorithm

1. 连接曲线首尾点 A、B，得到弦 AB。
2. 遍历中间点，找到到直线 AB 距离最大的点 C。
3. 若最大距离小于 epsilon，用 AB 近似整段并舍弃中间点。
4. 若最大距离不小于 epsilon，以 C 将曲线拆为 AC 与 CB，分别递归处理。
5. 按原顺序连接所有保留的分割点，得到简化后的折线。

## Visual Evidence

来源包含一张算法折线示意图，以及同一路径的原始轨迹与四组 epsilon 结果图。地图对比显示阈值提高后线条逐渐减少细小转折，epsilon 为 0.001 的结果最为折线化。

## Key Quotes

> “实际上将这些多余的点剔除仍然能保证轨迹曲线大体不变，并且还能节省存储空间，这样的过程我们称之为抽稀。”

> “仅用4%的点就可以展示大致路径，这个压缩率还是很高的，在传输及存储都显著的降低了成本。”

## Connections

- [[RamerDouglasPeuckerAlgorithm]] - 文章介绍的递归曲线简化方法。
- [[TrajectorySimplification]] - 文章所处理的车辆轨迹压缩问题。

## Contradictions

- 当前空白语料库中没有可对照的既有结论。

## Qualifications

- 812 点到 35 点的结果是单一路径和一组阈值下的案例，不能直接泛化为其他轨迹的固定压缩率。
- 文章未说明经纬度距离使用平面近似、投影坐标还是球面距离；epsilon 的数值含义因此依赖坐标系与距离实现。
- 原文“相关代码”和“路径显示代码”段落在保存的 Markdown 中没有代码正文，无法据此验证实现复杂度或复现结果。

## Attribution

原文及其图片由码田匠心发布；原网页标注采用 [CC BY-NC 4.0](https://creativecommons.org/licenses/by-nc/4.0/) 许可。
