---
title: "Frank Liang"
type: entity
tags: [computer-science, typography, algorithms]
sources:
  - lian-zi-fu-duan-ci-cong-yuan-li-dao-shi-jian
last_updated: 2026-10-11
knowledge_schema: synthesis-v1
---

## Overview
[[FrankLiang]] is the computer scientist represented in this wiki through his design of a dictionary-derived weighted-pattern algorithm and packed-trie storage for automatic word hyphenation in [[TeX]].

## Current Profile
The source identifies Liang as [[DonaldKnuth]]'s student and dates his participation in TeX development to 1977, with the new algorithm designed around 1978 and later incorporated into TeX82. His dissertation, *Word Hy-phen-a-tion by Com-put-er*, is cited as the fuller account of the pattern-generation and packed-trie design.

Liang's contribution is framed as a move away from brittle, language-expert-authored rules and literal whole-dictionary storage. It learns reusable weighted substrings from a hyphenated dictionary, resolves their overlapping evidence at runtime, and stores them compactly. The article also says he later worked on page layout and printing for Microsoft Word in 1982, but provides no primary biographical documentation.

## Key Characteristics
- Participated in TeX development as Donald Knuth's student.
- Designed the weighted hyphenation-pattern method used in TeX82.
- Associated pattern lookup with a packed-trie representation intended to reduce storage waste.
- Documented the work in *Word Hy-phen-a-tion by Com-put-er*.
- Is linked by the source to later Microsoft Word page-layout and printing work.

## Evidence
- Project role: [[lian-zi-fu-duan-ci-cong-yuan-li-dao-shi-jian]] places Liang in TeX development beginning in 1977 and credits him with the replacement hyphenator.
- Technical contribution: [[lian-zi-fu-duan-ci-cong-yuan-li-dao-shi-jian]] explains the dictionary-to-pattern pipeline, weighted matching, and packed-trie rationale attributed to Liang.
- Publication context: [[lian-zi-fu-duan-ci-cong-yuan-li-dao-shi-jian]] cites Liang's dissertation for the detailed data-structure and algorithm account.
- Later work: [[lian-zi-fu-duan-ci-cong-yuan-li-dao-shi-jian]] states that Liang joined Microsoft Word development in 1982 for layout and printing work.

## Qualifications
This profile is derived from one secondary technical article rather than Liang's dissertation, archival TeX materials, or a verified biography. Dates, authorship boundaries, the exact packed-trie representation, and the Microsoft Word role are not independently corroborated in the supplied evidence. The source's simplified statement that packed tries save space by merging identical prefixes does not distinguish the structure adequately from an ordinary trie.

## What Changed
- Created the profile around Liang's source-attributed role in automatic hyphenation and compact pattern lookup.

## Relationships
- [[DonaldKnuth]] - supervised Liang and created the TeX context for his work.
- [[TeX]] - incorporated Liang's hyphenation algorithm in TeX82.
- [[LiangHyphenationAlgorithm]] - is the principal technical contribution attributed to Liang.
- [[Hyphenation]] - is the typography problem his algorithm addresses.
