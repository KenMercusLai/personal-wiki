---
title: "Decentralized Architecture Governance"
type: concept
tags: [software-architecture, governance, team-autonomy, organizational-learning]
sources:
  - blog-andrew-harmel-law-martinfowler-com-scaling-the-practice-of-architecture-conversationally
last_updated: 2026-09-25
knowledge_schema: synthesis-v1
---

## Definition
[[DecentralizedArchitectureGovernance]] is an operating model that distributes architectural decisions to the people doing the work while using mandatory advice, visible records, recurring conversations, shared principles, and landscape sensing to preserve coherence and learning.

## Current Synthesis
The model replaces a permanent central decision-maker with many accountable decision centers. Its core [[AdviceProcess]] lets anyone decide after consulting affected people and relevant experts; the decision-taker must hear and record advice but need not obtain consensus. This keeps ownership close to implementation while exposing the decision to wider context and dissent.

Four practices provide supporting structure. [[ArchitectureDecisionRecords]] make the reasoning and advice durable; an [[ArchitectureAdvisoryForum]] creates an open, recurring venue for discussion; team-sourced principles provide shared direction; and a locally maintained [[TechnologyRadar]] maps current and emerging technical choices. Their value lies in mutual reinforcement rather than independent adoption.

The architect remains necessary, but as a steward of conditions rather than a shadow approver. The job is to help the right conversations occur, broaden participation, make learning safe, and notice when local decisions threaten coherence. Technical strategy and cross-functional requirements remain necessary external context, not outputs fully supplied by this model.

## Key Claims
- Decision authority can remain local when consultation and accountability are mandatory.
- Coherence emerges from linked social and documentary mechanisms rather than a central approval queue alone.
- Conversation matters because implemented architecture reflects developers' shared understanding, not only formal diagrams.
- Small, visible failures can accelerate collective learning when decisions are revisitable and psychologically safe.
- Architects add value by enabling, connecting, and guiding conversations without covertly retaking control.
- Participation breadth is an operating requirement because a nominally open process can still concentrate influence among usual suspects.

## Evidence
- Core decision model: [[blog-andrew-harmel-law-martinfowler-com-scaling-the-practice-of-architecture-conversationally]] gives decision rights to anyone who first consults affected people and relevant experts.
- Supporting system: [[blog-andrew-harmel-law-martinfowler-com-scaling-the-practice-of-architecture-conversationally]] links ADRs, an advisory forum, principles, and a local radar around the Advice Process.
- Learning mechanism: [[blog-andrew-harmel-law-martinfowler-com-scaling-the-practice-of-architecture-conversationally]] describes visible decisions, dissent, reversals, and small failures as decision lore for less experienced practitioners.
- Failure modes: [[blog-andrew-harmel-law-martinfowler-com-scaling-the-practice-of-architecture-conversationally]] warns against narrow participation, punishment of off-grid decisions, mistrust, and shadow architecture.

## Counterevidence & Qualifications
The evidence is a practitioner's repeated experience, not a controlled comparison or a measured longitudinal study. Open invitations do not guarantee equitable influence, and mandatory consultation can become slow or ceremonial if affected parties are numerous, incentives are weak, or power differences suppress dissent. The approach also assumes enough trust and skill for teams to hold decision ownership. It references technical strategy and testable cross-functional requirements as necessary context but does not explain how to produce them.

## What Changed
- Created the concept from Harmel-Law's five-element conversational architecture model.

## Related Concepts
- [[AdviceProcess]] - supplies the model's decentralized decision rule.
- [[ArchitectureDecisionRecords]] - make reasoning, advice, and revision history inspectable.
- [[ArchitectureAdvisoryForum]] - scales advice and learning through recurring open conversation.
- [[SystemArchitecturePrinciples]] - provide shared criteria for aligned local decisions.
- [[TechnologyRadar]] - provides collective awareness of the local technical landscape.
- [[ArchitectureAlignmentForces]] - explains why decision process and formality should reflect social distance and blast radius.
