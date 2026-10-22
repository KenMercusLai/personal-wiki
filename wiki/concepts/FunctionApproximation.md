---
title: "Function Approximation"
type: concept
tags: [reinforcement-learning, machine-learning, neural-networks]
sources:
  - rlbook
last_updated: 2026-10-22
knowledge_schema: synthesis-v1
---

## Definition
[[FunctionApproximation]] represents a value function or policy with shared parameters instead of storing an independent entry for every state or state-action pair.

## Current Synthesis
Approximation makes continuous or very large state spaces tractable and allows experience in one state to generalize to related states. The same coupling means an update can improve some states while degrading others, so the state-sampling distribution and explicit interest weights define which errors matter. TD with approximation is usually a semi-gradient method: it differentiates the current estimate but treats a bootstrapped target containing another estimate as fixed. Neural networks provide a nonlinear parameterization, while replay, target networks, regularization, and architectural memory address different data-correlation, moving-target, overfitting, and partial-observability problems.

## Key Claims
- Approximation trades exact per-state storage for parameter sharing and generalization.
- Sampling states on-policy with equal per-sample step sizes implicitly weights the objective by their visitation frequency.
- Bootstrapped semi-gradients ignore the target's dependence on the current parameters and therefore are not true gradients of the displayed squared error.
- Function approximation alone cannot reconstruct hidden history when the current observation lacks decision-relevant information.
- Neural value, action-value, and policy networks differ mainly in what their outputs represent and how RL constructs their learning signals.
- Constant or adaptive step sizes are often preferable to simple visit-count averages when targets, policies, or environments move.

## Evidence
- Objective and distribution: [[rlbook]] derives continuing and episodic on-policy state distributions and explains how equal treatment of encountered samples induces visitation weighting.
- Semi-gradient boundary: [[rlbook]] separates the parameter effect on the current estimate from the ignored effect on a bootstrapped target.
- Neural interaction and memory: [[rlbook]] maps states to value, action-value, or policy outputs and distinguishes feed-forward approximation from history stacking or recurrent memory.

## Counterevidence & Qualifications
The source is an informal study notebook rather than a modern deep-RL survey. Its suggestions about experience replay and target networks are common engineering patterns, not universal fixes, and its convergence claims are not supplied with full assumptions. Similar observations can still correspond to different hidden states, so generalization can amplify representation error as well as reduce sample needs.

## What Changed
- Added parameter sharing, visitation weighting, and the semi-gradient distinction.
- Separated generalization from memory for partial observability.
- Connected neural-network outputs to RL-generated targets and gradients.

## Related Concepts
- [[TemporalDifferenceLearning]] - supplies bootstrapped targets and semi-gradient updates.
- [[PolicyGradient]] - parameterizes and directly differentiates a stochastic policy.
- [[DeepLearning]] - provides nonlinear neural function classes used for value and policy models.
- [[MarkovDecisionProcess]] - defines the states and values being approximated.
