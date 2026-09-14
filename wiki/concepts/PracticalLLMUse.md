---
title: "Practical LLM Use"
type: concept
tags: [ai, llm, productivity, programming]
sources:
  - blog-nicholas-carlini-how-i-use-ai
last_updated: 2026-09-14
knowledge_schema: synthesis-v1
---

## Definition
[[PracticalLLMUse]] is the use of large language models for concrete bounded tasks where they reduce friction, speed up work, teach unfamiliar material, or generate inspectable starting points without requiring the model to be perfectly reliable.

## Current Synthesis
Carlini's source frames practical LLM use as a present-tense productivity claim rather than a prediction about future automation. The strongest pattern is not "the model replaces the worker" but "the model lowers the cost of starting, looking up, transforming, explaining, and automating." It helps build small applications, learn new technologies, produce first drafts of code, simplify complex artifacts, handle repetitive formatting, answer API questions, search for hard-to-name things, write throwaway scripts, teach concepts, and diagnose errors.

The concept is therefore complementary to [[AIWorkflowDesign]] and [[AICodingPractice]]. It emphasizes task fit: LLMs are especially useful when the task is small enough to inspect, when a rough beginning is valuable, when the user can verify the result, or when the alternative is tedious search, boilerplate, or one-off glue code. The same source explicitly keeps serious limitations in view, so the synthesis is optimistic but bounded.

## Key Claims
- LLM usefulness can be real even if models hallucinate, behave inconsistently, and raise serious ethical or social concerns.
- Productivity gains often come from reducing startup friction rather than producing final work in one pass.
- LLMs work well as interactive tutors because they adapt explanations to the user's immediate goal and missing background.
- Natural-language assistance can turn non-experts into temporary power users for transformations, automation, and tool usage.
- One-off scripts, boilerplate, data formatting, API lookup, and error interpretation are high-fit use cases because the outputs are bounded and often easy to check.
- The user's ability to judge, test, or discard the output is the main boundary between useful assistance and risky delegation.

## Evidence
- Present usefulness: [[blog-nicholas-carlini-how-i-use-ai]] states the narrow claim that current LLMs are useful now, without arguing for full job automation.
- Application scaffolding: [[blog-nicholas-carlini-how-i-use-ai]] describes using GPT-4 to build most of an interactive quiz application that the author might not otherwise have made.
- Tutoring: [[blog-nicholas-carlini-how-i-use-ai]] describes learning Docker, Podman, and GPU passthrough through guided interaction rather than static tutorials.
- Blank-page reduction: [[blog-nicholas-carlini-how-i-use-ai]] uses generated CUDA code as a starting point, then iterates through compilation errors and performance considerations.
- Simplification: [[blog-nicholas-carlini-how-i-use-ai]] uses LLMs to extract minimal examples and even reconstruct source-like code from Python bytecode disassembly.
- Boring-task automation: [[blog-nicholas-carlini-how-i-use-ai]] lists boilerplate, tests, documentation templates, book-list formatting, citations, HTML diff formatting, data processing, and file manipulation.
- Power-user floor: [[blog-nicholas-carlini-how-i-use-ai]] contrasts complex editor macros with natural-language commands for text transformation.
- Search and reference: [[blog-nicholas-carlini-how-i-use-ai]] uses LLMs for command syntax, library references, hard-to-keyword concepts, shell errors, and crash dumps.

## Counterevidence & Qualifications
The source is a personal practitioner report, not a controlled productivity study. Its examples are strongest for users who can recognize bad output, run tests, inspect code, or treat the result as disposable. It explicitly excludes several broader conclusions: that LLMs solve all problems, replace all programmers, or will continue improving at the same rate. It also brackets unresolved concerns about hallucination, robustness, privacy, training-data ethics, copyright, labor, misinformation, surveillance, job displacement, and power concentration.

## What Changed
- Created this concept to capture Carlini's taxonomy of concrete LLM productivity uses.

## Related Concepts
- [[AIWorkflowDesign]] - practical use becomes stronger when tasks are decomposed into controllable workflows.
- [[AICodingPractice]] - coding is one of the source's highest-frequency practical domains.
- [[HumanCodeResponsibility]] - bounded usefulness still depends on human judgment and ownership.
- [[AIAssistedWriting]] - writing workflows share the pattern of using AI for starts, variants, and cleanup while retaining human authorship.
- [[LLMContextManagement]] - practical results depend on supplying the right problem details and interaction history.
- [[PersonalProductivity]] - LLMs function as a productivity tool when they reduce search, setup, and repetitive-work friction.
