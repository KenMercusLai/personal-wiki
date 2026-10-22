---
title: "Markov Decision Process"
type: concept
tags: [reinforcement-learning, sequential-decision-making, probability]
sources:
  - rlbook
last_updated: 2026-10-22
knowledge_schema: synthesis-v1
---

## Definition
[[MarkovDecisionProcess]] is a sequential decision model in which a state summarizes the information needed for the distribution of the next state and reward given the current action.

## Current Synthesis
A finite MDP connects states, actions, rewards, transition probabilities, policies, returns, and value functions. The Markov condition is best treated as a requirement on state representation: if prediction needs earlier observations, the state is incomplete and may need history or memory. A policy is evaluated by expected return rather than one realized return, and Bellman equations recursively connect present value to immediate reward and successor value. Dynamic programming computes full expected updates when the model is known; sampled methods estimate the same structure from experience.

## Key Claims
- The Markov property constrains what the state representation must contain, not how simple the underlying world must be.
- State value and action value are conditional expected returns under a policy; realized return remains random.
- Optimal value takes the best achievable policy value for each state, and finite discounted or episodic MDPs admit optimal policies under standard assumptions.
- Bellman equations decompose return into immediate reward plus discounted successor return or value.
- Partial observability and state aliasing can make the same observation correspond to different decision-relevant hidden states.
- Dynamic programming needs a known transition-and-reward model, while sample-based methods can learn without enumerating the successor distribution.

## Evidence
- State and observability: [[rlbook]] contrasts fully visible tic-tac-toe state with hidden state, aliased observations, history-augmented representations, and belief-like inference.
- Return and value: [[rlbook]] distinguishes a sampled return from its policy-conditioned expectation and derives state and action values through recursive return decomposition.
- Planning and sampling: [[rlbook]] compares Bellman expectation updates over all reachable successors with Monte Carlo and TD sample updates.

## Counterevidence & Qualifications
The source focuses on finite textbook settings and pedagogical examples. Claims about existence and convergence depend on assumptions such as finite spaces, appropriate discounting or termination, adequate visitation, and stationary dynamics. Adding a few historical observations does not necessarily restore a sufficient Markov state in a partially observable process.

## What Changed
- Added the state-representation interpretation of the Markov condition.
- Connected expected return, value functions, Bellman recursion, and optimal policy.
- Made partial observability and model dependence explicit boundaries.

## Related Concepts
- [[ReinforcementLearning]] - uses MDPs as a common formal model for sequential interaction.
- [[MultiArmedBandit]] - is the stateless special case used to isolate exploration.
- [[TemporalDifferenceLearning]] - estimates MDP values from sampled one- or multi-step transitions.
- [[FunctionApproximation]] - represents values or policies when tabulating every MDP state is impractical.
