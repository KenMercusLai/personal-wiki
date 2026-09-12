---
title: "Retrieval-Augmented Generation"
type: concept
tags: [ai, rag, retrieval]
sources:
  - ling-ji-chu-da-jian-ji-yu-si-yu-shu-ju-de-chatgpt
  - mu-jiang-chui-zi-ding-zi
last_updated: 2026-09-12
knowledge_schema: synthesis-v1
---

## Definition
[[RetrievalAugmentedGeneration]] is an LLM application pattern that retrieves relevant external information and supplies it as context to a model so generated answers can be grounded in that information.

## Current Synthesis
The first source explains RAG through a private-data chatbot workflow. Documents are imported and chunked, chunks are embedded and stored in a vector database, user questions are embedded for similarity search, and the retrieved passages are sent to the LLM alongside the current question and previous conversation history. In this framing, RAG is the practical bridge between general-purpose language models and user-specific data.

PsiACE's coding-agent source adds a sharper fit boundary. RAG is less reliable when the target corpus is a frequently changing codebase: static indexes grow stale, chunking and indexing can interrupt development flow, and generic embeddings may not bridge natural language and code semantics. In those situations, [[AgenticRAG]] can retrieve current code context through grep, reading, and iterative agent-loop exploration.

## Key Claims
- RAG starts with document ingestion, parsing, chunking, and embedding source chunks plus user questions for similarity search.
- A vector database stores document vectors for later retrieval.
- The retrieved chunks become contextual evidence for the LLM answer.
- Conversation history can be included with retrieved passages and the current question.
- Chunk size, corpus stability, update frequency, retrieval timing, and semantic representation quality affect whether the model receives enough relevant context, too much irrelevant material, or stale material.
- Live codebases may be better served by [[AgenticRAG]] than by static vector indexes.

## Evidence
- Pipeline overview: [[ling-ji-chu-da-jian-ji-yu-si-yu-shu-ju-de-chatgpt]] lists import/parse/split, embeddings, FAISS storage, question embeddings, similarity search, and LLM answering as the main steps.
- Context assembly: [[ling-ji-chu-da-jian-ji-yu-si-yu-shu-ju-de-chatgpt]] says the current question, previous Q&A, and found passages are passed to the model together.
- Chunking tradeoff: [[ling-ji-chu-da-jian-ji-yu-si-yu-shu-ju-de-chatgpt]] explains that chunk size controls how much reference information the model receives.
- Implementation tools: [[ling-ji-chu-da-jian-ji-yu-si-yu-shu-ju-de-chatgpt]] identifies LangChain splitters, OpenAI embeddings, vector stores, FAISS, and LLMChain as implementation pieces.
- Codebase limits: [[mu-jiang-chui-zi-ding-zi]] says frequently changing codebases create indexing cost and freshness problems for naive RAG.
- Semantic limits: [[mu-jiang-chui-zi-ding-zi]] says common embeddings can struggle to represent code from natural-language queries.
- Agentic alternative: [[mu-jiang-chui-zi-ding-zi]] says grep plus reading plus an agent loop can be more intuitive and effective for coding agents.

## Counterevidence & Qualifications
The private-data chatbot source presents the basic pattern but does not cover advanced retrieval quality, reranking, source attribution, evaluation, prompt injection, access control, freshness, or conflict handling across retrieved passages. The coding-agent source is a practitioner critique rather than a benchmark and explicitly preserves a role for naive RAG when code and comments are stable, semantically rich, versioned, or documentation-like.

## What Changed
- Created the initial concept page for retrieval-augmented generation.
- Added coding-agent fit boundaries around freshness, code semantics, and agentic retrieval.

## Related Concepts
- [[PrivateDataChatbot]] - private-data chatbots use RAG to answer from uploaded data.
- [[Embeddings]] - embeddings make semantic retrieval possible.
- [[VectorDatabase]] - vector databases provide the retrieval store for embedded chunks.
- [[AIApplicationFramework]] - frameworks such as LangChain package RAG implementation steps.
- [[NaturalLanguageInterface]] - RAG lets natural-language questions operate over external data.
- [[AgenticRAG]] - agentic RAG retrieves current task context through search/read loops.
