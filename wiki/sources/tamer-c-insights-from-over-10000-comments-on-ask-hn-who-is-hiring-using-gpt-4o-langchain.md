---
title: "Insights from over 10,000 comments on Ask HN: Who Is Hiring using GPT-4o & LangChain"
type: source
tags: [llm, structured-extraction, data-analysis, job-market, hacker-news]
date: 2024-07-03
source_file: "/mnt/ken_personal_wiki/Articles/Tamer C - Insights from over 10,000 comments on Ask HN Who Is Hiring using GPT-4o & LangChain.md"
---

## Summary
[[TamerC]] describes turning 10,891 top-level comments from monthly [[HackerNews]] "Who Is Hiring?" threads into SQL-queryable job records with GPT-4o, Pydantic field definitions, and [[LangChain]] batch processing. The case makes [[LLMStructuredExtraction]] concrete: a model can quickly impose a schema on messy text, but field definitions, allowed categories, delimiters, missing-value policy, model accuracy, sample selection, and cost determine whether the resulting analysis is trustworthy. The reported corpus cost US$54.09 and took about 90 minutes of initial coding and processing, excluding cleanup and visualization.

## Key Claims
- The workflow used Selenium to find monthly thread IDs, the Hacker News API to collect top-level comments, SQLite to store raw and extracted data, GPT-4o plus LangChain to classify postings, and SQL to produce chart inputs.
- Processing 10,891 comments from May 2022 through June 2024 reportedly cost US$54.09; three example months took 43.5–65.1 seconds, 318–433 requests, and US$1.53–US$2.05 each.
- Precise schema language materially affects extraction: city and country should be separate and normalized, categorical fields should enumerate the permitted classes, and set-like values should specify a delimiter.
- A bare boolean instruction was unreliable enough that the author strengthened the prompt, while the rule that unknown remote status becomes `false` introduces a systematic classification risk.
- The source reports that explicitly remote listings remained common after the pandemic and visa sponsorship was comparatively stable, while senior experience, Bay Area and New York locations, PostgreSQL, and React dominated their respective views.
- Once job posts are structured, the same corpus could support a recurring job-matching product that compares user preferences with new monthly listings.

## Key Quotes
> "You have to describe your model fields as precisely as possible." - the author's main schema-design lesson.

> "When categorizing, declare the classes in the description" - on replacing illustrative examples with explicit allowed values.

> "When extracting a set, give the delimiter in the description." - on making multi-value output reliably parseable.

## Connections
- [[TamerC]] - author and practitioner who built the extraction and analysis workflow.
- [[LLMStructuredExtraction]] - central method of converting heterogeneous job-post prose into typed records.
- [[LLMDataAnalysis]] - the extraction feeds conventional SQL analysis while adding model- and schema-quality risks upstream.
- [[LangChain]] - supplies forced structured output and batched model calls in the described implementation.
- [[HackerNews]] - source community and monthly job-post dataset.
- [[PracticalLLMUse]] - bounded automation case where generated records remain inspectable and queryable.
- [[RemoteWork]] - one employment attribute the source attempts to measure over time.

## Contradictions
- The source treats Hacker News as a relatively honest market signal, but [[HackerNews]] documents that the community is specialized and nonrepresentative. Monthly top-level posts can describe one technical submarket, not the overall labor market.
- No labeled validation set, extraction-accuracy metric, retry policy, model/version pin, or uncertainty field is reported. Prompt fixes and the `unknown -> false` remote rule show that schema choices can change the trends later queried with SQL.
- The supplied Markdown contains prose interpretations but not the result charts, axes, counts, or salary distribution. The only effective local image is a decorative New York skyline, which was opened and omitted; therefore the article's visual comparisons could not be independently inspected during ingest.
