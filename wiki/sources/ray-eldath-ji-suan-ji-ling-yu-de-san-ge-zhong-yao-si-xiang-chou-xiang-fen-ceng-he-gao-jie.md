---
title: "计算机领域的三个重要思想：抽象，分层和高阶"
type: source
tags: [programming, abstraction, layering, higher-order-computation]
date: 2021-03-06
source_file: "/mnt/ken_personal_wiki/Articles/Ray Eldath - 计算机领域的三个重要思想：抽象，分层和高阶.md"
---

## Summary
[[RayEldath]] presents [[SoftwareAbstraction]], layering, and [[HigherOrderAbstraction]] as related ways of managing and generating computational ideas. The essay's strongest practical claim is that abstractions remain useful without making implementation details disappear: [[AbstractionLeakage|Hyrum's Law]] predicts that sufficiently popular interfaces acquire dependencies on every observable behavior. Its higher-order section then uses currying and [[PartialEvaluation]] to explain the three [[FutamuraProjections]], while a 2024 edit retracts much of the original concern about whether industrial programmers need deep mathematical foundations to use abstractions effectively.

## Key Claims
- [[SoftwareAbstraction]] extracts reusable interfaces, structures, and names from concrete data, classes, and situations, but its value depends on helping people design or use programs rather than on mathematical terminology alone.
- A layer separates contract from implementation so callers can focus on a smaller surface, yet [[AbstractionLeakage]] means that observable behavior outside the stated contract can become a de facto dependency at sufficient scale.

![xkcd workflow complaints showing users depending on undocumented observable behavior after an update](../../wiki-assets/ray-eldath-ji-suan-ji-ling-yu-de-san-ge-zhong-yao-si-xiang-chou-xiang-fen-ceng-he-gao-jie/observable-behavior-workflow-breakage.png)

- TCP contention and row-versus-column array traversal illustrate how performance or failure can force programmers below network, virtual-machine, or cache abstractions.
- [[HigherOrderAbstraction]] applies a concept-forming process to objects of the same kind, producing forms such as functions of functions and types of types.
- Currying separates a multi-input computation into nested one-input functions; supplying only an initial subset of inputs produces partial application.
- [[PartialEvaluation]] specializes a program against known inputs and leaves a residual program for the remaining inputs.
- The [[FutamuraProjections]] successively specialize an interpreter, a partial evaluator with respect to an interpreter, and a partial evaluator with respect to itself, yielding a compiled target program, a compiler, and a compiler generator.

## Key Quotes
> “随着一个层的用户逐渐增多，层逐渐失去了区隔契约和实现细节的作用” - on observable implementation behavior becoming depended upon.

> “抽象带来的效率提升，是以更大的学习负担（对实现细节的学习）为代价的” - the essay's strong conclusion about abstraction and professional expertise.

> “部分求值器作用于一个程序和它的一些参数，输出一个该程序对于这组参数‘特化’后的新的程序。” - the operational definition used to derive the Futamura projections.

## Connections
- [[RayEldath]] - author of the personal synthesis and its 2024 qualification.
- [[SoftwareAbstraction]] - general process of extracting reusable concepts and interfaces from concrete cases.
- [[AbstractionLeakage]] - explains why layer contracts cannot hide every operationally relevant behavior.
- [[HigherOrderAbstraction]] - recurring “A of A” construction used for functions, types, and program transformers.
- [[PartialEvaluation]] - specialization mechanism that turns known inputs into a residual program.
- [[FutamuraProjections]] - principal extended example of higher-order program transformation.
- [[FunctionalProgramming]] - supplies the higher-order functions, closures, currying, and partial-application vocabulary used in the explanation.
- [[EssentialAndAccidentalComplexity]] - related account of abstractions reducing, shifting, or creating implementation and learning costs.

## Contradictions
- The 2024 edit explicitly withdraws much of the original question about whether programmers need abstract algebra to understand monads and functors; it retains only the narrower objection to unnecessary jargon and notes that operational understanding can be sufficient for programming use.
- Hyrum's Law does not imply that layers are “meaningless” whenever one implementation detail matters. Interfaces can still reduce the amount most users must know, and the source provides examples rather than prevalence, comparative cost, or a threshold for when leakage dominates the benefit.
- Hyrum's Law and the Law of Leaky Abstractions are closely related in the essay but are not identical formulations: the former concerns dependencies on observable behavior at scale, while the latter more broadly says non-trivial abstractions leak.
- The TCP, cache-locality, PyPy, and GraalVM cases are explanatory illustrations, not measured comparisons establishing that higher abstraction necessarily increases total learning burden or that the described virtual machines implement the simplified derivation exactly.
- The three projections are explained conceptually; the source does not cover binding-time analysis, staging correctness, termination, code quality, self-applicability requirements, or practical limits of partial evaluation.
