---
title: "Fork Recovery"
type: concept
tags: [ai, agents, reliability, debugging]
sources:
  - wei-shen-me-xian-you-de-agent-infra-wu-fa-zhi-cheng-sheng-chan-ji-ying-yong
last_updated: 2026-09-12
knowledge_schema: synthesis-v1
---

## Definition
[[ForkRecovery]] is the ability to resume an agent from a precise execution-graph checkpoint while preserving model outputs, tool outputs, and the effect-log position for that branch.

## Current Synthesis
The source frames agent execution as search through a decision graph rather than a single linear process. Each branch needs a checkpoint containing enough semantic closure to resume: model output, tool output, and the effect-log cursor. With those checkpoints, a failure becomes a precise graph location from which the agent can continue, debug, or explore alternatives without starting over or repeating completed external operations.

## Key Claims
- Agent execution is better modeled as a graph of decisions than as one deterministic line.
- Each branch needs its own checkpoint.
- A useful checkpoint must include model output, tool output, and effect-log cursor position.
- Fork recovery is required for debugging, not only performance.
- Recovery without sealed side effects can repeat destructive actions.
- Traceability must be built into agent infrastructure from the beginning.

## Evidence
- Search framing: [[wei-shen-me-xian-you-de-agent-infra-wu-fa-zhi-cheng-sheng-chan-ji-ying-yong]] describes agent execution as exploration through a large decision space.
- Semantic closure: [[wei-shen-me-xian-you-de-agent-infra-wu-fa-zhi-cheng-sheng-chan-ji-ying-yong]] specifies model output, tool output, and effect-log cursor as checkpoint contents.
- Debugging role: [[wei-shen-me-xian-you-de-agent-infra-wu-fa-zhi-cheng-sheng-chan-ji-ying-yong]] says fork recovery is a prerequisite for debugging, because otherwise failures leave developers guessing.
- Crash example: [[wei-shen-me-xian-you-de-agent-infra-wu-fa-zhi-cheng-sheng-chan-ji-ying-yong]] uses a cloud-migration agent that fails after a database modification to show why restarting from scratch is unsafe.

## Counterevidence & Qualifications
The source does not specify checkpoint storage, graph compaction, privacy handling, or how much model trace should be retained. It also depends on effect logs and capability boundaries being in place first; otherwise resuming a branch may still be unsafe.

## What Changed
- Created the concept page for fork recovery as the article's debugging and resumption primitive.

## Related Concepts
- [[AgentResumability]] - fork recovery is one mechanism for resumable agent execution.
- [[EffectLog]] - branch checkpoints include effect-log cursor state.
- [[ProductionAgentInfrastructure]] - fork recovery is the recovery primitive in the production stack.
- [[LLMContextManagement]] - checkpoints preserve the context and tool observations needed for continuation.
- [[SoftwareVerification]] - replayable traces support failure analysis beyond pre-deployment tests.
- [[HarnessEngineering]] - fork recovery gives the harness a way to inspect and resume agent work.
