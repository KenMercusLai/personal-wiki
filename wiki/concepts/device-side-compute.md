---
title: "Device-side compute"
description: "Device-side compute moves selected work, caches, and trained models onto mobile devices when local processing improves latency, cost, resilience, or user experience."
type: "concept"
updated: "2026-09-02"
source_keys: ["hallway-debates-2016-product-manager-discussion-guide"]
---

来源：[Hallway Debates]({{< relref "/wiki/sources/hallway-debates-2016-product-manager-discussion-guide.md" >}})

Device-side compute 指移动设备不只是显示服务器结果，也承担更多本地计算、缓存和模型推理。来源认为，随着 ARM/移动生态的性能、存储和图形能力提高，许多过去必须往返服务器的体验可以重新分配到设备端。

这种架构判断来自用户体验和成本。某些服务端往返既慢又贵，即使网络条件良好，延迟也会被用户感知。把特定查询、分类或缓存放在设备本地，可以让应用在关键时刻更快、更可靠，也减少对持续连接的依赖。

来源用拼写和语法检查说明这个变化：早期词典本地安装，互联网时代转向在线服务，后续则可能把大规模语料训练出的专用模型打包到设备上本地使用。类似模式也可能出现在识别、分类和推荐等移动场景中。
