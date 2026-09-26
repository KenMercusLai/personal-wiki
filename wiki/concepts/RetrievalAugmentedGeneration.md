---
title: "Retrieval-Augmented Generation"
type: concept
tags: [ai, rag, retrieval]
sources:
  - ling-ji-chu-da-jian-ji-yu-si-yu-shu-ju-de-chatgpt
  - mu-jiang-chui-zi-ding-zi
  - aws-blog-optimize-generative-ai-applications-with-pgvector-indexing
  - yan-li-how-llm-agents-became-what-they-look-like-in-2026
  - blog-arthur-chiao-yi-ai-agent-ji-shu-bai-pi-shu-google-2024
  - blog-intel-labs-knowledge-retrieval-takes-center-stage
  - blog-timescale-rag-is-more-than-just-vector-search
  - yuan-chao-fa-rag-jin-hua-zhi-lu-chuan-tong-rag-dao-gong-ju-yu-qiang-hua-xue-xi-shuang-lun-qu-dong-de-agentic-rag
last_updated: 2026-09-26
knowledge_schema: synthesis-v1
---

## Definition
[[RetrievalAugmentedGeneration]] is an LLM application pattern that retrieves external information and supplies it as answer context so a model can work with private, current, or source-grounded evidence beyond its parametric memory.

## Current Synthesis
The baseline RAG architecture has an offline and an online path. Offline ingestion loads documents, splits them into chunks, creates embeddings, and stores chunks and vectors. Online answering embeds or otherwise transforms a user query, retrieves candidates, filters or reranks them, assembles a prompt with selected evidence, and asks an LLM to generate the response. This separation makes general models useful over private or changing corpora without retraining on all underlying records.

RAG is broader than vector similarity. Useful retrieval can include lexical matching, metadata and time filters, joins, aggregation, raw-record access, generated summaries, SQL, or file and chunk tools. Its infrastructure choices matter: exact vector search preserves recall at greater cost, while IVFFlat and HNSW trade recall, build effort, memory, and latency. Corpus quality, chunking, embeddings, index freshness, routing, reranking, context construction, permissions, and model interpretation can each determine whether an answer is grounded.

The fixed retrieve-once pipeline has fit boundaries. Top-k context can be noisy or incomplete, multi-hop questions may require task decomposition, and a weak first query may need rewriting or fallback exploration. [[AgenticRAG]] addresses those cases by making search and reading iterative model-controlled actions, while conventional RAG remains useful when predictable interactive latency matters. A hybrid system can retain vector or structured retrieval as tools inside a bounded agent loop.

[[RetrievalCentricGeneration]] exposes another boundary: ordinary RAG often supplements facts already in the model, whereas RCG proposes making curated retrieval the dominant factual layer and training the model mainly to interpret unseen context. This highlights conflicts between retrieved and memorized facts without establishing that one architecture is generally superior.

## Key Claims
- Baseline RAG separates offline ingestion and indexing from online retrieval, context assembly, and generation.
- Retrieved context can connect a general model to private, proprietary, current, or source-grounded information without full-corpus retraining.
- RAG can compose vector search with lexical, metadata, temporal, relational, summary, raw-record, and SQL retrieval.
- Corpus quality, chunking, embedding fit, freshness, routing, reranking, index choice, and context limits jointly shape answer quality.
- Exact and approximate vector search trade recall, latency, build cost, memory, and tuning effort.
- Fixed RAG favors predictable bounded latency, while multi-hop or initially weak retrieval may justify iterative [[AgenticRAG]].
- Retrieved evidence can conflict with parametric memory, motivating architectures that make external curated sources more authoritative.

