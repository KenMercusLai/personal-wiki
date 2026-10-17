---
title: "Solver-Aided Optimization"
type: concept
tags: [optimization, constraint-solving, bit-vectors, formal-methods, performance]
sources:
  - leap-year-three-instructions
last_updated: 2026-10-17
knowledge_schema: synthesis-v1
---

## Definition
[[SolverAidedOptimization]] uses a constraint solver to search implementation parameters or program forms that satisfy a behavioral specification, often over a bounded domain where exhaustive symbolic constraints are tractable.

## Current Synthesis
The leap-year case uses Z3 not to prove an arbitrary implementation after the fact, but to synthesize constants for a chosen expression template: multiply an unsigned year by a factor, mask the product, and compare it with a threshold. A bit-vector specification equates that candidate with the Gregorian divisibility rule for every year in a bounded range. Restricting the expression form makes an otherwise infeasible search over three 32-bit constants solvable and allows the author to extend the range until the first unavoidable failure.

The solver result is only the start of the engineering argument. Hüffner decomposes the constants into masked bit fields, relates those fields to divisibility by 4, 25, and 16, and explains the middle field through fixed-point approximation and modular arithmetic. Exhaustive enumeration exposes exactly where false residue classes enter or leave and why correctness ends at 102499. This combination of synthesis, human-readable derivation, and domain-specific verification is stronger than presenting opaque constants alone.

Performance remains a separate question from correctness. The synthesized predicate removes data-dependent branches and wins on random years in one microbenchmark, but predictable branching is slightly faster for a repeated contemporary year. Solver-aided optimization is therefore most useful when its validity domain, machine arithmetic, maintainability cost, compiler behavior, and representative workload are all explicit.

## Key Claims
- A restricted expression grammar can turn implementation design into a tractable parameter-synthesis problem.
- Fixed-width bit-vector constraints can model unsigned multiplication, remainder, masking, and comparison exactly.
- Bounded-domain synthesis can exploit application limits that general-purpose compiler optimizations must usually preserve.
- Solver-produced constants need a derivation that explains which logical conditions their bit fields encode.
- Correctness, optimality within the chosen form, and practical performance are distinct claims requiring different evidence.
- A fast bounded implementation must make its first invalid input and arithmetic assumptions visible to callers and maintainers.

## Evidence
Synthesis and verification:
- [[leap-year-three-instructions]] asks Z3 to equate the candidate expression with the leap-year specification for every year through a chosen bound.
- [[leap-year-three-instructions]] reports a 32-bit solution correct for 0 through 102499 and a 64-bit form correct through 5965232499.

Interpretation:
- [[leap-year-three-instructions]] decomposes the mask and threshold into three ordered bit blocks that reproduce the leap-year decision sequence inside one unsigned comparison.
- [[leap-year-three-instructions]] explains the middle block as a 17-bit fixed-point approximation to 7/100 and enumerates residue-class transitions around its error accumulation.

Evaluation boundary:
- [[leap-year-three-instructions]] reports a gain for random inputs but a small loss for a fixed predictable year and calls for realistic enclosing benchmarks before adoption.

## Counterevidence & Qualifications
The evidence comes from one recreational optimization with a compact specification and a deliberately narrow candidate grammar. A solver can establish only the encoded property, arithmetic model, and input bound; it cannot supply omitted requirements such as readability, portability, calendar semantics, side-channel behavior, or realistic workload value. The reported optimality applies to the restricted expression form and bit width, not to every possible leap-year algorithm. Magic constants also raise review and maintenance costs even when their derivation is sound.

## What Changed
- Established bounded bit-vector synthesis as a way to exploit narrower application domains than general-purpose compilers can assume.
- Separated solver satisfaction, human explanation, expression-form optimality, and workload performance as distinct evidence layers.
- Added explicit first-invalid-input analysis as part of the correctness contract for range-limited arithmetic tricks.

## Related Concepts
- [[SoftwareVerification]] - supplies the distinction between an encoded proof obligation and broader software correctness.
- [[ModularCompilerArchitecture]] - situates solver-found low-level transformations within a larger compilation and optimization pipeline.
- [[PerformanceBudget]] - represents the user-facing constraint that should justify accepting a less transparent implementation.
- [[FalkHuffner]] - practitioner who demonstrates the method through the bounded leap-year predicate.
- [[DanielLemire]] - co-author of cited constant-remainder techniques that motivate the candidate arithmetic form.
