---
title: "为什么现有的 Agent Infra 无法支撑生产级应用？"
type: source
tags: [ai, agents, infrastructure, reliability, security]
date: 2026-03-17
source_file: /mnt/ken_personal_wiki/Articles/为什么现有的 Agent Infra 无法支撑生产级应用？.md
---

## Summary
[[Guanlan]] argues that production-grade agents need infrastructure designed for long-running, high-permission, probabilistic execution with real side effects. The article says existing process, sandbox, and workflow systems such as [[Kubernetes]], [[Firecracker]], [[GVisor]], [[Modal]], [[E2B]], [[Temporal]], and [[NetflixConductor]] operate at the wrong abstraction layer unless agent systems first add [[EffectLog]], [[CapabilityGateway]], [[ForkRecovery]], and [[AgentResumability]].

## Key Claims
- Production agents combine long-running execution, hostile inputs, real credentials, nondeterministic decisions, and irreversible side effects, making [[ProductionAgentInfrastructure]] structurally different from ordinary request-processing infrastructure.
- Existing agent stacks lack three core guarantees: durable side-effect records, recoverable execution state, and hard capability boundaries.
- [[EffectLog]] should treat tool calls like write-ahead logged effects, with different recovery rules for reads, idempotent writes, irreversible writes, and mixed read/write operations.
- [[CapabilityGateway]] should mediate all external access through scoped, temporary, revocable credentials rather than giving the agent process raw API keys.
- [[ForkRecovery]] requires checkpoints that include model output, tool output, and the effect-log cursor so failed or alternate execution branches can resume without replaying completed side effects.
- For agents, [[AgentResumability]] is a better reliability target than uptime because long-running autonomous work must preserve execution semantics across crashes, restarts, and vertical scaling.
- Execution sandboxes and workflow orchestrators may remain useful, but they do not provide [[SemanticIsolation]] for model-chosen capabilities and side effects.

## Key Quotes
> "Agent 的执行是概率性的、长程的、带状态的。" - on the execution-model mismatch.

> "Infra 决定边界。" - on the role of infrastructure around agent behavior.

> "正确的指标是 Resumability" - on the reliability target.

## Connections
- [[ProductionAgentInfrastructure]] - central concept for infrastructure purpose-built around agent execution semantics.
- [[EffectLog]] - proposed base primitive for recording and recovering external side effects.
- [[CapabilityGateway]] - proposed primitive for capability isolation and scoped credentials.
- [[ForkRecovery]] - proposed primitive for recovering agent execution as a decision graph.
- [[AgentResumability]] - proposed reliability metric for long-running agent work.
- [[SemanticIsolation]] - distinction between isolating code execution and isolating capabilities plus side effects.
- [[HarnessEngineering]] - the article deepens harness thinking from engineering workflow constraints into runtime safety boundaries.
- [[AIFirstEngineering]] - the article qualifies autonomous AI-first execution by showing what production infrastructure must provide before high-permission agents are safe.
- [[ModelContextProtocol]] - tool interfaces need side-effect semantics and capability enforcement beyond typed calls.
- [[ComputerUse]] - high-permission computer-control agents inherit the same real-side-effect and recovery risks.
- [[OpenClaw]] - cited as a visible example of the risks created when models gain real system permissions.
- [[ClawShell]] - cited as Guanlan's open-source practice around scoped agent capability control.
- [[Temporal]] - durable workflow system discussed as useful but insufficient for nondeterministic, untrusted LLM execution.
- [[NetflixConductor]] - workflow orchestrator discussed as solving a different class of durable execution problem.
- [[Kubernetes]] - process and resource isolation system discussed as operating below tool-call semantics.
- [[Firecracker]] - microVM isolation system discussed as useful but semantically insufficient.
- [[GVisor]] - user-space kernel sandbox discussed as useful but semantically insufficient.
- [[Modal]] - code execution platform discussed as not solving capability isolation or side-effect recovery.
- [[E2B]] - agent code-execution sandbox discussed as not solving raw credential or effect-log problems.

## Contradictions
- No direct contradiction with existing wiki pages. The source qualifies [[AIFirstEngineering]] and [[HarnessEngineering]] by arguing that production-grade autonomous agents need semantic recovery and capability boundaries, not only tests, CI/CD, observability, and workflow scaffolds.
