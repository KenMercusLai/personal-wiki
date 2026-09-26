---
title: "Agentic RAG"
type: concept
tags: [ai, agents, rag, retrieval, coding-agent]
sources:
  - mu-jiang-chui-zi-ding-zi
  - ru-he-zi-jian-yi-ge-zi-ji-de-cursor-codebase
  - blog-minusx-nuwanda-what-makes-claude-code-so-damn-good
  - blog-guangzhengli-vibe-coding-and-context-coding
  - yuan-chao-fa-rag-jin-hua-zhi-lu-chuan-tong-rag-dao-gong-ju-yu-qiang-hua-xue-xi-shuang-lun-qu-dong-de-agentic-rag
last_updated: 2026-09-26
knowledge_schema: synthesis-v1
---

## Definition
[[AgenticRAG]] is a retrieval pattern where a model controls iterative search, inspection, and reading actions, adapting its evidence-gathering strategy before producing an answer instead of relying only on a fixed retrieve-once pipeline.

## Current Synthesis
The combined sources broaden agentic RAG from a code-search tactic into a general retrieval-control pattern. The defining change is not a more complex model or the disappearance of ordinary retrieval, but the placement of search behind tools that the model can call, inspect, refine, and call again. A useful loop can rewrite a weak query, browse a file list, inspect metadata, read exact chunks, seek adjacent context, or stop when the evidence is sufficient.

Live codebases remain the strongest repeated use case. Their rapid change can make indexes stale, and natural-language embeddings can miss names, calls, dependencies, and business relationships. Grep-style search plus targeted file reads lets an agent work against the current workspace and exposes its retrieval trace for debugging. Cursor-style semantic RAG and live search are nevertheless complementary: semantic similarity can supply candidates while exact exploration follows current code relationships.

[[Chatbox]] shows a document-oriented coarse-to-fine implementation. Tool-capable models can move among semantic search, file listing, metadata inspection, and chunk reading; a fallback path for models without tool calling uses an LLM routing prompt, vector retrieval, optional reranking, and context injection. [[SearchR1]] moves a different design choice into training: reinforcement learning optimizes when to search, what query to issue, and how to continue from results, using bounded tagged rollouts and answer-level reward.

## Key Claims
- Agentic RAG makes retrieval an adaptive model-controlled loop rather than a single fixed search before generation.
- Coarse-to-fine tools can separate candidate discovery, file or metadata inspection, exact chunk reading, and cited answer construction.
- Live code retrieval often benefits from grep/search and targeted reads because index freshness and natural-language-to-code semantic gaps can weaken static RAG.
- Agentic traces can be more debuggable because searches, observations, reads, and query refinements remain visible.
- Semantic RAG and agentic live search are complementary retrieval signals rather than universal substitutes.
- Retrieval policies can be hand-shaped through prompts and tools or learned through reinforcement learning.
- Greater adaptability carries latency, training-cost, data, evaluation, security, and action-budget tradeoffs.

## Evidence
- Adaptive tool loop: [[yuan-chao-fa-rag-jin-hua-zhi-lu-chuan-tong-rag-dao-gong-ju-yu-qiang-hua-xue-xi-shuang-lun-qu-dong-de-agentic-rag]] diagrams repeated model-tool interaction and examples of query rewriting and adjacent-chunk reading before answering.
- Coarse-to-fine document retrieval: [[yuan-chao-fa-rag-jin-hua-zhi-lu-chuan-tong-rag-dao-gong-ju-yu-qiang-hua-xue-xi-shuang-lun-qu-dong-de-agentic-rag]] analyzes Chatbox's semantic search, file listing, metadata, and exact chunk-reading tools.
- Freshness and semantic gap: [[mu-jiang-chui-zi-ding-zi]] says frequently changing codebases amplify index cost and stale recall while generic embeddings can poorly represent code meaning.
- Minimal live-code implementation: [[ru-he-zi-jian-yi-ge-zi-ji-de-cursor-codebase]] implements codebase QA with `search_codebase` and `read_file_segment`, and its screenshots show repeated searches and Go-file reads.
- Debuggable exploration: [[blog-minusx-nuwanda-what-makes-claude-code-so-damn-good]] contrasts visible `ripgrep` and file-reading traces with hidden choices around chunking, similarity, reranking, and index freshness.
- Complementary retrieval: [[blog-guangzhengli-vibe-coding-and-context-coding]] argues that semantic similarity does not equal code association or business context and forecasts AI IDEs combining RAG with grep/search.
- Learned search control: [[yuan-chao-fa-rag-jin-hua-zhi-lu-chuan-tong-rag-dao-gong-ju-yu-qiang-hua-xue-xi-shuang-lun-qu-dong-de-agentic-rag]] presents Search-R1's bounded search/answer rollout and outcome-based reinforcement-learning objective.

## Counterevidence & Qualifications
The sources are tutorials and practitioner analyses rather than joint benchmarks. They do not compare agentic RAG systematically with modern code-aware embeddings, hybrid retrievers, IDE indexes, or human-guided search, and they do not measure ranking quality, large-corpus recall, citation faithfulness, prompt-injection resistance, permissions, or total cost. Static RAG can remain preferable for stable, versioned, document-like corpora or latency-sensitive interactions. The Search-R1 account is secondary and simplified, while the Chatbox analysis may not reflect later code revisions; their diagrams establish architecture, not general superiority.

## What Changed
- Expanded the concept from live-code retrieval to a general model-controlled search, inspection, and reading loop.
- Added Chatbox's dual tool-capable and prompted fallback paths as a coarse-to-fine document-retrieval example.
- Added Search-R1 as evidence that retrieval decisions can be learned rather than only prompt-programmed.
- Made latency, training cost, action budgets, and evaluation gaps explicit limits on adaptability claims.

## Related Concepts
- [[RetrievalAugmentedGeneration]] - agentic RAG changes who controls retrieval and whether it can iterate.
- [[CodingAgentMinimalTooling]] - grep, reading, and shell tools provide a compact live-retrieval substrate.
- [[LLMContextManagement]] - iterative retrieval selects which evidence enters the finite model context.
- [[Embeddings]] - semantic embeddings can supply candidates even when exact live search is also needed.
- [[SemanticSearch]] - semantic search is one possible tool inside a broader agentic retrieval policy.
- [[ReinforcementLearning]] - reinforcement learning can optimize multi-step search decisions from outcome feedback.
- [[Chatbox]] - Chatbox illustrates coarse-to-fine knowledge-base tools and a non-tool fallback.
- [[SearchR1]] - Search-R1 learns interleaved reasoning-and-search behavior.
