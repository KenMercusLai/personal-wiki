---
title: "Kthena"
description: "Kthena 是一个 Go 实现的推理 router，来源将其与 AIBrix 比较，并强调其加权路由编排和单二进制数据面。"
type: "entity"
updated: "2026-09-01"
source_keys: ["segmentfault-ai-inference-load-balancing-open-source-implementations"]
entity_kind: "software"
---

Kthena 是来源 [《锐评主流AI推理负载均衡开源实现》]({{< relref "/wiki/sources/segmentfault-ai-inference-load-balancing-open-source-implementations.md" >}}) 讨论的推理 router。文章认为它与 AIBrix Gateway 架构相近，但有两个明显改进：支持多个路由算法按权重编排，并采用单个 Go 二进制作为 router。

来源将 Kthena 的单二进制设计与 AIBrix 的 Envoy 加 Go sidecar 组合做对比，认为前者更简单，后续调整空间也更大。不过文章也批评 Kthena 仍使用 `cl100k_base` 作为 tiktoken encoding，认为这延续了不充分理解模型 tokenizer 适配问题的做法。

## 关联主题

Kthena 在来源中主要服务于两个主题：一是推理路由算法可以通过权重组合，而不是把复杂多因子策略全部写进单个算法；二是网关数据面越简单，响应路径、计数和扩展边界越容易保持清晰。
