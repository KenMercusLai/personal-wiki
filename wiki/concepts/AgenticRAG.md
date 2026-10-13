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
  - training-100x-cheaper-retrieval-models-neon-and-castform
last_updated: 2026-10-13
knowledge_schema: synthesis-v1
---

## Definition
[[AgenticRAG]] is a retrieval pattern where a model controls iterative search, inspection, and reading actions, adapting its evidence-gathering strategy before producing an answer instead of relying only on a fixed retrieve-once pipeline.

## Current Synthesis
The combined sources broaden agentic RAG from a code-search tactic into a general retrieval-control pattern. The defining change is not a more complex model or the disappearance of ordinary retrieval, but the placement of search behind tools that the model can call, inspect, refine, and call again. A useful loop can rewrite a weak query, browse a file list, inspect metadata, read exact chunks, seek adjacent context, or stop when the evidence is sufficient.

Live codebases remain the strongest repeated use case. Their rapid change can make indexes stale, and natural-language embeddings can miss names, calls, dependencies, and business relationships. Grep-style search plus targeted file reads lets an agent work against the current workspace and exposes its retrieval trace for debugging. Cursor-style semantic RAG and live search are nevertheless complementary: semantic similarity can supply candidates while exact exploration follows current code relationships.

[[Chatbox]] shows a document-oriented coarse-to-fine implementation. Tool-capable models can move among semantic search, file listing, metadata inspection, and chunk reading; a fallback path for models without tool calling uses an LLM routing prompt, vector retrieval, optional reranking, and context injection. [[SearchR1]] moves a different design choice into training: reinforcement learning optimizes when to search, what query to issue, and how to continue from results, using bounded tagged rollouts and answer-level reward.

The [[Castform]] and [[Neon]] case study adds a specialized deployment path. A company's corpus is converted into synthetic questions and inferred answers, a small open-weights model repeatedly calls a shared BM25-plus-vector tool, and the reward scores retrieval, citation, and final-answer correctness. Its reported fine-tune occupies a favorable cost/reward position and its training curve rises, but the source does not expose the benchmark design needed to generalize that result. Thousands of parallel multi-search rollouts also move the bottleneck into bursty database capacity, while future state-changing agents require isolated and resettable environments.

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
- Corpus-derived training: [[training-100x-cheaper-retrieval-models-neon-and-castform]] derives questions and ground truths from company documents, then rewards correct retrieval, citation, and answers over a hybrid search tool.
- Vendor-reported efficiency: [[training-100x-cheaper-retrieval-models-neon-and-castform]] charts its fine-tune at $0.000920 per rollout and 1.447 mean reward versus $0.087338 and 1.369 for GPT-5.6 Sol, alongside smaller gaps to cheaper comparison models.
- Environment load and isolation: [[training-100x-cheaper-retrieval-models-neon-and-castform]] shows bursty rollout-search CPU demand and proposes per-rollout database branches for state-changing agents.

## Counterevidence & Qualifications
Most sources are tutorials, practitioner analyses, or vendor accounts rather than independent joint benchmarks. They do not compare agentic RAG systematically with modern code-aware embeddings, hybrid retrievers, IDE indexes, or human-guided search, and they do not measure ranking quality, large-corpus recall, citation faithfulness, prompt-injection resistance, permissions, or total cost. Static RAG can remain preferable for stable, versioned, document-like corpora or latency-sensitive interactions. The Search-R1 account is secondary and simplified, while the Chatbox analysis may not reflect later code revisions. The Castform benchmark omits dataset, sample count, uncertainty, token and hardware assumptions, equivalent tool budgets, and held-out behavior; its title's near-100x gap applies to the displayed GPT-5.6 Sol comparison, not every model. The diagrams and curves establish architectures and reported observations, not general superiority.

## What Changed
- Added corpus-derived synthetic tasks and composite retrieval/citation/answer rewards as one path to training a specialized retrieval policy.
- Added vendor-reported cost/reward evidence while limiting the near-100x result to one displayed comparison.
- Added bursty database capacity and per-rollout state isolation as environment-level requirements for training retrieval and state-changing agents.

## Related Concepts
- [[RetrievalAugmentedGeneration]] - agentic RAG changes who controls retrieval and whether it can iterate.
- [[CodingAgentMinimalTooling]] - grep, reading, and shell tools provide a compact live-retrieval substrate.
- [[LLMContextManagement]] - iterative retrieval selects which evidence enters the finite model context.
- [[Embeddings]] - semantic embeddings can supply candidates even when exact live search is also needed.
- [[SemanticSearch]] - semantic search is one possible tool inside a broader agentic retrieval policy.
- [[ReinforcementLearning]] - reinforcement learning can optimize multi-step search decisions from outcome feedback.
- [[Chatbox]] - Chatbox illustrates coarse-to-fine knowledge-base tools and a non-tool fallback.
- [[SearchR1]] - Search-R1 learns interleaved reasoning-and-search behavior.
- [[Castform]] - provides the synthetic-task and reinforcement-learning workflow in the Neon case study.
- [[Neon]] - supplies the shared hybrid-search and database environment used during training and inference.
