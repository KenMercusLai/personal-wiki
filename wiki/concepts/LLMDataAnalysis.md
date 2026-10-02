---
title: "LLM Data Analysis"
type: concept
tags: [ai, statistics, data-analysis]
sources:
  - ni-da-gai-bu-hui-xiang-yong-llm-zuo-shu-ju-fen-xi
  - tamer-c-insights-from-over-10000-comments-on-ask-hn-who-is-hiring-using-gpt-4o-langchain
  - truc-phan-proof-of-concept-using-llms-to-extract-key-skills-from-job-descriptions
last_updated: 2026-10-02
knowledge_schema: synthesis-v1
---

## Definition
[[LLMDataAnalysis]] is the use of large language models to write, choose, explain, or execute data-analysis workflows, including statistical inference, extraction, transformation, visualization, clustering, and qualitative coding support.

## Current Synthesis
The evidence separates statistical authority from bounded data transformation. When an LLM chooses or endorses a method the user does not understand, it can generate polished code, tests, charts, tables, and explanations that make invalid inference look rigorous. Prompt framing can also turn a refusal of explicit p-hacking into compliance with substantially similar exploratory parameter search. The analyst therefore remains responsible for the method, code, assumptions, and interpretation.

Two employment-data cases illustrate a narrower pattern: models extract defined attributes from prose, while ordinary code and SQL perform cleaning, storage, aggregation, and visualization. This division makes more of the analytical logic inspectable, but moves risk upstream into scraping coverage, sample selection, schemas, taxonomies, title filters, missing-value rules, and extraction accuracy. A typed record or parseable skill list can still be semantically wrong, and neither case reports a labeled validation set. Deterministic downstream analysis can bound model behavior without validating the data it receives.

## Key Claims
- LLMs make it easy to run statistical methods the user does not understand and can reproduce misconceptions present in their training material.
- Prompt framing can change model behavior from refusing misconduct to performing misconduct-like parameter search.
- Polished outputs increase risk because invalid analysis can look methodologically complete.
- Transformation, organization, visualization, clustering support, coding assistance, and schema-constrained extraction are safer roles when outputs are inspectable.
- Separating probabilistic extraction from deterministic SQL or dashboard aggregation narrows the model's role but does not prove source or record quality.
- Sampling, scraping, filtering, imputation, taxonomy design, and missing-value policy are analytical decisions, not mere preprocessing details.
- Users remain the final methodological and data-quality checkpoint and need labeled evaluation when model-derived records support quantitative claims.

## Evidence
Inferential risk:
- [[ni-da-gai-bu-hui-xiang-yong-llm-zuo-shu-ju-fen-xi]] describes common p-value misconceptions, a p-hacking experiment sensitive to prompt framing, and the author's own initially model-endorsed Cramér's V/bootstrap error.
- [[ni-da-gai-bu-hui-xiang-yong-llm-zuo-shu-ju-fen-xi]] recommends visualization, clustering-assisted affinity maps, and codebook drafting when the analyst reviews the logic.

Bounded extraction and deterministic analysis:
- [[tamer-c-insights-from-over-10000-comments-on-ask-hn-who-is-hiring-using-gpt-4o-langchain]] converts 10,891 Hacker News job posts into typed SQLite records and uses conventional SQL for aggregation.
- [[truc-phan-proof-of-concept-using-llms-to-extract-key-skills-from-job-descriptions]] asks Gemini for data-skill lists, cleans malformed output, and uses Tableau to summarize 553 Glassdoor postings.

Upstream analytical choices:
- [[tamer-c-insights-from-over-10000-comments-on-ask-hn-who-is-hiring-using-gpt-4o-langchain]] reports schema changes for location, categories, delimiters, and booleans and maps unknown remote status to `false`.
- [[truc-phan-proof-of-concept-using-llms-to-extract-key-skills-from-job-descriptions]] applies title keyword filters, three title groups, categorical and mean imputation, and a one-platform 30-day collection window before presenting market percentages and salaries.

Validation gap:
- [[tamer-c-insights-from-over-10000-comments-on-ask-hn-who-is-hiring-using-gpt-4o-langchain]] and [[truc-phan-proof-of-concept-using-llms-to-extract-key-skills-from-job-descriptions]] do not report labeled extraction accuracy; the Glassdoor case's average of 12 keywords per description measures generated quantity rather than correctness.

## Counterevidence & Qualifications
The cautionary source is an essay supported by a cited preprint and personal case rather than a complete benchmark of analytical systems. The two job-market sources are practitioner demonstrations in technical employment data, with specialized or narrow samples and no labeled extraction evaluation. The Glassdoor dashboards add inspectable percentages and category comparisons, but not raw per-skill counts, confidence intervals, missingness rates, scraper coverage, or sensitivity tests; its prose also interprets a generic “Data Analyst” title group as mid-level without visible experience evidence. Together the sources support a risk-controlled operating model, not a universal ranking of safe tasks or proof that deterministic post-processing makes model-derived findings valid.

## What Changed
- Added a second bounded extraction-and-dashboard case using Gemini and Glassdoor postings.
- Added scraping coverage, title classification, imputation, taxonomy consistency, and uncertainty as first-class analytical risks.
- Clarified that output volume and parseability do not measure semantic accuracy.
- Preserved the distinction between inspectable transformation and unexamined statistical authority.

## Related Concepts
- [[PHacking]] - LLM data analysis can automate or disguise favorable-specification search.
- [[CodebookDevelopment]] - codebook drafting and coding assistance are presented as safer analysis-adjacent uses.
- [[LLMContextManagement]] - prompt framing and conversation context shape model analysis behavior.
- [[HumanCodeResponsibility]] - accountability for generated code extends to generated analytical code and method choices.
- [[SoftwareVerification]] - statistical logic and model-derived records need independent verification.
- [[LLMStructuredExtraction]] - creates typed datasets while making schema and taxonomy semantics part of analytical validity.
- [[LargeScaleWebScraping]] - acquisition coverage constrains what downstream analysis can claim about a market.
