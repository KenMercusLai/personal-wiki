---
title: "MancoDB"
type: entity
tags: [project, translation, retrieval]
sources:
  - wei-jie-ru-he-yong-bao-li-ji-suan-fan-yi-xie-yin-geng-nv-xing-jiao-liu-fan-yi-bi-ji
last_updated: 2026-09-11
knowledge_schema: synthesis-v1
---

## Overview
[[MancoDB]] is the name Wei Jie gives to a retrieval workflow for finding Chinese homophone-pun translation candidates.

## Current Profile
MancoDB is presented as a machine-assisted translation aid rather than a public database product. It combines a sensitive-word list, large-scale real dialogue text, homophone filtering, vectorization, and semantic retrieval to help translators locate target-language sentences that are close in meaning to a source line while containing a needed pun-like term.

## Key Characteristics
- Starts from a domain-specific list of taboo or sensitive target terms.
- Searches large real-user dialogue corpora for sentences containing homophones of those terms.
- Uses pinyin matching, described as possible with a DFA automaton, to filter candidate text.
- Stores vectorized candidate sentences in a [[VectorDatabase]] for [[SemanticSearch]].
- Returns semantically similar candidate lines that a human translator or model can adapt into the final localization.

## Evidence
- Term-list setup: [[wei-jie-ru-he-yong-bao-li-ji-suan-fan-yi-xie-yin-geng-nv-xing-jiao-liu-fan-yi-bi-ji]] says the workflow begins with a list of roughly four hundred sensitive words.
- Corpus requirement: [[wei-jie-ru-he-yong-bao-li-ji-suan-fan-yi-xie-yin-geng-nv-xing-jiao-liu-fan-yi-bi-ji]] recommends collecting as many real online dialogue sentences as possible.
- Homophone filtering: [[wei-jie-ru-he-yong-bao-li-ji-suan-fan-yi-xie-yin-geng-nv-xing-jiao-liu-fan-yi-bi-ji]] suggests using pinyin matching and a DFA automaton to find homophone-bearing sentences.
- Retrieval store: [[wei-jie-ru-he-yong-bao-li-ji-suan-fan-yi-xie-yin-geng-nv-xing-jiao-liu-fan-yi-bi-ji]] says selected sentences are vectorized with an NLP model and stored in a vector database.
- Translator loop: [[wei-jie-ru-he-yong-bao-li-ji-suan-fan-yi-xie-yin-geng-nv-xing-jiao-liu-fan-yi-bi-ji]] says retrieved candidates are handed to a human translator or large model with the source text.

## Qualifications
The source explains MancoDB at workflow level. It does not provide code, retrieval metrics, corpus governance details, privacy handling, or systematic quality evaluation.

## What Changed
- Created the initial entity profile for MancoDB as a named localization workflow.

## Relationships
- [[WeiJie]] - Wei Jie names and describes the workflow.
- [[WomenCommunication]] - the workflow was used in the game's Chinese localization.
- [[ComputationalPunTranslation]] - MancoDB operationalizes computational pun translation.
- [[SemanticSearch]] - semantic search ranks candidate sentences by meaning similarity.
- [[VectorDatabase]] - vector storage supports retrieval over filtered candidate sentences.
- [[RetrievalAugmentedGeneration]] - the workflow is explicitly compared to RAG.
