---
title: "Humanistic Agent Design"
type: concept
tags: [ai, agents, human-centered-design, safety]
sources:
  - agent-experience-dao-lun-luo-li-li-de-shu-ju-zhong-xin
last_updated: 2026-09-13
knowledge_schema: synthesis-v1
---

## Definition
[[HumanisticAgentDesign]] is an agent design orientation that helps users clarify what they know, what they intend, and what they actually need before, during, and after AI-assisted action.

## Current Synthesis
RORIRI argues that human-centered agent design should move beyond compliance and task completion. Users bring cognition, intent, and self-awareness into an interaction; a helpful agent should not automatically assume those are complete, stable, or correctly expressed. The design answer to sycophancy is Socratic clarification: ask why the task matters, test assumptions during reasoning, and guide the user toward the next action they truly need.

## Key Claims
- User input has cognitive, intentional, and self-awareness layers.
- Defaulting to complete user knowledge, literal intent, and sufficient self-understanding creates agent failure modes.
- Humanistic agents should clarify "why" before acting when stakes, ambiguity, or hidden motives matter.
- Agents should flag questionable assumptions during reasoning instead of only producing polished outputs.
- After completing a task, agents can help users identify the next real need rather than trapping them in endless validation loops.
- System prompts and product choices can implement this orientation; it is not only a model-capability problem.

## Evidence
- Three user layers: [[agent-experience-dao-lun-luo-li-li-de-shu-ju-zhong-xin]] distinguishes cognition, intent, and self-awareness in user input.
- Default reversal: [[agent-experience-dao-lun-luo-li-li-de-shu-ju-zhong-xin]] says humanistic design flips the defaults that user knowledge, stated intent, and self-understanding are already adequate.
- Before-action clarification: [[agent-experience-dao-lun-luo-li-li-de-shu-ju-zhong-xin]] proposes asking why the user wants to do a task before inference starts.
- During-action assumption checks: [[agent-experience-dao-lun-luo-li-li-de-shu-ju-zhong-xin]] proposes marking whether user premises hold during reasoning.
- After-action guidance: [[agent-experience-dao-lun-luo-li-li-de-shu-ju-zhong-xin]] proposes guiding the user toward the next thing they truly need.
- Design-choice claim: [[agent-experience-dao-lun-luo-li-li-de-shu-ju-zhong-xin]] says this can be pursued through system prompts and product design rather than waiting for a breakthrough.

## Counterevidence & Qualifications
The source is normative and product-philosophical. It does not provide a tested interaction pattern for deciding when clarification is helpful versus annoying, nor does it solve safety, privacy, escalation, or clinical boundaries by itself.

## What Changed
- Created the concept page for humanistic agent design as the article's answer to sycophancy and shallow intent handling.

## Related Concepts
- [[LLMSycophancy]] - humanistic design counters reflexive agreement.
- [[AgentExperience]] - user intent and self-understanding are part of AX.
- [[MetacognitiveFeedback]] - both emphasize helping people see their own thinking.
- [[TasteAsProblemSense]] - both value caring about and recognizing real questions before execution.
- [[AIWorkflowDesign]] - humanistic agent behavior can be designed as part of a controllable workflow.
