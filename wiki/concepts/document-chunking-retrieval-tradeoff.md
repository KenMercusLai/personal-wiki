---
title: "文档切片的检索权衡"
description: "切片过小可能丢失上下文，切片过大可能引入无关内容；参数必须结合语料和问答任务评估。"
type: "concept"
updated: "2026-08-30"
source_keys: ["shensiquan-private-data-chatgpt-langchain"]
featured: false
---

## 核心权衡

在[检索增强生成流水线]({{< relref "/wiki/concepts/retrieval-augmented-generation-pipeline.md" >}})中，文档通常先被拆成片段，再生成Embedding并建立索引。片段同时是语义检索的基本单元和返回给模型的上下文单元。

来源文章提出两个方向相反的风险：

- **片段太小：** 一个事实、论证或步骤可能被切断，检索结果缺少理解所需的上下文。
- **片段太大：** 命中片段可能夹带更多无关信息，占用上下文并稀释真正相关的内容。

## 不能从来源推出的结论

来源只解释了这个工程权衡，没有报告不同Chunk大小、重叠策略、文档类型或查询集合的对照实验。因此不能从文章中推出通用的最佳`chunk_size`，也不能断言某种字符级切分器适合所有资料。

## 实践含义

切片策略应与文档结构、查询粒度和验证指标一起设计。像[LangChain]({{< relref "/wiki/entities/langchain.md" >}})这样的框架可以提供切分组件，但组件的存在不会自动解决边界选择问题。

## 来源

- [《零基础｜搭建基于私域数据的ChatGPT》]({{< relref "/wiki/sources/shensiquan-private-data-chatgpt-langchain.md" >}})
