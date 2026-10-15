---
title: "Policy Gradient"
type: concept
tags: [reinforcement-learning, policy-optimization, neural-networks, monte-carlo]
sources:
  - policy-gradient
last_updated: 2026-10-15
knowledge_schema: synthesis-v1
---

## Definition
[[PolicyGradient]] methods optimize the parameters of a policy directly by estimating how changes in action log probabilities affect expected return.

## Current Synthesis
The source contrasts a value-first method such as Q-learning with a stochastic neural policy $\pi_\theta(a\mid s)$ that emits action probabilities from the current state. Its vanilla derivation defines expected trajectory return $J(\theta)$, applies the [[ScoreFunctionEstimator]] to the trajectory distribution, and factors that distribution into initial-state, action-policy, and environment-transition probabilities. Assuming the initial-state distribution and transition dynamics do not depend on $\theta$, only the sum of action log-probability gradients remains. Sampled trajectories therefore support gradient ascent on expected return, or equivalently gradient descent on a negative return-weighted log-probability loss.

## Key Claims
- Direct policy optimization learns action probabilities rather than selecting actions only through an estimated state-action value.
- The objective is expected return over trajectories sampled from the current policy.
- The [[LogDerivativeTrick]] converts a trajectory-distribution derivative into an expectation that can be sampled.
- Parameter-independent initial-state and transition terms contribute zero to the trajectory log-probability gradient.
- A vanilla estimator reinforces every sampled action in proportion to the trajectory return, but this coarse credit assignment can have high variance.
- Automatic differentiation can optimize the negative sampled log-probability-weighted return as a loss.

## Evidence
- Objective and estimator: [[policy-gradient]] defines $J(\theta)=\mathbb{E}_{\tau\sim\pi_\theta}[R(\tau)]$ and derives its likelihood-ratio gradient.
- Trajectory factorization: [[policy-gradient]] decomposes trajectory probability and removes the initial-state and transition terms under parameter independence.
- Implementation bridge: [[policy-gradient]] converts gradient ascent on expected return into a negative return-weighted log-probability loss for automatic differentiation.

## Counterevidence & Qualifications
The evidence is one pedagogical tutorial, not a controlled comparison or primary algorithm paper. The displayed estimator assigns the same undiscounted total trajectory return to each action, omits a baseline or learned value function, and does not use reward-to-go or advantage estimates. The author explicitly notes sparse rewards and high variance, so the derivation establishes the core mechanism rather than practical stability or sample efficiency. PPO and GRPO are named as later directions but are not derived or evaluated.

## What Changed
- Added a direct derivation from expected trajectory return to a sample-based policy gradient.
- Distinguished policy-controlled action probabilities from parameter-independent environment dynamics.
- Added the automatic-differentiation loss interpretation.
- Preserved high variance and coarse credit assignment as explicit limits of the vanilla estimator.

## Related Concepts
- [[ReinforcementLearning]] - is the broader reward-driven sequential decision framework.
- [[ScoreFunctionEstimator]] - provides the general likelihood-ratio gradient used for trajectories.
- [[LogDerivativeTrick]] - rewrites the trajectory-probability derivative into a sampleable expectation.
- [[MonteCarloEstimation]] - approximates the trajectory expectation using sampled episodes.
- [[GroupRelativePolicyOptimization]] - is a later critic-free policy-optimization method mentioned by the source.
- [[AsynchronousReinforcementLearning]] - changes how completed policy rollouts are scheduled and consumed.
