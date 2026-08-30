---
title: "分布式调度器的状态采集权衡"
description: "轮询、集中聚合和事件流在状态新鲜度、扇出成本、瓶颈与一致性之间交换。"
type: "concept"
updated: "2026-08-30"
source_keys: ["spacewander-ai-inference-load-balancing"]
featured: false
---

## 三种常见路径

- **每个Router轮询每个Worker：** 简单直接，但成本约为`G×E×f`，会随Router数、引擎数和频率增长。
- **集中采集或聚合：** 减少重复扇出，却可能增加中心瓶颈、数据延迟和故障依赖。
- **Worker发布事件：** 解耦生产者与消费者，适合KV Block等状态变化；代价是事件完整性、重放、顺序和副本同步机制。

调度质量依赖状态新鲜度，但更高频采集会增加网络与处理开销。多个Router各自维护路由历史时，副本同步可以达到最终一致，却无法消除网络延迟造成的瞬时视图差异。

## 设计检查

评估状态系统时，应分别测量采集扇出、数据年龄、消息丢失恢复、中心组件吞吐、Router扩展效率和错误状态对路由尾延迟的影响，而不能只比较名义刷新间隔。

## 来源

- [《锐评主流AI推理负载均衡开源实现》]({{< relref "/wiki/sources/spacewander-ai-inference-load-balancing.md" >}})
