---
title: "KV Cache 感知路由"
description: "KV Cache 感知路由通过识别请求 token 前缀和缓存 block 重叠，将请求发送到更可能复用已有缓存的推理引擎。"
type: "concept"
updated: "2026-09-01"
source_keys: ["segmentfault-ai-inference-load-balancing-open-source-implementations"]
---

KV Cache 感知路由尝试把请求发送到能复用已有 KV cache 的推理引擎，以减少重复 prefill 计算。来源 [《锐评主流AI推理负载均衡开源实现》]({{< relref "/wiki/sources/segmentfault-ai-inference-load-balancing-open-source-implementations.md" >}}) 强调，这种复用通常要按 token 前缀和 block 粒度处理，因为推理引擎按 block 共享 KV cache，而后续 token 的 KV cache 计算依赖前面的 token 序列。

不同实现对缓存状态的观察方式不同。AIBrix 消费推理引擎的 KV event，并结合 tokenizer 做前缀树匹配。Gateway API Inference Extension 没有消费推理引擎的 KV event，而是在路由请求后认为目标引擎创建了对应 KV block，并用 LRU 模拟删除。Dynamo 将缓存重叠纳入 worker 成本函数，同时使用 KV event 中的 active blocks 和 router 路由历史估算负载。

## 设计含义

KV cache 命中不能简单按任意相同 token 片段计算。只要中间 token 序列不同，后续计算结果也会不同，因此来源把前缀匹配视为缓存复用路由的关键约束。
