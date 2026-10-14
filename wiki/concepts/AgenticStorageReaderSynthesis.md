---
title: "Agentic Storage Reader Synthesis"
type: concept
tags: [llm-agents, code-synthesis, databases, verification]
sources:
  - 2607.07696
last_updated: 2026-10-13
knowledge_schema: synthesis-v1
---

## Definition
[[AgenticStorageReaderSynthesis]] is a generate-and-verify workflow in which LLM-backed roles turn a database schema and documented physical format into compiled reader code, test it against deterministic database-derived ground truth, and iteratively repair failures.

## Current Synthesis
Jailbreak decomposes the task into four stages. A Dataset Generator creates a small schema-matched table with deterministic values and expected statistics. An Architect translates storage documentation and source knowledge into a structured format specification. A Coder emits a complete C++ shared library, and a QA Tester compiles, loads, runs, and compares its Arrow output with the oracle.

The strongest design choice is that the model does not judge success. Compilation and row or column statistics supply objective feedback; an LLM is called only to diagnose a mismatch, after which the Coder receives the raw failure and accumulated diagnosis history. Retry budgets, checkpoints, resume support, source hashes, and forced strategy changes make the loop bounded and recoverable.

## Key Claims
- Storage readers are plausible synthesis targets because open formats expose detailed executable contracts in code, headers, and documentation.
- Role separation turns schema generation, specification, coding, and verification into distinct bounded contexts.
- Deterministic compilation and data checks are stronger gates than model self-evaluation.
- Failure history, duplicate detection, checkpointing, and retry budgets reduce opaque repetition and make long-running repair resumable.
- General viability remains unproven until the pipeline's convergence, latency, version breadth, ablations, and failure modes are systematically measured.

## Evidence
- Bounded input: [[2607.07696]] gives the Architect the database type, information-schema table definition, and a storage-format knowledge base.
- Generated artifact: [[2607.07696]] requires the Coder to produce a self-contained C++17 shared library with a fixed C and Arrow interface and runtime column parsing.
- Objective oracle: [[2607.07696]] creates deterministic values and compares row count plus per-column aggregates, invoking an LLM diagnosis only on mismatch.
- Recovery controls: [[2607.07696]] records complete attempts in a checkpoint, caps each run at ten tries, supports resume, hashes outputs, and requests subsystem replacement after repeated failures.
- Evaluation gap: [[2607.07696]] says systematic convergence, retry-distribution, generation-latency, broader-schema and version tests, and agent ablations are immediate future work.

## Counterevidence & Qualifications
The paper demonstrates LLM-assisted reader development and describes an implemented pipeline, but does not report how often the pipeline independently reaches a correct artifact. Aggregate statistics can miss row permutations, offset corruption, rare-value errors, or compensating mistakes unless the oracle is expanded. A synthetic table of roughly fifty rows cannot cover all storage states, transaction histories, encodings, overflow paths, corruption, or version changes. Pretraining knowledge may also be stale; authoritative source and version-pinned specifications remain necessary. The workflow therefore shows a credible verification architecture, not yet general autonomous regeneration.

## What Changed
- Added a source-grounded generate-compile-run-compare-repair pattern for storage systems code.
- Distinguished demonstrated reader performance from still-unreported autonomous pipeline convergence.

## Related Concepts
- [[DatabaseBypass]] - supplies the target capability produced by the synthesized reader.
- [[AgenticWorkflowPatterns]] - evaluator-optimizer and sequential-role patterns structure the loop.
- [[SpecDrivenAgentDevelopment]] - a structured physical-format specification constrains generated code.
- [[SoftwareVerification]] - deterministic compilation and output comparison determine acceptance.
- [[AgentResumability]] - checkpoints and accumulated feedback allow repair to continue across retry budgets.
- [[AgentTDDResidual]] - deterministic tests leave residual semantic and coverage risk outside the oracle.
