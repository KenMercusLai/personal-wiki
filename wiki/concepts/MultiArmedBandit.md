---
title: "Multi-Armed Bandit"
type: concept
tags: [reinforcement-learning, exploration, online-learning]
sources:
  - rlbook
last_updated: 2026-10-22
knowledge_schema: synthesis-v1
---

## Definition
[[MultiArmedBandit]] is a sequential choice problem in which an agent repeatedly selects among actions with unknown reward distributions but has no changing state or delayed state-transition dynamics.

## Current Synthesis
The setting strips [[ReinforcementLearning]] down to action-value estimation and exploration versus exploitation. Evaluative feedback reveals only the reward for the selected action, not the counterfactual rewards or the identity of the best action. Sample averages estimate stationary action values, constant step sizes emphasize recent outcomes in nonstationary tasks, and upper-confidence methods add an uncertainty bonus so under-sampled actions retain exploratory priority.

## Key Claims
- Bandits are nonassociative because the action choice is not conditioned on distinguishable states.
- Evaluative feedback lacks the unchosen-action labels that would make the problem ordinary supervised learning.
- Sample-average estimates give all observations equal eventual weight and are appropriate when action-value distributions remain stationary.
- Constant step sizes exponentially discount older observations and therefore track changing action values better.
- Upper-confidence selection combines estimated reward with uncertainty driven by action count.

## Evidence
- Setting and feedback: [[rlbook]] contrasts evaluative rewards with instructive labels and removes state-action association, transition dynamics, and delayed credit assignment.
- Estimation and exploration: [[rlbook]] compares sample averages, constant-step recency weighting, optimistic initialization, and upper-confidence bounds.

## Counterevidence & Qualifications
The source is a learner's notebook built largely from AI-generated explanations, not a primary statistical analysis. Its upper-confidence discussion is intuitive and does not state a particular concentration bound or its assumptions. A mixture of hidden bandit tasks looks stationary only when the task-mixture probabilities and component reward distributions remain fixed.

## What Changed
- Established the stateless bandit problem as the minimal exploration-versus-exploitation setting.
- Distinguished stationary sample averages from recency-weighted nonstationary tracking.
- Added evaluative feedback and uncertainty bonuses as separate sources of exploration pressure.

## Related Concepts
- [[ReinforcementLearning]] - adds state, transitions, delayed return, and credit assignment to the bandit core.
- [[MonteCarloEstimation]] - supplies the sample-average principle used to estimate action rewards.
- [[MarkovDecisionProcess]] - introduces state-conditioned action choice and sequential dynamics absent from a bandit.
