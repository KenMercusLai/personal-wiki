---
title: "Score Function Estimator"
type: concept
tags: [probability, gradient-estimation, sampling, machine-learning]
sources:
  - policy-gradient
last_updated: 2026-10-15
knowledge_schema: synthesis-v1
---

## Definition
The [[ScoreFunctionEstimator]] expresses the parameter gradient of an expectation as $\nabla_\theta\mathbb{E}_{p_\theta}[f(x)]=\mathbb{E}_{p_\theta}[f(x)\nabla_\theta\log p_\theta(x)]$, allowing it to be estimated from samples of a parameterized distribution.

## Current Synthesis
The estimator follows by differentiating the expectation, applying the [[LogDerivativeTrick]], and recognizing the resulting integral as an expectation under $p_\theta$. A sample average of $f(x_i)\nabla_\theta\log p_\theta(x_i)$ then supplies a stochastic gradient. [[PolicyGradient]] is a sequential instance: the sampled variable is a trajectory, the function is its return, and the score decomposes into a sum of action log-probability gradients when environment dynamics are parameter-independent.

## Key Claims
- The estimator handles objectives whose sampling distribution depends on the optimized parameters.
- It requires only samples, evaluated returns or function values, and differentiable log probabilities.
- The estimator remains applicable when sampled outcomes or environment transitions are not differentiable with respect to the policy parameters.
- Its basic trajectory form is unbiased under the stated identity and interchange assumptions but can have high variance.

## Evidence
- General derivation: [[policy-gradient]] converts the gradient of $\mathbb{E}_{p(x;\theta)}[f(x)]$ into an expectation of a log-probability gradient weighted by $f(x)$.
- Reinforcement-learning instance: [[policy-gradient]] substitutes trajectories and returns, then decomposes the trajectory score into policy-controlled action terms.

## Counterevidence & Qualifications
The source does not state the regularity conditions for moving a derivative through an integral, and one intermediate displayed line contains an apparent $d(x)$-for-$f(x)$ typo. It also does not cover variance-reduction baselines, control variates, reward-to-go, off-policy correction, or reparameterization estimators. The plain estimator's high variance can make a mathematically valid gradient too noisy for efficient learning.

## What Changed
- Added the general likelihood-ratio gradient identity.
- Added its sample-based interpretation and differentiability advantage.
- Added the trajectory-level policy-gradient specialization and variance boundary.

## Related Concepts
- [[LogDerivativeTrick]] - supplies the algebraic identity behind the estimator.
- [[MonteCarloEstimation]] - turns the resulting expectation into a finite-sample average.
- [[PolicyGradient]] - specializes the estimator to policy-generated trajectories and rewards.
- [[ReinforcementLearning]] - supplies the sequential decision objective used in the specialization.
