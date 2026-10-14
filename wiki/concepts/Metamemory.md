---
title: "Metamemory"
type: concept
tags: [cognitive-science, ai, agents, memory]
sources:
  - "2607.01224"
last_updated: 2026-10-14
knowledge_schema: synthesis-v1
---

## Definition
[[Metamemory]] is the learned capacity to monitor and regulate memory: deciding what is worth encoding, when to retrieve it, and how stored knowledge should be organized.

## Current Synthesis
In cognitive science, metamemory describes a monitor-control relationship between a meta-level and memory processes at the object level. External aids such as notes, maps, and files can participate in that regulation by moving information beyond limited working memory.

For LLM agents, the concept shifts attention from owning a memory store to exercising judgment over it. A model can choose whether to write, search, read, update, or ignore external records; the schema and prompts constrain those choices, while training can improve the policy that selects among them. [[AutoMem]] supplies initial evidence that these structural and proficiency axes can be optimized separately and then combined.

## Key Claims
- Metamemory concerns memory control and monitoring rather than storage capacity alone.
- External records extend limited working context only when an agent selects, organizes, and retrieves them effectively.
- An agent's memory scaffold defines available operations and representations, while model proficiency determines how well those affordances are used.
- Explicit memory actions make delayed mistakes observable in complete trajectories and therefore available for review and training.
- Improving memory decisions can change downstream task behavior even when the task-action model remains frozen.

## Evidence
- Cognitive framing: [[2607.01224]] draws on Flavell's monitoring account, Nelson's meta-level/object-level loop, and the extended-mind view of external aids.
- Operationalization: [[2607.01224]] represents file reads, searches, appends, writes, creates, and map updates as actions selected alongside task behavior.
- Structure and proficiency: [[2607.01224]] reports gains from meta-LLM scaffold revision followed by LoRA training of a dedicated memory specialist.
- Behavioral change: [[2607.01224]] reports less redundant writing and empty search, more consultation before writing, smaller per-step context, and less unproductive gameplay.

## Counterevidence & Qualifications
The LLM-agent evidence comes from one paper, one base-model family, and three game environments with separate per-environment optimization. The study does not show that the trained behavior transfers to real-world work, a shared general specialist, persistent cross-episode memory, or human metamemory. Its use of a cognitive-science term is a productive engineering analogy and hypothesis, not evidence that the agent has human-like self-awareness or introspective experience.

## What Changed
- Established metamemory as the distinction between memory storage and learned control over memory operations.
- Added separate scaffold-structure and model-proficiency axes for agent memory skill.

## Related Concepts
- [[AgentMemory]] - provides the persistent substrate and lifecycle over which metamemory decisions operate.
- [[AutoMem]] - implements scaffold revision and proficiency training for explicit memory actions.
- [[LLMContextManagement]] - metamemory decides which external information should enter limited active context.
- [[CognitiveOffloading]] - external aids reduce working-memory demands when capture and later retrieval remain reliable.
- [[MemoryCompaction]] - consolidation is one possible controlled transformation of stored experience.
