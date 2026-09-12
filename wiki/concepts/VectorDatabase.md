---
title: "Vector Database"
type: concept
tags: [ai, retrieval, database]
sources:
  - ling-ji-chu-da-jian-ji-yu-si-yu-shu-ju-de-chatgpt
last_updated: 2026-09-11
knowledge_schema: synthesis-v1
---

## Definition
[[VectorDatabase]] is a retrieval store for vectorized data that supports similarity search over embedded document chunks or other representations.

## Current Synthesis
The source treats vector databases as the storage and retrieval layer in private-data chatbot architecture. After document chunks are embedded, their vectors are saved into a system such as FAISS or Pinecone so a user's embedded question can retrieve semantically related passages for the LLM.

## Key Claims
- Vector databases store embedded document chunks for later semantic search.
- Similarity retrieval over vectors selects passages likely to answer a user question.
- FAISS is used in the tutorial's Replit sample as the local vector store.
- Pinecone is named as an alternative vector database category example.
- Vector stores are often accessed through higher-level frameworks such as LangChain.

## Evidence
- Storage role: [[ling-ji-chu-da-jian-ji-yu-si-yu-shu-ju-de-chatgpt]] says embedded chunks are saved to FAISS after processing.
- Retrieval role: [[ling-ji-chu-da-jian-ji-yu-si-yu-shu-ju-de-chatgpt]] says an embedded user question is used to find corresponding passages in the FAISS library.
- Category examples: [[ling-ji-chu-da-jian-ji-yu-si-yu-shu-ju-de-chatgpt]] names FAISS and Pinecone as vector-database options.
- Framework integration: [[ling-ji-chu-da-jian-ji-yu-si-yu-shu-ju-de-chatgpt]] identifies LangChain VectorStores as the abstraction used in the sample.

## Counterevidence & Qualifications
The source does not compare vector database performance, persistence, metadata filtering, hybrid search, deployment topology, or security controls.

## What Changed
- Created the initial concept page for vector databases in private-data chatbot architecture.

## Related Concepts
- [[Embeddings]] - vector databases store embeddings generated from source text.
- [[RetrievalAugmentedGeneration]] - vector retrieval supplies external context for generation.
- [[PrivateDataChatbot]] - vector databases let chatbots search uploaded private corpora.
- [[AIApplicationFramework]] - application frameworks often wrap vector-store access.
