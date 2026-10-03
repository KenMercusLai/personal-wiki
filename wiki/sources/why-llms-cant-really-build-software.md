---
title: "Why LLMs Can't Really Build Software"
type: source
tags: [llm, software-engineering, ai, mental-models]
date: 2025-08-14
source_file: "/mnt/ken_personal_wiki/Articles/Why LLMs Cant Really Build Software.md"
---

## Summary
[[ConradIrwin]] argues that software engineering is an iterative comparison between a mental model of requirements and a mental model of actual program behavior, not merely code generation. Current LLMs can write and revise code, run tests, add logging, and use debuggers, but the author says context omission, recency bias, and hallucination prevent them from maintaining the two models reliably across non-trivial work. The practical conclusion is collaborative rather than anti-AI: use models for bounded implementation, requirements synthesis, and documentation while a human engineer remains responsible for intent, diagnosis, verification, and acceptance.

## Key Claims
- Effective [[SoftwareEngineering]] repeatedly models requirements, implements them, models what the code actually does, and reconciles the difference.
- Current LLMs are capable code generators and tool users, but local implementation skill does not by itself establish durable project-level understanding.
- Failed tests are ambiguous evidence: deciding whether code, tests, requirements, or the current diagnosis is wrong requires a model of intended and actual behavior.
- Context omission, recency bias, and hallucination make it difficult for generative models to maintain stable [[MentalModels]] across long, iterative work.
- Human engineers can suspend a broader task, investigate a subproblem, then restore the larger context or zoom between detail and system-level purpose; the author argues that current model architectures do this unreliably.
- LLMs remain useful for clear, bounded tasks, requirements synthesis, documentation, code generation, debugging tools, and updates directed by a diagnosed problem.
- [[HumanCodeResponsibility]] remains the operational boundary for non-trivial work: people must clarify requirements and determine whether the implementation actually satisfies them.

## Key Quotes
> "The distinguishing factor of effective engineers is their ability to build and maintain clear mental models." - on the capability the author treats as central to engineering.

> "Software engineering requires models that can do more than just generate code." - on the gap between local code production and sustained engineering work.

> "you are in the drivers seat, and the LLM is just another tool to reach for." - on the proposed human-agent relationship.

## Connections
- [[ConradIrwin]] - author of the mental-model account of LLM coding limits.
- [[Zed]] - organizational context for the article's human-agent collaboration position.
- [[SoftwareEngineering]] - framed as iterative reconciliation between intended and actual behavior.
- [[MentalModels]] - the capability the source treats as both the engineer's advantage and the LLM's current weakness.
- [[AICodingPractice]] - recommends bounded agent use under human diagnosis, context control, and acceptance.
- [[HumanCodeResponsibility]] - humans retain responsibility for requirements and actual behavior.
- [[SoftwareVerification]] - tests, logs, and debuggers provide evidence but do not decide what should change.
- [[AIAgentCollaboration]] - the source favors people and agents building together with the person in control.
- [[LLMContextManagement]] - context omission and recency bias are named mechanisms behind model instability.

## Contradictions
- The categorical title and claim that LLMs "cannot build software" tension [[Antirez]]'s substantial coding examples and AI-first case studies. The article's body supports a narrower interpretation: current models can implement bounded or even substantial work, but are unreliable owners of the long-running requirement-to-behavior reconciliation loop.
- The source attributes observed failures to missing stable mental models, but supplies no controlled comparisons, model evaluations, task-complexity threshold, or architectural evidence that this is the unique cause rather than a combination of context management, tool design, training objectives, verification quality, and workflow structure.
- Memory and model capabilities are explicitly treated as moving targets, so the 2025 judgment should not be generalized indefinitely or across all agent harnesses.
