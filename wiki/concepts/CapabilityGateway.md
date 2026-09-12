---
title: "Capability Gateway"
type: concept
tags: [ai, agents, security, infrastructure]
sources:
  - wei-shen-me-xian-you-de-agent-infra-wu-fa-zhi-cheng-sheng-chan-ji-ying-yong
last_updated: 2026-09-12
knowledge_schema: synthesis-v1
---

## Definition
[[CapabilityGateway]] is an infrastructure boundary that mediates an agent's external actions through scoped, temporary, revocable credentials and enforced tool-call semantics.

## Current Synthesis
The source argues that agent processes should not receive raw API keys, database credentials, or cloud tokens. Instead, all external access should pass through a gateway that grants only the specific capability needed for the current task, with limited time, limited scope, and immediate revocability. This shifts safety from model self-restraint into infrastructure enforcement and makes the agent's blast radius an explicit design choice.

## Key Claims
- Raw credentials should not live directly inside a high-permission agent process.
- Capability scope defines the blast radius of an agent failure or injection attack.
- Permission boundaries must be enforced below the model layer.
- Temporary and revocable tokens reduce damage after crash or compromise.
- The gateway should enforce the effect-log contract for side-effecting operations.
- Capability isolation remains important even if agents stay human-approved and low-autonomy.

## Evidence
- Credential mediation: [[wei-shen-me-xian-you-de-agent-infra-wu-fa-zhi-cheng-sheng-chan-ji-ying-yong]] proposes giving agents scoped temporary tokens through a gateway rather than direct credentials.
- Browser analogy: [[wei-shen-me-xian-you-de-agent-infra-wu-fa-zhi-cheng-sheng-chan-ji-ying-yong]] compares the approach to browsers denying JavaScript direct operating-system access.
- Blast-radius framing: [[wei-shen-me-xian-you-de-agent-infra-wu-fa-zhi-cheng-sheng-chan-ji-ying-yong]] says the granted permission range is the agent's explosion radius.
- Crash handling: [[wei-shen-me-xian-you-de-agent-infra-wu-fa-zhi-cheng-sheng-chan-ji-ying-yong]] says scoped tokens can expire or be revoked after crash, including crashes induced by malicious input.

## Counterevidence & Qualifications
The source does not specify a complete gateway API or policy language. It also acknowledges a usefulness-safety tradeoff: broader permissions make agents more capable, while narrower permissions reduce possible damage.

## What Changed
- Created the concept page for capability gateways as the article's proposed capability-isolation primitive.

## Related Concepts
- [[ProductionAgentInfrastructure]] - capability gateways provide the security boundary in production agent systems.
- [[EffectLog]] - gateways enforce side-effect classifications and recovery behavior.
- [[SemanticIsolation]] - capability gateways are the concrete mechanism for semantic isolation.
- [[ComputerUse]] - computer-control agents need hard capability boundaries when operating real systems.
- [[ModelContextProtocol]] - structured tool calls may route through a capability gateway for policy enforcement.
- [[HarnessEngineering]] - capability gateways make runtime constraints part of the agent harness.
