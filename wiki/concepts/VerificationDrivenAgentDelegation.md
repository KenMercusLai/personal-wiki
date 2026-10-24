---
title: "Verification-Driven Agent Delegation"
type: concept
tags: [ai, agents, verification, software-engineering]
sources:
  - lauren-tan-handing-work-to-agents
  - hundreds-of-prs-a-day-nine-work-lines
last_updated: 2026-10-25
knowledge_schema: synthesis-v1
---

## Definition
[[VerificationDrivenAgentDelegation]] is the practice of expanding an agent's concurrency and autonomy only as executable evidence and enforceable system constraints make its output trustworthy.

## Current Synthesis
The source frames agent adoption as a trust curve rather than a race to spawn more workers. Early use stays supervised because an operator lacks evidence that unattended work will be correct. Scale becomes plausible when the environment can expose failure and steer correction without depending on continuous human attention.

The strongest controls change the work surface itself: clear architecture, strong types, invariants, and boundaries make the easiest implementation path more likely to be the correct one. Static analysis, tests, CI, traces, screenshots, and other executable checks then convert behavior into feedback an agent can use. Written rules and Skills remain useful for procedures that cannot be enforced mechanically, while human review is reserved for ambiguity and judgment because it scales least well.

This makes intervention diagnostic. A repeated correction signals a missing invariant, check, tool, or workflow rather than merely a prompt that should be restated. The operator first walks the task manually, defines observable success, gives the agent a way to verify it, and increases parallelism only after the loop repeatedly works.

Risk routing and demand add operating constraints. Tan reportedly subjects every pull request to agentic review and risk assessment, automatically merges low- and medium-risk work, and retains human review for higher-risk cases. Jacob Gold's reported prompt-to-diff check similarly escalates any possible mismatch between requested intent and the change. These mechanisms make human supervision exception-based, but trustworthy throughput still depends on real bugs, features, and performance needs; verification can screen work without making unnecessary work valuable.

## Key Claims
- Agent count should follow demonstrated trust in outputs rather than serve as the starting measure of progress.
- Verification is the limiting resource when generation becomes cheap and fast.
- Architecture, types, invariants, and boundaries are stronger controls than prose because they constrain available actions.
- Executable checks let agents detect and correct some failures without waiting for a person.
- Repeated human corrections should be promoted into system-level constraints whenever practical.
- Human review remains necessary for judgment but should not be the only quality gate at machine production rates.
- Risk classification and intent checks can route routine work automatically while escalating uncertain or consequential changes.

## Evidence
- Trust before scale: [[lauren-tan-handing-work-to-agents]] reports Tan's warning that jumping from a few supervised agents to one hundred untrusted agents produces low-quality PRs, regressions, and bugs.
- Control hierarchy: [[lauren-tan-handing-work-to-agents]] orders investment from codebase architecture and invariants through static analysis and prose to scarce human review.
- Executable feedback: [[lauren-tan-handing-work-to-agents]] describes verification Skills that run an application, collect performance traces, find hotspots, and iterate on improvements.
- Learning from intervention: [[lauren-tan-handing-work-to-agents]] relays Tan's advice to eliminate recurring corrections and describes the codebase as externalized memory.
- Manual-to-automated path: [[lauren-tan-handing-work-to-agents]] recommends first performing an annoying workflow manually, then defining validation and automating the known process.
- Risk routing: [[hundreds-of-prs-a-day-nine-work-lines]] reports agentic review and risk assessment on every Tan pull request, with low- and medium-risk changes merging without human review.
- Intent validation: [[hundreds-of-prs-a-day-nine-work-lines]] says Jacob Gold compares pull-request changes with all prompts for the task and escalates any possible mismatch for a human decision.
- Demand boundary: [[hundreds-of-prs-a-day-nine-work-lines]] argues that user bugs, features, and performance needs make volume meaningful, while output created only to raise a count does not.

## Counterevidence & Qualifications
The concept rests on two secondary practitioner accounts by the same author. They report high PR volume and review mechanisms without output-size, defect, rollback, classifier-accuracy, false-negative, review-effort, token-cost, or comparative productivity data, and they do not establish thresholds for safe autonomy. A prompt-to-diff match also cannot prove that the prompt was correct or complete. Enforceable controls can encode known failure modes but cannot eliminate specification errors, correlated test blind spots, security failures, or novel product judgments. Human review may therefore remain dominant for irreversible, safety-critical, regulated, or poorly specified work even when automated verification is strong.

## What Changed
- Added risk-tiered review and prompt-to-diff intent checking as concrete exception-routing mechanisms.
- Added real demand as a separate prerequisite: verified output can still be unnecessary output.

## Related Concepts
- [[SoftwareVerification]] - supplies executable behavioral evidence for accepting or rejecting agent work.
- [[AICodingPractice]] - applies the method to codebase design, task execution, and review habits.
- [[LLMToolingSkills]] - packages repeatable verification procedures that an agent can invoke.
- [[AgentPermissionModel]] - limits autonomy according to evidence, scope, and consequence.
- [[BottleneckAwareAICoding]] - explains why faster generation merely moves the constraint to verification and review.
- [[HarnessEngineering]] - provides tools, context, checks, and feedback loops that make delegation reliable.
