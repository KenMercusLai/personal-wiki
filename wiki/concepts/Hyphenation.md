---
title: "Hyphenation"
type: concept
tags: [typography, line-breaking, css, language]
sources:
  - lian-zi-fu-duan-ci-cong-yuan-li-dao-shi-jian
last_updated: 2026-10-11
knowledge_schema: synthesis-v1
---

## Definition
[[Hyphenation]] is controlled, language-sensitive splitting of a word at a line boundary, usually with a visible hyphen, to improve paragraph layout without changing the underlying text.

## Current Synthesis
Hyphenation trades one visual cost for another. By adding legal break opportunities inside long words, it reduces large gaps in ragged-right text and excessive word-space expansion under justification, especially in narrow columns. Too much splitting, poorly placed fragments, or several consecutive hyphenated lines can reduce readability, so useful systems combine language-specific break knowledge with layout policy.

On the Web, the source presents language and region metadata as a prerequisite for selecting appropriate break patterns and `hyphens: auto` as the activation control. Minimum fragment length, consecutive-line limits, last-line policy, and a right-edge exclusion zone can then tune the balance between line fit and visible hyphens. The inserted hyphen remains a rendering decision rather than stored document content.

## Key Claims
- Hyphenation adds internal word-break opportunities that can reduce ragged edges and stretched word spaces.
- Correct break positions depend on language, spelling, morphology, pronunciation, and sometimes regional variation.
- A layout engine must balance compact line fitting against word recognition, fragment length, and repeated visible hyphens.
- Web hyphenation should preserve underlying text so selection, copying, and search operate on the unsplit word.
- Narrow columns increase the practical value of legal word-internal breaks.

## Evidence
- Layout effect: [[lian-zi-fu-duan-ci-cong-yuan-li-dao-shi-jian]] retains before-and-after paragraph images showing fewer large right-edge gaps after automatic splitting.
- Policy controls: [[lian-zi-fu-duan-ci-cong-yuan-li-dao-shi-jian]] describes language tags, `hyphens: auto`, fragment limits, consecutive-line limits, final-line handling, and a zone that trades fewer hyphens for more raggedness.
- Content boundary: [[lian-zi-fu-duan-ci-cong-yuan-li-dao-shi-jian]] quotes the CSS specification's rendering-only model and explains that search and selection should not see an inserted hyphen as stored text.
- Algorithmic grounding: [[lian-zi-fu-duan-ci-cong-yuan-li-dao-shi-jian]] contrasts manual rules, full dictionaries, and reusable weighted patterns for identifying language-specific breakpoints.

## Counterevidence & Qualifications
The source is a practitioner explainer, not a comparative readability study or browser interoperability report. Its illustrations establish a visible layout difference but do not measure reading speed, comprehension, accessibility, or user preference. Browser support and exact CSS property behavior are time-sensitive, and the suggested `8%` zone is a rule of thumb rather than a universal optimum. Languages and writing systems differ substantially: the article's contrast between Chinese character-level breaking and Western word spacing is useful but simplified by punctuation, grapheme, shaping, and script-specific line-breaking rules.

## What Changed
- Created the concept around hyphenation as a language-sensitive rendering policy rather than a mutation of text.
- Made the central optimization tradeoff explicit: smoother line fit versus the frequency and readability cost of visible splits.
- Added browser controls and narrow-column layout as practical operating contexts.

## Related Concepts
- [[LiangHyphenationAlgorithm]] - supplies language-derived candidate breakpoints through weighted substring patterns.
- [[NaturalLanguageProcessing]] - provides the broader computational setting for language-specific word analysis.
- [[DeepLearning]] - is an alternative learned approach mentioned for automatic breakpoint prediction.
