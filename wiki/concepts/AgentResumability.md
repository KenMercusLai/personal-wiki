---
title: "Agent Resumability"
type: concept
tags: [ai, agents, reliability, infrastructure]
sources:
  - wei-shen-me-xian-you-de-agent-infra-wu-fa-zhi-cheng-sheng-chan-ji-ying-yong
  - deepseek-harness-source-analysis
last_updated: 2026-10-25
knowledge_schema: synthesis-v1
---

## Definition
[[AgentResumability]] is the ability to re-enter an agent's execution at any point with its state, context, external-effect facts, and environment semantics intact.

## Current Synthesis
The sources argue that uptime is only a proxy metric for agents. Long-running agents will eventually encounter network failures, hardware faults, restarts, or scaling events, so reliability should mean preserving the correctness of execution semantics when failure occurs. Resumability turns crash and restart from exceptional cases into ordinary operations, especially when vertical scaling requires checkpoint-and-restart behavior.

The [[DeepSeekHarness]] analysis adds a concrete but partial implementation. Session events are buffered to persistent storage, and checkpoints wait for that buffer before a model request or top-level tool executes. On recovery, saved history is reused rather than replaying historical tools, while interrupted records are repaired with states that distinguish work not started from outcomes that are unknown. This narrows replay risk but cannot determine whether an external action succeeded after dispatch and before its result was saved. The analyzed SDK also exposes an integration boundary: session continuation works inside one live runtime, but a new SDK process does not restore an uncached persisted session merely by receiving its old ID.

## Key Claims
- Long-running agents should be designed to tolerate death rather than assumed to stay alive.
- Reliability depends on semantic correctness after recovery, not only process availability.
- Vertical scaling can make checkpoint and restart a normal path rather than an edge case.
- Resumability requires effect facts, context, and environment state to be recoverable together.
- A resumable agent can be more reliable than an always-on agent with no safe failure path.
- Resumability becomes more important as agents run for hours, days, or weeks.
- Checkpointed persistence and interrupted-run classification are necessary but insufficient unless the application entry point actually reconnects persisted sessions and uncertain external effects are reconciled.

## Evidence
- Uptime critique: [[wei-shen-me-xian-you-de-agent-infra-wu-fa-zhi-cheng-sheng-chan-ji-ying-yong]] says uptime is a proxy metric for agents because failure is statistically likely during long autonomous work.
- Semantic target: [[wei-shen-me-xian-you-de-agent-infra-wu-fa-zhi-cheng-sheng-chan-ji-ying-yong]] says the design goal should be preserving execution semantics when failure happens.
- Scaling implication: [[wei-shen-me-xian-you-de-agent-infra-wu-fa-zhi-cheng-sheng-chan-ji-ying-yong]] argues that vertical scaling often implies checkpoint and restart.
- Recovery example: [[wei-shen-me-xian-you-de-agent-infra-wu-fa-zhi-cheng-sheng-chan-ji-ying-yong]] returns to the cloud-migration failure and shows recovery from the precise post-effect point rather than restarting.
- Persistence boundary: [[deepseek-harness-source-analysis]] says DSH checkpoints buffered session events before model requests and top-level tool execution.
- Interrupted execution: [[deepseek-harness-source-analysis]] says recovery reuses saved tool results, repairs unfinished records, and preserves an unknown-result state rather than replaying history automatically.
- Entry-point limitation: [[deepseek-harness-source-analysis]] finds that the analyzed SDK continues cached sessions in one runtime but does not call the persisted-session resume path for an uncached ID in a new process.

## Counterevidence & Qualifications
The infrastructure article does not claim uptime is irrelevant for the underlying platform. It argues that uptime alone is insufficient for autonomous agents, especially when the agent has side effects that cannot be recreated safely after a process restart. DSH provides source-level evidence for checkpoint and repair mechanics, not a crash-injection benchmark or exactly-once guarantee. A durable call with no durable result remains uncertain, and resumability is incomplete when the host entry point does not connect an old identifier to the persisted resume service.

## What Changed
- Added a concrete checkpoint, saved-result reuse, and interrupted-record repair path.
- Added uncertain external outcomes as an explicit recovery boundary.
- Added host entry-point wiring as part of end-to-end resumability.

## Related Concepts
- [[ProductionAgentInfrastructure]] - resumability is the reliability goal for the infrastructure stack.
- [[EffectLog]] - effect records make safe resumability possible.
- [[ForkRecovery]] - fork checkpoints are the concrete resumption mechanism.
- [[SemanticIsolation]] - resumability preserves semantic boundaries across failures.
- [[CloudCostOptimization]] - vertical scaling and restart tradeoffs can affect infrastructure design.
- [[HarnessEngineering]] - resumability extends harness design into runtime failure semantics.
- [[DeepSeekHarness]] - supplies the analyzed checkpoint and session-repair implementation.
- [[TapeAndAnchors]] - retained history can reconstruct context, while resumability additionally requires execution and effect semantics.
