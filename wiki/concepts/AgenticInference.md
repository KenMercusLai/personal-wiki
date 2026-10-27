---
title: "Agentic Inference"
type: concept
tags: [ai, agents, inference, memory, compute]
sources:
  - spacex-ipo-data-centers-in-space
last_updated: 2026-10-27
knowledge_schema: synthesis-v1
---

## Definition
[[AgenticInference]] is the article's proposed category of model execution in which computers perform extended work under instructions from other computers, making task completion, memory capacity, and tool use more important than immediate human-facing response latency.

## Current Synthesis
Thompson separates future large-model workloads into training, answer inference, and agentic inference. Training continues to reward high-speed accelerators, high-bandwidth memory, and fast networking. Answer inference remains interactive and therefore values low latency. Agentic inference can often run asynchronously or overnight, allowing architectures to trade speed for larger, cheaper memory and adequate compute.

The architectural claim is that current GPUs alternate between underusing memory during prefill and underusing compute during decode. A more agent-oriented system could unbundle those resources into a deeper memory hierarchy, use conventional DRAM where latency permits, and place greater weight on CPU performance for tool execution. Because agents can create demand for other agents without one human initiating every inference step, Thompson expects this category to become the largest of the three.

That forecast also anchors the space-compute thesis: if delay is acceptable, distributed orbital racks become more plausible. The source does not benchmark such an architecture or establish that autonomous demand, memory-centric designs, tool reliability, or space deployment will develop as predicted.

## Key Claims
- Training, interactive answers, and autonomous agent work impose materially different latency, memory, compute, and networking requirements.
- Removing a waiting human from the loop makes slower execution acceptable for some long-running tasks.
- Capacity-oriented memory hierarchies and cheaper DRAM may matter more than peak accelerator speed for those tasks.
- Tool use can increase the importance of CPU and systems performance alongside model accelerators.
- Machine-generated work demand could make agentic inference larger than markets bounded by human prompts and attention.
- Latency tolerance makes agentic inference the article's strongest prospective workload for distributed orbital compute.

## Evidence
- Workload taxonomy: [[spacex-ipo-data-centers-in-space]] distinguishes training, answer inference, and agentic inference by who waits and which resources bind.
- Memory tradeoff: [[spacex-ipo-data-centers-in-space]] argues that asynchronous jobs can use slower, higher-capacity memory rather than optimize every step for human-perceived delay.
- Resource utilization: [[spacex-ipo-data-centers-in-space]] describes current GPUs as alternating between stranded high-bandwidth memory and stranded compute across prefill and decode.
- Market hypothesis: [[spacex-ipo-data-centers-in-space]] expects computer-directed work to scale with available compute rather than human interaction volume.
- Infrastructure fit: [[spacex-ipo-data-centers-in-space]] uses latency tolerance to connect agentic work with rack-like satellites.

## Counterevidence & Qualifications
The taxonomy and market ranking are one analyst's forecast, not a measured workload distribution. Agents may remain constrained by human approval, budgets, correctness, data access, tool latency, serial dependencies, security controls, or verification. Many long-running tasks still need fast communication, low tail latency, tightly coupled accelerators, high-bandwidth memory, or frequent human intervention. Replacing GPU-centric designs with memory-heavy heterogeneous systems may shift rather than remove bottlenecks, and cheaper memory does not guarantee lower cost per successful task. The source gives no benchmark, architecture implementation, demand curve, quality measure, or comparison with batching and scheduling on terrestrial systems.

## What Changed
- Created the concept from the article's three-workload taxonomy and memory-versus-latency argument.

## Related Concepts
- [[LLMInferenceSystems]] - supplies the broader execution context in which model-specific state, memory traffic, and compute interact.
- [[InferenceHostOverhead]] - CPU and orchestration costs may matter more when agents perform tools and extended workflows.
- [[AgentNativeComputing]] - describes the user and platform interface that can generate agentic workloads.
- [[SpaceBasedDataCenters]] - proposed infrastructure whose viability depends partly on latency-tolerant work.
- [[ComputerUse]] - tool interaction is one workload component that may shift importance toward host systems.
