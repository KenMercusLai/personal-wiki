---
title: "Local Coding Agents"
type: concept
tags: [ai, coding-agents, local-llm, privacy, developer-tools]
sources:
  - using-local-coding-agents
last_updated: 2026-10-14
knowledge_schema: synthesis-v1
---

## Definition
[[LocalCodingAgents]] are coding-agent systems in which an open-weight language model is served on user-controlled hardware and connected to a harness that can inspect, modify, execute, and verify work in a codebase.

## Current Synthesis
A local coding agent is not one program but a three-layer system: a model supplies reasoning and generation, an inference runtime exposes it through a callable endpoint, and a harness supplies files, shell commands, editing, context management, approvals, and verification. OpenAI-compatible APIs make the layers partly interchangeable, so model choice does not determine harness choice.

Locality changes the operating tradeoff rather than removing it. It can keep prompts and repository data on controlled hardware, work offline, stabilize model versions, expose implementation details, and turn repeated use into hardware-and-electricity cost. It also moves capacity planning, runtime configuration, updates, measurement, security, and troubleshooting to the user, while consumer-size open-weight models may still trail frontier proprietary models.

Evaluation therefore has four coupled dimensions. Hardware fit covers download size, memory, prefill, decode, and long-context degradation. Capability fit covers realistic tool selection and task completion. Harness fit covers token reuse, prompt growth, tool policies, and model-harness interaction. Trust fit covers permissions, file and secret scope, network egress, telemetry, prompt injection, plugins, updates, and recovery. A personal regression pack and a constrained test environment are more informative than assuming a benchmark winner or model-branded harness will fit a particular workflow.

## Key Claims
- The practical unit is model plus inference runtime plus coding harness, not the model alone.
- OpenAI-compatible local endpoints allow models and harnesses to be mixed, but compatibility does not guarantee equal performance.
- Long-context decode rate and memory behavior are more relevant to agent work than short-prompt peak speed alone.
- Small workflow-specific task packs can reveal tool-choice and harness failures that broad model rankings miss.
- Local inference improves control but does not eliminate telemetry, update, plugin, prompt-injection, filesystem, secret, or shell-execution risk.
- Harness design can materially change success rate, token use, and latency for the same model.
- Isolation, explicit approvals, egress controls, and verification remain necessary even when every model token is generated locally.

## Evidence
- Layered architecture: [[using-local-coding-agents]] diagrams interchangeable model, runtime, and coding-harness layers and configures Ollama's OpenAI-compatible endpoint for several harnesses.
- Hardware fit: [[using-local-coding-agents]] measures prefill, decode, and memory through 50k-word prompts on Mac and DGX systems rather than relying on short interactive tests.
- Capability fit: [[using-local-coding-agents]] reports materially different results for Qwen3.6, North Mini Code, Gemma 4 E2B, and Nemotron 3 Nano on a five-task personal problem pack.
- Harness fit: [[using-local-coding-agents]] reports Qwen3.6 at 4/5 in Qwen Code and 5/5 in Codex and Claude Code, while Codex uses fewer total tokens than the other harnesses for the capable models.
- Trust fit: [[using-local-coding-agents]] audits shell access, file and secret boundaries, telemetry, hooks, MCP, prompt injection, updates, and data egress before recommending an isolated test environment.
- Remote deployment: [[using-local-coding-agents]] uses SSH local-port forwarding so a Mac-side harness can reach a DGX-hosted Ollama endpoint as though it were local.

## Counterevidence & Qualifications
The evidence comes from one practitioner, a small hand-curated five-task pack, a limited set of model versions and quantizations, and two hardware platforms. Pass counts do not measure code quality, maintenance cost, regression breadth, adversarial robustness, or long-running autonomy. The reported macOS RSS understates Metal-backed memory use, and all throughput results depend on runtime, context, quantization, thermal state, and workload. Local inference does not prove local-only data handling because the harness and its integrations may still communicate externally. Remote inference through a tunnel also weakens the everyday meaning of "local" even when the hardware remains user-controlled.

## What Changed
- Established the model-runtime-harness stack as the unit of local coding-agent design.
- Added hardware, capability, harness, and trust fit as four separate evaluation dimensions.
- Added source-scoped evidence that harness choice can alter both task success and token cost for the same model.
- Qualified local privacy by separating inference locality from total system egress and authority.

## Related Concepts
- [[HarnessEngineering]] - harness context and orchestration determine how the local model acts.
- [[CodingAgentMinimalTooling]] - the harness exposes the file, edit, shell, and verification surface used by a local model.
- [[AgentPermissionModel]] - approvals and path boundaries limit local-machine authority.
- [[AgentSecurityLayering]] - operating-system isolation, egress controls, and secret separation bound failures below the model layer.
- [[AICodingPractice]] - personal regression tasks and human review connect local capability to responsible engineering work.
- [[SoftwareVerification]] - task completion and generated code require checks beyond model fluency.
