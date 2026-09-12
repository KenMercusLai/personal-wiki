---
title: "Codebook Development"
type: concept
tags: [research-methods, qualitative-analysis, ai]
sources:
  - ni-da-gai-bu-hui-xiang-yong-llm-zuo-shu-ju-fen-xi
last_updated: 2026-09-12
knowledge_schema: synthesis-v1
---

## Definition
[[CodebookDevelopment]] is the design, refinement, and validation of a structured coding scheme for qualitative or categorical research data.

## Current Synthesis
The source presents codebook development as a comparatively safer LLM-assisted research task because the model can draft categories, suggest definitions, and apply codes while the researcher reviews and revises the scheme. The author's usability-research workflow starts from the interview guide and research plan, asks the model for an initial codebook, then manually improves the dimensions and standards. Multi-model coding agreement is used as a diagnostic signal for whether categories are clear enough.

## Key Claims
- LLMs can help draft an initial codebook from research questions, interview guides, and study plans.
- Human review is required to align categories with domain theory and the actual data.
- A good codebook defines dimensions, categories, and coding standards clearly enough for consistent use.
- Multiple LLMs coding the same data can expose vague category definitions when their outputs disagree.
- Voting across repeated model codings can support categorical labeling, but it does not remove the need for researcher judgment.

## Evidence
- Drafting workflow: [[ni-da-gai-bu-hui-xiang-yong-llm-zuo-shu-ju-fen-xi]] describes giving an LLM the interview guide and research plan, then asking it to draft a user-error codebook.
- Human refinement: [[ni-da-gai-bu-hui-xiang-yong-llm-zuo-shu-ju-fen-xi]] says the author manually reviewed and modified the codebook based on data and theory.
- Category structure: [[ni-da-gai-bu-hui-xiang-yong-llm-zuo-shu-ju-fen-xi]] lists dimensions such as error type, usability problem, severity, task phase, and recovery strategy.
- Agreement check: [[ni-da-gai-bu-hui-xiang-yong-llm-zuo-shu-ju-fen-xi]] recommends comparing multiple LLMs' coding under the same codebook and revising unclear definitions when they disagree.

## Counterevidence & Qualifications
The source reports a successful personal workflow rather than a general validation study. Inter-model agreement can signal clearer categories, but models may share similar biases or training artifacts; agreement should not be mistaken for ground truth without human audit and, where appropriate, expert or participant validation.

## What Changed
- Created the concept page for codebook development as a safer, review-centered use of LLMs in research workflow.

## Related Concepts
- [[LLMDataAnalysis]] - codebook work is an analysis-adjacent LLM use with lower inferential risk when reviewed.
- [[PHacking]] - contrasts with biased significance search by focusing on coding clarity and reliability.
- [[HumanCodeResponsibility]] - human researchers remain accountable for model-assisted coding decisions.
- [[AIKnowledgeAssistant]] - both use LLMs to organize information, but codebooks require explicit category definitions and validation.
- [[SoftwareVerification]] - agreement checks and manual audits are verification practices for coded data.
