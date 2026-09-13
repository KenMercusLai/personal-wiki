---
title: "Agentic RAG"
type: concept
tags: [ai, agents, rag, retrieval, coding-agent]
sources:
  - mu-jiang-chui-zi-ding-zi
  - ru-he-zi-jian-yi-ge-zi-ji-de-cursor-codebase
last_updated: 2026-09-13
knowledge_schema: synthesis-v1
---

## Definition
[[AgenticRAG]] is a retrieval pattern where an agent uses search, reading, and iterative tool calls to gather context on demand instead of relying only on a prebuilt static retrieval index.

## Current Synthesis
The sources present agentic RAG as a better fit for many coding-agent situations than naive vector or full-text RAG. Live codebases change frequently, so indexing creates freshness and cost problems; code also creates a semantic gap because natural-language embedding models may fail to represent code meaning well. In that setting, grep, reading files, and looping through search-refine-read actions can be more intuitive and effective because the agent retrieves from the current workspace at task time.

The Agno codebase tutorial supplies a compact implementation example. Instead of building a vector database, it gives an agent two tools: text search over the repository and file-segment reading around relevant lines. The inspected screenshots show the loop concretely: a user asks how a repository determines memory usage, the agent searches terms such as `memory`, `mem_usage`, `cgroup`, and `/proc/meminfo`, reads `pkg/memory.go` and `pkg/cpu.go`, then explains the cgroup-based implementation.

## Key Claims
- Static RAG can be costly for frequently changing codebases.
- Chunking and indexing can create freshness problems that interfere with normal development.
- Natural-language embeddings may poorly represent code semantics.
- Code retrieval often falls back to keyword and transformed-keyword matching.
- Agent-loop retrieval can use live grep/search plus reading to assemble context only when needed.
- A two-tool search/read implementation can be enough for useful codebase QA when the agent has task-specific instructions.
- Naive RAG remains useful for stable code, released dependencies, documentation, specifications, and consensus documents.

## Evidence
- Freshness problem: [[mu-jiang-chui-zi-ding-zi]] says frequently changing codebases amplify vector/full-text indexing costs and create stale recall.
- Semantic gap: [[mu-jiang-chui-zi-ding-zi]] says training data differences and natural-language/code mismatch weaken common embedding models for code.
- Agent-loop alternative: [[mu-jiang-chui-zi-ding-zi]] says grep plus reading plus agent loop became a more intuitive and effective approach.
- Minimal implementation: [[ru-he-zi-jian-yi-ge-zi-ji-de-cursor-codebase]] implements codebase QA with `search_codebase` and `read_file_segment` rather than a vector store.
- Screenshot trace: [[ru-he-zi-jian-yi-ge-zi-ji-de-cursor-codebase]] shows an agent searching memory-related terms, reading Go files, and producing a grounded explanation from the retrieved code.
- Residual RAG fit: [[mu-jiang-chui-zi-ding-zi]] says naive RAG can still work for semantically good, stable, versioned code and especially documentation or specifications.

## Counterevidence & Qualifications
The sources do not benchmark agentic RAG against modern code-aware retrievers, hybrid search, or IDE indexers. The Agno tutorial demonstrates feasibility for a small example, but it does not address ranking quality, large-repository recall, security, sandboxing, or evaluation. The strongest claim applies to live, frequently changing codebases; the sources leave room for static RAG when the corpus is stable, well-structured, or document-like.

## What Changed
- Created the concept page for agentic RAG as a code-oriented retrieval pattern.
- Added an Agno implementation example where search/read tools replace a vector store for codebase QA.

## Related Concepts
- [[RetrievalAugmentedGeneration]] - agentic RAG is a task-time, loop-driven variant of retrieval-augmented generation.
- [[CodingAgentMinimalTooling]] - grep, read, and bash provide the retrieval substrate in the source.
- [[LLMContextManagement]] - agentic RAG assembles only the needed context instead of preloading a corpus.
- [[Embeddings]] - the source criticizes generic embeddings for code retrieval.
- [[SemanticSearch]] - agentic RAG can include semantic search, but the source emphasizes live textual exploration.
- [[Agno]] - Agno hosts the tutorial's search/read codebase agent.
