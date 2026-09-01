---
title: "锐评主流AI推理负载均衡开源实现"
description: "这篇 SegmentFault 文章比较 AIBrix、Kthena、Gateway API Inference Extension 和 Dynamo 在 tokenizer、指标采集与路由策略上的设计取舍。"
type: "source"
updated: "2026-09-01"
source_key: "segmentfault-ai-inference-load-balancing-open-source-implementations"
image_status: "not_selected"
source_date: "2026-03-29"
source_url: "https://segmentfault.com/a/1190000047682071"
---

## 摘要

这篇文章讨论 AI 推理请求负载均衡的开源实现，并把推理负载均衡简称为 ILB。文章认为，一个 ILB 至少要回答三个基础问题：如何对请求做 tokenization 来理解负载，如何取得与均衡相关的指标，以及如何根据这些指标把请求路由到合适的推理引擎。限额策略可以建立在同一套负载计数之上。

文章逐项比较了 AIBrix、Kthena、Gateway API Inference Extension 和 Dynamo。AIBrix 支持按 byte、tiktoken 和远程 tokenize API 三种方式估算 token，也通过高频轮询、Prometheus 查询和 KV event 消费采集指标；文章重点批评了 tiktoken encoding 选择、远程 tokenize 链路，以及分布式网关轮询所有引擎时的规模成本。Kthena 与 AIBrix 架构相近，但支持按权重编排多个路由算法，并用单个 Go router 二进制替代 Envoy 加 sidecar 的数据面组合。

Gateway API Inference Extension 被文章描述为一个中心化 Endpoint Picker：它可以与外部数据面对接，由 EPP 选择推理引擎节点。文章认为这种设计降低了采集侧的重复轮询，但如果请求和响应路径都经过 EPP，瓶颈仍可能集中在这个 Go 组件上。Dynamo 则被评价为指标采集更简洁的方案：它主要依赖 KV event 中的 active blocks 与 router 维护的路由历史，并用副本同步和温度随机性缓解多 router 场景下的状态不一致与惊群。

## 关键观点

- AI 推理负载均衡不能只按请求数分配，而要理解输入 token、prefill 成本、decode 成本、KV cache 命中和实时后端状态。
- 在网关侧复用 Hugging Face tokenizer 直接完成本地 tokenization，可以避免远程 tokenize API 带来的额外链路和重复计算。
- 分布式网关高频轮询每个推理引擎会在大规模集群中形成明显的交叉采集成本，Prometheus 查询也不能天然提供更实时的数据。
- KV cache 感知路由必须以 token 前缀和 block 粒度为基础，因为后续 KV cache 的计算依赖前文 token 序列。
- Dynamo 的设计亮点是把后端负载观察收敛到 KV event、active blocks 和 router 本地路由历史，减少对推理引擎指标接口的直接轮询。

## 相关知识

- [AI 推理负载均衡]({{< relref "/wiki/concepts/ai-inference-load-balancing.md" >}})
- [AI 网关中的请求 Tokenization]({{< relref "/wiki/concepts/ai-gateway-tokenization.md" >}})
- [AI 推理网关指标采集]({{< relref "/wiki/concepts/ai-inference-gateway-metric-collection.md" >}})
- [KV Cache 感知路由]({{< relref "/wiki/concepts/kv-cache-aware-routing.md" >}})
- [AIBrix]({{< relref "/wiki/entities/aibrix.md" >}})
- [Kthena]({{< relref "/wiki/entities/kthena.md" >}})
- [Gateway API Inference Extension]({{< relref "/wiki/entities/gateway-api-inference-extension.md" >}})
- [Dynamo]({{< relref "/wiki/entities/dynamo-inference-platform.md" >}})
