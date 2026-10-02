---
title: "Gemini"
type: entity
tags: [ai, llm, writing, structured-extraction]
sources:
  - shi-de-wo-yong-ai-xie-wen-zhang-za-di
  - philipp-schmid-gemini-3-prompting-best-practices-for-general-usage
  - truc-phan-proof-of-concept-using-llms-to-extract-key-skills-from-job-descriptions
last_updated: 2026-10-02
knowledge_schema: synthesis-v1
---

## Overview
[[Gemini]] is a multimodal AI model family represented in the sources through assisted writing and image generation, a model-specific prompting playbook, and API-based skill extraction from job descriptions.

## Current Profile
The sources place Gemini in three bounded roles. [[FengRuohang]] uses it alongside ChatGPT to cross-check article drafts and uses its visible interface for candidate image generation. [[PhilippSchmid]] reports that Gemini 3 Pro responds well to direct instructions, consistent structure, explicit parameters, deliberate long-context placement, multimodal references, planning, and output review. [[TrucPhan]] uses a Gemini API call inside a Python pipeline to extract data-related skills, tools, and languages from Glassdoor descriptions before deterministic cleaning and Tableau aggregation.

Together these accounts show a model embedded inside larger human- and software-controlled workflows rather than acting as the final authority. The job-post case demonstrates parseable, analysis-ready output but reports no model version, labeled accuracy test, or comparison with human coding. The profile therefore records practitioner-reported uses and heuristics, not stable product capabilities or validated performance.

## Key Characteristics
- Supports drafting-adjacent fact checking and image-generation workflows under human editorial responsibility.
- Is reported to favor concise, direct, consistently structured prompts with explicit goals and output requirements.
- Can be prompted over long inputs by placing the task after the evidence while keeping durable behavioral constraints early.
- Is treated as multimodal, with prompts expected to identify the text, image, audio, or video inputs to synthesize.
- Supports planning, self-review, and tool-oriented workflows whose results still require external verification.
- Can return structured skill lists through an API for downstream cleaning, aggregation, and visualization.
- Producing parseable lists or many keywords does not establish semantic extraction accuracy.

## Evidence
Writing and visual workflow:
- [[shi-de-wo-yong-ai-xie-wen-zhang-za-di]] says the author sends drafts to Gemini and ChatGPT for checking before manual verification of critical facts and shows Gemini generating candidate images.

Prompting behavior:
- [[philipp-schmid-gemini-3-prompting-best-practices-for-general-usage]] recommends direct goals, defined parameters, consistent boundaries, deliberate long-context placement, explicit modality references, planning, critique, persistence, and iteration.

Structured extraction:
- [[truc-phan-proof-of-concept-using-llms-to-extract-key-skills-from-job-descriptions]] uses Gemini through an API to identify data skills, tools, and programming languages and then handles empty lists and malformed JSON before analysis.
- [[truc-phan-proof-of-concept-using-llms-to-extract-key-skills-from-job-descriptions]] reports an average of 12 keywords per description across 553 postings but no labeled accuracy metric.

Accountability boundary:
- [[shi-de-wo-yong-ai-xie-wen-zhang-za-di]] keeps publication responsibility with the author, while [[philipp-schmid-gemini-3-prompting-best-practices-for-general-usage]] treats prompt templates as empirical starting points and [[truc-phan-proof-of-concept-using-llms-to-extract-key-skills-from-job-descriptions]] relies on downstream cleanup rather than treating raw output as automatically valid.

## Qualifications
All three sources are practitioner accounts rather than standardized capability evaluations. They do not provide common task sets, accuracy results, latency and cost controls, or cross-model comparisons. The extraction source does not specify the Gemini model version or publish labeled precision and recall, and its average keyword count is not a correctness measure. Recommendations tied to “Gemini 3 Pro” may not generalize across versions or domains, while product capabilities, ownership, pricing, and safety behavior can change independently of these archived cases.

## What Changed
- Added API-based structured extraction as a third reported Gemini role.
- Extended the profile from creative and prompting workflows to a model-in-the-loop data pipeline.
- Made parseability, output volume, and semantic accuracy explicit separate concerns.

## Relationships
- [[FengRuohang]] - uses Gemini for draft checking and visual packaging.
- [[ChatGPT]] - paired with Gemini for cross-model checking in the writing workflow.
- [[Claude]] - helps generate image-scene prompts later used in Gemini.
- [[PhilippSchmid]] - publishes the Gemini 3 Pro prompting playbook summarized here.
- [[TrucPhan]] - uses the Gemini API for job-description skill extraction.
- [[PromptEngineering]] - organizes goals, boundaries, process, and output constraints around model use.
- [[LLMStructuredExtraction]] - describes Gemini's bounded record-producing role in the job-post pipeline.
- [[LLMContextManagement]] - explains instruction placement and evidence anchoring around large inputs.
