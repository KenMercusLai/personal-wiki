---
title: "Computational Pun Translation"
type: concept
tags: [translation, localization, nlp]
sources:
  - wei-jie-ru-he-yong-bao-li-ji-suan-fan-yi-xie-yin-geng-nv-xing-jiao-liu-fan-yi-bi-ji
last_updated: 2026-09-11
knowledge_schema: synthesis-v1
---

## Definition
[[ComputationalPunTranslation]] is a machine-assisted translation approach that searches large target-language corpora for meaning-adjacent text containing required pun or homophone features.

## Current Synthesis
The source frames pun translation as a search problem when a work contains too many jokes for pure inspiration to scale. Instead of asking the translator to invent every target-language pun from scratch, the workflow filters real sentences for homophones of target taboo terms, embeds those candidate sentences, retrieves semantically similar options for each source line, and leaves final composition to a human translator or model. In this case, computation expands the candidate space while human judgment preserves tone, context, and playability.

## Key Claims
- Pun translation can be inverted from free invention into corpus search over target-language material.
- Homophone filtering supplies candidates that satisfy a formal joke constraint before semantic ranking begins.
- [[SemanticSearch]] helps find candidate lines whose meaning is close enough to the source line to be useful.
- The workflow resembles [[RetrievalAugmentedGeneration]] because retrieved material is supplied as context for final generation or translation.
- Machine assistance is most valuable for scale and candidate discovery, while final quality still depends on human revision.

## Evidence
- Search inversion: [[wei-jie-ru-he-yong-bao-li-ji-suan-fan-yi-xie-yin-geng-nv-xing-jiao-liu-fan-yi-bi-ji]] argues that if humans struggle to write such sentences from scratch, machines can search existing text for suitable near matches.
- Formal constraint: [[wei-jie-ru-he-yong-bao-li-ji-suan-fan-yi-xie-yin-geng-nv-xing-jiao-liu-fan-yi-bi-ji]] filters a large dialogue corpus for sentences containing homophones of listed sensitive words.
- Semantic matching: [[wei-jie-ru-he-yong-bao-li-ji-suan-fan-yi-xie-yin-geng-nv-xing-jiao-liu-fan-yi-bi-ji]] vectorizes source lines and candidate sentences to retrieve semantically related options.
- RAG analogy: [[wei-jie-ru-he-yong-bao-li-ji-suan-fan-yi-xie-yin-geng-nv-xing-jiao-liu-fan-yi-bi-ji]] explicitly says the workflow is somewhat like RAG.
- Human revision: [[wei-jie-ru-he-yong-bao-li-ji-suan-fan-yi-xie-yin-geng-nv-xing-jiao-liu-fan-yi-bi-ji]] notes that many jokes still require repeated human deliberation.

## Counterevidence & Qualifications
The method depends on corpus size, corpus fit, homophone matching quality, embedding quality, and translator taste. The source provides persuasive examples but not a controlled comparison against conventional translation or a quantitative evaluation of retrieval quality.

## What Changed
- Created the initial concept page for computational pun translation from Wei Jie's game-localization case study.

## Related Concepts
- [[SemanticSearch]] - semantic search ranks homophone-bearing candidates by meaning similarity.
- [[Embeddings]] - embeddings make source lines and candidate sentences comparable.
- [[VectorDatabase]] - vector databases store the candidate sentence set for retrieval.
- [[RetrievalAugmentedGeneration]] - the workflow resembles RAG in its retrieval-plus-generation structure.
- [[TranslationDomestication]] - pun translation may require target-culture adaptation beyond sentence-level matching.
- [[GameLocalization]] - pun translation is one problem inside broader game localization.
