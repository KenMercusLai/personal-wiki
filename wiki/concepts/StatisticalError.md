---
title: "Statistical Error"
type: concept
tags: [statistics, regression, inference]
sources:
  - li-jie-wu-cha-luo-li-li-de-shu-ju-zhong-xin
last_updated: 2026-09-12
knowledge_schema: synthesis-v1
---

## Definition
[[StatisticalError]] is the unobserved gap between the world as measured or modeled and the fuller target truth that the analysis is trying to estimate.

## Current Synthesis
RORIRI frames statistical error as the cost of finite measurement and simplified modeling. A sample mean estimates a population value that is treated as fixed but inaccessible, so repeated samples produce random movement around it. Regression adds another layer: observed outcomes are split into the part the model explains and the part left outside the model. That leftover error may come from sampling design, omitted variables, measurement bias, or the deliberate choice not to model every small cause in the [[DataGeneratingProcess]].

## Key Claims
- Statistical error appears because analysts infer unobservable targets from finite, noisy samples.
- Sampling methods create biased error when the sample does not represent the target population.
- Model specification creates error when relevant real-world factors are left outside the model.
- The zero-mean error assumption is a design obligation, not something directly observable in the data.
- Residuals are estimates of error, not the true error itself.
- Error structure matters: constant offsets, correlated omitted causes, and unequal variance damage different parts of a model.

## Evidence
- Finite sampling: [[li-jie-wu-cha-luo-li-li-de-shu-ju-zhong-xin]] uses human average weight to show why a sample statistic moves across repeated draws while the target population value is fixed.
- Sampling bias: [[li-jie-wu-cha-luo-li-li-de-shu-ju-zhong-xin]] contrasts all humans with nearby high-school students to show how a non-representative sample can systematically miss the target.
- Model specification: [[li-jie-wu-cha-luo-li-li-de-shu-ju-zhong-xin]] presents observed outcomes as model-explained parts plus factors the model leaves unexplained.
- Zero-mean assumption: [[li-jie-wu-cha-luo-li-li-de-shu-ju-zhong-xin]] says errors can be positive or negative but must average to zero if estimates are to converge on the target.
- Residual proxy: [[li-jie-wu-cha-luo-li-li-de-shu-ju-zhong-xin]] distinguishes true error from residuals produced by an estimated model.
- Error structure: [[li-jie-wu-cha-luo-li-li-de-shu-ju-zhong-xin]] separates scale offsets, [[OmittedVariableBias]], and [[Heteroskedasticity]] by the different model judgments they corrupt.

## Counterevidence & Qualifications
The source uses intuitive regression examples rather than a full mathematical treatment of estimator properties. It also treats zero-mean error as a core condition, but practical modeling often needs additional assumptions about independence, functional form, measurement process, and uncertainty estimation.

## What Changed
- Created this concept to distinguish the general error term from residuals, sampling bias, omitted variables, and heteroskedasticity.

## Related Concepts
- [[StatisticalModelThinking]] - statistical error is the unexplained part that makes model thinking necessary.
- [[DataGeneratingProcess]] - the omitted pieces of the generating system become part of the model's error term.
- [[OmittedVariableBias]] - one damaging error case where omitted causes correlate with included predictors.
- [[Heteroskedasticity]] - one damaging error case where error variance differs across observations.
- [[LLMDataAnalysis]] - human analysts need error assumptions to evaluate AI-generated statistical work.
