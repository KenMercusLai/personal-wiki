---
title: "锐评主流AI推理负载均衡开源实现"
type: source
tags: [ai-inference, load-balancing, open-source]
date: 2026-03-29
source_file: Articles/锐评主流AI推理负载均衡开源实现.md
---

## Summary
文章以请求 tokenization、指标获取和均衡决策为比较框架，评述 [[AIBrix]]、[[Kthena]]、[[GatewayAPIInferenceExtension]] 与 [[NvidiaDynamo]] 的开源推理负载均衡实现。作者认为，本地使用与模型匹配的 tokenizer 优于字节估算或远程 tokenize 服务，而基于 KV 事件和路由历史的状态维护比网关高频轮询后端更适合大规模集群；这些判断主要来自架构与代码层面的分析，未提供统一基准测试。

## Key Claims
- 推理负载均衡至少要正确估算请求负载、及时获取后端状态，并依据指标实现均衡；限额是在这些负载信息之上的策略层。
- AIBrix 和 Kthena 使用面向 GPT 模型的 `cl100k_base` 会在模型不匹配时产生 token 估算风险；作者主张在网关内使用与部署模型一致的 Hugging Face tokenizer。
- 分布式网关逐一高频轮询所有推理引擎会随网关和引擎数量形成乘法级开销，并在规模扩大时迫使系统在实时性和资源消耗间取舍。
- [[KVCacheAwareRouting]] 只能复用共同前缀对应的缓存块，因为后续 KV 计算依赖此前 token；AIBrix 消费真实 KV 事件，GAIE 则以路由记录和 LRU 模拟缓存状态。
- Dynamo 以 KV active-block 事件和本地路由历史估算负载，通过副本同步和随机温度缓解多路由器状态片面与惊群问题，作者据此评价其指标路径最简洁。
- Kthena 与 GAIE 支持加权组合路由策略；Kthena 的单一 Go 数据面也避免了 AIBrix 的 Envoy 加 sidecar 路径所带来的响应侧计量限制。

## Key Quotes
> “一个负载均衡首先需要懂得跑在自己上面的负载是怎么样的，其次还要能知道离均衡状态还有多远。” — 作者提出评价推理负载均衡器的基本框架

> “负载的均衡性和实时性呈正相关” — 作者说明指标新鲜度与资源开销之间的架构取舍

## Connections
- [[InferenceLoadBalancing]] — 提供 tokenizer、指标采集和路由决策三方面的实现比较。
- [[KVCacheAwareRouting]] — 比较真实 KV 事件、前缀匹配与 LRU 模拟三种缓存感知方法。
- [[AIBrix]] — 被批评存在 tokenizer 配置和大规模轮询开销问题。
- [[Kthena]] — 以加权策略编排和单二进制数据面改进 AIBrix 式设计。
- [[GatewayAPIInferenceExtension]] — 采用中心化 EPP、字节估算和模拟 KV 缓存状态。
- [[NvidiaDynamo]] — 以事件驱动状态和成本函数构成作者最认可的实现。

## Contradictions
- 暂未发现与现有 wiki 内容直接矛盾；这是当前语料中首个推理负载均衡主题来源。
