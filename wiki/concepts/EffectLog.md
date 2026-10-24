---
title: "Effect Log"
type: concept
tags: [ai, agents, reliability, side-effects]
sources:
  - wei-shen-me-xian-you-de-agent-infra-wu-fa-zhi-cheng-sheng-chan-ji-ying-yong
  - deepchat-tape
last_updated: 2026-10-25
knowledge_schema: synthesis-v1
---

## Definition
[[EffectLog]] is a write-ahead record for agent tool calls that durably separates intent or dispatch commitment from observed outcome so recovery can avoid guessing whether an external side effect is safe to repeat.

## Current Synthesis
The infrastructure proposal treats the effect log as a foundation for production agents. Before a side-effecting tool call executes, the system should record intent, including idempotency keys, expected scope, and approval level. After execution, it should record completion data such as request, response, version fingerprints, and whether the operation became irreversible. Recovery then follows the recorded semantic class of the call rather than blindly rerunning prior steps.

[[DeepChat]] supplies a narrower implementation called the Execution Journal. It writes `run_started` before a run, `dispatch_committed` after local permission, parameter, and cancellation checks but before actual tool invocation, `tool_outcome` after a result returns locally, and `run_terminal` at the run's final state. If durable dispatch recording fails, the tool is not invoked. If dispatch exists without an outcome after a crash, the system marks the call `indeterminate`, parks the run, and forbids automatic retry because local evidence cannot prove whether the external world changed. This provides honest observability and a conservative recovery boundary, not exactly-once execution.

## Key Claims
- Side-effecting tool calls need durable records before dispatch and after a result becomes locally observable.
- A failed write-ahead record must prevent the call from crossing the execution boundary.
- Reads, idempotent writes, irreversible writes, and mixed read/write calls need different recovery rules.
- Dispatch without outcome is evidence of uncertainty, not proof of failure or completion, so automatic retry may duplicate an external effect.
- Tool developers should declare recovery semantics and idempotency as interface contracts.
- Conservative classification is safer when a tool is partly idempotent, irreversible, or outside the agent runtime's transactional control.

## Evidence
- Write-ahead framing: [[wei-shen-me-xian-you-de-agent-infra-wu-fa-zhi-cheng-sheng-chan-ji-ying-yong]] compares side-effect recording to write-ahead logging for the external world.
- Intent and completion records: [[wei-shen-me-xian-you-de-agent-infra-wu-fa-zhi-cheng-sheng-chan-ji-ying-yong]] describes intent records with idempotency keys and completion records with responses and irreversible-state markers.
- Recovery classification: [[wei-shen-me-xian-you-de-agent-infra-wu-fa-zhi-cheng-sheng-chan-ji-ying-yong]] separates pure reads, idempotent writes, irreversible writes, and mixed read/write calls.
- Conservative rule: [[wei-shen-me-xian-you-de-agent-infra-wu-fa-zhi-cheng-sheng-chan-ji-ying-yong]] uses a refund-like call to argue that any irreversible dimension should make recovery return the sealed result instead of replaying the operation.
- Concrete lifecycle: [[deepchat-tape]] documents `run_started`, `dispatch_committed`, `tool_outcome`, and `run_terminal` as DeepChat's persisted execution states.
- Write-ahead gate: [[deepchat-tape]] says `dispatch_committed` must be persisted before tool invocation and that a failed journal write prevents execution.
- Crash classification: [[deepchat-tape]] separates `not_dispatched`, `completed`, `indeterminate`, and `corruption`; indeterminate runs are parked without automatic replay.

## Counterevidence & Qualifications
The infrastructure source presents a broad proposed primitive rather than an implemented standard, while DeepChat demonstrates only a narrower dispatch-and-outcome journal. A `dispatch_committed` record proves that local checks passed and execution was about to be attempted; it does not prove that the external service received or applied the call. Conversely, a missing outcome does not prove non-execution. The design therefore supports accurate uncertainty classification but not atomicity, exactly-once delivery, idempotency, rollback, or compensation. Existing tools may also lack clean semantic classifications, and neither source demonstrates an ecosystem-wide contract or crash-injection benchmark.

## What Changed
- Added DeepChat's concrete write-ahead Execution Journal lifecycle.
- Reframed dispatch-without-outcome as an explicit `indeterminate` state that blocks automatic retry.
- Distinguished reliable evidence and conservative recovery from exactly-once external effects.

## Related Concepts
- [[ProductionAgentInfrastructure]] - effect logs are the first primitive in the proposed infrastructure stack.
- [[AgentResumability]] - resumability depends on knowing which effects already happened.
- [[ForkRecovery]] - fork checkpoints include the effect-log cursor.
- [[CapabilityGateway]] - gateways enforce tool-call contracts declared for effect logging.
- [[SoftwareVerification]] - effect logs provide runtime evidence of actual behavior, complementing tests.
- [[SemanticIsolation]] - effect logs isolate side-effect facts from model nondeterminism.
- [[TapeAndAnchors]] - DeepChat stores execution-journal facts on the same append-only timeline as conversation and model-view evidence.
- [[DeepChat]] - implements dispatch and outcome journaling with explicit parked recovery for uncertain effects.
