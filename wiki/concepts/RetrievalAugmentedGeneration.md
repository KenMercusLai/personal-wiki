---
title: "Retrieval-Augmented Generation"
type: concept
tags: [generative-ai, retrieval, embeddings]
sources:
  - ling-ji-chu-da-jian-ji-yu-si-yu-shu-ju-de-chatgpt
  - wei-jie-ru-he-yong-bao-li-ji-suan-fan-yi-xie-yin-geng-nu-xing-jiao-liu-fan-yi-bi-ji
last_updated: 2026-09-09
knowledge_schema: synthesis-v1
---

## Definition

Retrieval-augmented generation (RAG) is a pattern in which a system retrieves relevant material from an external corpus and supplies it as context to a generative model when answering a question.

## Current Synthesis

The sources establish a general retrieve-then-compose architecture with two distinct purposes. In knowledge-grounded generation, documents are chunked, embedded, indexed, retrieved against a question, and supplied with dialogue history to a model. In [[MachineAssistedPunTranslation]], phonetic constraints first narrow authentic dialogue, then semantic retrieval supplies creative candidates to a translator or model. The architectural resemblance does not make the latter factual RAG: its success criterion is functional wordplay and contextual fit rather than grounded answers.

## Key Claims

- Chunking determines the units available for retrieval and trades missing context against irrelevant context.
- Embedding both chunks and questions enables similarity-based retrieval from a vector store.
- Retrieved passages, the current question, and conversation history can jointly form the model context.
- External retrieval can extend answers beyond a model's static training knowledge without retraining it.
- Retrieve-then-compose can also support constrained creative work, but that use has different evaluation criteria from knowledge-grounded question answering.

## Evidence

### Index construction

- [[ling-ji-chu-da-jian-ji-yu-si-yu-shu-ju-de-chatgpt]] describes splitting text with a configurable chunk size, embedding each chunk, and storing vectors in FAISS.

### Retrieval and answer generation

- [[ling-ji-chu-da-jian-ji-yu-si-yu-shu-ju-de-chatgpt]] embeds the user's question, retrieves similar chunks, and passes those chunks with dialogue history to the model; its demonstration reports answers about facts newer than the unaugmented chat product could provide.

### Creative retrieval analogue

- [[wei-jie-ru-he-yong-bao-li-ji-suan-fan-yi-xie-yin-geng-nu-xing-jiao-liu-fan-yi-bi-ji]] calls its pun-translation workflow “a bit like RAG”: it retrieves semantically related, phonetically constrained sentences before human or model composition.

## Counterevidence & Qualifications

- The source is a tutorial and visual demonstration, not a controlled evaluation of retrieval accuracy or answer faithfulness.
- Similarity does not guarantee relevance, and retrieved context does not guarantee that the answer will remain grounded in it.
- The example uses a small text corpus and does not examine permissions, deletion, prompt injection, sensitive-data exposure, or production-scale indexing.
- Product knowledge cutoffs and supported file formats change over time; the article's specific claims are historical.
- The pun-translation case is a practitioner report without retrieval benchmarks and should not be treated as evidence of factual grounding.

## What Changed

- Broadened the synthesis to distinguish factual RAG from an analogous creative retrieve-then-compose workflow.
- Added phonetic pre-filtering as an example of domain constraints before semantic retrieval.

## Related Concepts

- [[LLMApplicationFrameworks]] - can orchestrate document loading, retrieval, memory, and generation stages.
- [[MachineAssistedPunTranslation]] - adapts retrieval to creative equivalence rather than factual grounding.
