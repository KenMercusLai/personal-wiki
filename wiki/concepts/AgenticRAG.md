---
title: "Agentic RAG"
type: concept
tags: [ai, agents, rag, retrieval, coding-agent]
sources:
  - mu-jiang-chui-zi-ding-zi
last_updated: 2026-09-12
knowledge_schema: synthesis-v1
---

## Definition
[[AgenticRAG]] is a retrieval pattern where an agent uses search, reading, and iterative tool calls to gather context on demand instead of relying only on a prebuilt static retrieval index.

## Current Synthesis
The source presents agentic RAG as a better fit for many coding-agent situations than naive vector or full-text RAG. Live codebases change frequently, so indexing creates freshness and cost problems; code also creates a semantic gap because natural-language embedding models may fail to represent code meaning well. In that setting, grep, reading files, and looping through search-refine-read actions can be more intuitive and effective because the agent retrieves from the current workspace at task time.

## Key Claims
- Static RAG can be costly for frequently changing codebases.
- Chunking and indexing can create freshness problems that interfere with normal development.
- Natural-language embeddings may poorly represent code semantics.
- Code retrieval often falls back to keyword and transformed-keyword matching.
- Agent-loop retrieval can use live grep/search plus reading to assemble context only when needed.
- Naive RAG remains useful for stable code, released dependencies, documentation, specifications, and consensus documents.

## Evidence
- Freshness problem: [[mu-jiang-chui-zi-ding-zi]] says frequently changing codebases amplify vector/full-text indexing costs and create stale recall.
- Semantic gap: [[mu-jiang-chui-zi-ding-zi]] says training data differences and natural-language/code mismatch weaken common embedding models for code.
- Agent-loop alternative: [[mu-jiang-chui-zi-ding-zi]] says grep plus reading plus agent loop became a more intuitive and effective approach.
- Residual RAG fit: [[mu-jiang-chui-zi-ding-zi]] says naive RAG can still work for semantically good, stable, versioned code and especially documentation or specifications.

## Counterevidence & Qualifications
The source does not benchmark agentic RAG against modern code-aware retrievers, hybrid search, or IDE indexers. Its strongest claim applies to live, frequently changing codebases; it explicitly leaves room for static RAG when the corpus is stable, well-structured, or document-like.

## What Changed
- Created the concept page for agentic RAG as a code-oriented retrieval pattern.

## Related Concepts
- [[RetrievalAugmentedGeneration]] - agentic RAG is a task-time, loop-driven variant of retrieval-augmented generation.
- [[CodingAgentMinimalTooling]] - grep, read, and bash provide the retrieval substrate in the source.
- [[LLMContextManagement]] - agentic RAG assembles only the needed context instead of preloading a corpus.
- [[Embeddings]] - the source criticizes generic embeddings for code retrieval.
- [[SemanticSearch]] - agentic RAG can include semantic search, but the source emphasizes live textual exploration.
