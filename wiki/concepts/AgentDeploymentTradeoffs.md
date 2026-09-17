---
title: "Agent Deployment Tradeoffs"
type: concept
tags: [ai, agents, latency, deployment]
sources:
  - yan-li-how-llm-agents-became-what-they-look-like-in-2026
last_updated: 2026-09-17
knowledge_schema: synthesis-v1
---

## Definition
[[AgentDeploymentTradeoffs]] are the constraints that keep agentic designs from being the right choice everywhere: response latency, output reproducibility, privacy and cost, and the need for multimodal or graphical interaction.

## Current Synthesis
The source separates the experience of building with coding agents from the experience of shipping assistants to ordinary users. The author tolerates a state-of-the-art model and long waits for the best result, but treats an acceptable chatbot time-to-first-token as roughly 20 to 30 seconds. That gap is the stated reason non-agentic [[RetrievalAugmentedGeneration]] still exists even where an agentic loop would score better.

Reproducibility is the second constraint. Even users who will wait for quality still expect predictable wait times and consistent outputs, and the source uses that expectation as the reason [[AgenticWorkflowPatterns]] - predefined, inspectable paths - remain relevant beside autonomous loops. Privacy and cost form the third constraint, pushing many users toward smaller open-weight or edge-sized models rather than the largest hosted model. The fourth is capability breadth: beyond coding, users want browser-use, computer-use, and GUI-specific agents, which is where the model's coverage is thinnest.

## Key Claims
- Agent quality and user-facing latency pull in opposite directions, so slower high-quality designs are not automatically the right product.
- The source's working latency heuristic is that chatbot time-to-first-token should stay within roughly 20 to 30 seconds.
- Latency is the stated reason non-agentic retrieval-augmented generation still persists.
- Reproducibility matters alongside quality: users expect predictable waits and consistent output even when they accept long runs.
- Privacy and cost justify smaller open-weight or edge models in many situations rather than the strongest available model.
- Demand extends past coding to browser-use, computer-use, and GUI-specific agents, which remain the least covered surfaces.

## Evidence
- Latency preference: [[yan-li-how-llm-agents-became-what-they-look-like-in-2026]] contrasts the author's tolerance for SOTA models and long waits with ordinary users' latency expectations.
- Latency heuristic: [[yan-li-how-llm-agents-became-what-they-look-like-in-2026]] proposes a TTFT of at most 20-30 seconds for a chatbot scenario.
- RAG persistence: [[yan-li-how-llm-agents-became-what-they-look-like-in-2026]] names latency as one reason non-agentic RAG still exists.
- Reproducibility: [[yan-li-how-llm-agents-became-what-they-look-like-in-2026]] says users expect predictable wait times and consistent outputs, which is why workflows continue to matter.
- Privacy and cost: [[yan-li-how-llm-agents-became-what-they-look-like-in-2026]] says users often choose smaller open-weight or edge-sized models for privacy or cost.
- Multimodal demand: [[yan-li-how-llm-agents-became-what-they-look-like-in-2026]] lists browser-use, computer-use, and specific-GUI interaction as desired capabilities beyond coding agents.

## Counterevidence & Qualifications
These are the author's heuristics rather than measured product thresholds. The 20-30 second time-to-first-token figure is asserted without evidence and is stated for chatbot scenarios specifically, not for asynchronous or background agents where latency tolerances differ. The tradeoff list is also not exhaustive; it omits evaluation, safety, permissioning, and integration cost, which other wiki sources treat as first-order agent concerns.

## What Changed
- Created the concept page for the latency, reproducibility, privacy/cost, and multimodality constraints on agent deployment.
- Added the claim that latency is a reason non-agentic RAG persists.

## Related Concepts
- [[LLMAgentStages]] - deployment constraints explain why the newest architecture layer is not universally applicable.
- [[RetrievalAugmentedGeneration]] - non-agentic retrieval survives partly on latency grounds.
- [[AgenticWorkflowPatterns]] - reproducibility is why predefined workflows remain useful beside autonomous agents.
- [[ComputerUse]] - browser-use and computer-use are the capability gaps users still ask for.
- [[UncannyValleyOfAI]] - both concern the gap between what a system implies it can do and what it can deliver.
