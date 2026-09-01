---
title: "Gateway API Inference Extension"
description: "Gateway API Inference Extension 是来源讨论的中心化 Endpoint Picker 方案，用 EPP 为外部数据面选择推理引擎节点。"
type: "entity"
updated: "2026-09-01"
source_keys: ["segmentfault-ai-inference-load-balancing-open-source-implementations"]
entity_kind: "software"
---

Gateway API Inference Extension 是来源 [《锐评主流AI推理负载均衡开源实现》]({{< relref "/wiki/sources/segmentfault-ai-inference-load-balancing-open-source-implementations.md" >}}) 讨论的独立推理负载均衡组件，文中简称 GAIE。来源把它描述为一个中心化的 Endpoint Picker，也就是由 EPP 为外部数据面选择要转发到的推理引擎节点。

来源指出，GAIE 的 tokenizer 只做 bytes 除以平均字符数的粗略估算。指标采集方面，它既可以轮询推理引擎，也能从推理响应结尾的 token usage 字段获得数量；但文章认为响应结束后的 usage 汇总缺少路由所需的实时性。

## 路由特点

GAIE 支持多种路由算法按权重编排。对于 KV cache aware routing，来源指出它没有消费推理引擎的 KV event，而是在路由请求后认为目标引擎创建了对应 KV block，并通过 LRU 方式模拟删除。
