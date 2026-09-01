---
title: "RAG 进化之路：传统 RAG 到工具与强化学习双轮驱动的 Agentic RAG"
description: "袁超发梳理 RAG 从固定检索生成流水线，演进到由工具调用、ReAct 循环和强化学习驱动的 Agentic RAG，并用 Chatbox 与 Search-R1 作为实现参照。"
type: "source"
updated: "2026-09-01"
source_key: "yuan-chaofa-agentic-rag-evolution"
image_status: "not_selected"
author: "袁超发"
source_date: "2025-10-03"
source_url: "https://yuanchaofa.com/post/from-native-rag-to-agentic-rag.html"
---

## 摘要

这篇文章的主线是给 Agentic RAG 祛魅：传统 RAG 先把文档离线切分、向量化并存入向量库，在线阶段再对用户问题做相似度检索，把 Top-K 文档拼进提示词，由大语言模型生成回答。这个流程容易实现，也足够解释 RAG 的核心价值，但它通常是一次性的固定流水线。

文章认为 Native RAG 的弱点集中在决策能力不足：它不会根据问题拆解任务，不会在证据不够时改写查询或补充搜索，也不擅长先粗后细地定位文件、查看元数据、读取片段并明确引用。Agentic RAG 的区别不是模型本身更神秘，而是让模型作为控制器，在回答前自主决定何时检索、检索什么、读取哪些片段，以及什么时候基于证据作答。

文章用 Chatbox 的知识库工具设计解释提示词和工具驱动的 Agentic RAG。典型工具包括 `query_knowledge_base`、`get_files_meta`、`read_file_chunks` 和 `list_files`。模型通过 ReAct 式的思考、行动、观察循环，先找候选，再看文件信息，最后精读少量片段并给出引用。文中还用 LangChain、LangGraph 和工具装饰器给出一个最小实现。

文章最后讨论 Search-R1 代表的强化学习方向。相比人工提示词和规则，Search-R1 让模型在推理过程中学习何时生成搜索查询、如何利用检索结果，以及如何通过多轮搜索继续推理。作者把这种方向概括为基于强化学习的 Agentic RAG：决策来自训练中习得的策略，适应性更强，但训练成本和数据依赖也更高。

## 关键观点

- RAG 的基本问题是如何检索到更有用的知识，以及如何让模型更好地利用这些知识生成回答。
- Native RAG 通常由离线入库和在线检索生成两条链路组成，在线阶段倾向于一次性检索、拼接和生成。
- Agentic RAG 把搜索能力变成模型可调用的工具，让模型根据任务状态自主改写查询、追加搜索、读取片段和组织答案。
- 工具化 Agentic RAG 的实际价值在于先粗后细的证据收集，而不是简单增加更多上下文。
- 基于强化学习的 Agentic RAG 试图让模型从经验中学习搜索策略，代表做法是 Search-R1 式的推理与搜索交织训练。
- 强化学习路线的适应性更高，但实现复杂度、训练成本和数据依赖也高于传统 RAG 与提示词工具路线。

## 相关知识

- [检索增强生成]({{< relref "/wiki/concepts/retrieval-augmented-generation.md" >}})
- [Native RAG]({{< relref "/wiki/concepts/native-rag.md" >}})
- [Agentic RAG]({{< relref "/wiki/concepts/agentic-rag.md" >}})
- [工具驱动的 Agentic RAG]({{< relref "/wiki/concepts/tool-driven-agentic-rag.md" >}})
- [强化学习驱动的 Agentic RAG]({{< relref "/wiki/concepts/reinforcement-learning-driven-agentic-rag.md" >}})
- [ReAct 智能体循环]({{< relref "/wiki/concepts/react-agent-loop.md" >}})
- [袁超发]({{< relref "/wiki/entities/yuan-chaofa.md" >}})
- [Chatbox]({{< relref "/wiki/entities/chatbox.md" >}})
- [Search-R1]({{< relref "/wiki/entities/search-r1.md" >}})
- [LangChain]({{< relref "/wiki/entities/langchain.md" >}})
