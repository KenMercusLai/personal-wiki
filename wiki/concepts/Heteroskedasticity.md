---
title: "Heteroskedasticity"
type: concept
tags: [statistics, regression, inference]
sources:
  - li-jie-wu-cha-luo-li-li-de-shu-ju-zhong-xin
last_updated: 2026-09-12
knowledge_schema: synthesis-v1
---

## Definition
[[Heteroskedasticity]] is a regression condition where the error variance differs across observations or groups instead of remaining roughly constant.

## Current Synthesis
RORIRI explains heteroskedasticity through two body-fat measurement channels: noisier home body-fat scales and more stable DEXA scans. Both groups can have zero-mean errors, so the model's direction may still converge correctly, but the spread of errors differs structurally. If the model treats every residual as equally reliable, its uncertainty estimates are built on the wrong assumption and the analyst loses a trustworthy measure of how much to believe the coefficient.

## Key Claims
- Error can satisfy a zero-mean condition while still having unequal variance across groups.
- Unequal measurement quality is one intuitive source of heteroskedasticity.
- Heteroskedasticity does not necessarily reverse coefficient direction or make every coefficient inconsistent.
- It can break the standard errors, uncertainty estimates, and confidence judgments used to interpret results.
- Residual diagnostics only inspect a proxy for true error, so the measurement design remains central.

## Evidence
- Unequal instruments: [[li-jie-wu-cha-luo-li-li-de-shu-ju-zhong-xin]] contrasts noisy home body-fat scales with controlled DEXA measurement.
- Zero-mean distinction: [[li-jie-wu-cha-luo-li-li-de-shu-ju-zhong-xin]] says both groups may average to zero error despite having different dispersion.
- Inference damage: [[li-jie-wu-cha-luo-li-li-de-shu-ju-zhong-xin]] argues that the coefficient can point in the right direction while the uncertainty ruler is broken.
- Residual limit: [[li-jie-wu-cha-luo-li-li-de-shu-ju-zhong-xin]] emphasizes that model diagnostics use residuals as estimates of unobserved errors.

## Counterevidence & Qualifications
The source gives an intuition for why unequal error variance matters but does not cover formal tests, robust standard errors, weighted least squares, or model-based remedies. It also distinguishes direction from uncertainty, so the concept should not be flattened into a claim that heteroskedasticity always invalidates every coefficient estimate.

## What Changed
- Created this concept to capture the article's unequal-error-variance inference warning.

## Related Concepts
- [[StatisticalError]] - heteroskedasticity is a pattern in the distribution of model error.
- [[StatisticalModelThinking]] - the concept shows why analysts must inspect uncertainty assumptions, not only coefficient direction.
- [[DataGeneratingProcess]] - differing measurement channels can create different error distributions.
- [[LLMDataAnalysis]] - automated analysis can overstate confidence when it misses violated regression assumptions.
