---
title: "AI 推理负载均衡"
description: "AI 推理负载均衡需要结合请求 token 规模、实时后端指标、KV cache 复用和限额策略来分配推理请求。"
type: "concept"
updated: "2026-09-01"
source_keys: ["segmentfault-ai-inference-load-balancing-open-source-implementations"]
---

AI 推理负载均衡面对的是 prompt 长短、prefill 成本、decode 成本和缓存复用差异明显的请求。来源 [《锐评主流AI推理负载均衡开源实现》]({{< relref "/wiki/sources/segmentfault-ai-inference-load-balancing-open-source-implementations.md" >}}) 将 ILB 的基础能力拆成三类问题：如何 tokenize 请求来估算负载，如何获取足够实时的均衡指标，以及如何根据指标选择推理引擎节点。

传统负载均衡常以连接数、请求数或延迟作为主信号。AI 推理场景还要考虑输入 token、输出 token、prefill 阶段成本、decode 阶段成本和 KV cache 命中。来源认为，限额策略可以建立在同一套负载认知之上；对于完整 prompt 到达后才开始推理的请求，限额触发后的操作通常比底层网络拥塞控制更直接。

## 实现维度

- AIBrix、Kthena、Gateway API Inference Extension 和 Dynamo 都把路由策略作为推理网关或推理平台的一部分。
- AIBrix、Kthena 和 Gateway API Inference Extension 都有多种路由算法，Kthena 和 Gateway API Inference Extension 还支持按权重编排多个路由算法。
- Dynamo 的核心策略用成本函数综合缓存重叠、prefill blocks 和 decode blocks，优先选择估算成本最低的 worker。
