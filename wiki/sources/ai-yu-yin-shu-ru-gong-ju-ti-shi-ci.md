---
title: "AI 语音输入工具提示词"
type: source
tags: [ai, voice-input, prompt, writing]
date: 2026-09-13
source_file: /mnt/ken_personal_wiki/Articles/AI 语音输入工具提示词.md
---

## Summary
This note shares a complete Chinese prompt for AI voice-input tools that allow custom post-processing instructions, especially [[Spokenly]] and [[VoiceInk]]. The author frames [[AIVoiceInput]] as a competitive tool category, compares domestic tools such as 闪电说、妙言, and 智普的小凹 at a surface level, and says their current working stack combines [[Spokenly]], [[Typeless]], [[Soniox]], and [[Grok4]]. The prompt itself defines a strict transcript-cleanup role: add punctuation, remove filler and false starts, lightly improve flow, structure only when the original calls for it, and never add information.

## Key Claims
- [[AIVoiceInput]] quality depends not only on speech recognition but also on disciplined AI post-processing that preserves meaning while making spoken text readable.
- A good transcript-cleanup prompt should explicitly handle punctuation, filler words, repetition, stutters, and self-corrections without inventing facts.
- Structural formatting should be "necessary and restrained": use bullets or numbered steps only when the original speech naturally contains lists, tasks, decisions, comparisons, or ordered processes.
- The author's practical stack separates roles: [[Spokenly]] is used as a local custom fallback, [[Typeless]] is valued for strong performance, [[Soniox]] supplies transcription, and [[Grok4]] supplies AI cleanup.
- The author reports that [[Soniox]] transcription felt better than the 11lab model in their current use, while domestic tools had not yet been deeply evaluated.

## Key Quotes
> "不新增任何信息" - on the core fidelity rule for transcript cleanup.

> "必要且克制" - on when to structure spoken text into lists or steps.

> "只输出清理后的正文文本" - on output format discipline.

## Connections
- [[AIVoiceInput]] - central tool category and workflow discussed by the note.
- [[AIWorkflowDesign]] - the prompt turns voice cleanup into a bounded, rule-based AI task.
- [[AIAssistedWriting]] - voice input becomes a writing workflow when speech is converted into clean prose.
- [[Spokenly]] - author's local customizable fallback tool.
- [[Typeless]] - author's high-performance voice-input tool focus.
- [[VoiceInk]] - example of a tool that can use custom AI prompts.
- [[Soniox]] - transcription model used in the author's Spokenly setup.
- [[Grok4]] - AI model used for post-processing in the author's Spokenly setup.
- [[Xiaohongshu]] - platform where the author's earlier AI voice-input article gained over 10,000 reads and prompted tool makers to request trials.

## Contradictions
- No direct contradictions with existing wiki content. The source complements existing AI workflow and writing pages by moving the same human-controlled workflow principle into real-time spoken-text cleanup.
