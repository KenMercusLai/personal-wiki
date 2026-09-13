---
title: "Production Agent Infrastructure"
type: concept
tags: [ai, agents, infrastructure, reliability, security]
sources:
  - wei-shen-me-xian-you-de-agent-infra-wu-fa-zhi-cheng-sheng-chan-ji-ying-yong
  - duo-agent-xie-zuo-ben-zhi-shi-fen-bu-shi-xi-tong-wen-ti-mo-xing-duo-qiang-ye-mei-yong
last_updated: 2026-09-13
knowledge_schema: synthesis-v1
---

## Definition
[[ProductionAgentInfrastructure]] is infrastructure designed to run long-lived, high-permission AI agents whose probabilistic decisions can create real external side effects.

## Current Synthesis
The source argues that production agents are not just LLM wrappers with tools. They combine long-running execution, hostile inputs, real credentials, nondeterministic model decisions, and irreversible side effects in one chain. Existing infrastructure usually handles only pieces of this problem: databases handle transactions, browsers sandbox hostile input, distributed systems checkpoint long-running work, containers isolate processes, and workflow engines replay deterministic tasks. Agent infrastructure needs a semantic layer that records effects, mediates capabilities, and resumes execution from precise checkpoints.

Multi-agent production systems also inherit consensus and liveness problems. Agents progress asynchronously, can hang inside tools, can kill their own process, and can continue from incompatible interpretations of an underspecified prompt. Production infrastructure therefore needs not only effect logs, capability gateways, and semantic recovery, but also coordination mechanisms, failure detection, and verification gates that decide when to retry, stop, or escalate.

## Key Claims
- Production agents differ from ordinary services because failure can occur after many state-changing decisions.
- The key risk is structural: long runtime, untrusted input, credentials, nondeterminism, and side effects interact.
- Durable side-effect records must exist before safe recovery is possible.
- Capability boundaries must be enforced by infrastructure rather than by model obedience.
- Recovery must preserve semantic correctness, not merely restart a process.
- Existing sandboxes and workflow engines can support agent systems but do not replace agent-specific primitives.
- Multi-agent agent infrastructure must handle consensus, failure detection, and liveness tradeoffs in addition to side effects and capabilities.

## Evidence
- Combined properties: [[wei-shen-me-xian-you-de-agent-infra-wu-fa-zhi-cheng-sheng-chan-ji-ying-yong]] lists long-running execution, hostile input, real permissions, uncertain decisions, and real side effects as the distinctive production-agent bundle.
- Missing guarantees: [[wei-shen-me-xian-you-de-agent-infra-wu-fa-zhi-cheng-sheng-chan-ji-ying-yong]] identifies absent side-effect logs, absent recoverable state, and absent isolation boundaries as the core infrastructure gaps.
- Primitive order: [[wei-shen-me-xian-you-de-agent-infra-wu-fa-zhi-cheng-sheng-chan-ji-ying-yong]] says side effects must be sealed before capability boundaries and recovery can be safely enforced.
- Existing-system limits: [[wei-shen-me-xian-you-de-agent-infra-wu-fa-zhi-cheng-sheng-chan-ji-ying-yong]] treats Kubernetes, Firecracker, gVisor, Modal, E2B, Temporal, and Conductor as useful at their own layers but outside agent semantic needs.
- Consensus and liveness: [[duo-agent-xie-zuo-ben-zhi-shi-fen-bu-shi-xi-tong-wen-ti-mo-xing-duo-qiang-ye-mei-yong]] maps agent hangs, asynchronous tool progress, and incompatible prompt interpretations onto distributed-system failure modes.
- Failure detection: [[duo-agent-xie-zuo-ben-zhi-shi-fen-bu-shi-xi-tong-wen-ti-mo-xing-duo-qiang-ye-mei-yong]] notes that even imperfect failure detectors can make consensus more practical.

## Counterevidence & Qualifications
The production-infrastructure source assumes that mainstream agents will converge toward long-running, high-permission autonomous execution. It explicitly notes an alternate path where agents stay short-running, low-permission, and human-approved at every step; in that world, capability isolation remains important but effect logs and fork recovery become less urgent. The distributed-systems source adds that coordination mechanisms improve practical outcomes but still make safety, liveness, and fault-tolerance tradeoffs.

## What Changed
- Created the concept page for the article's production-agent infrastructure frame.
- Added distributed-consensus, failure-detection, and liveness concerns for multi-agent infrastructure.

## Related Concepts
- [[EffectLog]] - provides durable side-effect semantics for production agents.
- [[CapabilityGateway]] - enforces capability boundaries for production agents.
- [[ForkRecovery]] - restores production agents from semantic checkpoints.
- [[AgentResumability]] - names the reliability target for production-agent execution.
- [[SemanticIsolation]] - distinguishes agent-specific safety boundaries from process isolation.
- [[HarnessEngineering]] - production agent infrastructure is a runtime extension of agent harness design.
- [[DistributedConsensus]] - multi-agent production systems need coordination despite failures and ambiguity.
- [[TrustTopology]] - verification gates help decide when to accept, retry, stop, or escalate agent work.
