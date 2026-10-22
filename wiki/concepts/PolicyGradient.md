---
title: "Policy Gradient"
type: concept
tags: [reinforcement-learning, policy-optimization, neural-networks, monte-carlo]
sources:
  - policy-gradient
  - rlbook
last_updated: 2026-10-22
knowledge_schema: synthesis-v1
---

## Definition
[[PolicyGradient]] methods optimize the parameters of a policy directly by estimating how changes in action log probabilities affect expected return.

## Current Synthesis
The sources contrast a value-first method such as Q-learning with a stochastic neural policy $\pi_\theta(a\mid s)$ that emits action probabilities from the current state. The vanilla derivation defines expected trajectory return $J(\theta)$, applies the [[ScoreFunctionEstimator]] to the trajectory distribution, and factors that distribution into initial-state, action-policy, and environment-transition probabilities. Assuming the initial-state distribution and transition dynamics do not depend on $\theta$, only the sum of action log-probability gradients remains. Sampled trajectories therefore support gradient ascent on expected return, or equivalently gradient descent on a negative return-weighted log-probability loss. A state-dependent baseline can be subtracted without changing the expected gradient because the conditional expected policy score is zero; an appropriate baseline reduces variance, linking REINFORCE to actor-critic methods.

## Key Claims
- Direct policy optimization learns action probabilities rather than selecting actions only through an estimated state-action value.
- The objective is expected return over trajectories sampled from the current policy.
- The [[LogDerivativeTrick]] converts a trajectory-distribution derivative into an expectation that can be sampled.
- Parameter-independent initial-state and transition terms contribute zero to the trajectory log-probability gradient.
- A vanilla estimator reinforces every sampled action in proportion to the trajectory return, but this coarse credit assignment can have high variance.
- Automatic differentiation can optimize the negative sampled log-probability-weighted return as a loss.
- A baseline independent of the sampled action preserves the expected update and can reduce gradient variance, though an arbitrary baseline is not guaranteed to do so.

## Evidence
- Objective and estimator: [[policy-gradient]] defines $J(\theta)=\mathbb{E}_{\tau\sim\pi_\theta}[R(\tau)]$ and derives its likelihood-ratio gradient.
- Trajectory factorization: [[policy-gradient]] decomposes trajectory probability and removes the initial-state and transition terms under parameter independence.
- Implementation bridge: [[policy-gradient]] converts gradient ascent on expected return into a negative return-weighted log-probability loss for automatic differentiation.
- Baseline and variance: [[rlbook]] derives the zero-mean policy score and explains why subtracting a state baseline preserves expectation while a well-chosen baseline reduces second moment and variance.

## Counterevidence & Qualifications
The evidence consists of pedagogical notes, not a controlled comparison or primary algorithm paper; the newer notebook is largely AI-generated and not independently verified. The first estimator assigns the same undiscounted total trajectory return to each action and omits reward-to-go or advantage estimates. The notebook's variance discussion correctly needs a well-chosen baseline: expectation is unchanged for any action-independent state baseline, but variance is not guaranteed to fall for every choice. The material establishes the core mechanism rather than practical stability or sample efficiency. PPO and GRPO are named as later directions but are not derived or evaluated here.

## What Changed
- Added the state-dependent baseline identity and its conditional zero-score proof.
- Distinguished unbiasedness from guaranteed variance reduction.
- Connected vanilla REINFORCE to value-baseline actor-critic methods.

## Related Concepts
- [[ReinforcementLearning]] - is the broader reward-driven sequential decision framework.
- [[ScoreFunctionEstimator]] - provides the general likelihood-ratio gradient used for trajectories.
- [[LogDerivativeTrick]] - rewrites the trajectory-probability derivative into a sampleable expectation.
- [[MonteCarloEstimation]] - approximates the trajectory expectation using sampled episodes.
- [[GroupRelativePolicyOptimization]] - is a later critic-free policy-optimization method mentioned by the source.
- [[AsynchronousReinforcementLearning]] - changes how completed policy rollouts are scheduled and consumed.
- [[FunctionApproximation]] - supplies the parameterized policy and optional learned value baseline.
