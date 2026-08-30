---
title: "推理负载均衡器的三层设计"
description: "推理路由需要依次解决请求成本估计、后端状态采集与多目标路由决策。"
type: "concept"
updated: "2026-08-30"
source_keys: ["spacewander-ai-inference-load-balancing"]
featured: true
---

## 三层问题

推理负载均衡器不能只按请求数轮询。它需要连续解决三类问题：

1. **估计请求成本：** 输入Token、可能的输出Token、Prefill/Decode比例和缓存命中。
2. **取得后端状态：** 队列、活跃序列、GPU利用率、KV Block与历史路由。
3. **选择后端：** 在负载、缓存复用、公平性、亲和性和限额之间优化。

Tokenization是第一层的重要输入。Tokenizer不匹配模型或语言，会让Token级成本与配额出现系统误差。Remote Tokenization能保证模型一致性，却会增加链路、流量和故障面；本地Tokenization更直接，但要求网关能加载正确模型配置。

第二层见[分布式调度状态采集]({{< relref "/wiki/concepts/distributed-scheduler-state-collection.md" >}})，第三层常结合[KV Cache感知路由]({{< relref "/wiki/concepts/kv-cache-aware-routing.md" >}})。

## 验证原则

任何路由器优劣都应以端到端指标验证：TTFT、TPOT、吞吐、尾延迟、缓存命中率、状态采集开销，以及故障和副本扩展时的稳定性。组件清单或架构推断不能代替负载实测。

## 来源

- [《锐评主流AI推理负载均衡开源实现》]({{< relref "/wiki/sources/spacewander-ai-inference-load-balancing.md" >}})
