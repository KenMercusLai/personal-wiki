---
title: "Chatbox"
type: entity
tags: [project, ai, chat, rag, open-source]
sources:
  - yuan-chao-fa-rag-jin-hua-zhi-lu-chuan-tong-rag-dao-gong-ju-yu-qiang-hua-xue-xi-shuang-lun-qu-dong-de-agentic-rag
last_updated: 2026-09-26
knowledge_schema: synthesis-v1
---

## Overview
[[Chatbox]] is an open-source LLM chat application used by the source as a production-oriented example of file-aware [[AgenticRAG]].

## Current Profile
The inspected architecture gives Chatbox two knowledge-base paths. Tool-capable models receive file-search, listing, metadata, and chunk-reading tools and decide how to use them; models without tool calling first use an LLM prompt to decide whether search is needed, then follow semantic retrieval, optional reranking, context injection, and answer generation.

## Key Characteristics
- Exposes semantic knowledge-base search as one tool rather than the entire retrieval workflow.
- Lets the model inspect file inventories and metadata before reading selected chunks.
- Supports a non-tool-calling fallback with prompted routing, vector retrieval, optional reranking, and augmented generation.
- Uses chunk-level reading to support coarse-to-fine evidence collection.

## Evidence
- Tool surface: [[yuan-chao-fa-rag-jin-hua-zhi-lu-chuan-tong-rag-dao-gong-ju-yu-qiang-hua-xue-xi-shuang-lun-qu-dong-de-agentic-rag]] identifies `query_knowledge_base`, `list_files`, `get_files_meta`, and `read_file_chunks`.
- Dual path: [[yuan-chao-fa-rag-jin-hua-zhi-lu-chuan-tong-rag-dao-gong-ju-yu-qiang-hua-xue-xi-shuang-lun-qu-dong-de-agentic-rag]] diagrams separate tool-capable and prompted-search branches that converge on a final response.
- Evidence refinement: [[yuan-chao-fa-rag-jin-hua-zhi-lu-chuan-tong-rag-dao-gong-ju-yu-qiang-hua-xue-xi-shuang-lun-qu-dong-de-agentic-rag]] gives a worked example where an incomplete hit causes adjacent chunks to be read before answering.

## Qualifications
The available source is an external code-reading and tutorial account, not Chatbox's own architecture specification or a controlled product evaluation. It attributes stronger complex-scenario behavior to file-specific tooling and relaxed latency constraints but supplies no comparative benchmark, and the implementation may evolve after the cited revision.

## What Changed
- Created a source-bounded profile of Chatbox's two knowledge-base retrieval paths.

## Relationships
- [[AgenticRAG]] - Chatbox operationalizes model-directed search, metadata inspection, and chunk reading.
- [[RetrievalAugmentedGeneration]] - its fallback branch retains a more conventional retrieve-rerank-generate pipeline.
- [[YuanChaofa]] - Yuan analyzes Chatbox as the article's principal implementation case.
