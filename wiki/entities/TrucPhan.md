---
title: "Truc Phan"
type: entity
tags: [data-analysis, llm, job-market]
sources:
  - truc-phan-proof-of-concept-using-llms-to-extract-key-skills-from-job-descriptions
last_updated: 2026-10-02
knowledge_schema: synthesis-v1
---

## Overview
[[TrucPhan]] is represented in this wiki as the author and builder of a proof-of-concept pipeline for scraping data-analyst job postings, extracting skills with Gemini, and visualizing the resulting market snapshot.

## Current Profile
Phan combines browser automation, DataFrame cleaning, prompt-constrained model output, API integration, and dashboard design in one inspectable workflow. The source shows practical end-to-end implementation and publishes code, cleaned datasets, and a Tableau workbook, but it does not report extraction accuracy, scraper coverage, or uncertainty around its market conclusions.

## Key Characteristics
- Uses a personal job search as the motivation for a data-driven market analysis.
- Implements Selenium-based acquisition and structured tabular cleaning in Python.
- Assigns Gemini the bounded task of extracting data-related skills, tools, and languages from descriptions.
- Converts model output into datasets intended for conventional aggregation and visualization.
- Communicates results through Tableau dashboards and a public code repository.
- Treats the project as a proof of concept rather than presenting a validated labor-market measurement system.

## Evidence
End-to-end implementation:
- [[truc-phan-proof-of-concept-using-llms-to-extract-key-skills-from-job-descriptions]] describes Phan's scraping, cleaning, model extraction, post-processing, and dashboard stages.

Published outputs:
- [[truc-phan-proof-of-concept-using-llms-to-extract-key-skills-from-job-descriptions]] links a GitHub repository containing the notebook and datasets and a public Tableau workbook.

Empirical boundaries:
- [[truc-phan-proof-of-concept-using-llms-to-extract-key-skills-from-job-descriptions]] reports 553 postings and dashboard percentages but no labeled extraction evaluation or scrape-coverage audit.

## Qualifications
The profile derives from one self-authored project article rather than independent evaluation. It establishes the reported workflow and outputs, not the correctness of every extracted skill, the representativeness of Glassdoor listings, or the durability of its February 2024 market findings.

## What Changed
- Created a profile centered on Phan's LLM-assisted job-post analysis proof of concept.

## Relationships
- [[Gemini]] - Phan uses its API for skill extraction.
- [[Python]] - implementation language for acquisition, cleaning, and processing.
- [[LLMStructuredExtraction]] - core transformation pattern in the project.
- [[LLMDataAnalysis]] - broader analytical workflow that contains the extraction stage.
- [[LargeScaleWebScraping]] - related acquisition discipline, though the proof of concept does not establish large-scale operational robustness.
