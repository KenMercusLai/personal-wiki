---
title: "AIBrix"
description: "AIBrix 是一个推理平台，其网关在来源中被用来分析 tokenizer、指标采集和 KV cache 感知路由的设计取舍。"
type: "entity"
updated: "2026-09-01"
source_keys: ["segmentfault-ai-inference-load-balancing-open-source-implementations"]
entity_kind: "software"
---

AIBrix 是来源 [《锐评主流AI推理负载均衡开源实现》]({{< relref "/wiki/sources/segmentfault-ai-inference-load-balancing-open-source-implementations.md" >}}) 讨论的 AI 推理平台之一。文章在比较时主要关注它的网关能力：tokenizer、指标采集机制和路由算法。

来源称，AIBrix 支持按 byte 切分、使用 tiktoken，以及调用远程 tokenize API。文章批评它在 tiktoken 路径中选择过时或不匹配的 encoding，并认为远程 tokenize API 会增加不必要的串联链路。指标采集方面，AIBrix 既会由网关 worker 高频轮询推理引擎 metrics，也会查询 Prometheus，还会消费推理引擎推送的 KV event。

## 路由特点

AIBrix 支持多种路由算法，其中 KV cache aware 路由会结合 KV event 和 tokenizer 输出做前缀树匹配，以寻找更容易复用缓存的推理引擎。来源同时指出，AIBrix 的 Envoy 加 Go sidecar 数据面组合会影响某些路由算法对响应路径真实 output token 的掌握。
