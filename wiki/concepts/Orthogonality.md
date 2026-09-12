---
title: "Orthogonality"
type: concept
tags: [statistics, modeling]
sources:
  - li-jie-fang-cha-de-ke-jia-xing-luo-li-li-de-shu-ju-zhong-xin
last_updated: 2026-09-12
knowledge_schema: synthesis-v1
---

## Definition
[[Orthogonality]] is a zero-covariance relationship in which two variables' deviations do not share systematic linear movement within the data being analyzed.

## Current Synthesis
RORIRI distinguishes orthogonality from independence. Two variables can be independently generated in the ground-truth process while a finite sample still produces a nonzero sample correlation or covariance because of noise. This distinction matters for variance additivity: simple sums of variances require orthogonal observed variables, not merely a verbal claim that their data-generating processes were independent.

## Key Claims
- Orthogonality means zero covariance or zero correlation in the analyzed data.
- Independence describes the data-generating process, while orthogonality describes an observed mathematical relationship.
- Independently generated variables will not usually appear perfectly orthogonal in finite noisy samples.
- Variance components add cleanly only under orthogonality.
- LLMs can mislead learners when they collapse independence, sample noise, and orthogonality into one explanation.

## Evidence
- Independent simulation: [[li-jie-fang-cha-de-ke-jia-xing-luo-li-li-de-shu-ju-zhong-xin]] generates A and B without reference to each other yet still computes nonzero sample correlations.
- Additivity condition: [[li-jie-fang-cha-de-ke-jia-xing-luo-li-li-de-shu-ju-zhong-xin]] states that variance additivity holds in the simple sense only when all variables are orthogonal.
- LLM caution: [[li-jie-fang-cha-de-ke-jia-xing-luo-li-li-de-shu-ju-zhong-xin]] warns that many large language models misattribute the issue to sample size rather than the independence/orthogonality distinction.

## Counterevidence & Qualifications
In many statistical contexts, stronger independence assumptions imply zero population covariance, but the source is focused on finite observed samples and the practical interpretation of computed variance decompositions.

## What Changed
- Created this concept to preserve the source's distinction between data-generation independence and observed zero-covariance structure.

## Related Concepts
- [[VarianceAdditivity]] - simple variance additivity requires orthogonal components.
- [[Covariance]] - orthogonality is the zero-covariance case.
- [[DataGeneratingProcess]] - independence belongs to the generating process, while orthogonality is checked in data.
- [[LLMDataAnalysis]] - statistical explanations from LLMs need review for this kind of conceptual conflation.
