---
title: "如何自建一个自己的 cursor codebase？"
type: source
tags: [ai, coding-agent, codebase, rag, agno]
date: 2025-12-29
source_file: /mnt/ken_personal_wiki/Articles/如何自建一个自己的 cursor codebase？.md
---

## Summary
The article explains how to build a small [[Cursor]]-like codebase question-answering agent with [[Agno]], but deliberately uses text search rather than a vector database. It frames source code as a knowledge base for troubleshooting logs and answering code-structure questions, using two tools: one to grep the repository and another to read file segments around relevant lines. The inspected screenshots show the agent searching memory-related terms, reading Go files, and then producing a Chinese analysis of container memory accounting through cgroups and `/proc/meminfo`.

## Key Claims
- [[Cursor]] codebase search works by vectorizing functions, classes, and logic blocks so similar code can be retrieved for AI question answering.
- For field troubleshooting, source code can become a practical knowledge base when logs are used to drive retrieval and explanation.
- A minimal [[Agno]] implementation can approximate codebase QA with `search_codebase` and `read_file_segment` tools instead of a vector store.
- The agent prompt separates log troubleshooting from general code analysis, giving each path an explicit search/read/reason/report procedure.
- Screenshot evidence shows [[AgenticRAG]] in action: the agent issues multiple searches, reads targeted files, and converts current repository evidence into a structured answer.

## Key Quotes
> "没有使用向量库，而是使用文本匹配。" - on the implementation choice.

> "基于代码做知识库解答" - on treating code as a domain knowledge source for log analysis.

> "两个工具函数，分别是 search_codebase 和 read_file_segment" - on the minimal retrieval tool surface.

## Connections
- [[Cursor]] - the article starts from Cursor's codebase feature and builds a local approximation.
- [[Agno]] - framework used to implement the sample code-analysis agent.
- [[AgenticRAG]] - the sample retrieves code through iterative search and reading at task time.
- [[CodingAgentMinimalTooling]] - the implementation relies on a very small search/read tool set.
- [[AIApplicationFramework]] - Agno is used as the agent framework around model calls, tools, instructions, and a CLI loop.
- [[Gemini]] - the sample model configuration uses Gemini placeholders.
- [[Kubernetes]] - the prompt gives the agent a cloud-native and Kubernetes-controller troubleshooting role.

## Contradictions
- No direct contradictions with existing wiki pages were found. The source reinforces the existing claim that live codebase retrieval can work through grep/read agent loops, while preserving Cursor-style vector search as a separate semantic-retrieval approach.
