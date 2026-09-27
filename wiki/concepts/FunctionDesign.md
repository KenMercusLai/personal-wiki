---
title: "Function Design"
type: concept
tags: [software-quality, python, programming]
sources:
  - bob-belderbos-10-tips-to-write-better-functions-in-python
  - do-one-thing
last_updated: 2026-09-27
knowledge_schema: synthesis-v1
---

## Definition
[[FunctionDesign]] is the practice of shaping individual functions so their names, responsibilities, inputs, outputs, state effects, and defaults make behavior easy to read, reuse, test, and maintain.

## Current Synthesis
Belderbos frames functions as Python's primary building blocks: they package input, transformation, and output while giving code modularity, scope boundaries, reuse, documentation hooks, and testability. Good function design is therefore not only a local readability preference; it is a small-scale form of [[InternalSoftwareQuality]].

The practical center of gravity is interface discipline. A function should usually expose a small argument surface, validate bad input early, keep variables close to use, use Python's argument controls where they clarify calls, and make return types predictable. Type hints strengthen this interface by making expected inputs and outputs visible to readers and tools.

“Do one thing” is a useful design question but not an objective sizing test. Batchelder shows that several operations can be grouped as one responsibility at a chosen abstraction level, and that a seemingly cohesive unit can later yield a better boundary when new reuse or change needs appear. Function design should therefore compare clarity, coherence, reuse, testing, and change isolation rather than count steps or treat responsibility as binary compliance.

The strongest caution is about hidden state. Globals and mutable default arguments make function behavior depend on prior calls or outer-scope mutation, which undermines the clean input-transform-output model and makes bugs harder to localize.

## Key Claims
- Function names are a major readability surface and should describe behavior clearly.
- A function should usually have a coherent responsibility, a small interface, and early input validation.
- Keyword-only or positional-only arguments, type hints, and consistent return types can make function contracts clearer.
- Variables are easier to follow when they are defined close to where they are used.
- Hidden state from globals or mutable default arguments makes function behavior surprising.
- Small, isolated functions improve reuse and [[SoftwareVerification]] by making behavior easier to test.
- Responsibility boundaries require judgment and may change as surrounding uses reveal independently reusable behavior.

## Evidence
- Naming and responsibility: [[bob-belderbos-10-tips-to-write-better-functions-in-python]] recommends descriptive names and invokes the single-responsibility principle for function scope.
- Interface contract: [[bob-belderbos-10-tips-to-write-better-functions-in-python]] recommends small argument lists, sparse use of arbitrary args or keyword args, early validation, and clear caller contracts.
- Python API clarity: [[bob-belderbos-10-tips-to-write-better-functions-in-python]] points to keyword-only and positional-only arguments, type hints, and consistent return types as readability and tooling aids.
- State hazards: [[bob-belderbos-10-tips-to-write-better-functions-in-python]] warns against `global` and mutable default arguments because they create side effects or reused cross-call data.
- Testability link: [[bob-belderbos-10-tips-to-write-better-functions-in-python]] repeatedly connects modular, single-purpose functions with easier testing.
- Responsibility ambiguity: [[do-one-thing]] shows that operation count, names containing “and,” stakeholder counts, and reasons to change do not produce a mechanical boundary test.
- Evolutionary boundary: [[do-one-thing]] uses Zellij's `PointMap`-to-`Defuzzer` refactoring to show how new reuse needs can reveal a smaller, more useful abstraction.

## Counterevidence & Qualifications
The sources offer practitioner heuristics rather than universal laws. A 15-line pause point and return-type consistency are useful defaults, while “one thing” is inherently interpretive. Excessive splitting can scatter a coherent flow across many tiny units; real systems may also need exceptions for performance, API compatibility, framework conventions, or clarity at a larger scale.

## What Changed
- Reframed “do one thing” from a simple rule into a judgment-dependent, change-sensitive heuristic.
- Added reuse pressure and surrounding-code evolution as signals for revisiting a function boundary.

## Related Concepts
- [[InternalSoftwareQuality]] - function design is a local code-quality practice that can lower change cost.
- [[SoftwareVerification]] - small explicit functions are easier to test and reason about.
- [[PythonConcurrencyLibraries]] - Python functions may become task boundaries in concurrent or distributed code.
- [[DeveloperTooling]] - type hints and strict interfaces give tools more useful structure to inspect.
- [[SingleResponsibilityPrinciple]] - supplies the responsibility heuristic while making its ambiguity explicit.
