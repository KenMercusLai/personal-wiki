---
title: "TeX"
type: entity
tags: [typesetting, typography, software]
sources:
  - lian-zi-fu-duan-ci-cong-yuan-li-dao-shi-jian
last_updated: 2026-10-11
knowledge_schema: synthesis-v1
---

## Overview
[[TeX]] is [[DonaldKnuth]]'s digital typesetting system and the implementation context in which [[FrankLiang]] developed the weighted-pattern approach to automatic [[Hyphenation]].

## Current Profile
The source presents TeX through one subsystem rather than as a complete typesetting platform. Its early 1977 hyphenator combined prefix and suffix removal, a vowel-consonant-consonant-vowel rule, special rules, and an exception dictionary of roughly 300 words. The article reports that this approach covered only 40% of permissible breakpoints in a small test dictionary at a 1% error rate and was hard to extend to other languages.

Liang's later dictionary-derived patterns and packed trie replaced that rule-heavy approach in TeX82 and became influential beyond TeX. In this profile, TeX therefore acts both as the production constraint that made automatic breakpoint selection important and as the host through which a reusable algorithm spread.

## Key Characteristics
- Was created by Donald Knuth in response to dissatisfaction with the typesetting of his books.
- Uses automatic hyphenation as part of paragraph composition, particularly for justified text.
- Initially relied on hand-designed linguistic rules and a small exception dictionary.
- Adopted Liang's weighted-pattern and packed-trie approach in TeX82.
- Serves as the historical software context for the source's algorithmic account rather than as a complete TeX profile.

## Evidence
- Origin context: [[lian-zi-fu-duan-ci-cong-yuan-li-dao-shi-jian]] links Knuth's work on *The Art of Computer Programming* to the creation of TeX and its uptake in academic publishing.
- Early algorithm: [[lian-zi-fu-duan-ci-cong-yuan-li-dao-shi-jian]] enumerates prefix, suffix, VCCV, special-case, and exception-dictionary mechanisms and reports their limited coverage.
- Replacement path: [[lian-zi-fu-duan-ci-cong-yuan-li-dao-shi-jian]] says Liang's pattern method replaced the first algorithm in TeX82 and was reused by other publishing and word-processing systems.

## Qualifications
The source is a secondary practitioner explanation focused narrowly on hyphenation. It does not document TeX's paragraph-optimization algorithm, macro system, font metrics, implementation chronology, licensing, or present ecosystem, and it does not independently reproduce the historical coverage and error figures. The account should not be treated as a complete history of TeX or proof that its hyphenator alone determines paragraph quality.

## What Changed
- Created a source-bounded TeX profile centered on the transition from manual rules to Liang's reusable patterns.

## Relationships
- [[DonaldKnuth]] - created TeX and designed its original hyphenation approach with collaborators.
- [[FrankLiang]] - developed the pattern algorithm later incorporated into TeX82.
- [[Hyphenation]] - is the paragraph-layout function examined by the source.
- [[LiangHyphenationAlgorithm]] - replaced TeX's earlier rule-heavy breakpoint selection.
