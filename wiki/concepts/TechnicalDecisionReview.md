---
title: "Technical Decision Review"
type: concept
tags: [software-engineering, decision-making, technical-leadership, reliability]
sources:
  - five-questions
  - introductory-bullshit-detection-for-non-technical-managers
last_updated: 2026-09-30
knowledge_schema: synthesis-v1
---

## Definition
[[TechnicalDecisionReview]] is structured inquiry that lets accountable leaders test a technical plan's user problem, constraints, value, evidence, failure behavior, response options, and reversibility without pretending to possess the implementing team's specialist knowledge.

## Current Synthesis
Both sources begin with intent: what the team is doing, why it is necessary, whose concrete problem it solves, and whether the mechanism or extra scope adds avoidable risk. The broader managerial checklist adds an explicit operating envelope - supported platforms, memory and performance bounds, dependencies, prerequisites, representative users, and measurable examples - and treats vague claims of genericity, independence, future-proofing, or framework value as prompts for clarification rather than proof of merit.

The review also joins technical plausibility to economic judgment. Management sets how much the outcome is worth, asks what capability, cost, or end-user quality will improve, and compares the proposal with previous art, an adequate partial solution, dependencies, maintenance, displaced work, expected lifetime, and a fallback plan. Prototypes, simulations, realistic data, independent QA, and off-script failure demonstrations provide evidence before and during commitment; they do not convert uncertain development into certainty.

Detection, response, and reversibility make the review operational. A new project needs milestones and check-ins that reveal whether it is off track; a migration, service change, or bug fix needs manual or automated signals before customer complaints become the first alert. The team should discuss recovery even when the exact failure is unknowable, because a difficult revert, weak Plan B, or approaching point of no return changes the decision. Leaders contribute by requiring understandable answers, judging value and risk, and translating evidence into action, not by breaking unfamiliar implementation into tasks.

## Key Claims
- A technical plan should connect a necessary, concrete user problem to an explainable solution and explicit operating constraints without avoidable scope.
- Approval should reflect an outcome's value ceiling, alternatives, opportunity cost, dependencies, maintenance burden, prerequisites, and expected lifetime rather than initial build effort alone.
- Prototypes, simulations, independent verification, milestones, monitoring, and off-script failure demonstrations make plausibility and deterioration more observable.
- Failure-mode and fallback questions reveal assumptions, recovery difficulty, worst cases, and decision stakes without claiming exhaustive prediction.
- Reversibility is a risk variable: lacking an undo path may be acceptable, but it should raise the evidence and confidence required to proceed.
- Structured questions let leaders exercise judgment in unfamiliar systems without substituting plain-language inquiry for specialist review or manager-led implementation design.

## Evidence
- Purpose and scope: [[five-questions]] asks reviewers to test whether the problem and solution are clearly explained, the work is necessary, and the proposal solves more than the problem requires.
- User and constraint definition: [[introductory-bullshit-detection-for-non-technical-managers]] asks for a concrete beneficiary and example plus enumerated platform, memory, and performance bounds.
- Value and lifecycle cost: [[introductory-bullshit-detection-for-non-technical-managers]] assigns management the value ceiling and asks about previous art, dependencies, displaced work, maintenance, prerequisites, and planned system lifetime.
- Failure assumptions: [[five-questions]] asks for plausible, far-fetched, and worst-case failure scenarios so reviewers can probe assumptions without trying to plan for every event.
- Evidence and detection: [[five-questions]] maps projects to milestones, check-ins, and monitoring; [[introductory-bullshit-detection-for-non-technical-managers]] adds prototypes or simulations, independent QA, and failure demonstrations.
- Response boundary: [[five-questions]] uses difficult reversion and the point of no return to expose stakes, while [[introductory-bullshit-detection-for-non-technical-managers]] asks for a fallback that can still meet a deadline.
- Reversibility: [[five-questions]] asks whether an escape hatch exists and whether it is cheaper to build now than later, while allowing that a plan may rationally proceed without one.
- Leadership under unfamiliarity: both [[five-questions]] and [[introductory-bullshit-detection-for-non-technical-managers]] present understandable inquiry and accountable judgment as substantive leadership while leaving specialist implementation to the team.

## Counterevidence & Qualifications
The evidence consists of two practitioner arguments rather than comparative studies of decision quality. Structured questions can expose weak reasoning, but understandable answers can still be wrong and cannot replace architecture analysis, domain expertise, security, safety, accessibility, compliance review, testing, quantitative risk estimation, or accountable ownership. The second source's claims that memory access is the most common bottleneck and maintenance overwhelmingly dominates build cost lack workload and lifecycle evidence. Its “80/50 rule” is an unvalidated heuristic that may misclassify front-loaded research, infrastructure, compliance, integration, migration, or hardware work. An “undo” may revert code without restoring data, clients, dependent systems, or operational state, so reversibility must be defined at the relevant system boundary.

## What Changed
- Expanded review from one technical change to user representation, operating constraints, value ceilings, alternatives, lifecycle cost, and displaced work.
- Added prototypes, independent verification, off-script failure demonstrations, and fallback plans as confidence evidence.
- Clarified that structured leadership inquiry does not authorize manager-led implementation decomposition or replace specialist review.

## Related Concepts
- [[UnderstandDesignBuild]] - problem and solution clarity are the first gate before implementation.
- [[PrematureImplementation]] - review reduces the risk of committing to work before the problem is understood.
- [[UnknownUnknowns]] - failure analysis probes assumptions without claiming exhaustive foresight.
- [[ServiceObservability]] - monitoring and user-impact signals make deterioration detectable.
- [[ChangeSafety]] - staged change, escape hatches, and recovery boundaries reduce the stakes of a wrong decision.
- [[TechnicalLeadershipRoleDesign]] - structured review is one way a lead contributes across systems beyond their deepest expertise.
- [[ArchitectureDecisionRecords]] - records can preserve the rationale, risks, and response assumptions exposed by review.
- [[SoftwareEstimation]] - delivery forecasts can inform value and sequencing when engineers own decomposition and uncertainty remains visible.
- [[OpportunityCost]] - approving one plan consumes resources unavailable to other valuable work.
- [[DeveloperCustomerExposure]] - representative users help verify that the stated problem and outcome match lived needs.
