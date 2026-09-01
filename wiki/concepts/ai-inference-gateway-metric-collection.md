---
title: "AI 推理网关指标采集"
description: "AI 推理网关指标采集需要在实时性、采集成本和路由决策准确性之间权衡。"
type: "concept"
updated: "2026-09-01"
source_keys: ["segmentfault-ai-inference-load-balancing-open-source-implementations"]
---

AI 推理网关指标采集为路由决策提供后端状态。来源 [《锐评主流AI推理负载均衡开源实现》]({{< relref "/wiki/sources/segmentfault-ai-inference-load-balancing-open-source-implementations.md" >}}) 将主流方案分为高频轮询推理引擎、查询 Prometheus、从响应 token usage 中汇总，以及消费推理引擎推送的 KV event。

来源认为，分布式网关直接高频轮询每个推理引擎会在大规模集群中产生明显的交叉采集成本；Prometheus 的数据如果来自同一批 metrics 接口，也不能天然提升实时性。Gateway API Inference Extension 的中心化 EPP 可以减少重复采集，但如果请求和响应路径都经过 EPP，路由“大脑”本身也可能成为瓶颈。

## 事件驱动采集

Dynamo 被来源评价为指标采集更简洁的设计。它主要消费 KV event 中的 active blocks，并结合 router 自己维护的路由历史估算当前负载；多 router 场景下再通过副本同步共享状态，并用温度随机性降低惊群风险。
