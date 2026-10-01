---
title: "Futamura Projections"
type: concept
tags: [programming-languages, compilers, partial-evaluation]
sources:
  - ray-eldath-ji-suan-ji-ling-yu-de-san-ge-zhong-yao-si-xiang-chou-xiang-fen-ceng-he-gao-jie
last_updated: 2026-10-01
knowledge_schema: synthesis-v1
---

## Definition
The [[FutamuraProjections]] are three staged uses of a self-applicable partial evaluator that derive a compiled target program from an interpreter and source, a compiler from a partial evaluator and interpreter, and a compiler generator from a partial evaluator specialized with respect to itself.

## Current Synthesis
The projections expose compilation as repeated program specialization. In the first, fixing an interpreter's source-program input produces a residual target program for later runtime input. In the second, fixing the interpreter input of a partial evaluator produces a compiler that can accept source programs. In the third, specializing the partial evaluator with respect to itself produces a generator that accepts interpreters and emits compilers.

The sequence is a strong example of higher-order reasoning because the tool performing transformation is also a program eligible for transformation. The elegance of the derivation does not imply “free” production compilers under arbitrary conditions: self-applicability, binding-time information, termination, semantic preservation, specialization cost, and residual-code quality remain decisive engineering constraints.

## Key Claims
- The first projection specializes an interpreter with respect to a source program and yields a target program.
- The second projection specializes a partial evaluator with respect to an interpreter and yields a compiler.
- The third projection specializes a partial evaluator with respect to itself and yields a compiler generator.
- Each projection shifts one input from runtime work into an earlier specialization stage.
- The construction depends on a suitable self-applicable specializer rather than on currying alone.

## Evidence
- First projection: [[ray-eldath-ji-suan-ji-ling-yu-de-san-ge-zhong-yao-si-xiang-chou-xiang-fen-ceng-he-gao-jie]] fixes interpreter and source, then identifies the residual program as compiled code awaiting runtime input.
- Second projection: [[ray-eldath-ji-suan-ji-ling-yu-de-san-ge-zhong-yao-si-xiang-chou-xiang-fen-ceng-he-gao-jie]] fixes the partial evaluator's interpreter input and identifies the residual program as a compiler awaiting source code.
- Third projection: [[ray-eldath-ji-suan-ji-ling-yu-de-san-ge-zhong-yao-si-xiang-chou-xiang-fen-ceng-he-gao-jie]] applies the same higher-order move to the partial evaluator itself and identifies the result as a compiler generator.

## Counterevidence & Qualifications
The essay intentionally simplifies the projections for exposition. It does not provide formal notation, an executable specializer, proof of equivalence, or measurements of generated-code quality. The phrase “compiler for free” hides the difficult work required to construct an effective interpreter and self-applicable partial evaluator. The source also gestures toward further projections without resolving whether they are useful or distinct under formal treatment.

## What Changed
- Created the concept with the three projection stages and the practical constraints hidden by the “free compiler” intuition.

## Related Concepts
- [[PartialEvaluation]] - specialization mechanism from which all three projections are derived.
- [[HigherOrderAbstraction]] - explains why a program transformer can itself become transformation input.
- [[FunctionalProgramming]] - supplies first-class function and partial-application intuitions used in the exposition.
- [[SoftwareAbstraction]] - makes interpreter, compiler, and specializer roles composable as input-output relationships.
- [[SoftwareVerification]] - provides the semantic-preservation obligation for generated residual programs.
