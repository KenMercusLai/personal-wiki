---
title: "clice"
type: entity
tags: [cpp, language-server, developer-tools, ai]
sources:
  - agent-shi-dai-de-clice
last_updated: 2026-10-11
knowledge_schema: synthesis-v1
---

## Overview
[[Clice]] is an experimental C++ language server and real-time compilation system designed around cancellation-aware asynchronous execution, compiler-process isolation, modern C++ support, and semantic interfaces for both editors and coding agents.

## Current Profile
The 2026 project update presents clice as a small domain-logic layer built on the extracted [[Kotatsu]] infrastructure library. Its server organizes asynchronous work through [[StructuredConcurrency]], sends compilation into stateful and stateless worker processes to contain Clang failures, and adds include-graph scanning, C++20 named-module support, and switchable compilation contexts for source and non-self-contained header files.

The project is also moving beyond LSP as its only consumer. A daemon and command-line query process already expose compilation commands, symbol lookup, and call graphs, while the longer-term [[AgentNativeLanguageServer]] direction proposes a separate agentic protocol optimized for batch requests, concurrent worktrees, selective diagnostic retrieval, and semantic code navigation. The author describes the architecture as largely in place but with known cross-environment issues still blocking a formal 1.0 release.

## Key Characteristics
- Uses cancellation-aware structured concurrency to bind task lifetime and propagation to an explicit asynchronous graph.
- Isolates Clang frontend work in reusable worker processes so a compiler crash, hang, or leak does not terminate the server.
- Supports fast approximate include scanning, C++20 module dependency work, and multiple compilation contexts.
- Treats LSP as one consumer of a broader real-time compilation system rather than the system's defining boundary.
- Exposes early daemon and CLI semantic queries as the first step toward agent-native access.
- Uses coding agents heavily for implementation while the author retains architectural, review, and release decisions.

## Evidence
- Concurrency architecture: [[agent-shi-dai-de-clice]] describes first-class cancellation, parent-child task lifetime, and exportable task graphs.
- Failure isolation: [[agent-shi-dai-de-clice]] places compilation in stateful and stateless worker processes and characterizes IPC as small relative to typical compilation work.
- Language features: [[agent-shi-dai-de-clice]] reports include scanning, module dependency builds and cycle detection, and selectable source or header compilation contexts.
- Agent interface: [[agent-shi-dai-de-clice]] reports a daemon plus CLI queries for compilation commands, symbols, and call graphs and proposes a dedicated agentic protocol.
- Readiness boundary: [[agent-shi-dai-de-clice]] says the current branch works locally but still has known corner cases that should be resolved before 1.0.

## Qualifications
The profile comes from the project's developer rather than an independent evaluation. Performance and overhead figures do not include reproducible benchmark conditions, the agent-native advantages remain hypotheses awaiting task-level validation, and no released 1.0 or broad deployment evidence is presented. The article's claim that Clang causes 99 percent of clangd crashes and leaks is an informal estimate, not a measured attribution suitable for generalization.

## What Changed
- Created the project profile from its 2026 architecture and agent-native progress report.

## Relationships
- [[Kotatsu]] - supplies clice's reusable async, I/O, IPC, serialization, reflection, CLI, and testing infrastructure.
- [[StructuredConcurrency]] - governs clice task lifetime, dependency, and cancellation propagation.
- [[AgentNativeLanguageServer]] - names clice's emerging semantic interface for coding agents.
- [[AgentTeam]] - provides much of the implementation and cross-review capacity described by the developer.
- [[ConcurrentProgramming]] - is the broader programming model within which clice's coroutine and cancellation design operates.
