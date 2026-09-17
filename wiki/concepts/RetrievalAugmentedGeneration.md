---
title: "Retrieval-Augmented Generation"
type: concept
tags: [ai, rag, retrieval]
sources:
  - ling-ji-chu-da-jian-ji-yu-si-yu-shu-ju-de-chatgpt
  - mu-jiang-chui-zi-ding-zi
  - aws-blog-optimize-generative-ai-applications-with-pgvector-indexing
  - yan-li-how-llm-agents-became-what-they-look-like-in-2026
last_updated: 2026-09-17
knowledge_schema: synthesis-v1
---

## Definition
[[RetrievalAugmentedGeneration]] is an LLM application pattern that retrieves relevant external information and supplies it as context to a model so generated answers can be grounded in that information.

## Current Synthesis
The first source explains RAG through a private-data chatbot workflow. Documents are imported and chunked, chunks are embedded and stored in a vector database, user questions are embedded for similarity search, and the retrieved passages are sent to the LLM alongside the current question and previous conversation history. In this framing, RAG is the practical bridge between general-purpose language models and user-specific data.

RAG has a sharp fit boundary in frequently changing codebases: static indexes grow stale, chunking and indexing can interrupt development flow, and generic embeddings may not bridge natural language and code semantics. In those situations, [[AgenticRAG]] can retrieve current code context through grep, reading, and iterative agent-loop exploration.

Enterprise RAG also has a database layer. The pattern can fill the gap between general foundation models and private enterprise context, but its retrieval path depends on embedding generation, vector storage, and index choice. For PostgreSQL-backed RAG, exact search may be acceptable for small or accuracy-critical cases, while [[ApproximateNearestNeighborSearch]] with [[IVFFlatIndex]] or [[HNSWIndex]] can make retrieval fast enough for larger interactive applications.

A staged-history source adds a product-fit reason the non-agentic form survives. It argues that agentic loops buy quality with latency, and that ordinary chatbot users expect a response within roughly 20-30 seconds, so a single retrieval pass can still be the better design even when an agent could answer more thoroughly. In that account RAG persists not because retrieval is better than agency but because its response-time profile matches interactive use, which places the pattern inside the wider set of [[AgentDeploymentTradeoffs]].

## Key Claims
- RAG starts with document ingestion, parsing, chunking, and embedding source chunks plus user questions for similarity search.
- A vector database stores document vectors, and retrieved chunks become contextual evidence for the LLM answer; the single-pass design also keeps non-agentic RAG viable where an agentic loop would be too slow.
- Conversation history can be included with retrieved passages and the current question.
- Chunk size, corpus stability, update frequency, retrieval timing, and semantic representation quality affect whether the model receives enough relevant context, too much irrelevant material, or stale material.
- Live codebases may be better served by [[AgenticRAG]] than by static vector indexes.
- Enterprise RAG often exists because foundation models lack organization-specific context.
- PostgreSQL plus pgvector can act as the vector retrieval layer for a RAG application, where index choice introduces a recall-latency tradeoff that affects grounding.

## Evidence
- Pipeline overview: [[ling-ji-chu-da-jian-ji-yu-si-yu-shu-ju-de-chatgpt]] lists import/parse/split, embeddings, FAISS storage, question embeddings, similarity search, and LLM answering as the main steps.
- Context assembly: [[ling-ji-chu-da-jian-ji-yu-si-yu-shu-ju-de-chatgpt]] says the current question, previous Q&A, and found passages are passed to the model together.
- Chunking tradeoff: [[ling-ji-chu-da-jian-ji-yu-si-yu-shu-ju-de-chatgpt]] explains that chunk size controls how much reference information the model receives.
- Implementation tools: [[ling-ji-chu-da-jian-ji-yu-si-yu-shu-ju-de-chatgpt]] identifies LangChain splitters, OpenAI embeddings, vector stores, FAISS, and LLMChain as implementation pieces.
- Codebase limits: [[mu-jiang-chui-zi-ding-zi]] says frequently changing codebases create indexing cost and freshness problems for naive RAG.
- Semantic limits: [[mu-jiang-chui-zi-ding-zi]] says common embeddings can struggle to represent code from natural-language queries.
- Agentic alternative: [[mu-jiang-chui-zi-ding-zi]] says grep plus reading plus an agent loop can be more intuitive and effective for coding agents.
- Enterprise-context motivation: [[aws-blog-optimize-generative-ai-applications-with-pgvector-indexing]] says foundation models need RAG or other customization methods to answer with private enterprise context.
- PostgreSQL retrieval layer: [[aws-blog-optimize-generative-ai-applications-with-pgvector-indexing]] stores product-catalog embeddings in PostgreSQL with pgvector and retrieves similar chunks for prompts.
- Index tradeoff: [[aws-blog-optimize-generative-ai-applications-with-pgvector-indexing]] compares exact search, IVFFlat, and HNSW as retrieval-performance choices.
- Latency fit: [[yan-li-how-llm-agents-became-what-they-look-like-in-2026]] says the tolerable latency of a chatbot is roughly 20-30 seconds to first token and names that as one reason non-agentic RAG still exists.

## Counterevidence & Qualifications
The private-data chatbot source presents the basic pattern but does not cover advanced retrieval quality, reranking, source attribution, evaluation, prompt injection, access control, freshness, or conflict handling across retrieved passages. The coding-agent source is a practitioner critique rather than a benchmark and explicitly preserves a role for naive RAG when code and comments are stable, semantically rich, versioned, or documentation-like. The AWS source benchmarks retrieval infrastructure but does not publish answer-quality or recall measurements for generated responses. The latency argument is an assertion about user tolerance rather than a measured threshold, and it compares retrieval against agency in general rather than against a fast, bounded agent loop.

## What Changed
- Created the initial concept page for retrieval-augmented generation.
- Added coding-agent fit boundaries around freshness, code semantics, and agentic retrieval.
- Added PostgreSQL/pgvector indexing as a database-layer constraint for enterprise RAG.
- Added latency as a stated reason non-agentic RAG remains a live option.

## Related Concepts
- [[PrivateDataChatbot]] - private-data chatbots use RAG to answer from uploaded data.
- [[Embeddings]] - embeddings make semantic retrieval possible.
- [[VectorDatabase]] - vector databases provide the retrieval store for embedded chunks.
- [[AIApplicationFramework]] - frameworks such as LangChain package RAG implementation steps.
- [[NaturalLanguageInterface]] - RAG lets natural-language questions operate over external data.
- [[AgenticRAG]] - agentic RAG retrieves current task context through search/read loops.
- [[Pgvector]] - pgvector can provide the PostgreSQL vector retrieval layer for RAG.
- [[ApproximateNearestNeighborSearch]] - ANN can reduce retrieval latency when exact search is too slow.
- [[AgentDeploymentTradeoffs]] - response-time expectations help decide between retrieval and agency.
