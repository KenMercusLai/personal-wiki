---
title: "Gemini"
type: entity
tags: [ai, llm, writing, structured-extraction]
sources:
  - shi-de-wo-yong-ai-xie-wen-zhang-za-di
  - philipp-schmid-gemini-3-prompting-best-practices-for-general-usage
  - truc-phan-proof-of-concept-using-llms-to-extract-key-skills-from-job-descriptions
  - manage-requirements-like-code
last_updated: 2026-10-18
knowledge_schema: synthesis-v1
---

## Overview
[[Gemini]] is a multimodal AI model family and product environment represented in the sources through assisted writing and image generation, a model-specific prompting playbook, API-based skill extraction, and a Canvas-centered product-requirements workflow.

## Current Profile
The sources place Gemini in four bounded roles. [[FengRuohang]] uses it alongside ChatGPT to cross-check article drafts and uses its visible interface for candidate image generation. [[PhilippSchmid]] reports that Gemini 3 Pro responds well to direct instructions, consistent structure, explicit parameters, deliberate long-context placement, multimodal references, planning, and output review. [[TrucPhan]] uses a Gemini API call inside a Python pipeline to extract data-related skills, tools, and languages from Glassdoor descriptions before deterministic cleaning and Tableau aggregation.

Zhang's product-management account uses a custom Gem and Canvas as a coordinated workspace for versioned PRDs, Mermaid flows, HTML prototypes, role-based reviews, Python-backed spreadsheet analysis, and small internal web tools. Google Docs and [[NotebookLM]] externalize approved history, while plan-confirm-execute gates, atomic-edit rules, visible versions, and context resets preserve human control. Together these accounts show Gemini embedded inside larger human- and software-controlled workflows rather than acting as the final authority. The profile therefore records practitioner-reported uses and heuristics, not stable product capabilities or validated performance.

## Key Characteristics
- Supports drafting, diagram, prototype, and image-generation workflows under human editorial responsibility.
- Is reported to favor concise, direct, consistently structured prompts with explicit goals and output requirements.
- Can be prompted over long inputs by placing the task after the evidence while keeping durable behavioral constraints early.
- Is treated as multimodal, with prompts expected to identify the text, image, audio, or video inputs to synthesize.
- Supports custom-Gem protocols, Canvas deliverables, planning, role-based review, and tool-oriented workflows whose results still require external verification.
- Can return structured skill lists through an API for downstream cleaning, aggregation, and visualization.
- Can execute Python for deterministic analysis when explicitly instructed, but generated interpretation and product claims still need verification.

## Evidence
Writing and visual workflow:
- [[shi-de-wo-yong-ai-xie-wen-zhang-za-di]] says the author sends drafts to Gemini and ChatGPT for checking before manual verification of critical facts and shows Gemini generating candidate images.

Prompting behavior:
- [[philipp-schmid-gemini-3-prompting-best-practices-for-general-usage]] recommends direct goals, defined parameters, consistent boundaries, deliberate long-context placement, explicit modality references, planning, critique, persistence, and iteration.

Structured extraction:
- [[truc-phan-proof-of-concept-using-llms-to-extract-key-skills-from-job-descriptions]] uses Gemini through an API to identify data skills, tools, and programming languages and then handles empty lists and malformed JSON before analysis.
- [[truc-phan-proof-of-concept-using-llms-to-extract-key-skills-from-job-descriptions]] reports an average of 12 keywords per description across 553 postings but no labeled accuracy metric.

Requirements and prototype workspace:
- [[manage-requirements-like-code]] documents a custom Gem with fixed PRD structure, semantic versions, scoped-edit rules, approval gates, review commands, and distinct conversation and Canvas output channels.
- [[manage-requirements-like-code]] shows Canvas carrying a versioned PRD, editable Mermaid sequence logic, and an interactive chargeback prototype whose contents can be shared or externally hosted.
- [[manage-requirements-like-code]] instructs Gemini to use Python over complete spreadsheet rows with visible counts and intermediate totals, and recommends exporting artifacts and restarting when a long conversation drifts.

Accountability boundary:
- [[shi-de-wo-yong-ai-xie-wen-zhang-za-di]] keeps publication responsibility with the author, while [[philipp-schmid-gemini-3-prompting-best-practices-for-general-usage]] treats prompt templates as empirical starting points and [[truc-phan-proof-of-concept-using-llms-to-extract-key-skills-from-job-descriptions]] relies on downstream cleanup rather than treating raw output as automatically valid.

## Qualifications
All four sources are practitioner accounts rather than standardized capability evaluations. They do not provide common task sets, accuracy results, latency and cost controls, or cross-model comparisons. The extraction source does not specify the Gemini model version or publish labeled precision and recall, and its average keyword count is not a correctness measure. The requirements source does not measure PRD defects, review quality, rollback fidelity, prototype accuracy, or data-governance outcomes; its text-based versions are not demonstrated Git history. Recommendations tied to “Gemini 3 Pro,” Gems, Canvas, sharing, or cloud Python may not generalize across versions or domains, while product capabilities, retention, ownership, pricing, and safety behavior can change independently of these archived cases.

## What Changed
- Added custom Gems and Canvas as a requirements, diagram, prototype, review, and computation workspace.
- Added externalized project continuity through Google Docs, NotebookLM, exported artifacts, and clean-session recovery.
- Distinguished visible document versions and approval protocols from actual source-control guarantees.

## Relationships
- [[FengRuohang]] - uses Gemini for draft checking and visual packaging.
- [[ChatGPT]] - paired with Gemini for cross-model checking in the writing workflow.
- [[Claude]] - helps generate image-scene prompts later used in Gemini.
- [[PhilippSchmid]] - publishes the Gemini 3 Pro prompting playbook summarized here.
- [[TrucPhan]] - uses the Gemini API for job-description skill extraction.
- [[NotebookLM]] - supplies archived project knowledge and business rules to later Gemini sessions.
- [[RequirementsAsCode]] - applies explicit structure, versions, review gates, and recovery to Gemini-generated PRDs and prototypes.
- [[PromptEngineering]] - organizes goals, boundaries, process, and output constraints around model use.
- [[LLMStructuredExtraction]] - describes Gemini's bounded record-producing role in the job-post pipeline.
- [[LLMContextManagement]] - explains instruction placement and evidence anchoring around large inputs.
