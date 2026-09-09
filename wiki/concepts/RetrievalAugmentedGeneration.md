---
title: "Retrieval-Augmented Generation"
type: concept
tags: [generative-ai, retrieval, embeddings]
sources:
  - ling-ji-chu-da-jian-ji-yu-si-yu-shu-ju-de-chatgpt
last_updated: 2026-09-09
knowledge_schema: synthesis-v1
---

## Definition

Retrieval-augmented generation (RAG) is a pattern in which a system retrieves relevant material from an external corpus and supplies it as context to a generative model when answering a question.

## Current Synthesis

The current source presents RAG as a practical separation between a model's language capability and a user's private or newer knowledge. Documents are split into chunks, embedded, stored in a vector index, retrieved by similarity to an embedded question, and combined with the question and conversation history for generation. [[LLMApplicationFrameworks]] can package these stages, but retrieval quality and answer grounding are not established merely by connecting the components.

## Key Claims

- Chunking determines the units available for retrieval and trades missing context against irrelevant context.
- Embedding both chunks and questions enables similarity-based retrieval from a vector store.
- Retrieved passages, the current question, and conversation history can jointly form the model context.
- External retrieval can extend answers beyond a model's static training knowledge without retraining it.

## Evidence

### Index construction

- [[ling-ji-chu-da-jian-ji-yu-si-yu-shu-ju-de-chatgpt]] describes splitting text with a configurable chunk size, embedding each chunk, and storing vectors in FAISS.

### Retrieval and answer generation

- [[ling-ji-chu-da-jian-ji-yu-si-yu-shu-ju-de-chatgpt]] embeds the user's question, retrieves similar chunks, and passes those chunks with dialogue history to the model; its demonstration reports answers about facts newer than the unaugmented chat product could provide.

## Counterevidence & Qualifications

- The source is a tutorial and visual demonstration, not a controlled evaluation of retrieval accuracy or answer faithfulness.
- Similarity does not guarantee relevance, and retrieved context does not guarantee that the answer will remain grounded in it.
- The example uses a small text corpus and does not examine permissions, deletion, prompt injection, sensitive-data exposure, or production-scale indexing.
- Product knowledge cutoffs and supported file formats change over time; the article's specific claims are historical.

## What Changed

- Added the wiki's first end-to-end account of private-data retrieval for generation.
- Established chunk size and contextual assembly as central design choices.
- Preserved the gap between a working demo and validated production behavior.

## Related Concepts

- [[LLMApplicationFrameworks]] - can orchestrate document loading, retrieval, memory, and generation stages.
