---
title: "Introductory bullshit detection for non-technical managers"
type: source
tags: [engineering-management, software-projects, decision-making, delivery-risk]
date: 2017-06-10
source_file: "/mnt/ken_personal_wiki/Articles/Introductory bullshit detection for non-technical managers.md"
---

## Summary
This practitioner checklist argues that managers do not need implementation-level expertise to govern technical work, but do need plain-language answers about the user problem, operating constraints, value ceiling, alternatives, dependencies, maintenance burden, verification, and failure behavior. It extends [[TechnicalDecisionReview]] from one proposed change to project selection and continuing delivery confidence, while drawing a boundary around [[SoftwareEstimation]]: managers should fund an outcome within an explicit value budget and inspect evidence, rather than direct work through task breakdowns and task-duration demands.

## Key Claims
- A manager should stop a proposal that cannot identify a concrete user problem, one practical example, a representative user, and the actual platform, memory, and performance constraints.
- Claims of genericity, platform independence, future-proofing, frameworks, or refactoring should trigger requests for problem-specific benefit and evidence rather than automatic approval or rejection.
- Management owns the value judgment: decide what solving the problem is worth, stop when cost crosses that ceiling, and ask what new capability, lower cost, or higher end-user quality will result.
- Cost review should include previous art, build-versus-buy options, prototypes or simulations, dependencies, fallback plans, displaced work, prerequisites, planned lifetime, and long-run maintenance.
- Independent verification and demonstrations of off-script failure provide stronger progress evidence than scripted success demonstrations alone.
- The proposed “80/50 rule” treats a project as behind unless a shippable version exists after half its resources are consumed, but the article supplies no empirical validation for that threshold.
- Managers should govern the why, value, cost, constraints, and confidence boundary while leaving implementation task decomposition and task-duration estimation to the experts doing the work.

## Key Quotes
> “What problem are you actually trying to solve?” - the first gate before a project proceeds.

> “What’s Plan B if this doesn’t work?” - a test of whether the team is attached to one solution rather than the underlying outcome.

> “Can you demonstrate a failure?” - a request to expose off-script behavior rather than only the rehearsed success path.

## Connections
- [[TechnicalDecisionReview]] - the checklist broadens structured technical inquiry to user need, constraints, value, lifecycle cost, independent verification, fallback paths, and delivery confidence.
- [[SoftwareEstimation]] - the article rejects manager-led task-duration interrogation but remains compatible with engineer-led estimates used as uncertain planning inputs.
- [[OpportunityCost]] - the cost of a project includes the valuable work that scarce engineering capacity cannot do instead.
- [[TechnicalDebtTracking]] - refactoring can address real liabilities, but its benefit and priority still need to be stated in project terms.
- [[DeveloperCustomerExposure]] - a named representative user can verify expectations and keep technical work connected to concrete needs.
- [[ChangeSafety]] - fallback paths, visible failures, and verification reduce the consequences of a solution that behaves unexpectedly.

## Contradictions
- The article directly warns managers not to ask for specific task breakdowns or task-duration estimates, while [[SoftwareEstimation]] contains practitioner advice that decomposition and codebase-informed peer review improve schedule discussion. The claims can coexist if engineers own decomposition and managers use estimates as uncertain resource-allocation evidence rather than directing unfamiliar implementation work or treating estimates as promises.
- The claim that memory access is the most common bottleneck and that maintenance overwhelmingly dominates development cost may fit many systems but is asserted without workload data, lifecycle accounting, or domain boundaries.
- The “80/50 rule” is a forceful delivery heuristic, not a measured forecasting law. Some projects have front-loaded research, infrastructure, compliance, integration, migration, or hardware work that cannot yield a responsibly shippable system at the halfway point.
- Plain-language explanation improves managerial scrutiny but does not prove that an answer is complete or correct, and it cannot replace specialist architecture, security, safety, accessibility, legal, operational, or domain review.
- All three local images were opened. They are duplicate crops of the handwritten article title and add no evidence beyond the prose, so none was retained and no asset manifest was created.
