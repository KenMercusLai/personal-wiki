---
title: "kotatsu"
type: entity
tags: [cpp, infrastructure, concurrency, developer-tools]
sources:
  - agent-shi-dai-de-clice
last_updated: 2026-10-11
knowledge_schema: synthesis-v1
---

## Overview
[[Kotatsu]] is a reusable modern C++ infrastructure library extracted from [[Clice]] to provide the tested foundations needed by language servers and related projects.

## Current Profile
Kotatsu combines an original [[StructuredConcurrency]] framework and static-reflection layer with wrappers or integrations around existing C++ libraries. The reported modules cover asynchronous execution, I/O, IPC, HTTP, serialization and codecs, command-line parsing, and unit testing. Extracting this layer reduced clice itself toward language-server business logic and gave the infrastructure a broader operating-system, compiler, and build-option CI matrix.

The library also supports other clice-io projects such as catter. The author presents it as an answer to a practical gap in reusable C++ components rather than as a from-scratch replacement for the ecosystem: dependencies include simdjson, toml++, FlatBuffers, cpptrace, and libuv, with the new async model and static reflection providing the principal abstractions.

## Key Characteristics
- Provides cancellation-aware asynchronous tasks whose lifetime follows an explicit parent-child graph.
- Bundles I/O, IPC, HTTP, serialization, reflection, CLI, and testing facilities behind consistent C++ abstractions.
- Is tested independently from clice across combinations of operating systems, compilers, and build options.
- Reduces clice's core toward domain logic and is shared by other clice-io projects.
- Builds on established libraries rather than reimplementing every low-level facility.

## Evidence
- Extraction boundary: [[agent-shi-dai-de-clice]] says clice's infrastructure modules were moved into kotatsu after redesign and expanded testing.
- Module coverage: [[agent-shi-dai-de-clice]] lists async, I/O, IPC, HTTP, static reflection, serialization, command-line parsing, and unit testing.
- Reuse: [[agent-shi-dai-de-clice]] reports use by catter as well as clice.
- Ecosystem composition: [[agent-shi-dai-de-clice]] names simdjson, toml++, FlatBuffers, cpptrace, and libuv as dependencies and identifies async plus static reflection as the library's core innovations.

## Qualifications
This is a project-author description without independent adoption, API-stability, compatibility, or comparative maintenance evidence. The author says release versions may follow after APIs stabilize, so the current breadth should not be confused with a stable general-purpose C++ platform. Claims about gaps in the C++ ecosystem reflect the author's integration experience and may vary by requirements.

## What Changed
- Created the library profile from the clice infrastructure refactor report.

## Relationships
- [[Clice]] - primary consumer from which kotatsu was extracted.
- [[StructuredConcurrency]] - forms the library's cancellation-aware async module.
- [[ConcurrentProgramming]] - provides the broader model for kotatsu's asynchronous task and synchronization facilities.
- [[SoftwareVerification]] - the independent CI matrix and tests are intended to stabilize the infrastructure boundary.
