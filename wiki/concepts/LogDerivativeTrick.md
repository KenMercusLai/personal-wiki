---
title: "Log Derivative Trick"
type: concept
tags: [probability, gradients, machine-learning, reinforcement-learning]
sources:
  - policy-gradient
last_updated: 2026-10-15
knowledge_schema: synthesis-v1
---

## Definition
The [[LogDerivativeTrick]] is the identity $\nabla_\theta p(x;\theta)=p(x;\theta)\nabla_\theta\log p(x;\theta)$, obtained by applying the chain rule to the logarithm of a differentiable positive probability density or mass function.

## Current Synthesis
The identity is useful when model parameters affect the distribution from which a variable is sampled. A raw derivative $\nabla_\theta p(x;\theta)$ is not itself a probability distribution, but multiplying the log-probability gradient by $p(x;\theta)$ places a valid sampling measure back into the integral. This converts the derivative of an expectation into a [[ScoreFunctionEstimator]] that [[MonteCarloEstimation]] can approximate. In [[PolicyGradient]], the same move turns a trajectory-probability derivative into an expectation over sampled trajectories.

## Key Claims
- The identity follows directly from $\nabla_\theta\log p=(\nabla_\theta p)/p$ where the logarithm is defined.
- Its main computational value is restoring the sampling distribution inside a differentiated expectation.
- It permits gradient estimation without differentiating through the sampled outcome itself.
- Applied to trajectory probabilities, logarithms turn products of action and transition factors into sums.

## Evidence
- General identity and estimator: [[policy-gradient]] derives the chain-rule identity and substitutes it into the derivative of an expected function.
- Trajectory application: [[policy-gradient]] factors $\pi_\theta(\tau)$ and removes initial-state and environment-transition gradients when those terms are independent of $\theta$.

## Counterevidence & Qualifications
The identity is exact under the regularity assumptions needed to exchange differentiation and integration, but the source invokes Leibniz's rule without detailing those assumptions. The resulting Monte Carlo estimator can have high variance, and zero-probability events require care because $\log p$ is undefined there. The trick enables an estimator; it does not by itself supply baselines, credit assignment, variance control, or stable policy updates.

## What Changed
- Added the exact chain-rule identity and its domain boundary.
- Added its role in restoring a probability measure for sampling.
- Connected the general estimator to factorized trajectory probabilities.

## Related Concepts
- [[ScoreFunctionEstimator]] - is the expectation-gradient estimator produced by applying this identity.
- [[MonteCarloEstimation]] - approximates the resulting expectation from samples.
- [[PolicyGradient]] - applies the identity to the distribution of policy-generated trajectories.
- [[ReinforcementLearning]] - provides the policy and return objective in the tutorial's main application.
