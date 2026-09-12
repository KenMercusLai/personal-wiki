---
title: "Variance Additivity"
type: concept
tags: [statistics, modeling]
sources:
  - li-jie-fang-cha-de-ke-jia-xing-luo-li-li-de-shu-ju-zhong-xin
last_updated: 2026-09-12
knowledge_schema: synthesis-v1
---

## Definition
[[VarianceAdditivity]] is the property that the variance of a sum can be decomposed into component variances plus covariance terms, reducing to a simple sum of variances only when the components are orthogonal.

## Current Synthesis
RORIRI treats variance additivity as useful but often oversimplified. For two variables, the variance of A+B equals the variance of A plus the variance of B plus twice their covariance; for A-B, the covariance term changes sign. The simple classroom version works only when covariance is zero, so the practical lesson is to inspect joint variation rather than treating component effects as independent blocks.

## Key Claims
- Variance is useful because it measures dispersion after signed deviations are squared.
- Total variance can be decomposed, but covariance terms are part of that decomposition.
- For A+B, ignoring covariance explains why simulated examples rarely equal the naive variance sum exactly.
- For A-B, the squared nature of variance still makes covariance the key correction term.
- Variance is favored in many statistical models because squaring supports clean algebraic decomposition.

## Evidence
- Two-variable simulation: [[li-jie-fang-cha-de-ke-jia-xing-luo-li-li-de-shu-ju-zhong-xin]] shows that A+B does not always match Var(A)+Var(B) exactly in finite samples.
- Covariance correction: [[li-jie-fang-cha-de-ke-jia-xing-luo-li-li-de-shu-ju-zhong-xin]] adds `2 * cov(a, b)` and gets the value matching the variance of the combined variable.
- Multi-variable matrix: [[li-jie-fang-cha-de-ke-jia-xing-luo-li-li-de-shu-ju-zhong-xin]] represents a four-variable system as a covariance matrix containing both diagonal variances and off-diagonal covariances.

## Counterevidence & Qualifications
The source's examples use simple additive simulated variables. Real models may include nonlinear transformations, interactions, measurement error, sampling design, or distributional assumptions that require more than the basic variance-of-sums formula.

## What Changed
- Created this concept to anchor the wiki's explanation of when variance components do and do not add cleanly.

## Related Concepts
- [[Covariance]] - covariance terms determine whether component variances add naively.
- [[Orthogonality]] - simple additivity requires zero covariance between components.
- [[DataGeneratingProcess]] - the generating system determines whether variables share variation.
- [[StatisticalModelThinking]] - variance additivity is a concrete example of formula learning needing model interpretation.
