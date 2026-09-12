---
title: "Omitted Variable Bias"
type: concept
tags: [statistics, regression, inference]
sources:
  - li-jie-wu-cha-luo-li-li-de-shu-ju-zhong-xin
last_updated: 2026-09-12
knowledge_schema: synthesis-v1
---

## Definition
[[OmittedVariableBias]] is regression bias that occurs when a left-out factor affects the outcome and is correlated with an included explanatory variable.

## Current Synthesis
RORIRI uses calorie intake, exercise, and body weight to show why omitted variables are not merely missing detail. If exercise affects weight and is also related to calorie intake, the error term carries exercise's effect while moving with the predictor. The model can no longer distinguish the effect of calorie intake from the hidden effect of exercise, so the slope absorbs a mixed relationship rather than the intended causal association.

## Key Claims
- Omitted variables become part of the model's error term.
- Omission is especially damaging when the omitted factor affects the outcome and correlates with an included predictor.
- In that case, the slope estimate can become biased rather than only noisy.
- More optimization or fitting cannot separate two effects that the model specification has already merged.
- Omitted-variable reasoning links regression interpretation back to the underlying [[DataGeneratingProcess]].

## Evidence
- Hidden exercise effect: [[li-jie-wu-cha-luo-li-li-de-shu-ju-zhong-xin]] says exercise affects weight while also being associated with calorie intake.
- Slope contamination: [[li-jie-wu-cha-luo-li-li-de-shu-ju-zhong-xin]] argues that the fitted calorie coefficient then mixes calorie and exercise effects.
- Specification limit: [[li-jie-wu-cha-luo-li-li-de-shu-ju-zhong-xin]] frames the problem as a model-design error rather than a failure that optimization can repair.
- DGP dependence: [[li-jie-wu-cha-luo-li-li-de-shu-ju-zhong-xin]] roots the omitted-variable question in the full list of factors that actually produce body weight.

## Counterevidence & Qualifications
The source explains the mechanism conceptually and does not provide formal identification tests or remedies. In practice, omitted-variable bias depends on the omitted factor's relationship with both the outcome and included predictors; not every omitted detail creates the same kind of bias.

## What Changed
- Created this concept to capture the article's central slope-bias case.

## Related Concepts
- [[StatisticalError]] - omitted variables enter the unexplained part of a model.
- [[DataGeneratingProcess]] - omitted-variable analysis asks which real causes were left outside the model.
- [[StatisticalModelThinking]] - the concept shows why model interpretation depends on assumptions, not just fitted coefficients.
- [[PHacking]] - biased specification search can exploit or hide omitted-variable problems.
- [[LLMDataAnalysis]] - AI-generated analyses can miss omitted-variable structure when they focus on polished outputs.
