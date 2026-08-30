---
title: "锐评主流AI推理负载均衡开源实现"
description: "spacewander按Tokenization、状态采集和路由决策比较AIBrix、Kthena、GAIE与Dynamo的推理负载均衡设计。"
type: "source"
author: "spacewander"
source_date: "2026-03-29"
updated: "2026-08-30"
source_url: "https://segmentfault.com/a/1190000047682071"
source_key: "spacewander-ai-inference-load-balancing"
featured: true
image_status: "原文没有图片引用"
---

## 核心摘要

文章把[推理负载均衡器]({{< relref "/wiki/concepts/inference-load-balancer-design.md" >}})拆成三个问题：如何估计请求负载、如何取得与均衡有关的状态，以及如何据此选择后端。它用这套框架比较AIBrix、Kthena、Gateway API Inference Extension（GAIE）和Dynamo。

文章最有价值的部分不是给项目排固定名次，而是揭示推理路由的专有约束：Tokenization必须与模型匹配；Prompt前缀决定[KV Cache感知路由]({{< relref "/wiki/concepts/kv-cache-aware-routing.md" >}})的收益；状态采集的实时性、扇出成本和一致性存在结构性权衡。

> **时间边界：** 这是2026-03-29的项目实现快照。默认参数、组件关系、Tokenizer选项和命令行开关可能快速变化，使用前必须回到对应项目和版本核验。

> **图片状态：** 原文没有图片引用，本次Ingest没有生成或补配架构图。

## 比较框架

### 1. 请求成本估计

推理负载不仅取决于请求数。输入Token影响Prefill，输出Token影响Decode，缓存命中又会减少需要重新计算的前缀。网关若要做Token级配额或路由，需要采用与目标模型兼容的Tokenizer。

作者质疑按Byte近似、固定`averageCharactersPerToken`以及不匹配模型的`tiktoken`编码。这个批评的稳定部分是：**估算器必须按目标语料和模型校准**。至于某一编码在特定项目中是否“错误”，仍需结合当时支持模型、实际调用路径和误差测试确认。

### 2. 状态采集

文章区分三种信号来源：

- 网关轮询推理引擎Metrics；
- 查询Prometheus等聚合系统；
- 消费引擎发布的KV Cache或Active Block事件。

作者指出，如果每个网关都轮询每个引擎，请求数会随网关数与引擎数乘积增长。文中“500个引擎×20个网关×每秒20次=200k请求/秒”的算术成立，但把这种模式概括为`O(n²)`需要前提：网关数也随引擎规模线性增长。更准确的表达是`O(G×E×f)`，其中`G`为采集者数、`E`为引擎数、`f`为轮询频率。

这形成了[分布式调度状态采集]({{< relref "/wiki/concepts/distributed-scheduler-state-collection.md" >}})的核心权衡：新鲜度、采集成本、中心瓶颈和副本一致性不能同时免费获得。

### 3. 路由决策

- **AIBrix：** 文中描述其支持多种路由算法，并可利用KV事件和Token前缀树寻找缓存复用机会。
- **Kthena：** 作者看重多算法加权和单一Go Router数据面，同时批评其Tokenizer选择。
- **GAIE：** EPP集中做Endpoint选择，可避免每个数据面独立采集；作者担心请求/响应经过EPP形成吞吐瓶颈，并质疑其用路由历史加LRU模拟KV状态的精度。
- **Dynamo：** 以未命中的Prefill Block与估计Decode Block构造成本函数，通过KV事件、路由历史和Router副本同步维护状态，减少全量轮询。

## KV Cache为什么依赖前缀

自回归Transformer中，后续Token的Key/Value状态依赖此前Token序列。只有从开头连续相同的Token前缀才能直接复用相应Cache Block；中间序列相同但前文不同，状态通常不能直接替换。因此，缓存感知路由会同时考虑前缀重叠和当前后端负载。

## 作者评价与可复核事实

文章大量使用“毫无意义”“不够专业”“鹦鹉学舌”等评价。编译时保留其背后的可检验问题，但不把语气当结论：

- Tokenizer与模型是否匹配，可用项目配置和误差基准复核；
- Prometheus路径是否冗余，取决于采集间隔、聚合价值与故障隔离；
- EPP是否成为瓶颈，需要吞吐、并发和副本扩展实测；
- 事件驱动状态是否优于轮询，取决于事件完整性、延迟和恢复机制；
- 多Router同步只能缩小状态偏差，不能提供无延迟的全局真相。

## 来源

- spacewander，[《锐评主流AI推理负载均衡开源实现》](https://segmentfault.com/a/1190000047682071)，2026-03-29。
