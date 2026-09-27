---
title: "Technical Decision Review"
type: concept
tags: [software-engineering, decision-making, technical-leadership, reliability]
sources:
  - five-questions
last_updated: 2026-09-28
knowledge_schema: synthesis-v1
---

## Definition
[[TechnicalDecisionReview]] is a structured inquiry that tests a technical plan's purpose, failure modes, detection signals, response options, and reversibility before a team commits to it.

## Current Synthesis
The five-question protocol begins with intent: what the team is doing, why it is necessary, how the proposed mechanism solves the understood problem, and whether extra scope adds avoidable risk. It then treats failure analysis as a way to expose assumptions and stakes rather than an attempt to predict everything.

Detection and response make the review operational. A new project needs near-term milestones and check-ins that reveal whether it is off track; a migration, service change, or bug fix needs manual or automated signals that show whether the new state is worse than expected. Depending on customers to report the first symptoms is a dangerous default. The team should also discuss its response, even when the exact failure is unknowable, because a difficult revert or an approaching point of no return changes the decision.

The final test is reversibility. An escape hatch is not mandatory in every case, but its presence, cost, and feasibility should be explicit before proceeding. The framework therefore lets a technical leader contribute without pretending to possess every specialist detail: the leader's work is to ask, understand, judge, and translate answers into action.

## Key Claims
- A technical plan should connect a necessary, clearly articulated problem to an explainable solution without avoidable scope.
- Failure-mode questions reveal assumptions, worst cases, and decision stakes even when exhaustive prediction is impossible.
- Monitoring, manual checks, milestones, and check-ins should reveal deterioration before customer complaints become the primary signal.
- Discussing failure response exposes recovery difficulty and the point at which changing course becomes prohibitively expensive.
- Reversibility is a risk variable: lacking an undo path may be acceptable, but it should raise the evidence and confidence required to proceed.
- Structured questions let leaders exercise judgment in unfamiliar systems without substituting general inquiry for specialist knowledge.

## Evidence
- Purpose and scope: [[five-questions]] asks reviewers to test whether the problem and solution are clearly explained, the work is necessary, and the proposal solves more than the problem requires.
- Failure assumptions: [[five-questions]] asks for plausible, far-fetched, and worst-case failure scenarios so reviewers can probe assumptions without trying to plan for every event.
- Detection: [[five-questions]] maps new projects to milestones and check-ins, and service or migration changes to manual or automated monitoring rather than customer-reported discovery.
- Response boundary: [[five-questions]] uses difficult reversion and the project point of no return to make the stakes of proceeding visible.
- Reversibility: [[five-questions]] asks whether an escape hatch exists and whether it is cheaper to build now than later, while allowing that a plan may rationally proceed without one.
- Leadership under unfamiliarity: [[five-questions]] presents asking, understanding, and converting answers into action as a substantive development-lead contribution alongside technical navigation skill.

## Counterevidence & Qualifications
The evidence is one development lead's practitioner reflection rather than a comparative study of decision quality. The five questions can expose weak reasoning, but they do not replace architecture analysis, domain expertise, security or compliance review, testing, quantitative risk estimation, or accountable decision ownership. Answers can also sound complete while remaining wrong, and some failures emerge only in production or after irreversible state change. An “undo” may revert code without restoring data, clients, dependent systems, or operational state, so reversibility must be defined at the relevant system boundary.

## What Changed
- Created a unified review protocol connecting problem clarity, failure analysis, detection, response, and reversibility.
- Framed technical leadership under unfamiliarity as structured inquiry plus action, not simulated expertise.

## Related Concepts
- [[UnderstandDesignBuild]] - problem and solution clarity are the first gate before implementation.
- [[PrematureImplementation]] - review reduces the risk of committing to work before the problem is understood.
- [[UnknownUnknowns]] - failure analysis probes assumptions without claiming exhaustive foresight.
- [[ServiceObservability]] - monitoring and user-impact signals make deterioration detectable.
- [[ChangeSafety]] - staged change, escape hatches, and recovery boundaries reduce the stakes of a wrong decision.
- [[TechnicalLeadershipRoleDesign]] - structured review is one way a lead contributes across systems beyond their deepest expertise.
- [[ArchitectureDecisionRecords]] - records can preserve the rationale, risks, and response assumptions exposed by review.
