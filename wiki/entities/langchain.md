---
title: "LangChain"
description: "用于组合语言模型、提示、检索、记忆和工具调用的大模型应用开发框架；本页保留来源文章中的早期历史定位。"
type: "entity"
entity_kind: "software"
updated: "2026-08-30"
source_keys: ["shensiquan-private-data-chatgpt-langchain"]
featured: false
---

## 概览

来源文章把LangChain描述为大模型应用的中间框架层：开发者通过框架连接底层模型、外部数据和应用工作流，而不必为每个项目重新实现所有组合逻辑。

## 来源文章中的模块划分

文章提到模型调用、Prompt模板、Chains、Memory、向量存储和Agents等模块，并把它们用于[检索增强生成]({{< relref "/wiki/concepts/retrieval-augmented-generation-pipeline.md" >}})示例：文档切片、Embedding、向量检索、历史问答和模型调用被组织为一个完整流程。

## 历史边界

这是一篇约2023年3月的生态快照。模块名称、API、样例仓库、融资和估值信息都可能已经变化；本页不把这些历史操作细节升级为当前使用说明。需要实现新系统时，应以当前官方文档和真实端到端测试为准，尤其要实测[切片与检索之间的权衡]({{< relref "/wiki/concepts/document-chunking-retrieval-tradeoff.md" >}})。

## 来源

- [《零基础｜搭建基于私域数据的ChatGPT》]({{< relref "/wiki/sources/shensiquan-private-data-chatgpt-langchain.md" >}})
