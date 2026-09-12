---
title: "LLM Data Analysis"
type: concept
tags: [ai, statistics, data-analysis]
sources:
  - ni-da-gai-bu-hui-xiang-yong-llm-zuo-shu-ju-fen-xi
last_updated: 2026-09-12
knowledge_schema: synthesis-v1
---

## Definition
[[LLMDataAnalysis]] is the use of large language models to write, choose, explain, or execute data-analysis workflows, especially statistical analysis, data transformation, visualization, clustering, and qualitative coding support.

## Current Synthesis
The source frames LLM-assisted analysis as useful but dangerous when the model is treated as a statistical authority. LLMs can quickly generate code, tests, charts, tables, and methodological explanations, which makes weak analysis look professional. The central control is user understanding: the analyst must understand the method, inspect the code, check the statistical logic, and avoid asking the model to rescue a desired result.

## Key Claims
- LLMs make it easier to run statistical methods the user does not understand.
- Statistical misconceptions in published literature and online text can be reproduced by models trained on those corpora.
- Prompt framing can change model behavior from refusing misconduct to performing misconduct-like parameter search.
- Polished outputs increase risk because invalid analysis can look rigorous.
- LLMs are better suited to data transformation, organization, visualization, clustering support, and coding assistance than to unexamined statistical inference.
- The user remains the final methodological checkpoint.

## Evidence
- Misconception inheritance: [[ni-da-gai-bu-hui-xiang-yong-llm-zuo-shu-ju-fen-xi]] cites widespread confusion about nonsignificant p-values and argues that models may internalize those mistakes from training data.
- Prompt framing: [[ni-da-gai-bu-hui-xiang-yong-llm-zuo-shu-ju-fen-xi]] describes a Stanford p-hacking experiment where direct requests were refused but reframed exploratory prompts led models to search many parameter combinations.
- Polished invalidity: [[ni-da-gai-bu-hui-xiang-yong-llm-zuo-shu-ju-fen-xi]] recounts the author's Cramér's V/bootstrap analysis, where multiple models initially endorsed a flawed inference until the author supplied objections.
- Safer workflow: [[ni-da-gai-bu-hui-xiang-yong-llm-zuo-shu-ju-fen-xi]] recommends using LLMs for visualizations, clustering-assisted affinity maps, and codebook drafting when the analyst reviews the logic.

## Counterevidence & Qualifications
The source is a practitioner essay, not a broad benchmark of model statistical reliability. Its strongest empirical support is a cited preprint and personal case study, so its guidance should be treated as a cautionary operating model rather than a complete taxonomy of all safe and unsafe analytical tasks. It also allows that LLMs can be valuable when the user understands the method and verifies outputs.

## What Changed
- Created the concept page for LLM-assisted data analysis as a risk-controlled workflow rather than a blanket prohibition.

## Related Concepts
- [[PHacking]] - LLM data analysis can automate or disguise p-hacking when prompted to find favorable specifications.
- [[CodebookDevelopment]] - codebook drafting and coding assistance are presented as safer analysis-adjacent uses.
- [[LLMContextManagement]] - prompt framing and conversation context shape model analysis behavior.
- [[HumanCodeResponsibility]] - accountability for generated code extends to generated analytical code and method choices.
- [[SoftwareVerification]] - statistical workflows need independent verification of code and logic.
- [[AIKnowledgeAssistant]] - both use LLMs over information, but data analysis adds stricter inferential-risk constraints.
