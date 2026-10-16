---
title: "Static Single Assignment"
type: concept
tags: [compilers, intermediate-representation, dataflow, optimization]
sources:
  - llvm-compiler
last_updated: 2026-10-17
knowledge_schema: synthesis-v1
---

## Definition
[[StaticSingleAssignment|Static Single Assignment (SSA)]] is an intermediate-representation discipline in which each variable-like value has one definition, with explicit merge operations representing values that arrive from different control-flow paths.

## Current Synthesis
LLVM IR integrates partial SSA form with a control-flow graph for each function and represents merges through explicit Phi instructions. The form makes definition-to-use flow explicit, simplifying many data-flow analyses and transformations. By replacing repeated mutable names with distinct values, SSA also removes false anti-dependencies and output dependencies that would otherwise constrain safe instruction reordering.

SSA is an enabling representation choice rather than a complete optimizer. Correct construction and maintenance still depend on control-flow analysis, memory effects require additional modeling, and transformations must preserve language and machine semantics beyond local value flow.

## Key Claims
- Single definitions make value provenance and use chains explicit.
- Phi operations represent control-flow-dependent value merges.
- SSA simplifies many local-variable data-flow optimizations.
- Renaming removes false dependencies that inhibit reordering.
- SSA works with, rather than replaces, a function's control-flow graph.
- Memory, aliasing, exceptions, and concurrency require analysis beyond basic SSA values.

## Evidence
LLVM design:
- [[llvm-compiler]] identifies partial SSA plus a per-function control-flow graph as a founding property of LLVM IR.

Optimization mechanism:
- [[llvm-compiler]] explains explicit Phi instructions, definition-to-use flow, and elimination of spurious anti-dependencies and output dependencies.

Historical context:
- [[llvm-compiler]] contrasts LLVM's early pervasive SSA design with GCC, whose cited SSA support appeared in GCC 4.0 in 2005.

## Counterevidence & Qualifications
The source provides an architectural explanation, not a comparative benchmark isolating SSA's effect on compile time, code quality, or implementation complexity. Its historical contrast with GCC should not be read as a current capability comparison. SSA's benefits depend on the surrounding IR, analyses, pass pipeline, and treatment of memory and exceptional control flow.

## What Changed
- Established SSA's role in LLVM IR and optimization.
- Added explicit Phi merges and dependency-removal mechanisms.
- Bounded the concept against broader memory and control semantics.

## Related Concepts
- [[LLVMIntermediateRepresentation]] - uses partial SSA as its core value-flow discipline.
- [[LLVM]] - production infrastructure applying SSA across analyses and transformations.
- [[ModularCompilerArchitecture]] - allows multiple passes to consume and preserve SSA structure.
- [[LifelongCompilation]] - retains an SSA-based representation for optimization at later stages.
