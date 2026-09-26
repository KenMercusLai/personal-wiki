---
title: "RAG 进化之路：传统 RAG 到工具与强化学习双轮驱动的 Agentic RAG"
type: source
tags: [ai, rag, agentic-rag, reinforcement-learning, search]
date: 2025-10-03
source_file: "/mnt/ken_personal_wiki/Articles/袁超发 - RAG 进化之路：传统 RAG 到工具与强化学习双轮驱动的 Agentic RAG.md"
---

## Summary
[[YuanChaofa]] explains [[RetrievalAugmentedGeneration]] as a fixed offline-ingestion and online-retrieval pipeline, then defines [[AgenticRAG]] by placing model-directed search, reading, and query revision inside an iterative tool loop. The article uses [[Chatbox]] to show a prompt-and-tool implementation that moves from candidate discovery to file metadata and chunk-level reading, and [[SearchR1]] to show how [[ReinforcementLearning]] can train the search policy rather than encode it only in prompts. The retained diagrams make the control boundaries, fallback branches, bounded multi-turn rollout, and evidence-return path explicit.

## Key Claims
- Traditional [[RetrievalAugmentedGeneration]] separates offline document loading, splitting, embedding, and storage from online query embedding, retrieval, context assembly, and generation.

![Native RAG offline ingestion and online retrieval-generation pipeline](../../wiki-assets/yuan-chao-fa-rag-jin-hua-zhi-lu-chuan-tong-rag-dao-gong-ju-yu-qiang-hua-xue-xi-shuang-lun-qu-dong-de-agentic-rag/native-rag-offline-online-pipeline.png)

- [[AgenticRAG]] makes search a tool under model control, allowing repeated reason-act-observe cycles, query rewriting, fallback exploration, and evidence gathering before the final response.

![Agentic RAG loop between an LLM and search tools until the model answers](../../wiki-assets/yuan-chao-fa-rag-jin-hua-zhi-lu-chuan-tong-rag-dao-gong-ju-yu-qiang-hua-xue-xi-shuang-lun-qu-dong-de-agentic-rag/agentic-rag-tool-loop.png)

- [[Chatbox]] implements two retrieval paths: tool-capable models can choose among semantic search, file listing, metadata inspection, and chunk reading, while models without tool calling use an LLM routing prompt followed by semantic search, optional reranking, and augmented generation.

![Chatbox routing between tool-driven agentic retrieval and a prompted retrieval fallback](../../wiki-assets/yuan-chao-fa-rag-jin-hua-zhi-lu-chuan-tong-rag-dao-gong-ju-yu-qiang-hua-xue-xi-shuang-lun-qu-dong-de-agentic-rag/chatbox-agentic-rag-routing.png)

- A coarse-to-fine retrieval policy first finds candidate files or chunks, inspects metadata where useful, then reads a small number of exact chunks so the answer can cite evidence actually observed by the model.
- [[SearchR1]] uses [[ReinforcementLearning]] to teach a model when to search, what query to issue, and how to continue reasoning from returned evidence instead of relying entirely on hand-written prompt rules.

![Search-R1 reasoning loop that searches when needed and returns to reasoning with results](../../wiki-assets/yuan-chao-fa-rag-jin-hua-zhi-lu-chuan-tong-rag-dao-gong-ju-yu-qiang-hua-xue-xi-shuang-lun-qu-dong-de-agentic-rag/search-r1-reason-search-loop.png)

- Search-R1 represents search and answer actions with explicit tags, enforces a maximum action budget, inserts retrieved information into the rollout, and asks the model to rethink malformed actions before continuing.

![Search-R1 bounded multi-turn rollout algorithm with search, answer, and rethink branches](../../wiki-assets/yuan-chao-fa-rag-jin-hua-zhi-lu-chuan-tong-rag-dao-gong-ju-yu-qiang-hua-xue-xi-shuang-lun-qu-dong-de-agentic-rag/search-r1-multi-turn-rollout-algorithm.png)

- A worked Search-R1 trajectory repeatedly searches two people, compares their retrieved professions, and answers only after identifying the shared profession, illustrating interleaved reasoning and retrieval rather than a single top-k lookup.

![Search-R1 example trajectory using repeated searches to identify a shared profession](../../wiki-assets/yuan-chao-fa-rag-jin-hua-zhi-lu-chuan-tong-rag-dao-gong-ju-yu-qiang-hua-xue-xi-shuang-lun-qu-dong-de-agentic-rag/search-r1-example-trajectory.png)

## Key Quotes
> "Agentic RAG 的核心不是更复杂的模型，而是让模型学会做事。" - on agency as retrieval control rather than model size.

> "先粗后细" - the article's compact retrieval strategy.

> "何时搜索、搜索什么以及如何利用搜索结果" - the decisions Search-R1 is intended to learn.

## Connections
- [[YuanChaofa]] - author explaining the progression from fixed RAG to tool- and learning-driven retrieval.
- [[RetrievalAugmentedGeneration]] - baseline offline and online pipeline against which the agentic variants are compared.
- [[AgenticRAG]] - central pattern of model-directed, iterative evidence retrieval.
- [[Chatbox]] - production-oriented example of prompt routing, file-aware tools, semantic search, and chunk reading.
- [[SearchR1]] - reinforcement-learning framework for interleaving reasoning and multi-turn search.
- [[ReinforcementLearning]] - optimization method used to learn retrieval behavior from answer-level reward.
- [[LangChain]] - framework used in the article's traditional RAG example.
- LangGraph - framework used to assemble the ReAct-style tool agent example.

## Contradictions
- The source expands the wiki's earlier codebase-centered [[AgenticRAG]] account into a general document-search pattern; it does not contradict the code-specific evidence but shows that semantic search, metadata inspection, and chunk reading can remain useful inside the agent loop.
- The comparison table ranks RL-based Agentic RAG as more adaptive than prompt-based Agentic RAG, but the article provides tutorial examples rather than a controlled benchmark and explicitly notes higher training cost and data dependence.
