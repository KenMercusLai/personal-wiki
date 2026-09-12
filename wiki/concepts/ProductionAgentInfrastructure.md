---
title: "Production Agent Infrastructure"
type: concept
tags: [ai, agents, infrastructure, reliability, security]
sources:
  - wei-shen-me-xian-you-de-agent-infra-wu-fa-zhi-cheng-sheng-chan-ji-ying-yong
last_updated: 2026-09-12
knowledge_schema: synthesis-v1
---

## Definition
[[ProductionAgentInfrastructure]] is infrastructure designed to run long-lived, high-permission AI agents whose probabilistic decisions can create real external side effects.

## Current Synthesis
The source argues that production agents are not just LLM wrappers with tools. They combine long-running execution, hostile inputs, real credentials, nondeterministic model decisions, and irreversible side effects in one chain. Existing infrastructure usually handles only pieces of this problem: databases handle transactions, browsers sandbox hostile input, distributed systems checkpoint long-running work, containers isolate processes, and workflow engines replay deterministic tasks. Agent infrastructure needs a semantic layer that records effects, mediates capabilities, and resumes execution from precise checkpoints.

## Key Claims
- Production agents differ from ordinary services because failure can occur after many state-changing decisions.
- The key risk is structural: long runtime, untrusted input, credentials, nondeterminism, and side effects interact.
- Durable side-effect records must exist before safe recovery is possible.
- Capability boundaries must be enforced by infrastructure rather than by model obedience.
- Recovery must preserve semantic correctness, not merely restart a process.
- Existing sandboxes and workflow engines can support agent systems but do not replace agent-specific primitives.

## Evidence
- Combined properties: [[wei-shen-me-xian-you-de-agent-infra-wu-fa-zhi-cheng-sheng-chan-ji-ying-yong]] lists long-running execution, hostile input, real permissions, uncertain decisions, and real side effects as the distinctive production-agent bundle.
- Missing guarantees: [[wei-shen-me-xian-you-de-agent-infra-wu-fa-zhi-cheng-sheng-chan-ji-ying-yong]] identifies absent side-effect logs, absent recoverable state, and absent isolation boundaries as the core infrastructure gaps.
- Primitive order: [[wei-shen-me-xian-you-de-agent-infra-wu-fa-zhi-cheng-sheng-chan-ji-ying-yong]] says side effects must be sealed before capability boundaries and recovery can be safely enforced.
- Existing-system limits: [[wei-shen-me-xian-you-de-agent-infra-wu-fa-zhi-cheng-sheng-chan-ji-ying-yong]] treats Kubernetes, Firecracker, gVisor, Modal, E2B, Temporal, and Conductor as useful at their own layers but outside agent semantic needs.

## Counterevidence & Qualifications
The source assumes that mainstream agents will converge toward long-running, high-permission autonomous execution. It explicitly notes an alternate path where agents stay short-running, low-permission, and human-approved at every step; in that world, capability isolation remains important but effect logs and fork recovery become less urgent.

## What Changed
- Created the concept page for the article's production-agent infrastructure frame.

## Related Concepts
- [[EffectLog]] - provides durable side-effect semantics for production agents.
- [[CapabilityGateway]] - enforces capability boundaries for production agents.
- [[ForkRecovery]] - restores production agents from semantic checkpoints.
- [[AgentResumability]] - names the reliability target for production-agent execution.
- [[SemanticIsolation]] - distinguishes agent-specific safety boundaries from process isolation.
- [[HarnessEngineering]] - production agent infrastructure is a runtime extension of agent harness design.
