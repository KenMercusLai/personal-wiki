---
title: "Verification-Driven Agent Delegation"
type: concept
tags: [ai, agents, verification, software-engineering]
sources:
  - lauren-tan-handing-work-to-agents
last_updated: 2026-10-25
knowledge_schema: synthesis-v1
---

## Definition
[[VerificationDrivenAgentDelegation]] is the practice of expanding an agent's concurrency and autonomy only as executable evidence and enforceable system constraints make its output trustworthy.

## Current Synthesis
The source frames agent adoption as a trust curve rather than a race to spawn more workers. Early use stays supervised because an operator lacks evidence that unattended work will be correct. Scale becomes plausible when the environment can expose failure and steer correction without depending on continuous human attention.

The strongest controls change the work surface itself: clear architecture, strong types, invariants, and boundaries make the easiest implementation path more likely to be the correct one. Static analysis, tests, CI, traces, screenshots, and other executable checks then convert behavior into feedback an agent can use. Written rules and Skills remain useful for procedures that cannot be enforced mechanically, while human review is reserved for ambiguity and judgment because it scales least well.

This makes intervention diagnostic. A repeated correction signals a missing invariant, check, tool, or workflow rather than merely a prompt that should be restated. The operator first walks the task manually, defines observable success, gives the agent a way to verify it, and increases parallelism only after the loop repeatedly works.

## Key Claims
- Agent count should follow demonstrated trust in outputs rather than serve as the starting measure of progress.
- Verification is the limiting resource when generation becomes cheap and fast.
- Architecture, types, invariants, and boundaries are stronger controls than prose because they constrain available actions.
- Executable checks let agents detect and correct some failures without waiting for a person.
- Repeated human corrections should be promoted into system-level constraints whenever practical.
- Human review remains necessary for judgment but should not be the only quality gate at machine production rates.

## Evidence
- Trust before scale: [[lauren-tan-handing-work-to-agents]] reports Tan's warning that jumping from a few supervised agents to one hundred untrusted agents produces low-quality PRs, regressions, and bugs.
- Control hierarchy: [[lauren-tan-handing-work-to-agents]] orders investment from codebase architecture and invariants through static analysis and prose to scarce human review.
- Executable feedback: [[lauren-tan-handing-work-to-agents]] describes verification Skills that run an application, collect performance traces, find hotspots, and iterate on improvements.
- Learning from intervention: [[lauren-tan-handing-work-to-agents]] relays Tan's advice to eliminate recurring corrections and describes the codebase as externalized memory.
- Manual-to-automated path: [[lauren-tan-handing-work-to-agents]] recommends first performing an annoying workflow manually, then defining validation and automating the known process.

## Counterevidence & Qualifications
The concept currently rests on one secondary practitioner profile. The source reports high PR volume without output-size, defect, rollback, review-effort, or comparative productivity data, and it does not establish thresholds for safe autonomy. Enforceable controls can encode known failure modes but cannot eliminate specification errors, correlated test blind spots, security failures, or novel product judgments. Human review may therefore remain dominant for irreversible, safety-critical, regulated, or poorly specified work even when automated verification is strong.

## What Changed
- Created the concept from a reported progression from supervised agent use to verification-backed delegation.

## Related Concepts
- [[SoftwareVerification]] - supplies executable behavioral evidence for accepting or rejecting agent work.
- [[AICodingPractice]] - applies the method to codebase design, task execution, and review habits.
- [[LLMToolingSkills]] - packages repeatable verification procedures that an agent can invoke.
- [[AgentPermissionModel]] - limits autonomy according to evidence, scope, and consequence.
- [[BottleneckAwareAICoding]] - explains why faster generation merely moves the constraint to verification and review.
- [[HarnessEngineering]] - provides tools, context, checks, and feedback loops that make delegation reliable.
