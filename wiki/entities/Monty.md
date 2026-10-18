---
title: "Monty"
type: entity
tags: [python, interpreter, sandboxing, ai-agents]
sources:
  - unikernel-agent
last_updated: 2026-10-18
knowledge_schema: synthesis-v1
---

## Overview
[[Monty]] is a Pydantic open-source interpreter for a restricted Python subset, presented as a very fast sandboxed execution option for agent-generated code.

## Current Profile
The source uses Monty to expose a central sandbox tradeoff. Its retained comparison graphic reports 0.06 ms startup, strict security, easy setup, easy file mounting, and easy snapshots, far below the listed startup figures for fuller runtimes. That speed is purchased by language incompleteness: the article says classes and modules such as `sys` are unsupported, making Monty unsuitable when agents require broad CPython behavior or common system tooling.

## Key Characteristics
- Interprets a subset of Python rather than full CPython.
- Targets tightly sandboxed execution of small code fragments.
- Has a reported 0.06 ms startup in the retained comparison graphic.
- Trades language and module compatibility for startup speed and a smaller execution surface.

## Evidence
- Runtime category: [[unikernel-agent]] identifies Monty as a partial-Python interpreter and compares it with containers, WebAssembly, Starlark, services, and unrestricted local Python.
- Reported speed: [[unikernel-agent]] retains a graphic listing 0.06 ms startup alongside qualitative security, setup, file-mounting, and snapshot properties.
- Compatibility limit: [[unikernel-agent]] says the supported subset excludes classes and modules such as `sys`.

## Qualifications
The article explicitly calls the comparison casual and says the sandboxing-service row combines technically different products. It supplies no benchmark method, hardware, version, workload, memory result, security audit, or compatibility suite. The 0.06 ms figure should therefore be treated as source-scoped rather than as a like-for-like production comparison.

## What Changed
- Created a source-bounded profile of Monty's startup and compatibility tradeoff.

## Relationships
- [[Unikernel]] - alternative attempt to combine small execution environments with greater native-language compatibility.
- [[AgenticSandboxInfrastructure]] - may use restricted interpreters when a full operating-system sandbox is unnecessary.
- [[MicroVM]] - stronger general-purpose compatibility boundary with higher initialization and image costs.
