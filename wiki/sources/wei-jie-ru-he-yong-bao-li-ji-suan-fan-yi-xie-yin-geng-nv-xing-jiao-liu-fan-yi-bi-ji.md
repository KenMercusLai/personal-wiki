---
title: "魏杰 - 如何用暴力计算翻译谐音梗——《女性交流》翻译笔记"
type: source
tags: [translation, localization, game, nlp]
date: 2026-02-05
source_file: /mnt/ken_personal_wiki/Articles/魏杰 - 如何用暴力计算翻译谐音梗——《女性交流》翻译笔记.md
---

## Summary
魏杰 describes how the Chinese localization of the Japanese indie game [[WomenCommunication]] used [[MancoDB]], a machine-assisted workflow for translating large numbers of pun-like sensitive-word jokes. The note combines [[SemanticSearch]], [[Embeddings]], and [[VectorDatabase]] retrieval with human judgment, then explains why [[TranslationDomestication]] and carefully reproduced [[PlayerGuidance]] were needed to preserve the original player's experience.

## Key Claims
- [[ComputationalPunTranslation]] can reduce reliance on spontaneous translator inspiration by searching large real-text corpora for semantically similar sentences that contain homophones of target taboo terms.
- The MancoDB workflow resembles [[RetrievalAugmentedGeneration]]: collect a target term list and large dialogue corpus, filter homophone-bearing sentences, vectorize them, retrieve semantically close candidates, and let a human translator or model compose the final line.
- For pun-dense character names, full [[TranslationDomestication]] may be more coherent than preserving the original setting while inserting target-language puns.
- [[PlayerGuidance]] in text and mechanics can steer players toward discovering an untaught game rule; localization must recreate not only literal wording but also attention, timing, and affordance cues.
- Machine retrieval improves candidate discovery, but the final localization still depends on human taste, compression, and repeated revision.

## Key Quotes
> "用电脑的计算代替人脑的冥思苦想" — the source's framing of machine-assisted pun translation.

> "机器只是辅助" — qualification that retrieval does not replace translator judgment.

> "用中文重现这里的弱引导" — description of recreating the original game-design cueing effect.

## Connections
- [[WeiJie]] — author and Chinese localization programmer discussed in the note.
- [[WomenCommunication]] — game whose Chinese localization provides the case study.
- [[MancoDB]] — project/workflow name for the pun-candidate retrieval database.
- [[ComputationalPunTranslation]] — central method described by the source.
- [[SemanticSearch]] — retrieval mechanism used to find meaning-adjacent pun candidates.
- [[TranslationDomestication]] — strategy used for pun-heavy character names and setting adaptation.
- [[PlayerGuidance]] — concept explaining the source's "weak guidance" analysis.
- [[RetrievalAugmentedGeneration]] — adjacent architecture pattern explicitly compared to the translation workflow.

## Contradictions
- None identified against the existing wiki. The source extends the wiki's retrieval and embedding thread into creative translation and game localization.
