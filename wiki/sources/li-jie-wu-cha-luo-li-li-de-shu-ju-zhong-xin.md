---
title: "理解误差 | 螺莉莉的数据中心"
type: source
tags: [statistics, regression, data-analysis]
date: 2026-04-02
source_file: /mnt/ken_personal_wiki/Articles/理解误差 螺莉莉的数据中心.md
---

## Summary
RORIRI explains [[StatisticalError]] as the gap created when finite samples and simplified models try to infer an unobservable true population or true model. The article distinguishes sampling bias, model specification error, residuals as imperfect proxies for true error, [[OmittedVariableBias]], and [[Heteroskedasticity]] as separate ways statistical interpretation can go wrong.

## Key Claims
- Statistical work uses noisy, finite samples to infer population features that cannot be directly observed.
- Sampling error becomes biased when the sampled group systematically differs from the target population.
- [[StatisticalError]] also comes from model specification: omitted real-world factors remain outside the model and become part of the error term.
- The zero-mean error condition cannot be verified directly from data; it must be protected through design, sampling, and measurement choices.
- A constant measurement offset can bias the intercept and predictions without necessarily biasing the slope.
- [[OmittedVariableBias]] occurs when an omitted factor affects the outcome and is correlated with an included explanatory variable.
- [[Heteroskedasticity]] can leave coefficient direction intact while breaking the model's standard uncertainty estimates.

## Key Quotes
> "观测量 = 模型能解释的部分 + 模型解释不了的部分" - the article's regression-level version of model plus error.

> "残差不是误差本身" - the source's warning that diagnostics use residuals as a proxy for unobserved true errors.

## Connections
- [[RORIRI]] - author of the source.
- [[StatisticalModelThinking]] - the article turns model/error thinking into regression assumptions and diagnostic limits.
- [[DataGeneratingProcess]] - the true model is framed as an unreachable full system of factors behind observed outcomes.
- [[StatisticalError]] - central concept covering sampling error, model specification error, and residual proxy limits.
- [[OmittedVariableBias]] - slope-bias case where omitted factors correlate with included predictors.
- [[Heteroskedasticity]] - unequal error variance case where inference uncertainty becomes unreliable.
- [[LLMDataAnalysis]] - related warning that statistical work fails when method assumptions are not understood.

## Contradictions
- No direct contradiction with existing wiki pages. The source strengthens [[StatisticalModelThinking]] by separating bias in sampling, bias in model specification, residual diagnostics, and unequal error variance.
