---
title: "Retrieval-Augmented Generation"
type: concept
tags: [ai, rag, retrieval]
sources:
  - ling-ji-chu-da-jian-ji-yu-si-yu-shu-ju-de-chatgpt
last_updated: 2026-09-11
knowledge_schema: synthesis-v1
---

## Definition
[[RetrievalAugmentedGeneration]] is an LLM application pattern that retrieves relevant external information and supplies it as context to a model so generated answers can be grounded in that information.

## Current Synthesis
The source explains RAG through a private-data chatbot workflow. Documents are imported and chunked, chunks are embedded and stored in a vector database, user questions are embedded for similarity search, and the retrieved passages are sent to the LLM alongside the current question and previous conversation history. In this framing, RAG is the practical bridge between general-purpose language models and user-specific data.

## Key Claims
- RAG starts with document ingestion, parsing, and chunking.
- Embedding both source chunks and user questions enables similarity search.
- A vector database stores document vectors for later retrieval.
- The retrieved chunks become contextual evidence for the LLM answer.
- Conversation history can be included with retrieved passages and the current question.
- Chunk size affects whether the model receives enough relevant context or too much irrelevant material.

## Evidence
- Pipeline overview: [[ling-ji-chu-da-jian-ji-yu-si-yu-shu-ju-de-chatgpt]] lists import/parse/split, embeddings, FAISS storage, question embeddings, similarity search, and LLM answering as the main steps.
- Context assembly: [[ling-ji-chu-da-jian-ji-yu-si-yu-shu-ju-de-chatgpt]] says the current question, previous Q&A, and found passages are passed to the model together.
- Chunking tradeoff: [[ling-ji-chu-da-jian-ji-yu-si-yu-shu-ju-de-chatgpt]] explains that chunk size controls how much reference information the model receives.
- Implementation tools: [[ling-ji-chu-da-jian-ji-yu-si-yu-shu-ju-de-chatgpt]] identifies LangChain splitters, OpenAI embeddings, vector stores, FAISS, and LLMChain as implementation pieces.

## Counterevidence & Qualifications
The source presents the basic pattern but does not cover advanced retrieval quality, reranking, source attribution, evaluation, prompt injection, access control, freshness, or conflict handling across retrieved passages.

## What Changed
- Created the initial concept page for retrieval-augmented generation.

## Related Concepts
- [[PrivateDataChatbot]] - private-data chatbots use RAG to answer from uploaded data.
- [[Embeddings]] - embeddings make semantic retrieval possible.
- [[VectorDatabase]] - vector databases provide the retrieval store for embedded chunks.
- [[AIApplicationFramework]] - frameworks such as LangChain package RAG implementation steps.
- [[NaturalLanguageInterface]] - RAG lets natural-language questions operate over external data.
