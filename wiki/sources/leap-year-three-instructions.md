---
title: "A leap year check in three instructions"
type: source
tags: [bit-twiddling, compiler-optimization, z3, calendrical-algorithms, benchmarking]
date: 2025-05-15
source_file: "/mnt/ken_personal_wiki/Articles/leap-year-three-instructions.md"
---

## Summary
[[FalkHuffner|Falk Hüffner]] derives a branchless 32-bit leap-year predicate that uses one multiplication, one bitwise AND, and one unsigned comparison and is correct for years 0 through 102499. The article first reduces the conventional Gregorian test through divisibility facts and compiler-style constant-modulo lowering, then explains how Z3 found a range-limited packed predicate whose masked product encodes the tests for divisibility by 4, 25, and 16. The result is faster for random inputs in one microbenchmark but slightly slower than predictable branching for a fixed year, making it an instructive [[SolverAidedOptimization]] case rather than a universal replacement.

## Key Claims
- Once divisibility by 4 is known, testing divisibility by 100 can be reduced to divisibility by 25; once divisibility by 25 is known, testing divisibility by 400 can be reduced to divisibility by 16.
- Compilers can replace constant modulo with multiplication, comparison, and masking, so handwritten magic-number C usually adds little when GCC or Clang already performs the lowering.
- Z3 can search the 96-bit parameter space of `((y * f) & m) <= t` by expressing the desired leap-year behavior as bit-vector constraints over a bounded input domain.
- The 32-bit constants are correct only through year 102499: at 102500 the masked fixed-point approximation stops identifying every multiple of 100.
- A related 64-bit construction is correct through year 5965232499, covering every 32-bit year; the article reports that Code Golf contributors later proved this range optimal for the searched form.
- On the reported i7-8700K benchmark, the three-instruction predicate took 0.69 ns for both fixed and random inputs, versus 0.65 ns and 2.61 ns respectively for the conventional branching implementation.
- Microbenchmark advantage does not by itself justify production adoption because realistic years are often predictable, the check is normally a tiny subroutine, and the optimized predicate has a non-obvious validity boundary.

## Key Quotes
> "To fully justify a change, ideally we would have a benchmark with realistic data" — qualification on replacing conventional calendar code.

## Connections
- [[FalkHuffner]] - author who constructed, benchmarked, and explained the bounded predicate.
- [[SolverAidedOptimization]] - Z3 searches constants under bit-vector constraints and supports optimality arguments for the restricted expression form.
- [[SoftwareVerification]] - exhaustive bounded comparison and solver proofs establish correctness only for an explicitly stated domain.
- [[DanielLemire]] - co-author of cited work on lowering constant remainder computations through multiplication.

## Contradictions
- The source metadata records publication on 1 May 2025 while the displayed article date is 15 May 2025; this note uses the displayed date.
- The headline's "about 3 CPU instructions" describes the compiled arithmetic form, not a portable C execution guarantee across architectures and compilers.
- The 3.8× random-input speedup is hardware-, compiler-, flag-, workload-, and microbenchmark-specific; the same result is about 6% slower for the perfectly predictable fixed input.
