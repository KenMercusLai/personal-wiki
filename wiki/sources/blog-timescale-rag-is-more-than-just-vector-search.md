---
title: "RAG Is More Than Just Vector Search"
type: source
tags: [rag, vector-search, postgresql, text-to-sql, evaluations]
date: 2024-09-13
source_file: "/mnt/ken_personal_wiki/Articles/Blog - Timescale - RAG Is More Than Just Vector Search.md"
---

## Summary
Timescale argues that useful [[RetrievalAugmentedGeneration]] systems need more than embedding similarity: questions over GitHub issues may also require time filters, lexical constraints, joins, aggregation, raw records, summaries, and [[TextToSQL]]. Its example enriches issues with LLM-generated summaries and labels, stores source and derived records with embeddings in [[PostgreSQL]], routes questions among typed tools, and uses small tool-selection tests as an early form of [[EvalsDrivenAIDevelopment]]. The implementation illustrates a layered retrieval architecture, but it is a vendor tutorial with unverified benchmark claims and several schema inconsistencies that prevent the code from being treated as a production-ready reference.

## Key Claims
- [[RetrievalAugmentedGeneration]] should compose semantic retrieval with structured filters, time-series operations, joins, aggregations, and task-specific tools instead of treating vector similarity as the whole application.
- Working backward from concrete user questions helps determine which metadata, labels, indexes, and retrieval paths should exist before adding more agentic complexity.
- LLM-based ingestion can turn raw GitHub issues into typed summaries and status labels, while concurrency limits and streaming subsets make experimentation faster and more controllable.
- [[PostgreSQL]], [[Pgvector]], and [[Pgvectorscale]] can colocate vectors with relational and time-series fields so one query layer can combine similarity with structured constraints.
- [[EvalsDrivenAIDevelopment]] can test whether a model selects the expected typed tool before the tool implementation is complete, separating routing behavior from execution behavior.
- [[TextToSQL]] needs detailed schema context, domain-specific functions, field constraints, and explicit anti-hallucination guidance rather than a minimal generic prompt.
- Fuzzy entity matching can repair misspelled repository names, but it adds another thresholded retrieval decision that needs its own validation.

## Key Quotes
> "Embedding search alone won't cut it for a good RAG system." - on the article's central retrieval claim.

> "Think about user needs and work backwards." - on choosing metadata and tools from intended questions.

> "Only resort to SQL queries if the other tools are not able to answer the user's query." - the routing rule used in the example agent.

## Connections
- [[Timescale]] - author and vendor presenting the PostgreSQL-centered architecture.
- [[PostgreSQL]] - shared relational, vector, and time-series query layer in the example.
- [[Pgvector]] - vector storage and distance-search extension used for issue and summary embeddings.
- [[Pgvectorscale]] - Timescale extension used for DiskANN vector indexes in the tutorial.
- [[Pgai]] - related Timescale project promoted for embedding creation and LLM reasoning near PostgreSQL data.
- [[RetrievalAugmentedGeneration]] - broader application pattern expanded beyond vector-only retrieval.
- [[TextToSQL]] - fallback tool for analytical questions that specialized retrieval tools cannot answer.
- [[EvalsDrivenAIDevelopment]] - early tool-routing tests used to shape the application before full implementation.
- [[Embeddings]] - representation used for similarity search over raw issues and generated summaries.
- [[VectorDatabase]] - specialized category the proposed PostgreSQL stack attempts to consolidate with structured data.

## Contradictions
- The article strengthens rather than contradicts the wiki's existing RAG model: vector retrieval remains useful, but becomes one path within a broader retrieval and query system.
- The code creates a `label` column but later tells the text-to-SQL model to use `issue_label`; it also references the `issue_label` type without showing its creation. These inconsistencies undercut the claim that the snippets form a directly runnable end-to-end implementation.
- The source reports large latency, throughput, and cost advantages for pgvectorscale over Pinecone by linking to a separate Timescale benchmark; this article does not reproduce enough methodology to independently support those numbers.
- Tool-selection assertions test routing only. They do not establish SQL correctness, retrieval recall, answer faithfulness, execution safety, or usefulness to real users.
