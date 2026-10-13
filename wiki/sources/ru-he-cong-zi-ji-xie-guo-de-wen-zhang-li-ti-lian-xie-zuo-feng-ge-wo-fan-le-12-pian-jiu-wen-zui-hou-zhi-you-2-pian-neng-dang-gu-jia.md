---
title: "如何从自己写过的文章里提炼写作风格：我翻了 12 篇旧文，最后只有 2 篇能当骨架"
type: source
tags: [ai, writing, skills, style]
date: 2026-08-06
source_file: "/mnt/ken_personal_wiki/Articles/如何从自己写过的文章里提炼写作风格：我翻了 12 篇旧文，最后只有 2 篇能当骨架.md"
---

## Summary
[[MaiYang]] describes a first attempt at [[WritingStyleDistillation]]: read her own original Markdown, separate structural exemplars from voice samples, encode the result as an [[LLMToolingSkills|LLM Skill]], and improve it through real editing diffs. The article argues that generic prompts and word bans cannot reproduce an authorial voice because structure, evidence habits, concrete openings, uncertainty, and revision behavior matter more than isolated vocabulary. Its strongest boundary is factual rather than stylistic: an assistant must expose missing numbers, owners, commitments, risk levels, and quotations instead of inventing certainty.

## Key Claims
- [[WritingStyleDistillation]] requires verbatim source material because summaries preserve topics while deleting sentence length, punctuation, headings, idioms, formatting, and other style evidence.
- More samples are not automatically better: the author selected two of twelve articles as structural exemplars, used weaker year-end posts only for candid tone, and excluded the rest from the exemplar set.
- A writing Skill should prioritize generative structure over a blacklist. Mai Yang's preferred skeleton begins with a concrete event, admits mistakes, uses checkable numbers, states a first-person judgment, offers an immediate next step, and names uncertainty.
- A blacklist can suppress jargon without creating a recognizable voice; every borrowed prohibition should be checked against the author's strongest passages and narrowed when it rejects authentic usage.
- Style extraction should separate dimensions such as structure and tone because the article with the best organization may not contain the author's most natural self-deprecation or candor.
- For work documents, factual integrity outranks stylistic imitation: unknown data, owners, commitments, risk levels, and quotations must remain visibly unresolved rather than be converted into confident prose.
- The proposed improvement loop is to test the Skill on real work, edit the result manually, compare the draft and revision, and feed the observed changes back into the structure and rules.

## Key Quotes
> “风格恰恰全在这些地方。” — on why summaries cannot replace verbatim writing samples.

> “不知道就写不知道。” — on preserving uncertainty instead of disguising it as an action item.

> “一条规则如果和你写得最好的那句话冲突，改规则，别改句子。” — on validating borrowed style rules against the author's own strongest evidence.

## Connections
- [[MaiYang]] - author and subject of the first-person writing-style experiment.
- [[WritingStyleDistillation]] - central method of selecting, decomposing, encoding, and revising an author-specific style guide.
- [[LLMToolingSkills]] - the style guide is packaged as `SKILL.md`, a blacklist reference, and verbatim voice samples.
- [[AIAssistedWriting]] - the article narrows AI's role through evidence-grounded style guidance, manual revision, and factual accountability.
- [[SemanticAblation]] - summary-only corpora and generic rewriting can remove the small structural and lexical choices that carry voice.
- [[PersonaDistillation]] - both compress behavioral traces, but this source targets a bounded writing workflow rather than simulation of a whole person.
- [[PromptEngineering]] - generic requests such as “write conversationally” are treated as transient and underspecified compared with a maintained workflow artifact.

## Contradictions
- The source directly qualifies the idea that a larger corpus necessarily yields a better style model: averaging weak and strong pieces can encode habits the author wants to remove.
- It also qualifies blacklist-first attempts to remove “AI flavor”: avoiding jargon can reduce obvious symptoms while leaving the model's framework-first structure unlike the author.
- The evidence is one author's first extraction pass across twelve selected posts, only eight of which were available verbatim. The resulting Skill has not yet completed the proposed edit-and-diff feedback loop, and the article reports no blind style ratings, comparison prompts, task outcomes, or evidence that the method generalizes across writers and document genres.
- The article names an intended public repository path but says the exact path is still pending, so the three claimed Skill files are described rather than supplied for independent inspection in this source.
- The supplied Markdown contains no effective image references, so no visual assets or manifest were required.
