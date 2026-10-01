---
title: "Partial Evaluation"
type: concept
tags: [programming-languages, compilers, program-transformation]
sources:
  - ray-eldath-ji-suan-ji-ling-yu-de-san-ge-zhong-yao-si-xiang-chou-xiang-fen-ceng-he-gao-jie
last_updated: 2026-10-01
knowledge_schema: synthesis-v1
---

## Definition
[[PartialEvaluation]] specializes a source program with respect to inputs known in advance, producing a residual program that accepts the remaining inputs.

## Current Synthesis
The source introduces partial evaluation through partial application: if a computation consumes a program and runtime input, fixing the program in advance can leave a new computation waiting only for runtime data. Applied to an interpreter, specialization with respect to source code produces a target or residual program whose later execution yields the same output expected from interpreting that source against the remaining input.

This makes partial evaluation a bridge between interpretation and compilation, but it is not merely currying. A useful specializer must analyze what can be computed early, preserve the meaning of the original computation, generate residual code, and avoid non-termination or harmful code growth. Those requirements are outside the essay's simplified derivation and bound its practical claims.

## Key Claims
- A partial evaluator consumes a program plus some known inputs and emits a specialized residual program.
- The residual program accepts the inputs that were not fixed during specialization.
- Specializing an interpreter with respect to source code can produce a compiled target program.
- Interpreters and partial evaluators are themselves programs and can therefore become specialization inputs.
- Practical specialization requires more than ordinary currying or partial application.

## Evidence
- Operational definition: [[ray-eldath-ji-suan-ji-ling-yu-de-san-ge-zhong-yao-si-xiang-chou-xiang-fen-ceng-he-gao-jie]] defines source and residual programs and describes specialization against a subset of parameters.
- Interpreter case: [[ray-eldath-ji-suan-ji-ling-yu-de-san-ge-zhong-yao-si-xiang-chou-xiang-fen-ceng-he-gao-jie]] fixes source code as one interpreter input and identifies the residual program with compiled execution over later input.
- Recursion into tools: [[ray-eldath-ji-suan-ji-ling-yu-de-san-ge-zhong-yao-si-xiang-chou-xiang-fen-ceng-he-gao-jie]] then specializes partial evaluators with respect to interpreters and themselves to derive the later Futamura projections.

## Counterevidence & Qualifications
The source is a conceptual exposition, not an implementation or correctness proof. It omits binding-time analysis, staging annotations, effects, termination, residual-code quality, specialization overhead, self-applicability, and the conditions under which the result behaves like a practical compiler. Its references to PyPy and GraalVM are motivating industry analogies and should not be read as proof that their current architectures are literally the simple two-input construction described here.

## What Changed
- Created the concept around program specialization and the residual-program boundary, with explicit limits on the currying analogy.

## Related Concepts
- [[HigherOrderAbstraction]] - provides the mental move for treating program transformers as transformable programs.
- [[FutamuraProjections]] - derives compiled programs, compilers, and compiler generators through successive specialization.
- [[FunctionalProgramming]] - supplies partial-application vocabulary used as the introductory analogy.
- [[SoftwareAbstraction]] - lets interpreters and specializers be treated through stable input-output roles.
- [[SoftwareVerification]] - meaning preservation is essential when transforming a source program into residual code.
