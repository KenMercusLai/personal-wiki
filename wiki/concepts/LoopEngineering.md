---
title: "Loop Engineering"
type: concept
tags: [ai, agents, software-engineering, automation]
sources:
  - loop-engineering-pi
last_updated: 2026-10-27
knowledge_schema: synthesis-v1
---

## Definition
[[LoopEngineering]] is the practice of designing a persistent control system that repeatedly discovers agent work, supplies context and tools, verifies outcomes, records state, and decides whether to continue, stop, or escalate.

## Current Synthesis
The pattern moves the human from manually writing and reviewing every prompt into designing the loop around the agent. Its control surface has distinct parts: a scheduler determines when work starts; inspection converts tests and operational signals into candidate work; durable repository state restores unfinished items and prior lessons; a goal defines completion; verifiers and role-separated review test the result; connectors permit real actions; and explicit stop, retry, and escalation rules bound execution.

The worked CI design shows why cadence and completion should remain separate. A scheduled run first reconciles fresh inspection evidence with durable state. If neither contains an actionable item, it records a no-op result and exits before creating a branch. If work exists, it selects one issue, follows gated planning and repair, runs the smallest relevant validation set, opens a merge request only with the required evidence, and updates the state file. Pi requires the scheduler to manage goal lifecycle explicitly because its loop plugin and goal extension do not automatically compose.

Loop engineering is therefore a selective investment, not a default for every agent task. Setup is most defensible when work recurs, success can be checked automatically, token and infrastructure costs are acceptable, and the agent has the same debugging and observability surfaces expected of a senior engineer. The recommended adoption path is incremental: make one manual run reliable, package its knowledge as a Skill, add one state file and one verification gate, then schedule it.

## Key Claims
- The primary design object is the control loop around model calls, not an isolated prompt.
- Scheduling cadence, goal completion, verification, durable state, and external action are distinct responsibilities that should be composed explicitly.
- Production telemetry can trigger and ground code work when it is reconciled with tests and persistent work state.
- Early exit, bounded retries, narrow change scope, and human escalation limit wasted work and unsafe autonomy.
- Repetition, automated verifiability, adequate budget, and production-grade tools are prerequisites for a loop to repay its setup cost.
- Maker-checker separation improves control but does not remove shared-evidence, specification, or correlated-model failure.

## Evidence
- System shift and components: [[loop-engineering-pi]] contrasts human-driven prompt/review cycles with automation, state, verification, Skills, connectors, and subagents surrounding an automatic agent cycle.
- Layered control: [[loop-engineering-pi]] separates token, turn, goal, meta, and open-exploration loops by exit condition and timescale, and distinguishes `/loop` cadence from `/goal` completion.
- Operational workflow: [[loop-engineering-pi]] combines lint, tests, E2E checks, metrics, logs, Sentry, `LOOP.md`, repair gates, branching, review, and merge-request creation in a recurring CI triage design.
- Bounded autonomy: [[loop-engineering-pi]] specifies a no-op gate, one-issue focus, retry caps, prohibited files and branches, validation evidence, pause conditions, and escalation to humans.
- Incremental adoption: [[loop-engineering-pi]] recommends proving a manual run before packaging it as a Skill and scheduling the loop.

## Counterevidence & Qualifications
The concept currently rests on one self-reported implementation and a screenshot of a completed no-op run. It lacks comparative performance, defect, cost, acceptance, security, and long-term maintenance data, and it does not demonstrate an autonomous repair reaching production. Verification can be incomplete or gamed; telemetry can be noisy; state files can preserve stale or unsafe instructions; and a separate judge can share the maker's model, context, and blind spots. Recurring autonomy also expands credential, supply-chain, branch, notification, and resource-consumption risks. One-off, ambiguous, irreversible, regulated, or judgment-heavy tasks may cost less and remain safer under direct human control.

## What Changed
- Established loop engineering as a distinct harness-level control discipline.
- Separated cadence, goal completion, durable state, verification, and escalation responsibilities.
- Added a concrete inspection-to-repair workflow and its early-exit gate.
- Recorded the four-condition suitability test and incremental adoption order.

## Related Concepts
- [[HarnessEngineering]] - provides the broader instructions, tools, runtime, state, and feedback environment in which a loop operates.
- [[AgenticWorkflowPatterns]] - supplies reusable routing, orchestration, evaluation, and feedback structures that loop engineering makes persistent.
- [[AgentResumability]] - durable files and goal records restore work across scheduled executions and context changes.
- [[VerificationDrivenAgentDelegation]] - executable evidence and escalation rules govern how much autonomy the loop receives.
- [[ServiceObservability]] - operational metrics, logs, and errors can initiate and qualify repair work.
- [[HumanAgencyInAI]] - humans remain responsible for objective choice, permissions, stop conditions, and acceptance of consequences.
