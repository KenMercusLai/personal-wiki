---
title: "Effect Log"
type: concept
tags: [ai, agents, reliability, side-effects]
sources:
  - wei-shen-me-xian-you-de-agent-infra-wu-fa-zhi-cheng-sheng-chan-ji-ying-yong
last_updated: 2026-09-12
knowledge_schema: synthesis-v1
---

## Definition
[[EffectLog]] is a write-ahead log for agent tool calls that records intended and completed external side effects so recovery can continue without repeating irreversible operations.

## Current Synthesis
The source treats the effect log as the foundation for production agent infrastructure. Before a side-effecting tool call executes, the system records intent, including idempotency keys, expected scope, and approval level. After execution, it records completion data such as request, response, version fingerprints, and whether the operation became irreversible. Recovery then follows the recorded semantic class of the tool call rather than blindly rerunning the agent's prior steps.

## Key Claims
- Side-effecting tool calls need durable records before and after execution.
- Reads, idempotent writes, irreversible writes, and mixed read/write calls need different recovery rules.
- Irreversible effects should never be replayed during recovery.
- Mixed read/write tools are dangerous because rereading external state can produce divergent logic after a crash.
- Tool developers should declare recovery semantics as an interface contract.
- Conservative classification is safer when a tool is partly idempotent but also irreversible.

## Evidence
- Write-ahead framing: [[wei-shen-me-xian-you-de-agent-infra-wu-fa-zhi-cheng-sheng-chan-ji-ying-yong]] compares side-effect recording to write-ahead logging for the external world.
- Intent and completion records: [[wei-shen-me-xian-you-de-agent-infra-wu-fa-zhi-cheng-sheng-chan-ji-ying-yong]] describes intent records with idempotency keys and completion records with responses and irreversible-state markers.
- Recovery classification: [[wei-shen-me-xian-you-de-agent-infra-wu-fa-zhi-cheng-sheng-chan-ji-ying-yong]] separates pure reads, idempotent writes, irreversible writes, and mixed read/write calls.
- Conservative rule: [[wei-shen-me-xian-you-de-agent-infra-wu-fa-zhi-cheng-sheng-chan-ji-ying-yong]] uses a refund-like call to argue that any irreversible dimension should make recovery return the sealed result instead of replaying the operation.

## Counterevidence & Qualifications
The source presents the effect log as a proposed primitive, not an implemented standard. It also acknowledges integration friction because existing tools may not expose clean semantic classifications, leaving room for future intelligent semantic annotation but no proven ecosystem-wide solution.

## What Changed
- Created the concept page for effect logs as the base recovery primitive for agent side effects.

## Related Concepts
- [[ProductionAgentInfrastructure]] - effect logs are the first primitive in the proposed infrastructure stack.
- [[AgentResumability]] - resumability depends on knowing which effects already happened.
- [[ForkRecovery]] - fork checkpoints include the effect-log cursor.
- [[CapabilityGateway]] - gateways enforce tool-call contracts declared for effect logging.
- [[SoftwareVerification]] - effect logs provide runtime evidence of actual behavior, complementing tests.
- [[SemanticIsolation]] - effect logs isolate side-effect facts from model nondeterminism.
