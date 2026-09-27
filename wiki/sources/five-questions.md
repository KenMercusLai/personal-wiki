---
title: "Five Questions"
type: source
tags: [software-engineering, technical-leadership, decision-making, reliability]
date: 2015-10-08
source_file: "/mnt/ken_personal_wiki/Articles/Five Questions.md"
---

## Summary
An unnamed development lead presents five questions for evaluating technical plans in systems they do not yet understand deeply. The framework turns limited project-specific knowledge into disciplined [[TechnicalDecisionReview]] by clarifying purpose, probing failure modes, defining early warning signals, planning a response, and judging reversibility.

## Key Claims
- Technical leaders can contribute before they possess deep project-specific expertise by asking questions that expose a plan's reasoning, assumptions, risks, and recovery boundaries.
- A proposal should state both what will change and why, connect the solution to a clearly understood problem, and avoid unnecessary scope that adds risk.
- Asking how a plan could fail is useful for surfacing assumptions and stakes, not for attempting to predict or prevent every possible outcome.
- Teams should decide in advance how they will detect trouble through milestones, check-ins, manual checks, or automated monitoring rather than relying on customers as the first alert.
- A credible plan should describe what the team will do when trouble appears, including difficult recovery paths and the point after which changing course becomes prohibitively costly.
- Reversibility should be assessed explicitly: the absence of an undo mechanism may be acceptable, but it should change the threshold for proceeding.
- Technical leadership depends partly on asking, understanding, and translating answers into action rather than personally knowing every underlying technology in depth.

## Key Quotes
> "How will we know if it's going wrong?" - the question that connects a proposed plan to milestones, monitoring, and early intervention.

> "Is there an 'undo' button?" - the final test of whether the plan has an escape hatch and how its absence should affect the decision.

## Connections
- [[TechnicalDecisionReview]] - the article's five-question protocol for evaluating purpose, failure, detection, response, and reversibility.
- [[TechnicalLeadershipRoleDesign]] - a lead can add value through structured inquiry and judgment without being the deepest specialist in every technology.
- [[UnderstandDesignBuild]] - the first question tests whether the problem and proposed solution are understood before implementation proceeds.
- [[ServiceObservability]] - detection requires milestones, checks, monitoring, and user-impact signals before customers become the alerting system.
- [[ChangeSafety]] - response and reversibility questions expose rollback limits, escape hatches, and points of no return before a change is approved.
- [[UnknownUnknowns]] - failure-mode discussion probes assumptions while acknowledging that not every failure can be predicted.

## Contradictions
- Qualifies any reading of [[ChangeSafety]] that treats rollback as universally available: the article allows that some plans have no practical undo mechanism, but argues that this fact must raise the decision's stakes and be known before proceeding.
- The framework does not claim that general questions replace specialist review; it presents them as a way for a less project-familiar lead to understand the plan well enough to consent, object, and act.
