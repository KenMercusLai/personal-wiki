---
title: "MancoDB"
type: entity
tags: [semantic-search, translation, vector-database]
sources:
  - wei-jie-ru-he-yong-bao-li-ji-suan-fan-yi-xie-yin-geng-nu-xing-jiao-liu-fan-yi-bi-ji
last_updated: 2026-09-09
knowledge_schema: synthesis-v1
---

## Overview

MancoDB is the name [[WeiJie]] gives to the machine-assisted retrieval workflow used for the Chinese localization of [[WomanCommunication]].

## Current Profile

The source describes MancoDB as a corpus pipeline that detects homophones of a themed word list, embeds matching dialogue, and retrieves semantically similar candidates for a source line. It is presented as translator support rather than an autonomous translation product.

## Key Characteristics

- Uses a themed lexicon of roughly four hundred terms in the reported project.
- Applies phonetic matching to a large corpus of real user dialogue.
- Stores embeddings of matched sentences for similarity retrieval.
- Returns candidates to a human translator or language model for final composition.

## Evidence

### Pipeline

- [[wei-jie-ru-he-yong-bao-li-ji-suan-fan-yi-xie-yin-geng-nu-xing-jiao-liu-fan-yi-bi-ji]] outlines the lexicon, corpus filtering, embedding, vector storage, retrieval, and final human-or-model drafting stages.

### Project use

- [[wei-jie-ru-he-yong-bao-li-ji-suan-fan-yi-xie-yin-geng-nu-xing-jiao-liu-fan-yi-bi-ji]] reports using the workflow to localize a game containing hundreds of puns.

## Qualifications

- The source does not provide code, architecture details, corpus provenance, evaluation metrics, or an independent reproduction.
- It is unclear whether MancoDB denotes packaged software or the project-specific workflow as a whole.
- Reported quality and efficiency gains are not comparative measurements.

## What Changed

- Added a source-bounded profile of the named retrieval workflow.

## Relationships

- [[WeiJie]] - creator and named operator in the source.
- [[WomanCommunication]] - localization project for which the workflow was used.
- [[MachineAssistedPunTranslation]] - general method instantiated by the workflow.
- [[RetrievalAugmentedGeneration]] - architecturally similar retrieve-then-compose pattern with a different purpose.
