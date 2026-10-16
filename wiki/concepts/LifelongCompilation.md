---
title: "Lifelong Compilation"
type: concept
tags: [compilers, optimization, jit, profile-guided-optimization]
sources:
  - llvm-compiler
last_updated: 2026-10-17
knowledge_schema: synthesis-v1
---

## Definition
[[LifelongCompilation]] preserves a program representation and useful analysis information so compilation and optimization can occur at source build, link, load, run, idle, or distribution time rather than at one fixed stage.

## Current Synthesis
The LLVM strategy uses persistent [[LLVMIntermediateRepresentation|LLVM IR]] as a bridge between traditional ahead-of-time compilation and managed-language-style dynamic optimization. A compiler can still perform expensive native code generation offline, while retained IR allows whole-program linking, user-site retargeting, runtime specialization, and profile-guided optimization based on deployed behavior. Because LLVM does not impose one object model, exception system, or runtime, the strategy can support different source languages and mobile-code formats.

Persistence is optional and carries tradeoffs. Shipping or retaining IR can increase artifact, compatibility, security-review, and toolchain obligations; late compilation adds work and operational responsibility at distribution or execution sites. The article offers influential production examples but does not quantify these costs across modern deployments.

## Key Claims
- Program information can remain available beyond source compilation instead of being irreversibly collapsed into machine code.
- Offline native generation and later dynamic optimization can coexist rather than being mutually exclusive.
- Runtime profiles can guide optimizations for an end user's actual workload.
- Language-neutral IR enables uniform optimization across modules, libraries, runtimes, and sometimes system code.
- Late native generation can retarget one distributed representation to multiple processor variants.
- Persistent IR creates additional compatibility, security, deployment, and resource tradeoffs.

## Evidence
Capability model:
- [[llvm-compiler]] defines persistent information, offline code generation, user-specific profiling, runtime transparency, and uniform whole-program compilation as the five-part strategy.

Architecture:
- [[llvm-compiler]] diagrams retained linked IR branching to developer-site native code, user-site native code, and JIT/runtime optimization with profile feedback.

Production examples:
- [[llvm-compiler]] describes Apple App Store IR distribution through 2022 and LLVM-based run-time or load-time generation for PTX, Python, and WebAssembly-related systems.

## Counterevidence & Qualifications
The article's claim that no other system offers the full five-property combination is an author judgment, and the comparison does not systematically evaluate contemporary compiler stacks. The Apple example is historical rather than evidence that IR distribution remains the best current design. Benefits depend on preserved semantic information, deployment trust, target diversity, profiling quality, compilation latency, and the ability to maintain compatibility between producer and consumer toolchains.

## What Changed
- Established the five-part lifelong-compilation capability model.
- Added concrete static, link-time, user-site, JIT, and profile-feedback flows.
- Added deployment, compatibility, and operational qualifications.

## Related Concepts
- [[LLVMIntermediateRepresentation]] - persistent representation enabling later compilation stages.
- [[LLVM]] - infrastructure implementing the strategy across production and research uses.
- [[ModularCompilerArchitecture]] - supplies reusable analyses and generators for different lifecycle stages.
- [[StaticSingleAssignment]] - supports optimization on the retained IR's value flow.
