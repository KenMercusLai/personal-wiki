---
title: "Architecture Advisory Forum"
type: concept
tags: [software-architecture, governance, organizational-learning, meetings]
sources:
  - blog-andrew-harmel-law-martinfowler-com-scaling-the-practice-of-architecture-conversationally
last_updated: 2026-09-25
knowledge_schema: synthesis-v1
---

## Definition
An [[ArchitectureAdvisoryForum]] is an open, recurring cross-team conversation where decision originators present emerging work and proposed [[ArchitectureDecisionRecords]], receive advice, revisit decisions, and share technical signals without surrendering decision ownership to a review board.

## Current Synthesis
The forum is designed to reduce the search and coordination cost of the [[AdviceProcess]]. A typical weekly session brings team delegates together with relevant experts and affected functions, while keeping attendance open. The agenda can include new spikes, proposed ADRs, timeboxed status reviews, delivery metrics, cloud-spend trends, and other emerging issues.

Its defining boundary is advisory authority. The originator still makes the decision; participants offer advice or identify additional people to consult. This distinguishes the forum from an architecture review board whose approval is required. Moving some advice into a shared setting also turns individual conversations into organizational learning about domain history, legacy constraints, operations, product, and architectural judgment.

The meeting's existence is not proof of participation. Its health depends on breadth and diversity of voices, the timing and quality of conversations, safety around disagreement and changed decisions, and active attention to who is silent or repeatedly dominant.

## Key Claims
- A recurring open forum makes affected parties and expertise easier for decision-takers to reach.
- Decision originators retain authority; the group advises rather than approves.
- Proposed ADRs and early spikes focus discussion before implementation hardens a choice.
- Shared conversations distribute context and architectural skill beyond one-to-one consultations.
- Revisiting statuses and celebrating changed decisions can normalize learning from imperfect information.
- Participation quality and diversity matter more than attendance or meeting cadence alone.

## Evidence
- Format: [[blog-andrew-harmel-law-martinfowler-com-scaling-the-practice-of-architecture-conversationally]] describes a weekly, hour-long, open forum with delegates and advice-checklist representatives.
- Agenda: [[blog-andrew-harmel-law-martinfowler-com-scaling-the-practice-of-architecture-conversationally]] lists spikes, proposed decisions, status reviews, metrics, spend, and other business.
- Authority boundary: [[blog-andrew-harmel-law-martinfowler-com-scaling-the-practice-of-architecture-conversationally]] says attendees can advise or suggest consultees but the originator owns the decision.
- Learning effect: [[blog-andrew-harmel-law-martinfowler-com-scaling-the-practice-of-architecture-conversationally]] reports that the shared audience spreads organizational, domain, legacy, and experiential knowledge.

## Counterevidence & Qualifications
The claimed engagement and learning effects come from the author's experience and are not independently measured. An open invitation does not guarantee access, safety, attention, or equal influence. The forum can become an approval board in practice even without formal veto power, or a costly status meeting if ADRs are unprepared and relevant advisors do not attend. Some early or sensitive decisions still require targeted conversations outside the group.

## What Changed
- Created the concept from the article's weekly advisory-forum design and failure conditions.

## Related Concepts
- [[AdviceProcess]] - defines who should be consulted and preserves originator decision rights.
- [[ArchitectureDecisionRecords]] - supply prepared decision material and capture resulting advice.
- [[DecentralizedArchitectureGovernance]] - uses the forum as its shared conversational infrastructure.
- [[ScalingCommunication]] - the forum broadcasts context and learning across team boundaries.
- [[PsychologicalSafety]] - supports dissent, uncertainty, and visible decision reversal.
