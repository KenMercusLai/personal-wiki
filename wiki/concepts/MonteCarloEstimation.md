---
title: "Monte Carlo Estimation"
type: concept
tags: [probability, statistics, sampling, machine-learning]
sources:
  - policy-gradient
  - rlbook
last_updated: 2026-10-22
knowledge_schema: synthesis-v1
---

## Definition
[[MonteCarloEstimation]] approximates an expectation under a probability distribution with an empirical average of values computed from samples drawn from that distribution.

## Current Synthesis
For samples $x_i\sim p(x)$, the sources move from $\mathbb{E}_{p}[f(x)]$ to $\frac{1}{n}\sum_i f(x_i)$. In value prediction, an episodic agent waits for a complete return and averages returns observed after visiting a state. In [[PolicyGradient]], after the [[LogDerivativeTrick]] rewrites an awkward derivative as an expectation, complete trajectories estimate that gradient. The conversion supplies computability, not exactness; finite-sample variance, sample dependence, and delayed outcomes still govern the estimate.

## Key Claims
- A sample average can approximate an expectation when samples come from the distribution named by that expectation.
- The method applies to functions of a random variable as well as to the random variable itself.
- Rewriting a gradient as an expectation makes sample-based optimization possible but does not guarantee a low-variance estimate.
- In vanilla policy gradients, complete policy-generated trajectories are the samples and return-weighted log-probability gradients are the measured quantities.
- In episodic value prediction, complete realized returns provide samples of a state's policy-conditioned expected return without bootstrapping from another estimate.

## Evidence
- Expectation-to-average conversion: [[policy-gradient]] derives the empirical estimator for both $x$ and $f(x)$ from samples $x_i\sim p(x)$.
- Policy-gradient application: [[policy-gradient]] samples trajectories from $\pi_\theta$ after converting the objective gradient into an expectation through the score-function identity.
- Return-based value estimation: [[rlbook]] contrasts complete-return Monte Carlo updates with model-weighted dynamic programming and bootstrapped one-step or n-step TD targets.

## Counterevidence & Qualifications
The sources are introductory notes rather than a statistical treatment of consistency, convergence rates, correlated samples, importance sampling, or uncertainty intervals. The RL notebook is mostly AI-generated explanation and is not independently checked. Complete returns may require waiting for termination and can have high variance, while the policy-gradient example uses sparse full-trajectory returns. Monte Carlo estimability therefore does not imply practical sample efficiency or reliable optimization.

## What Changed
- Added complete episodic returns as value-function samples.
- Distinguished non-bootstrapped Monte Carlo targets from TD and dynamic-programming targets.
- Extended the variance boundary to delayed and dependent trajectory samples.

## Related Concepts
- [[LogDerivativeTrick]] - rewrites derivatives so the target expression becomes an expectation suitable for sampling.
- [[ScoreFunctionEstimator]] - combines Monte Carlo sampling with log-probability gradients.
- [[PolicyGradient]] - applies trajectory sampling to optimize expected return.
- [[ReinforcementLearning]] - supplies the sequential environments and reward-bearing trajectories in the source's application.
- [[TemporalDifferenceLearning]] - replaces the unobserved tail of a return with a current successor-value estimate.
