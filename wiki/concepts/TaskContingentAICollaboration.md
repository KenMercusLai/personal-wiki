---
title: "Task-Contingent AI Collaboration"
type: concept
tags: [ai, software-engineering, workflow]
sources:
  - claude-bian-cheng-gong-zuo-liu-chang-jing-hua-shi-jian
  - guo-qing-sui-bi-leetao
last_updated: 2026-10-07
knowledge_schema: synthesis-v1
---

## Definition
[[TaskContingentAICollaboration]] is the practice of selecting a human-agent interaction mode according to a task's risk, specification clarity, uncertainty, and cost of failure.

## Current Synthesis
The sources distinguish modes by both task properties and decision stage. High-stakes critical-path work calls for synchronous collaboration in which the human owns the core reasoning and the agent supplies alternatives and challenges. Clear but laborious execution can be delegated asynchronously inside an explicit scope and checked at completion. Unfamiliar-domain work benefits from a mixed exploratory sequence that moves from a map of the field to detailed questions and then guided practice. At the idea stage, AI can help discuss feasibility, define the smallest informative experiment, and make intermediate states observable.

The framework becomes operational through bounded experiments. A version-control checkpoint creates a recovery point; an autonomous attempt runs within a defined task; verification decides whether to retain or revert it. Independent agents may specialize on separable objectives, while screenshots can tighten the feedback loop for visual work. Leetao's reflection adds a motivational boundary: rapid validation also lowers the cost of abandonment, and a sequence of defensible negative conclusions can detach thought from hands-on practice. These patterns change the interaction surface but do not transfer final responsibility—or the decision to continue despite incomplete evidence—away from the human.

## Key Claims
- Collaboration intensity should rise with consequence, ambiguity, and architectural coupling.
- Autonomous delegation fits work whose scope, constraints, and acceptance checks can be stated in advance.
- Exploration should alternate explanation and practice rather than treating an unfamiliar domain as ordinary implementation.
- Reversible checkpoints can turn uncertain agent performance into bounded expected-cost experiments.
- Specialization and visual feedback can reduce some forms of ambiguity while introducing integration and nonvisual-specification gaps.
- Fast AI-supported validation should inform commitment without turning every weak or crowded signal into an automatic stop decision.

## Evidence
- Mode selection: [[claude-bian-cheng-gong-zuo-liu-chang-jing-hua-shi-jian]] maps critical-path work to synchronous collaboration, repetitive execution to asynchronous autonomy, and unfamiliar learning to mixed exploration.
- Recovery loop: [[claude-bian-cheng-gong-zuo-liu-chang-jing-hua-shi-jian]] describes committing a checkpoint, running an autonomous attempt, accepting a satisfactory result, or reverting and retrying.
- Specialized and visual loops: [[claude-bian-cheng-gong-zuo-liu-chang-jing-hua-shi-jian]] proposes independent agents for decomposed objectives and screenshot-based iteration for UI work.
- Enabling conditions: [[claude-bian-cheng-gong-zuo-liu-chang-jing-hua-shi-jian]] identifies `CLAUDE.md`, version control, and cultural tolerance for failed attempts as prerequisites.
- Idea-stage loop: [[guo-qing-sui-bi-leetao]] describes discussing an idea with AI, defining a minimum experiment, observing intermediate checkpoints, and closing the loop with results.
- Abandonment boundary: [[guo-qing-sui-bi-leetao]] reports that repeated negative AI research and experiment results made giving up easier until thinking displaced craft, after which restarting narrowed products restored momentum.

## Counterevidence & Qualifications
The framework rests on practitioner accounts rather than comparative studies. Li Hui's success-rate ranges are undefined and internally inconsistent between scenario and complexity classifications. Leetao supplies no experiment designs or outcomes that would show whether AI's negative conclusions were accurate or whether the revived products found users. Task types also overlap: architecture contains repetitive work, unfamiliar learning can be high risk, and “clear” implementation can hide integration constraints. Retrying may repeat the same failure or discard useful diagnosis, multiple agents impose coordination cost, and screenshots do not encode behavior, accessibility, data, or responsive edge cases. Continuing for craft, personal fit, or exploration can be rational, but it should not be relabeled as validated market demand.

## What Changed
- Established task risk, clarity, uncertainty, and reversibility as the routing variables for selecting an AI collaboration mode.
- Added checkpoint-and-retry, agent specialization, and screenshot feedback as qualified implementation patterns.
- Extended the framework upstream to idea feasibility and minimum experiments while adding premature abandonment as a workflow risk.

## Related Concepts
- [[AIAgentCollaboration]] - task-contingent routing selects the form and intensity of human-agent coordination.
- [[AgenticWorkflowPatterns]] - checkpoints, retries, specialization, and feedback loops implement the routing framework.
- [[LLMContextManagement]] - retrying from a clean session trades retained diagnosis for removal of misleading history.
- [[SoftwareVerification]] - acceptance checks determine whether autonomous output is retained.
- [[HumanCodeResponsibility]] - consequential decisions and final acceptance remain human obligations.
- [[BottleneckAwareAICoding]] - the preferred mode depends partly on whether implementation, review, integration, or learning is limiting progress.
- [[ActionBiasInAI]] - direct building protects the collaboration loop from becoming analysis without practice.
