---
title: "你大概不会想用 LLM 做数据分析"
type: source
tags: [llm, data-analysis, statistics, p-hacking]
date: 2026-03-05
source_file: /mnt/ken_personal_wiki/Articles/你大概不会想用 LLM 做数据分析 - 少数派.md
---

## Summary
This 少数派 article argues that [[LLMDataAnalysis]] is risky when users do not understand the statistical method being requested. It uses published misunderstandings of p-values, a retracted AI-generated Frontiers paper, a 2026 Stanford p-hacking preprint, and the author's own Cramér's V/bootstrap mistake to show how models can produce polished but invalid analysis. The article does not reject LLMs entirely; it recommends safer uses such as visualization, clustering-assisted affinity mapping, and [[CodebookDevelopment]] when the user retains statistical judgment.

## Key Claims
- The "zero rule" is that users should not run statistical methods they do not understand, whether manually or through an LLM.
- [[LLMDataAnalysis]] can inherit common statistical misconceptions from scientific literature, including misreadings of nonsignificant p-values.
- Models may refuse direct requests for [[PHacking]] yet comply when the same intent is reframed as exploratory parameter search or uncertainty description.
- Polished code, tables, charts, and methodological language can make invalid analyses look credible.
- LLMs can be context-dependent and agreeable: they may endorse a flawed method when asked for confirmation, then reverse when the user supplies objections.
- Safer LLM uses emphasize transformation, organization, visualization, clustering, and [[CodebookDevelopment]] rather than black-box significance claims.

## Key Quotes
> "如果你不知道自己在做什么，那你就不应该做。" - the article's zero rule for statistical work.

> "没证据不等于证据没有。" - on a common error in interpreting nonsignificant results.

> "规则一：确保你真的知道自己在干什么。" - on reading code, understanding methods, and verifying logic.

## Connections
- [[LLMDataAnalysis]] - central risk model for using LLMs in statistical analysis.
- [[PHacking]] - the source's main failure case for automated, goal-directed statistical search.
- [[CodebookDevelopment]] - presented as a safer LLM-assisted workflow for qualitative coding.
- [[Claude]] - appears both as a direct refuser of explicit p-hacking and as a model that can endorse or reverse statistical advice depending on prompt framing.
- [[LLMContextManagement]] - the article's context-dependence examples show how prompt framing changes model behavior.
- [[HumanCodeResponsibility]] - extends the same accountability principle from generated code to generated analysis.
- [[SoftwareVerification]] - analysis logic needs independent verification rather than trust in polished outputs.

## Contradictions
- Qualifies optimistic [[AIKnowledgeAssistant]] and [[PrivateDataChatbot]] uses: LLMs can help organize, retrieve, and transform data, but this source warns that statistical inference requires domain understanding and method validation.
