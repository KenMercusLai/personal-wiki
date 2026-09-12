---
title: "Agent Resumability"
type: concept
tags: [ai, agents, reliability, infrastructure]
sources:
  - wei-shen-me-xian-you-de-agent-infra-wu-fa-zhi-cheng-sheng-chan-ji-ying-yong
last_updated: 2026-09-12
knowledge_schema: synthesis-v1
---

## Definition
[[AgentResumability]] is the ability to re-enter an agent's execution at any point with its state, context, external-effect facts, and environment semantics intact.

## Current Synthesis
The source argues that uptime is only a proxy metric for agents. Long-running agents will eventually encounter network failures, hardware faults, restarts, or scaling events, so reliability should mean preserving the correctness of execution semantics when failure occurs. Resumability turns crash and restart from exceptional cases into ordinary operations, especially when vertical scaling requires checkpoint-and-restart behavior.

## Key Claims
- Long-running agents should be designed to tolerate death rather than assumed to stay alive.
- Reliability depends on semantic correctness after recovery, not only process availability.
- Vertical scaling can make checkpoint and restart a normal path rather than an edge case.
- Resumability requires effect facts, context, and environment state to be recoverable together.
- A resumable agent can be more reliable than an always-on agent with no safe failure path.
- Resumability becomes more important as agents run for hours, days, or weeks.

## Evidence
- Uptime critique: [[wei-shen-me-xian-you-de-agent-infra-wu-fa-zhi-cheng-sheng-chan-ji-ying-yong]] says uptime is a proxy metric for agents because failure is statistically likely during long autonomous work.
- Semantic target: [[wei-shen-me-xian-you-de-agent-infra-wu-fa-zhi-cheng-sheng-chan-ji-ying-yong]] says the design goal should be preserving execution semantics when failure happens.
- Scaling implication: [[wei-shen-me-xian-you-de-agent-infra-wu-fa-zhi-cheng-sheng-chan-ji-ying-yong]] argues that vertical scaling often implies checkpoint and restart.
- Recovery example: [[wei-shen-me-xian-you-de-agent-infra-wu-fa-zhi-cheng-sheng-chan-ji-ying-yong]] returns to the cloud-migration failure and shows recovery from the precise post-effect point rather than restarting.

## Counterevidence & Qualifications
The article does not claim uptime is irrelevant for the underlying platform. It argues that uptime alone is insufficient for autonomous agents, especially when the agent has side effects that cannot be recreated safely after a process restart.

## What Changed
- Created the concept page for resumability as the article's proposed production-agent reliability metric.

## Related Concepts
- [[ProductionAgentInfrastructure]] - resumability is the reliability goal for the infrastructure stack.
- [[EffectLog]] - effect records make safe resumability possible.
- [[ForkRecovery]] - fork checkpoints are the concrete resumption mechanism.
- [[SemanticIsolation]] - resumability preserves semantic boundaries across failures.
- [[CloudCostOptimization]] - vertical scaling and restart tradeoffs can affect infrastructure design.
- [[HarnessEngineering]] - resumability extends harness design into runtime failure semantics.
