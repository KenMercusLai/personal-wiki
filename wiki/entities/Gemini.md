---
title: "Gemini"
type: entity
tags: [ai, llm, writing]
sources:
  - shi-de-wo-yong-ai-xie-wen-zhang-za-di
  - philipp-schmid-gemini-3-prompting-best-practices-for-general-usage
last_updated: 2026-10-01
knowledge_schema: synthesis-v1
---

## Overview
[[Gemini]] is a multimodal AI model family represented in the sources as part of an assisted-writing pipeline and as the subject of a model-specific prompting playbook.

## Current Profile
Within [[FengRuohang]]'s workflow, Gemini is one of two models used to cross-check AI-generated article drafts, while its visible interface generates candidate images from prompts prepared with Claude. [[PhilippSchmid]] adds a different practitioner view centered on Gemini 3 Pro: he reports that it responds well to direct instructions, consistent structure, explicit parameters, deliberate long-context placement, multimodal references, planning, and output review.

Together the sources show a model used both inside a larger human-controlled production process and as an object of prompt optimization. Neither source is official product documentation or a controlled capability evaluation, so the profile records reported uses and heuristics rather than stable universal behavior.

## Key Characteristics
- Functions as one model in a cross-checking workflow for article facts.
- Provides a visual-generation interface in the illustrated packaging stage.
- Is used after initial drafting rather than as the source of the author's topic or argument.
- Is reported by Schmid to favor concise, direct, consistently structured prompts with explicit output requirements.
- Is prompted over long inputs by placing the task after the evidence while keeping durable behavioral constraints at the beginning.
- Is treated as multimodal, with prompts expected to identify and synthesize relevant text, image, audio, or video inputs.
- Supports planning, self-review, and tool-oriented workflows while leaving final accountability outside the model.

## Evidence
- Cross-checking: [[shi-de-wo-yong-ai-xie-wen-zhang-za-di]] says the author sends drafts to Gemini and ChatGPT for verification before manual checks of critical facts.
- Workflow position: [[shi-de-wo-yong-ai-xie-wen-zhang-za-di]] places Gemini after topic selection, argument structure, and initial draft generation.
- Visual generation: [[shi-de-wo-yong-ai-xie-wen-zhang-za-di]] includes a screenshot of Gemini producing image candidates from prompts for the article's final packaging.
- Accountability boundary: [[shi-de-wo-yong-ai-xie-wen-zhang-za-di]] says the author remains responsible for facts and final publication.
- Prompt style: [[philipp-schmid-gemini-3-prompting-best-practices-for-general-usage]] recommends direct goals, defined parameters, consistent XML or Markdown boundaries, and explicit verbosity.
- Long-context placement: [[philipp-schmid-gemini-3-prompting-best-practices-for-general-usage]] separates early role and behavior constraints from a final query anchored to the preceding evidence.
- Multimodal use: [[philipp-schmid-gemini-3-prompting-best-practices-for-general-usage]] says prompts should reference the input modalities that must be synthesized.
- Complex execution: [[philipp-schmid-gemini-3-prompting-best-practices-for-general-usage]] supplies patterns for planning, critique, persistence, research, writing, problem-solving, and education.

## Qualifications
The evidence consists of two practitioner accounts rather than standardized evaluations. Schmid does not provide prompt variants, task sets, accuracy results, latency costs, or cross-model controls, and explicitly frames his patterns as starting points. The page is not current product documentation for Gemini's capabilities, ownership, pricing, or safety behavior, and recommendations tied to “Gemini 3 Pro” may not generalize across versions or domains.

## What Changed
- Expanded Gemini from an auxiliary writing tool into the subject of a model-specific prompting profile.
- Added directness, structured boundaries, long-context placement, multimodal coherence, planning, and self-review as practitioner-reported behaviors.
- Added explicit limits around model-version specificity and the absence of comparative evaluation.

## Relationships
- [[FengRuohang]] - uses Gemini in his article workflow.
- [[AIAssistedWriting]] - Gemini supports verification and visual packaging in this workflow.
- [[ChatGPT]] - paired with Gemini for cross-model checking.
- [[Claude]] - Claude helps generate the image-scene prompts that are later used in Gemini.
- [[Google]] - Gemini is associated with Google's AI ecosystem, though this source focuses on use rather than provider details.
- [[PhilippSchmid]] - publishes the Gemini 3 Pro prompting playbook summarized here.
- [[PromptEngineering]] - organizes the source's instruction, structure, planning, and review practices.
- [[LLMContextManagement]] - explains the placement and anchoring of instructions around large inputs.
