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
last_updated: 2026-09-25
knowledge_schema: synthesis-v1
---

## Definition
[[RetrievalAugmentedGeneration]] is an LLM application pattern that retrieves relevant external information and supplies it as context so a model can answer with information beyond its parametric memory.

## Current Synthesis
The baseline RAG pipeline imports and chunks documents, embeds source chunks and questions, searches a vector store, and passes retrieved passages to an LLM with the current question and optionally conversation history. This gives general models access to private, proprietary, or changing information without putting the entire corpus into training. But vector similarity is only one retrieval operation: useful questions may also require lexical matching, metadata and time filters, joins, aggregation, raw-record access, derived summaries, or [[TextToSQL]].

RAG is both an application pattern and an infrastructure chain. Corpus quality, chunking, embeddings, index choice, filters, reranking, context construction, model interpretation, and source governance can all affect the answer. PostgreSQL with pgvector can provide the vector layer; exact search preserves recall at higher cost, while IVFFlat and HNSW introduce different recall, build, and latency tradeoffs. An agent can also use RAG as one tool within a wider observe-act loop.

The pattern has fit boundaries. Frequently changing codebases can make static indexes stale and generic embeddings can miss code relationships, so [[AgenticRAG]] may instead search and read the live workspace iteratively. Conversely, single-pass RAG remains useful where interactive latency matters more than an agent's deeper but slower exploration. A middle path uses a bounded router over specialized retrieval tools: the Timescale example chooses among original records, generated summaries, and SQL analysis, then evaluates routing separately from implementation.

[[RetrievalCentricGeneration]] supplies a second architectural boundary. In this framing, ordinary RAG leaves the model as a major source of information and uses retrieval as a supplement; RCG uses a similar retrieval front end but attempts to make external curated sources dominant and train the model mainly to interpret unseen context. That distinction usefully exposes possible conflicts between retrieved and memorized facts, although the available evidence does not establish RCG's general superiority.

## Key Claims
- RAG combines ingestion, enrichment, multiple retrieval methods, context assembly, and model generation; vector search is one component rather than the whole application.
- Retrieved context can connect general models to private, proprietary, or dynamic data without retraining on the full corpus.
- Chunk size, corpus freshness, embedding fit, retrieval timing, index choice, and context limits determine whether relevant evidence reaches the model.
- Exact and approximate vector search trade recall, latency, index-build cost, and tuning effort.
- Non-agentic RAG remains useful where bounded interactive latency matters, while live or semantically difficult corpora may favor iterative [[AgenticRAG]].
- RAG can route among vector search, structured filters, summaries, raw records, and SQL, but orchestration does not remove retrieval-quality, schema, or access-control failures.
- RAG may blend retrieved evidence with conflicting parametric memory; [[RetrievalCentricGeneration]] proposes making retrieved sources dominant instead.

## Evidence
- Baseline pipeline and context assembly: [[ling-ji-chu-da-jian-ji-yu-si-yu-shu-ju-de-chatgpt]] describes parsing, chunking, embeddings, FAISS retrieval, and passing found passages with the current question and conversation history.
- Enterprise motivation and vector infrastructure: [[aws-blog-optimize-generative-ai-applications-with-pgvector-indexing]] uses private product context to motivate RAG and compares exact search, IVFFlat, and HNSW in PostgreSQL with pgvector.
- Live-code limitation and agentic alternative: [[mu-jiang-chui-zi-ding-zi]] argues that codebase churn and natural-language-to-code embedding gaps can favor grep, reading, and an agent loop over static indexing.
- Latency fit: [[yan-li-how-llm-agents-became-what-they-look-like-in-2026]] names interactive response-time expectations as a reason single-pass, non-agentic RAG persists.
- Agent-tool placement: [[blog-arthur-chiao-yi-ai-agent-ji-shu-bai-pi-shu-google-2024]] depicts query embedding, vector matching, retrieved text, agent decision, and final response within an agent runtime.
- Parametric-memory conflict: [[blog-intel-labs-knowledge-retrieval-takes-center-stage]] argues that retrieved data can conflict with memorized facts and reproduces one [[SimplyRetrieve]] query where a RAG answer adds unsupported locations.
- Architectural boundary: [[blog-intel-labs-knowledge-retrieval-takes-center-stage]] shows RAG and RCG sharing a retrieval pipeline while assigning different informational roles to the model.
- Beyond vector-only retrieval: [[blog-timescale-rag-is-more-than-just-vector-search]] shows a GitHub-issue application combining embeddings with repository filters, time-series data, aggregation, raw records, summaries, and SQL.
- User-driven enrichment and routing: [[blog-timescale-rag-is-more-than-just-vector-search]] derives labels and summaries during ingestion, then tests model choice among three typed retrieval tools.

## Counterevidence & Qualifications
These sources explain architectures and implementation cases more than they measure end-to-end answer quality. They do not jointly benchmark modern hybrid search, reranking, citation faithfulness, prompt-injection defense, permissions, freshness, or conflict resolution. The codebase critique is practitioner evidence and explicitly leaves room for stable or documentation-like corpora; the latency threshold is asserted rather than measured; and the AWS and Timescale performance claims concern retrieval infrastructure rather than generated-answer accuracy. The Timescale snippets also mix `label` and `issue_label`, and their routing assertions do not test execution or answer quality. The Intel Labs RAG-versus-RCG comparison is a single qualitative query and the article concedes RAG may succeed elsewhere. Retrieval can improve grounding without guaranteeing that a source was retrieved, trusted, interpreted correctly, or followed instead of parametric memory.

## What Changed
- Added the distinction between retrieval as an augmentation to model memory and retrieval as the dominant factual layer.
- Added conflict between retrieved evidence and parametric memory as an explicit RAG failure mode.
- Qualified the RCG comparison as a proposed architecture supported by limited evidence.
- Expanded RAG from a vector pipeline to routed semantic, structured, temporal, and analytical retrieval.
- Added tool-routing evaluation as useful decomposition without treating it as end-to-end correctness.

## Related Concepts
- [[PrivateDataChatbot]] - private-data chatbots use RAG to answer from uploaded or organization-held content.
- [[Embeddings]] - embeddings represent questions and source chunks for semantic matching.
- [[VectorDatabase]] - vector databases store and search embedded source material.
- [[Pgvector]] - pgvector provides a PostgreSQL retrieval layer with exact and approximate indexes.
- [[ApproximateNearestNeighborSearch]] - ANN reduces search latency by accepting index and recall tradeoffs.
- [[AgenticRAG]] - agentic RAG retrieves and refines context through an iterative tool loop.
- [[AgentDeploymentTradeoffs]] - latency and predictability influence the choice between single-pass retrieval and agency.
- [[GenerativeAIAgentArchitecture]] - agents can use RAG as one external-information tool.
- [[RetrievalCentricGeneration]] - RCG proposes making retrieval the primary source of facts instead of an augmentation.
- [[SchemaBasedReasoning]] - retrieved evidence still requires structural interpretation to become a valid answer.
- [[TextToSQL]] - structured analytical retrieval covers questions vector similarity cannot answer alone.
- [[EvalsDrivenAIDevelopment]] - routing and answer behavior require separate, repeatable evaluation layers.
