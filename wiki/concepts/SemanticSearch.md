---
title: "Semantic Search"
type: concept
tags: [ai, retrieval, nlp]
sources:
  - wei-jie-ru-he-yong-bao-li-ji-suan-fan-yi-xie-yin-geng-nv-xing-jiao-liu-fan-yi-bi-ji
last_updated: 2026-09-11
knowledge_schema: synthesis-v1
---

## Definition
[[SemanticSearch]] retrieves text by similarity of meaning rather than exact keyword overlap, commonly by comparing embedding vectors.

## Current Synthesis
The source introduces semantic search through a practical translation workflow. Candidate sentences and source lines are represented as vectors, similarity scores identify meaning-adjacent options, and the retrieved candidates help a translator solve constrained homophone-pun problems. In this framing, semantic search is not only an information-retrieval tool but also a creativity aid that expands the translator's search space.

## Key Claims
- Semantic search can retrieve relevant text even when exact keywords do not match.
- Vector similarity provides a workable signal for "roughly similar meaning" in translation support.
- In pun translation, semantic search is useful only after candidates satisfy the required homophone constraint.
- Retrieved semantic neighbors can become prompts or raw material for human or model-assisted translation.
- Creative use cases need human filtering because semantic closeness alone does not guarantee tone, joke quality, or contextual fit.

## Evidence
- Keyword contrast: [[wei-jie-ru-he-yong-bao-li-ji-suan-fan-yi-xie-yin-geng-nv-xing-jiao-liu-fan-yi-bi-ji]] contrasts keyword search with vector-based semantic search using fruit examples.
- Translation signal: [[wei-jie-ru-he-yong-bao-li-ji-suan-fan-yi-xie-yin-geng-nv-xing-jiao-liu-fan-yi-bi-ji]] uses semantic similarity to find Chinese candidate lines close to Japanese source dialogue.
- Constraint-first workflow: [[wei-jie-ru-he-yong-bao-li-ji-suan-fan-yi-xie-yin-geng-nv-xing-jiao-liu-fan-yi-bi-ji]] first filters for homophone-bearing sentences, then stores their vectors for retrieval.
- Candidate handoff: [[wei-jie-ru-he-yong-bao-li-ji-suan-fan-yi-xie-yin-geng-nv-xing-jiao-liu-fan-yi-bi-ji]] gives retrieved sentences and source text to a human translator or large model.
- Quality boundary: [[wei-jie-ru-he-yong-bao-li-ji-suan-fan-yi-xie-yin-geng-nv-xing-jiao-liu-fan-yi-bi-ji]] says machine assistance does not remove the need for human polishing.

## Counterevidence & Qualifications
The source treats vector similarity as operationally useful but does not evaluate embedding models, multilingual alignment, similarity thresholds, false positives, or retrieval diversity.

## What Changed
- Created the initial concept page for semantic search as used in computational pun translation.

## Related Concepts
- [[Embeddings]] - semantic search depends on vector representations of text.
- [[VectorDatabase]] - vector databases support similarity search over embedded candidates.
- [[ComputationalPunTranslation]] - semantic search supplies meaning-adjacent pun candidates.
- [[RetrievalAugmentedGeneration]] - RAG uses semantic search to retrieve context for generation.
- [[PrivateDataChatbot]] - private-data chatbots use semantic search to find relevant source chunks.
