---
title: "Dynamo"
description: "Dynamo 是来源评价较高的推理平台方案，其 router 使用本地 tokenizer、KV event 和成本函数进行路由决策。"
type: "entity"
updated: "2026-09-01"
source_keys: ["segmentfault-ai-inference-load-balancing-open-source-implementations"]
entity_kind: "software"
---

Dynamo 是来源 [《锐评主流AI推理负载均衡开源实现》]({{< relref "/wiki/sources/segmentfault-ai-inference-load-balancing-open-source-implementations.md" >}}) 讨论的推理平台。文章认为它的 tokenizer 都是本地实现，包括 Hugging Face Tokenizer、基于 OpenAI tiktoken 的 fork，以及 encode 阶段使用 fastokens 的 fast tokenizer。

Dynamo 的路由策略可以配置，核心策略是用成本函数选择最优 worker。来源概括的成本由缓存重叠后的 prefill blocks、基于活跃序列估算的 decode blocks，以及调节缓存命中和负载分布的 overlap score weight 共同决定。

## 指标采集

来源将 Dynamo 的创新点归结为更简洁的指标采集：它主要依赖 KV event 中的 active blocks 和 router 自己维护的路由历史，不需要像其他方案那样高频轮询后端推理引擎。多 router 部署时，Dynamo 通过 router 副本间状态同步共享信息，并通过温度选项引入适度随机性。
