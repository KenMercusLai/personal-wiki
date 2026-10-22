---
title: "Temporal-Difference Learning"
type: concept
tags: [reinforcement-learning, bootstrapping, value-estimation]
sources:
  - rlbook
last_updated: 2026-10-22
knowledge_schema: synthesis-v1
---

## Definition
[[TemporalDifferenceLearning]] learns value estimates from sampled transitions by moving a current prediction toward a reward-plus-successor-estimate target.

## Current Synthesis
TD combines Monte Carlo's learning from experience with dynamic programming's bootstrapping. TD(0) updates after one transition using a target such as $R_{t+1}+\gamma V(S_{t+1})$; n-step methods use several observed rewards before bootstrapping, interpolating toward a complete Monte Carlo return. Sarsa learns action values on-policy through the next action actually selected, while expected Sarsa averages over the target policy and becomes Q-learning's target when that policy is greedy. Off-policy learning additionally requires coverage and correction because behavior and target policies differ.

## Key Claims
- TD uses a sampled successor rather than the complete model-weighted successor distribution used by dynamic programming.
- Bootstrapping permits online updates before an episode finishes but makes the learning target depend on another current estimate.
- The TD error is the gap between the reward-plus-successor target and the current prediction.
- n-step returns trade shorter biased bootstrapping against longer, higher-variance sampled reward sequences.
- Sarsa's policy improvement is implicit when action selection is recomputed from changing action values, commonly through decaying epsilon-greedy behavior.
- Batch TD's fixed point matches the Bellman solution of the empirical maximum-likelihood transition model even when that model is not explicitly constructed.

## Evidence
- Sample update and bootstrapping: [[rlbook]] contrasts full-distribution DP targets, complete-return Monte Carlo targets, and one-step TD targets.
- Control and policy relation: [[rlbook]] explains Sarsa, expected Sarsa, Q-learning, coverage, and gradual movement toward greediness.
- Batch fixed point: [[rlbook]] groups converged TD errors by observed successor frequency to recover the empirical-model Bellman equation.

## Counterevidence & Qualifications
The notebook is pedagogical and mostly AI-authored. Its convergence explanations omit some step-size, visitation, representation, and stochastic-approximation conditions. The n-step discussion initially frames delayed computation as the primary benefit, but the more general reason is the bias-variance and credit-propagation tradeoff. With function approximation, bootstrapping and off-policy sampling can create instability not covered by the tabular intuition.

## What Changed
- Distinguished TD sample bootstrapping from both expected dynamic programming and complete-return Monte Carlo learning.
- Added the n-step continuum and Sarsa policy-improvement mechanism.
- Added the empirical-model interpretation of batch TD.

## Related Concepts
- [[MarkovDecisionProcess]] - supplies the value and transition structure estimated by TD.
- [[MonteCarloEstimation]] - supplies complete sampled returns without bootstrapping.
- [[FunctionApproximation]] - generalizes TD estimates across states while adding stability risks.
- [[ReinforcementLearning]] - contains TD prediction and control as core model-free methods.
