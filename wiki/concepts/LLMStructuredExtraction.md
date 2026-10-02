---
title: "LLM Structured Extraction"
type: concept
tags: [llm, information-extraction, data-quality, schemas]
sources:
  - tamer-c-insights-from-over-10000-comments-on-ask-hn-who-is-hiring-using-gpt-4o-langchain
  - truc-phan-proof-of-concept-using-llms-to-extract-key-skills-from-job-descriptions
last_updated: 2026-10-02
knowledge_schema: synthesis-v1
---

## Definition
[[LLMStructuredExtraction]] is the use of a language model, constrained by a declared task and output structure, to transform heterogeneous prose into normalized, machine-queryable records or values.

## Current Synthesis
Two job-posting projects show a repeatable division of labor. A language model converts varied descriptions into structured fields or skill lists; deterministic code then cleans, stores, aggregates, and visualizes the results. This can make thousands of qualitative records queryable quickly: one case parses 10,891 Hacker News comments into typed SQLite rows, while another extracts skill keywords from 553 Glassdoor listings for Tableau analysis.

The useful unit is the full data contract rather than the model call alone. Source selection, scrape coverage, field decomposition, category definitions, delimiters, JSON handling, normalization, title rules, missing-value policy, model version, and retry behavior all shape the downstream dataset. Both projects report operational success but neither uses labeled ground truth, precision or recall, taxonomy-consistency measurement, or sensitivity analysis. Their dashboards therefore demonstrate analyzability, not verified extraction accuracy or representative labor-market measurement.

## Key Claims
- Constrained generation can turn inconsistent prose into records or lists suitable for conventional databases, dashboards, and repeated queries.
- Extraction works best as one bounded transformation inside a deterministic acquisition, cleaning, validation, storage, and analysis pipeline.
- Field descriptions and category taxonomies act as executable data definitions whose ambiguity propagates into every downstream result.
- Decomposed fields, exhaustive categories, explicit multi-value delimiters, and predictable JSON handling reduce avoidable output variation.
- Type-valid or parseable output can remain semantically wrong, especially when unknown values are coerced or similar skills are inconsistently normalized.
- Output volume, runtime, and API cost are operational measures; they do not substitute for labeled accuracy evaluation and error analysis.
- Market conclusions require separate evidence for source coverage, representativeness, missingness, classification sensitivity, and statistical uncertainty.

## Evidence
Scalable, bounded transformation:
- [[tamer-c-insights-from-over-10000-comments-on-ask-hn-who-is-hiring-using-gpt-4o-langchain]] reports converting 10,891 job-post comments into typed SQLite records and using SQL for aggregation.
- [[truc-phan-proof-of-concept-using-llms-to-extract-key-skills-from-job-descriptions]] reports prompting Gemini for skill lists across a cleaned 553-posting Glassdoor dataset and using Tableau for aggregation.

Contract specificity and cleanup:
- [[tamer-c-insights-from-over-10000-comments-on-ask-hn-who-is-hiring-using-gpt-4o-langchain]] separates city and country, recommends exhaustive categorical classes and delimiters, and reports that a boolean type alone did not reliably produce boolean values.
- [[truc-phan-proof-of-concept-using-llms-to-extract-key-skills-from-job-descriptions]] constrains extraction to data skills, tools, and languages and post-processes empty lists and malformed JSON.

Operational evidence:
- [[tamer-c-insights-from-over-10000-comments-on-ask-hn-who-is-hiring-using-gpt-4o-langchain]] reports US$54.09 total model cost and 43.5–65.1 seconds for three example monthly batches.
- [[truc-phan-proof-of-concept-using-llms-to-extract-key-skills-from-job-descriptions]] reports an average of 12 extracted keywords per description, which measures output volume rather than correctness.

Semantic and analytical boundaries:
- [[tamer-c-insights-from-over-10000-comments-on-ask-hn-who-is-hiring-using-gpt-4o-langchain]] maps unknown remote status to `false`, showing how a valid record can encode a biased assumption.
- [[truc-phan-proof-of-concept-using-llms-to-extract-key-skills-from-job-descriptions]] retains dashboards with skill percentages but reports no labeled extraction test, scrape-coverage audit, raw per-skill counts, or uncertainty intervals.

## Counterevidence & Qualifications
Both sources are self-reported practitioner cases in technical employment data rather than controlled extraction benchmarks. Neither provides a labeled validation set, human agreement baseline, precision, recall, model/version pin sufficient for reproduction, or robustness comparison across prompts and taxonomies. The Hacker News sample represents a specialized community; the Glassdoor sample covers 553 postings from one 30-day window and applies title filtering, category rules, and mean imputation. The cases support feasibility and expose design risks, but do not establish that their displayed job-market trends are accurate or generalizable.

## What Changed
- Added a second implementation using Gemini skill-list extraction from 553 Glassdoor postings.
- Broadened the concept from typed records to normalized lists while keeping schema and taxonomy semantics central.
- Distinguished output volume and dashboard usability from validated extraction accuracy.
- Added scrape coverage, classification sensitivity, imputation, and market representativeness as separate downstream validity requirements.

## Related Concepts
- [[LLMDataAnalysis]] - structured extraction creates the dataset on which deterministic analysis operates.
- [[PromptEngineering]] - task, category, delimiter, and output instructions define the extraction contract.
- [[DataFormatInteroperability]] - normalization preserves consistent meaning across model output, storage, and analysis.
- [[SoftwareVerification]] - labeled samples and error analysis are needed to test semantic correctness.
- [[PracticalLLMUse]] - extraction is bounded and valuable when outputs remain inspectable and queryable.
- [[TextToSQL]] - both connect language and structured data, but extraction writes records while text-to-SQL generates queries.
- [[LargeScaleWebScraping]] - acquisition coverage and source quality bound what an extractor can validly measure.
