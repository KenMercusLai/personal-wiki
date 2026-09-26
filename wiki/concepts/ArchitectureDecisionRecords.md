---
title: "Architecture Decision Records"
type: concept
tags: [software-architecture, decision-making, documentation, organizational-learning]
sources:
  - blog-andrew-harmel-law-martinfowler-com-scaling-the-practice-of-architecture-conversationally
  - blog-martinfowler-com-building-infrastructure-platforms
last_updated: 2026-09-25
knowledge_schema: synthesis-v1
---

## Definition
[[ArchitectureDecisionRecords]] are lightweight, versioned documents that preserve an architectural decision's context, considered options, consequences, status, and consulted advice close to the artifacts the decision affects.

## Current Synthesis
In the conversational governance model, an ADR is both a record and a thinking scaffold. Its fields prompt a decision-taker to clarify the need, compare alternatives, identify consequences, seek advice, and explain how dissent changed or failed to change the conclusion. Starting the record while the problem is still vague turns documentation into part of discovery rather than retrospective justification.

A collection of ADRs becomes organizational decision memory. Less experienced practitioners can inspect accepted, superseded, retired, and reversed choices, including compromises and incomplete information. Because decisions are point-in-time judgments, preserved context and criteria allow later reviewers to ask whether the original reasoning was sound given what was then known.

ADRs gain force from their connections to the rest of [[DecentralizedArchitectureGovernance]]. They enter discussion at the [[ArchitectureAdvisoryForum]], note relevant principles and radar blips, and preserve the advice required by the [[AdviceProcess]].

C4 diagrams and ADRs play complementary communication roles. Diagrams show a platform's present or intended structure at several levels, while ADRs preserve the architectural past: what was decided, when, in what context, with which consequences and participants. Keeping them in platform repositories makes decision memory available during later maintenance and incident investigation.

## Key Claims
- A lightweight template can improve decision thinking before it preserves the outcome.
- Context, options, consequences, status, and advice are the essential fields in this model.
- Advice should be recorded and actively addressed even when the decision-taker rejects it.
- Decision histories expose dissent, compromise, revision, and failure as reusable learning material.
- Preserving original context enables fairer hindsight review of point-in-time decisions.
- ADRs are most useful when integrated with conversation and governance practices rather than treated as archival paperwork.
- ADRs complement structural diagrams by preserving why a platform became the system now shown.

## Evidence
- Template: [[blog-andrew-harmel-law-martinfowler-com-scaling-the-practice-of-architecture-conversationally]] specifies title, status, decision, context, options, consequences, and advice.
- Thinking aid: [[blog-andrew-harmel-law-martinfowler-com-scaling-the-practice-of-architecture-conversationally]] says the fields act as a checklist for reasoning and conversation.
- Advice accountability: [[blog-andrew-harmel-law-martinfowler-com-scaling-the-practice-of-architecture-conversationally]] requires named, dated advice and encourages authors to engage with it in the options analysis.
- Learning history: [[blog-andrew-harmel-law-martinfowler-com-scaling-the-practice-of-architecture-conversationally]] describes ADR series as open decision lore showing both good and poor choices and later reversals.
- Platform memory: [[blog-martinfowler-com-building-infrastructure-platforms]] contrasts C4 views of architectural present or future with ADRs documenting past choices and their surrounding ecosystem.
- Minimal record: [[blog-martinfowler-com-building-infrastructure-platforms]] lists title, date, status, context, decision, consequences, and participants as a practical platform-repository format.

## Counterevidence & Qualifications
Both articles offer practitioner experience rather than evidence that a specific ADR template improves decision quality. Records can become stale, performative, or written after the fact, and visible text cannot guarantee that meaningful dissent was invited. The sources also assume lightweight records; documentation overhead that exceeds the decision's scope would undermine the model's speed and autonomy goals. Naming participants can improve transparency but must not be misused as blame attribution during an incident.

## What Changed
- Added ADRs as the historical complement to C4 views of a platform's present and future structure.
- Added the smaller platform-repository template and its maintenance and incident-investigation role.

## Related Concepts
- [[AdviceProcess]] - supplies the advice that ADRs must preserve and address.
- [[ArchitectureAdvisoryForum]] - uses proposed ADRs to focus collective discussion.
- [[DecentralizedArchitectureGovernance]] - gives ADRs their role in a broader decision system.
- [[SystemArchitecturePrinciples]] - provide evaluation criteria and deviations that ADRs can make explicit.
- [[TechnologyRadar]] - provides landscape context and records technology movements implied by a decision.
- [[InfrastructurePlatformProductManagement]] - uses ADRs to keep technical intent legible as the platform evolves.