## Evidence
- Offline/online pipeline: [[yuan-chao-fa-rag-jin-hua-zhi-lu-chuan-tong-rag-dao-gong-ju-yu-qiang-hua-xue-xi-shuang-lun-qu-dong-de-agentic-rag]] diagrams source loading, transformation, embeddings, vector/document storage, query embedding, filtering or reranking, prompt construction, and generation.
- Private-data grounding: [[ling-ji-chu-da-jian-ji-yu-si-yu-shu-ju-de-chatgpt]] describes parsing, chunking, embeddings, FAISS retrieval, and passing passages with the current question and history; [[aws-blog-optimize-generative-ai-applications-with-pgvector-indexing]] motivates the same pattern with private enterprise catalog data.
- Vector-index tradeoffs: [[aws-blog-optimize-generative-ai-applications-with-pgvector-indexing]] compares exact search, IVFFlat, and HNSW in PostgreSQL with pgvector.
- Beyond vector-only retrieval: [[blog-timescale-rag-is-more-than-just-vector-search]] combines embeddings with repository filters, time-series data, aggregation, raw records, summaries, and SQL.
- Agent-tool placement: [[blog-arthur-chiao-yi-ai-agent-ji-shu-bai-pi-shu-google-2024]] places query embedding, vector matching, and retrieved text inside an agent runtime; [[yuan-chao-fa-rag-jin-hua-zhi-lu-chuan-tong-rag-dao-gong-ju-yu-qiang-hua-xue-xi-shuang-lun-qu-dong-de-agentic-rag]] shows search as a repeatedly callable tool.
- Fit boundary: [[mu-jiang-chui-zi-ding-zi]] argues that code churn and embedding mismatch can favor live grep/read loops, while [[yan-li-how-llm-agents-became-what-they-look-like-in-2026]] names latency as a reason non-agentic RAG persists.
- Parametric-memory conflict: [[blog-intel-labs-knowledge-retrieval-takes-center-stage]] reproduces one query where a RAG answer adds unsupported locations and proposes retrieval-centric generation instead.

## Counterevidence & Qualifications
These sources explain architectures and implementation cases more often than they measure end-to-end answer quality. They do not jointly benchmark retrieval recall, citation faithfulness, reranking, prompt-injection defense, permissions, source freshness, conflict resolution, or total application cost. The AWS performance figures concern vector-query infrastructure rather than generated-answer accuracy; the Timescale tutorial contains schema inconsistencies; and the Intel Labs RAG-versus-RCG case is one qualitative query. The new native-versus-agentic comparison is conceptual and tutorial-based: iterative retrieval can recover from weak evidence, but it also adds latency, tool and policy failures, larger action surfaces, and evaluation burden.

## What Changed
- Added the explicit offline-ingestion and online-answering split for baseline RAG.
- Added fixed-pipeline failure modes around noisy top-k context, incomplete chunks, weak first queries, and multi-step evidence gathering.
- Clarified that vector and structured retrieval can remain tools inside an agentic loop rather than being replaced by it.
- Preserved latency as a reason to choose conventional RAG despite the greater adaptability of iterative retrieval.

## Related Concepts
- [[PrivateDataChatbot]] - private-data chatbots retrieve user- or organization-held content for grounded answers.
- [[Embeddings]] - embeddings represent source chunks and queries for semantic comparison.
- [[VectorDatabase]] - vector databases store and search embedded material.
- [[Pgvector]] - pgvector provides exact and approximate vector search within PostgreSQL.
- [[ApproximateNearestNeighborSearch]] - ANN reduces query work by accepting recall and tuning tradeoffs.
- [[AgenticRAG]] - agentic RAG turns retrieval into an iterative model-controlled process.
- [[AgentDeploymentTradeoffs]] - latency and reproducibility influence the choice between fixed retrieval and agency.
- [[RetrievalCentricGeneration]] - RCG proposes making retrieval the dominant source of facts.
- [[TextToSQL]] - structured analytical retrieval covers questions vector similarity cannot answer alone.
- [[EvalsDrivenAIDevelopment]] - routing, retrieval, and final-answer behavior need separate evaluation layers.
