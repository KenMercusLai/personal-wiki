---
title: "Task-Contingent AI Collaboration"
type: concept
tags: [ai, software-engineering, workflow]
sources:
  - claude-bian-cheng-gong-zuo-liu-chang-jing-hua-shi-jian
last_updated: 2026-10-03
knowledge_schema: synthesis-v1
---

## Definition
[[TaskContingentAICollaboration]] is the practice of selecting a human-agent interaction mode according to a task's risk, specification clarity, uncertainty, and cost of failure.

## Current Synthesis
The initial source distinguishes three modes. High-stakes critical-path work calls for synchronous collaboration in which the human owns the core reasoning and the agent supplies alternatives and challenges. Clear but laborious execution can be delegated asynchronously inside an explicit scope and checked at completion. Unfamiliar-domain work benefits from a mixed exploratory sequence that moves from a map of the field to detailed questions and then guided practice.

The framework becomes operational through bounded experiments. A version-control checkpoint creates a recovery point; an autonomous attempt runs within a defined task; verification decides whether to retain or revert it. Independent agents may specialize on separable objectives, while screenshots can tighten the feedback loop for visual work. These patterns change the interaction surface but do not transfer final responsibility away from the human.

## Key Claims
- Collaboration intensity should rise with consequence, ambiguity, and architectural coupling.
- Autonomous delegation fits work whose scope, constraints, and acceptance checks can be stated in advance.
- Exploration should alternate explanation and practice rather than treating an unfamiliar domain as ordinary implementation.
- Reversible checkpoints can turn uncertain agent performance into bounded expected-cost experiments.
- Specialization and visual feedback can reduce some forms of ambiguity while introducing integration and nonvisual-specification gaps.

## Evidence
- Mode selection: [[claude-bian-cheng-gong-zuo-liu-chang-jing-hua-shi-jian]] maps critical-path work to synchronous collaboration, repetitive execution to asynchronous autonomy, and unfamiliar learning to mixed exploration.
- Recovery loop: [[claude-bian-cheng-gong-zuo-liu-chang-jing-hua-shi-jian]] describes committing a checkpoint, running an autonomous attempt, accepting a satisfactory result, or reverting and retrying.
- Specialized and visual loops: [[claude-bian-cheng-gong-zuo-liu-chang-jing-hua-shi-jian]] proposes independent agents for decomposed objectives and screenshot-based iteration for UI work.
- Enabling conditions: [[claude-bian-cheng-gong-zuo-liu-chang-jing-hua-shi-jian]] identifies `CLAUDE.md`, version control, and cultural tolerance for failed attempts as prerequisites.

## Counterevidence & Qualifications
The framework currently rests on one practitioner's secondary synthesis of team anecdotes, not a comparative study. Its success-rate ranges are undefined and internally inconsistent between scenario and complexity classifications. Task types also overlap: architecture contains repetitive work, unfamiliar learning can be high risk, and “clear” implementation can hide integration constraints. Retrying may repeat the same failure or discard useful diagnosis, multiple agents impose coordination cost, and screenshots do not encode behavior, accessibility, data, or responsive edge cases.

## What Changed
- Established task risk, clarity, uncertainty, and reversibility as the routing variables for selecting an AI collaboration mode.
- Added checkpoint-and-retry, agent specialization, and screenshot feedback as qualified implementation patterns.

## Related Concepts
- [[AIAgentCollaboration]] - task-contingent routing selects the form and intensity of human-agent coordination.
- [[AgenticWorkflowPatterns]] - checkpoints, retries, specialization, and feedback loops implement the routing framework.
- [[LLMContextManagement]] - retrying from a clean session trades retained diagnosis for removal of misleading history.
- [[SoftwareVerification]] - acceptance checks determine whether autonomous output is retained.
- [[HumanCodeResponsibility]] - consequential decisions and final acceptance remain human obligations.
- [[BottleneckAwareAICoding]] - the preferred mode depends partly on whether implementation, review, integration, or learning is limiting progress.
