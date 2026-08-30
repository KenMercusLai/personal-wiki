---
title: "KV Cache感知路由"
description: "将共享Prompt前缀尽量发送到已有对应KV Cache的推理节点，同时避免制造负载热点。"
type: "concept"
updated: "2026-08-30"
source_keys: ["spacewander-ai-inference-load-balancing"]
featured: false
---

## 原理

自回归模型计算后续Token时依赖此前Token序列。相同的连续前缀可以复用已生成的Key/Value状态，减少Prefill计算；脱离前缀的局部相同片段通常不能直接复用。

KV Cache感知路由因此需要：

- 用与模型一致的Tokenizer识别Token前缀；
- 了解各Worker拥有或可能拥有的Cache Block；
- 估算未命中的Prefill成本；
- 同时考虑排队、Decode负载和缓存容量。

只追求缓存命中会把相似请求集中到少数节点，形成热点；只追求瞬时均衡又会丢掉前缀复用。实际路由是缓存局部性与负载分散之间的多目标优化。

## 状态可信度

缓存状态可以来自引擎事件、路由历史推断或LRU模拟。三者的实时性和准确度不同；多Router环境还会出现副本视图偏差。因此必须将状态采集机制纳入[推理负载均衡器设计]({{< relref "/wiki/concepts/inference-load-balancer-design.md" >}})评估。

## 来源

- [《锐评主流AI推理负载均衡开源实现》]({{< relref "/wiki/sources/spacewander-ai-inference-load-balancing.md" >}})
