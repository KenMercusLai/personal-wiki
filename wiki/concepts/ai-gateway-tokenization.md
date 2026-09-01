---
title: "AI 网关中的请求 Tokenization"
description: "AI 网关中的请求 tokenization 用来在路由前估算推理负载，tokenizer 的位置和模型适配会影响准确性与链路成本。"
type: "concept"
updated: "2026-09-01"
source_keys: ["segmentfault-ai-inference-load-balancing-open-source-implementations"]
---

AI 网关中的请求 tokenization 是在推理请求进入后端前估算输入规模的关键步骤。来源 [《锐评主流AI推理负载均衡开源实现》]({{< relref "/wiki/sources/segmentfault-ai-inference-load-balancing-open-source-implementations.md" >}}) 比较了几类实现：按 byte 或平均字符数粗略估算、使用 OpenAI tiktoken、调用远程 tokenize API，以及在网关本地使用 Hugging Face tokenizer。

来源的主要判断是，tokenizer 应尽量与实际部署模型匹配。为 GPT 系列设计的 tiktoken encoding 如果被直接用于其他模型，尤其在没有显式分隔符的中文内容上，可能带来明显偏差。远程 tokenize API 能把模型侧 tokenizer 能力暴露给网关，但会增加一次额外服务调用，并把请求流量复制到另一条链路。

## 方案取舍

- AIBrix 支持按 byte、tiktoken 和远程 tokenize API 三种方式。
- Kthena 被来源批评仍沿用 `cl100k_base` 作为 tiktoken encoding。
- Gateway API Inference Extension 使用 bytes 除以平均字符数的粗略估算方式。
- Dynamo 支持 Hugging Face Tokenizer、tiktoken fork 和 fast tokenizer 等本地 tokenizer。
