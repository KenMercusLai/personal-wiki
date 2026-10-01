---
title: "Gemini 3 Prompting: Best Practices for General Usage"
type: source
tags: [ai, prompting, gemini, context-engineering]
date: 2025-11-19
source_file: "/mnt/ken_personal_wiki/Articles/Philipp Schmid - Gemini 3 Prompting Best Practices for General Usage.md"
---

## Summary
[[PhilippSchmid]] presents a practitioner playbook for prompting [[Gemini]] 3 Pro through direct instructions, consistent structure, explicit parameters, deliberate context placement, planning, self-review, and persistent tool use. The article offers reusable XML and Markdown patterns for research, writing, problem-solving, and education, while stressing that these are empirical starting points to test and refine rather than a universal template.

## Key Claims
- [[PromptEngineering]] for Gemini 3 should favor concise goals, defined terms, consistent delimiters, explicit output requirements, and little persuasive filler.
- Behavioral constraints and role definitions belong in the system instruction or prompt opening, while a query over a large supplied context should appear after that context with an explicit bridge back to the evidence.
- Text, images, audio, and video should be treated as jointly relevant inputs, with instructions identifying the modalities the answer must synthesize.
- Planning prompts can ask the model to decompose the goal, check whether required information is present, consider stronger methods, outline the work, and validate its understanding before answering.
- Self-critique should compare the draft with the user's intent, tone, constraints, and any assumptions rather than merely restating the output.
- Agentic prompts can specify persistence and recovery after tool failure, but tool calls should remain tied to an explicit purpose, expected result, and contribution to the task.
- Prompt structures are baselines whose value depends on task, data, latency, and domain constraints, so iteration and measurement matter more than finding one perfect template.

## Key Quotes
> "Gemini 3 favors directness over persuasion and logic over verbosity." - the article's general prompting premise.

> "Context engineering is an empirical effort, not a fixed syntax." - on treating the template as a testable baseline.

## Connections
- [[PhilippSchmid]] - author sharing the practices from his own Gemini 3 Pro use.
- [[Gemini]] - model family for which the recommendations are presented.
- [[PromptEngineering]] - central practice of specifying goals, boundaries, process, and output.
- [[LLMContextManagement]] - instruction placement, long-context ordering, modality references, and context anchoring shape what the model attends to.
- [[StructuredProblemSolving]] - decomposition, completeness checks, alternative methods, and validation structure the reasoning workflow.
- [[AgenticWorkflowPatterns]] - persistence, tool recovery, planning, and self-review extend the prompt into an execution loop.

## Contradictions
- No direct contradiction with existing wiki content. The source complements [[LLMContextManagement]] by distinguishing durable constraints at the beginning from the task request placed after a long evidence block, and it qualifies its own templates as model- and task-dependent heuristics.
