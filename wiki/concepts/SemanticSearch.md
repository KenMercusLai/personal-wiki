---
title: "Semantic Search"
type: concept
tags: [ai, retrieval, nlp]
sources:
  - wei-jie-ru-he-yong-bao-li-ji-suan-fan-yi-xie-yin-geng-nv-xing-jiao-liu-fan-yi-bi-ji
  - jay-kim-building-an-ai-agent-to-parse-resumes-and-job-descriptions-and-recommend-the-best-candidates
last_updated: 2026-10-01
knowledge_schema: synthesis-v1
---

## Definition
[[SemanticSearch]] retrieves text by similarity of meaning rather than exact keyword overlap, commonly by comparing embedding vectors.

## Current Synthesis
The sources apply semantic search to two materially different ranking tasks. In translation, candidate sentences and source lines are represented as vectors, similarity identifies meaning-adjacent options, and a human filters those options through homophone, tone, and joke-quality constraints. In hiring, complete resumes and a job description are embedded with the same model, then cosine similarity supplies a ranked candidate list.

Together they show that semantic similarity is a candidate-generation or ordering signal, not a complete decision rule. The translation workflow explicitly retains human judgment and hard constraints; the hiring tutorial does not validate whether its score preserves qualifications, predicts performance, or avoids unfair effects. The higher the consequence of the ranking, the more important it is to test what semantic closeness omits.

## Key Claims
- Semantic search can retrieve relevant text even when exact keywords do not match.
- Vector similarity provides a workable signal for "roughly similar meaning" in translation support.
- In pun translation, semantic search is useful only after candidates satisfy the required homophone constraint.
- Retrieved semantic neighbors can become prompts or raw material for human or model-assisted translation.
- Creative use cases need human filtering because semantic closeness alone does not guarantee tone, joke quality, or contextual fit.
- The same vector-ranking pattern can order resumes against a job description, but a cosine score does not by itself establish candidate suitability.

## Evidence
- Keyword contrast: [[wei-jie-ru-he-yong-bao-li-ji-suan-fan-yi-xie-yin-geng-nv-xing-jiao-liu-fan-yi-bi-ji]] contrasts keyword search with vector-based semantic search using fruit examples.
- Translation signal: [[wei-jie-ru-he-yong-bao-li-ji-suan-fan-yi-xie-yin-geng-nv-xing-jiao-liu-fan-yi-bi-ji]] uses semantic similarity to find Chinese candidate lines close to Japanese source dialogue.
- Constraint-first workflow: [[wei-jie-ru-he-yong-bao-li-ji-suan-fan-yi-xie-yin-geng-nv-xing-jiao-liu-fan-yi-bi-ji]] first filters for homophone-bearing sentences, then stores their vectors for retrieval.
- Candidate handoff: [[wei-jie-ru-he-yong-bao-li-ji-suan-fan-yi-xie-yin-geng-nv-xing-jiao-liu-fan-yi-bi-ji]] gives retrieved sentences and source text to a human translator or large model.
- Quality boundary: [[wei-jie-ru-he-yong-bao-li-ji-suan-fan-yi-xie-yin-geng-nv-xing-jiao-liu-fan-yi-bi-ji]] says machine assistance does not remove the need for human polishing.
- Hiring application: [[jay-kim-building-an-ai-agent-to-parse-resumes-and-job-descriptions-and-recommend-the-best-candidates]] embeds each complete resume and the job description with `all-MiniLM-L6-v2`, computes cosine similarity, and sorts the resulting scores.

## Counterevidence & Qualifications
Neither source evaluates embedding models, similarity thresholds, false positives, ranking stability, or retrieval diversity. The translation case is a practitioner account without quality benchmarks. The hiring tutorial is especially limited because it supplies no labeled relevance judgments, field weighting, explanation fidelity, bias or adverse-impact analysis, privacy design, accommodation process, human-review procedure, or evidence that semantic similarity predicts job performance; its ranking is a technical demonstration, not a validated selection system.

## What Changed
- Created the initial concept page for semantic search as used in computational pun translation.
- Extended the concept to candidate ranking and made the decision-risk boundary explicit: meaning similarity is not equivalent to hiring suitability.

## Related Concepts
- [[Embeddings]] - semantic search depends on vector representations of text.
- [[VectorDatabase]] - vector databases support similarity search over embedded candidates.
- [[ComputationalPunTranslation]] - semantic search supplies meaning-adjacent pun candidates.
- [[RetrievalAugmentedGeneration]] - RAG uses semantic search to retrieve context for generation.
- [[PrivateDataChatbot]] - private-data chatbots use semantic search to find relevant source chunks.
