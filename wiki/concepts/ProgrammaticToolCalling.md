---
title: "Programmatic Tool Calling"
type: concept
tags: [ai, agents, tools, context-management, code-execution]
sources:
  - deepseek-harness-source-analysis
last_updated: 2026-10-25
knowledge_schema: synthesis-v1
---

## Definition
[[ProgrammaticToolCalling]] is an agent execution pattern in which a model generates a program that invokes available tools and processes their results inside a governed runtime before returning a smaller result to the model.

## Current Synthesis
The analyzed [[DeepSeekHarness]] implementation exposes PTC through a `run_code` tool. Instead of asking for several native tool calls and receiving every full result in the next model request, the model can generate code that calls the same tools, filters, aggregates, or combines their outputs, and returns only the data needed for continued reasoning. Tool calls inside the program still traverse DSH's policy chain and produce execution records.

PTC changes where deterministic intermediate processing happens; it does not remove the model from planning or final judgment. It is most plausible when tool results are large and the transformation rule is explicit. For small tasks, code generation, execution, failure handling, and retry can cost more than simply returning the original tool result.

## Key Claims
- Generated code can compose multiple existing tools without exposing every intermediate result to the next model request.
- Filtering and aggregation inside the execution runtime can reduce context consumption when raw tool outputs are large.
- Nested tool calls should retain the harness's ordinary permission, policy, and logging controls.
- PTC is an execution and data-reduction pattern, not a claim that generated programs are automatically correct.
- Net value depends on end-to-end correctness, latency, model usage, code-generation cost, and retry frequency.

## Evidence
- Execution shape: [[deepseek-harness-source-analysis]] shows a model placing generated code in `run_code`, with the program calling tools and returning a filtered result.
- Data-flow comparison: [[deepseek-harness-source-analysis]] and its retained diagram contrast native calls that return full outputs to the model with programmatic calls that filter and summarize inside the runtime.
- Policy continuity: [[deepseek-harness-source-analysis]] says tool calls made within PTC still pass through DSH's policy chain and leave call records.
- Scope condition: [[deepseek-harness-source-analysis]] says the technique is more promising for large results and clear processing rules than for a small heading-extraction task.

## Counterevidence & Qualifications
The source supplies architecture and illustrative examples rather than benchmark results. It does not quantify token savings, latency, code failure, retry rates, sandbox risk, or answer quality. Filtering can also discard evidence the model later needs, and generated programs add another untrusted execution layer whose resource limits and permissions matter. Images or other non-text outputs may need separate delivery paths rather than being represented by the program's compact return value.

## What Changed
- Created the concept from DSH's `run_code` design and native-versus-programmatic data-flow comparison.

## Related Concepts
- [[HarnessEngineering]] - the harness governs generated programs and their nested tool calls.
- [[LLMContextManagement]] - runtime filtering can reduce the intermediate content entering the next model request.
- [[BashAsMetaTool]] - both use a programmable surface to compose narrower capabilities.
- [[CodingAgentMinimalTooling]] - PTC composes an existing tool set rather than requiring one model-visible tool per workflow.
- [[SoftwareVerification]] - generated transformations need outcome, latency, and failure evaluation.
- [[DeepSeekHarness]] - runtime implementation analyzed as the source of the pattern.
