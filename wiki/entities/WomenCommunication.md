---
title: "女性交流"
type: entity
tags: [game, localization, translation]
sources:
  - wei-jie-ru-he-yong-bao-li-ji-suan-fan-yi-xie-yin-geng-nv-xing-jiao-liu-fan-yi-bi-ji
last_updated: 2026-09-11
knowledge_schema: synthesis-v1
---

## Overview
[[WomenCommunication]] is a Japanese indie game whose Chinese localization is used in the wiki as a case study in pun-heavy game translation.

## Current Profile
The source describes [[WomenCommunication]] as a school-themed game where the player, acting as a discipline committee member, identifies accidental sensitive words in everyday dialogue. Because the game contains hundreds of homophonic jokes and mechanics tied to text recognition, its Chinese localization required both computational candidate search and careful recreation of player-facing cues.

## Key Characteristics
- Built around finding sensitive words hidden in ordinary character dialogue.
- Contains hundreds of homophonic jokes, including one embedded in the Japanese title.
- Its Chinese localization used [[MancoDB]] to retrieve semantically related pun candidates.
- Character names were localized through [[TranslationDomestication]] to preserve pun effects in Chinese.
- Includes an overlap-shot mechanic whose discovery depends on [[PlayerGuidance]] through repeated text cues and mechanics.

## Evidence
- Game premise: [[wei-jie-ru-he-yong-bao-li-ji-suan-fan-yi-xie-yin-geng-nv-xing-jiao-liu-fan-yi-bi-ji]] describes players identifying sensitive words hidden in classmates' casual conversation.
- Pun density: [[wei-jie-ru-he-yong-bao-li-ji-suan-fan-yi-xie-yin-geng-nv-xing-jiao-liu-fan-yi-bi-ji]] says the game contains hundreds of homophonic jokes and that even the title contains one.
- Computational localization: [[wei-jie-ru-he-yong-bao-li-ji-suan-fan-yi-xie-yin-geng-nv-xing-jiao-liu-fan-yi-bi-ji]] explains how retrieved Chinese candidate lines helped preserve meanings or themes across many levels.
- Name strategy: [[wei-jie-ru-he-yong-bao-li-ji-suan-fan-yi-xie-yin-geng-nv-xing-jiao-liu-fan-yi-bi-ji]] details the localization of a Japanese-Western hybrid character name into a Chinese-Western hybrid name.
- Mechanic cueing: [[wei-jie-ru-he-yong-bao-li-ji-suan-fan-yi-xie-yin-geng-nv-xing-jiao-liu-fan-yi-bi-ji]] compares Japanese and Chinese versions of the hidden overlap-shot setup.

## Qualifications
The wiki currently knows the game through one localization note, not through a full review, developer interview, or technical postmortem.

## What Changed
- Created the initial entity profile for Women Communication as the object of the translation case study.

## Relationships
- [[WeiJie]] - Wei Jie describes working on the Chinese localization.
- [[MancoDB]] - the game localization used this workflow to find pun candidates.
- [[ComputationalPunTranslation]] - the game's pun density motivates computational assistance.
- [[TranslationDomestication]] - character names and setting cues were localized through domestication.
- [[PlayerGuidance]] - the game uses dialogue and mechanics to lead players toward discovering hidden rules.
