---
title: "Semantic Isolation"
type: concept
tags: [ai, agents, security, infrastructure]
sources:
  - wei-shen-me-xian-you-de-agent-infra-wu-fa-zhi-cheng-sheng-chan-ji-ying-yong
last_updated: 2026-09-12
knowledge_schema: synthesis-v1
---

## Definition
[[SemanticIsolation]] is isolation at the level of an agent's capabilities, credentials, tool-call meanings, and side effects, rather than only at the level of processes, containers, memory, or code execution.

## Current Synthesis
The source distinguishes execution isolation from semantic isolation. Containers, microVMs, user-space kernels, and code sandboxes can keep workloads from touching each other's memory or filesystem state, but they cannot decide whether an agent should use a legitimate API key to perform a harmful action chosen after prompt injection. Semantic isolation requires capability mediation and side-effect semantics around tool calls.

## Key Claims
- Process isolation does not understand tool-call intent or side-effect meaning.
- A maliciously steered agent may operate entirely through legitimate channels.
- Code sandboxes do not solve the problem of raw external credentials.
- Workflow orchestrators can replay tasks but do not create trust boundaries for untrusted model output.
- Semantic isolation needs capability boundaries and effect logs before orchestration.
- Traditional infrastructure remains useful but operates below the agent-specific trust layer.

## Evidence
- Kubernetes limit: [[wei-shen-me-xian-you-de-agent-infra-wu-fa-zhi-cheng-sheng-chan-ji-ying-yong]] says Kubernetes can isolate resources and processes but cannot see tool-call semantics.
- Sandbox limit: [[wei-shen-me-xian-you-de-agent-infra-wu-fa-zhi-cheng-sheng-chan-ji-ying-yong]] says Firecracker, gVisor, Modal, and E2B provide valuable workload or code isolation without solving capability isolation.
- Credential problem: [[wei-shen-me-xian-you-de-agent-infra-wu-fa-zhi-cheng-sheng-chan-ji-ying-yong]] notes that a clean sandbox still lets an agent use held API keys against external services.
- Orchestration limit: [[wei-shen-me-xian-you-de-agent-infra-wu-fa-zhi-cheng-sheng-chan-ji-ying-yong]] says Temporal and Conductor assume deterministic, trusted workflow logic and therefore do not protect against untrusted LLM decisions.

## Counterevidence & Qualifications
The source does not reject execution isolation. It says those systems are correct at their own abstraction layers and can still be used below or above agent-specific semantic primitives.

## What Changed
- Created the concept page for semantic isolation as the article's abstraction-layer distinction.

## Related Concepts
- [[CapabilityGateway]] - capability gateways enforce semantic isolation.
- [[EffectLog]] - effect logs isolate side-effect facts from replay decisions.
- [[ProductionAgentInfrastructure]] - semantic isolation defines what production agent infrastructure must add.
- [[ComputerUse]] - computer-use agents can need semantic boundaries around legitimate UI or API actions.
- [[ModelContextProtocol]] - structured tool calls still need semantic policy around what each call means.
- [[AgentResumability]] - resumability must preserve semantic, not only process, state.
