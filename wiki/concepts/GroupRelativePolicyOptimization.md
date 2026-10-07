---
title: "Group Relative Policy Optimization"
type: concept
tags: [ai, reinforcement-learning, grpo, policy-optimization]
sources:
  - large-language-model-technical-reports-overview
last_updated: 2026-10-07
knowledge_schema: synthesis-v1
---

## Definition
[[GroupRelativePolicyOptimization]] (GRPO) is a policy-optimization method that samples multiple outputs for the same prompt and estimates each output's advantage relative to group reward statistics instead of training a separate critic/value model.

## Current Synthesis
In the source's PPO comparison, PPO evaluates generated output with frozen reward and reference models, trains a critic to estimate value, and uses generalized advantage estimation to update the policy. GRPO removes the critic: it samples a response group, scores the responses, normalizes rewards relative to the group, and updates the policy while retaining a KL-style constraint against a reference model. This reduces model and training overhead, but it shifts importance toward prompt grouping, response diversity, reward reliability, and stable normalization rather than eliminating value estimation problems altogether.

## Key Claims
- GRPO replaces a learned critic baseline with relative reward statistics across responses to the same prompt.
- Removing the critic reduces memory, compute, and error from an inaccurate value model.
- Multiple sampled answers provide the comparison set needed to estimate relative advantage.
- A reference-policy or KL constraint still limits excessive policy drift.
- Rule-verifiable rewards can reduce dependence on a learned reward model for tasks with checkable answers and formats.
- GRPO remains sensitive to reward hacking, weak sample diversity, group composition, and tasks whose quality cannot be checked reliably.

## Evidence
- Architecture: [[large-language-model-technical-reports-overview]] reproduces a PPO-versus-GRPO diagram showing the missing GRPO value model and grouped outputs, rewards, and advantages.
- Advantage computation: [[large-language-model-technical-reports-overview]] explains normalization using the group's reward mean and variance.
- Reward design: [[large-language-model-technical-reports-overview]] reproduces DeepSeek-R1-Zero's accuracy and format reward rules.
- Practical role: [[large-language-model-technical-reports-overview]] presents GRPO as the reasoning-oriented RL method used for DeepSeek-R1-Zero and the later R1 pipeline.

## Counterevidence & Qualifications
The source is a secondary explanation and does not reproduce the algorithm's derivation, ablations, convergence behavior, sensitivity to group size, or total generation cost. Critic removal saves value-model training but requires multiple rollouts, and rule rewards fit mathematics, code, and constrained formats better than subjective or open-ended output. A relative score also says which sampled answer is better within a group, not that any answer is objectively good.

## What Changed
- Created a synthesis of GRPO's critic-free architecture, grouped advantage estimate, reward assumptions, and remaining failure modes.

## Related Concepts
- [[ReinforcementLearning]] - broader framework within which GRPO optimizes a policy from reward.
- [[ChainOfThoughtReasoning]] - response trajectories whose relative quality GRPO can reinforce.
- [[DeepSeekR1]] - model family using GRPO for reasoning-oriented training.
- [[SearchR1]] - retrieval-policy project whose source also names GRPO as its actual optimizer.
- [[ReasoningModelDistillation]] - an alternative or complementary route to small-model reasoning capability.
