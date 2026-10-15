---
title: "Notes on RL: Policy Gradient & Log Derivative Trick"
type: source
tags: [reinforcement-learning, policy-gradient, monte-carlo, probability]
date: 2025-02-25
source_file: /mnt/ken_personal_wiki/Articles/policy-gradient.md
---

## Summary
This Chinese-language tutorial derives vanilla [[PolicyGradient]] from [[MonteCarloEstimation]], the [[LogDerivativeTrick]], and the [[ScoreFunctionEstimator]]. It contrasts value-based Q-learning with a parameterized stochastic policy, factors trajectory probability into initial-state, action-policy, and environment-transition terms, and shows why only the action log-probabilities contribute gradients when the environment dynamics do not depend on policy parameters. The derivation is pedagogically useful but presents the high-variance full-trajectory-return estimator without the baselines, reward-to-go, discounting, or variance-reduction machinery used in more practical algorithms.

## Key Claims
- [[MonteCarloEstimation]] approximates an expectation with the empirical mean of samples drawn from the target distribution.
- The [[LogDerivativeTrick]] rewrites a probability derivative as the probability multiplied by its log-probability gradient: $\nabla_\theta p(x;\theta)=p(x;\theta)\nabla_\theta\log p(x;\theta)$.
- The [[ScoreFunctionEstimator]] uses that identity to express the gradient of an expectation as another expectation that can be estimated from samples.
- [[PolicyGradient]] directly parameterizes action probabilities $\pi_\theta(a\mid s)$ and maximizes expected trajectory return rather than first learning a table or network of state-action values.
- Factoring a trajectory distribution shows that initial-state and transition probabilities vanish from the policy gradient when they are independent of $\theta$, leaving a sum of action log-probability gradients weighted by return.
- Automatic-differentiation systems can optimize the negative sampled log-probability-weighted return as a loss, which is equivalent to gradient ascent on the stated objective.

## Key Quotes
> "主要就是应用了 Log Derivative Trick 来凑出概率函数，然后用蒙特卡洛方法来估算期望。" - the tutorial's summary of the derivation.

## Connections
- [[ReinforcementLearning]] - broader sequential decision framework within which policy gradients optimize behavior from reward.
- [[PolicyGradient]] - direct policy-optimization family derived in the tutorial.
- [[MonteCarloEstimation]] - converts expectations into sample averages over observed values or trajectories.
- [[LogDerivativeTrick]] - algebraic identity that restores a sampling distribution inside the gradient expression.
- [[ScoreFunctionEstimator]] - general gradient estimator instantiated by the policy-gradient derivation.
- [[GroupRelativePolicyOptimization]] - later policy-optimization method mentioned as a successor direction rather than derived here.

## Contradictions
- The source correctly labels the result as a simple vanilla policy gradient and acknowledges sparse rewards and high variance; it does not establish that the displayed estimator is practically competitive with PPO, GRPO, actor-critic methods, or other variance-reduced algorithms.
- The displayed derivation uses one total trajectory return for every action and omits discounting, reward-to-go, baselines, advantage estimates, entropy terms, and finite-horizon boundary details, so it is an introductory REINFORCE-style account rather than a full modern implementation recipe.
- One early intermediate equation appears to replace the intended factor $f(x)$ with $d(x)$; the surrounding equations restore $f(x)$ and make the intended score-function derivation clear.
