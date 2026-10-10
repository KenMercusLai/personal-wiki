---
title: "Deliverable-First Agent Design"
type: concept
tags: [ai, agents, workflow, automation]
sources:
  - cong-lauren-bu-xin-gui-hua-shuo-qi-wo-yong-grok-bot-da-growth-researcher-cai-guo-de-keng
last_updated: 2026-10-10
knowledge_schema: synthesis-v1
---

## Definition
[[DeliverableFirstAgentDesign]] is a workflow for defining an agent role through one bounded, reviewable result and accepted example outputs before encoding a broad job description, reusable Skill, recurring schedule, or larger agent organization.

## Current Synthesis
The source diagnoses a sequence error in agent adoption. A user can write a polished role, research framework, and recurring schedule before knowing what useful work from that role looks like. The agent then optimizes the visible process—plans, screening tables, templates, and long reports—while the operator still lacks an artifact that changes a decision or can be applied to a product.

The proposed correction is empirical. State the final result, constrain sources and conditions, specify when the agent must return for confirmation, and request one artifact that can be scored. Review several examples to discover requirements such as source dates, failure reporting, partial-completion disclosure, and prohibited placeholder deliverables. Only after those criteria stabilize should the operator turn the method into a Skill or routine. Role expansion follows the same gate: begin with one bot accountable for one result, then add specialists or channels when recurring work reveals a stable division.

## Key Claims
- A role description is weaker than an accepted deliverable because the artifact exposes whether the task definition produces usable work.
- Plans, frameworks, and templates can become process theater when they delay or substitute for the result the operator needs.
- Initial delegation should specify the outcome, permitted material, constraints, output format, and point for human confirmation.
- Skills should encode a method discovered through reviewed work rather than freeze an untested process.
- Recurring automation should begin only after examples reveal success criteria, source requirements, error behavior, and partial-completion rules.
- One agent should own one narrow result before stable work justifies specialist bots, channels, or a larger hierarchy.
- Deliverable-first does not mean plan-free; complex, coupled, or high-risk tasks can still require explicit planning before action.

## Evidence
- Planning-as-work failure: [[cong-lauren-bu-xin-gui-hua-shuo-qi-wo-yong-grok-bot-da-growth-researcher-cai-guo-de-keng]] says Growth Researcher repeatedly refined research plans, screening frameworks, structures, and briefs without producing strategy the author could use.
- Artifact gate: [[cong-lauren-bu-xin-gui-hua-shuo-qi-wo-yong-grok-bot-da-growth-researcher-cai-guo-de-keng]] recommends defining the final visible result, source boundary, escalation conditions, and a first output that can be scored.
- Workflow hardening: [[cong-lauren-bu-xin-gui-hua-shuo-qi-wo-yong-grok-bot-da-growth-researcher-cai-guo-de-keng]] says actual source and data dates, missing-data errors, and incomplete-work explanations became apparent only after reviewing delivered work.
- Automation sequencing: [[cong-lauren-bu-xin-gui-hua-shuo-qi-wo-yong-grok-bot-da-growth-researcher-cai-guo-de-keng]] includes the retained screenshot of the disabled daily routine and delays scheduling in the proposed restart until outputs are accepted.
- Role boundary: [[cong-lauren-bu-xin-gui-hua-shuo-qi-wo-yong-grok-bot-da-growth-researcher-cai-guo-de-keng]] contrasts a department-sized Growth Researcher with a narrow AICon bot that returned editable conference notes.
- Optional planning: [[cong-lauren-bu-xin-gui-hua-shuo-qi-wo-yong-grok-bot-da-growth-researcher-cai-guo-de-keng]] reproduces [[LaurenTan]]'s pstack passage keeping Cursor Plan Mode available while rejecting planning as the default.

## Counterevidence & Qualifications
The framework comes from one failed bot role and one favorable comparison, with no controlled prompts, complete transcripts, acceptance scores, or results from the proposed restart. The research memo contains concrete analysis, so “unusable” is an operator-specific judgment rather than proof of empty output. Narrow roles can also increase handoff, integration, duplicated context, and coordination costs. Complex architecture, safety-critical action, organizational commitments, and irreversible operations may need substantial planning before any artifact is produced. The useful claim is therefore about sequencing validation before institutionalization, not eliminating plans, documentation, broad synthesis, or scheduled work.

## What Changed
- Created the concept from Mai Yang's Growth Researcher retrospective and Lauren Tan's optional-planning position.

## Related Concepts
- [[TaskContingentAICollaboration]] - routes delegation by clarity, risk, reversibility, and acceptance criteria.
- [[AIWorkflowDesign]] - turns accepted work into traceable, repeatable task sequences.
- [[ActionBiasInAI]] - prevents planning artifacts from substituting for feedback-producing work.
- [[AgentTeam]] - role specialization should follow a demonstrated division of work rather than imitate an organization chart prematurely.
- [[AgentPermissionModel]] - staged authority is the safety counterpart to staged workflow automation.
- [[IterativeProductShipping]] - both use concrete output and review to refine the next cycle.
