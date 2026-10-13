---
title: "Group Relative Policy Optimization"
type: concept
tags: [ai, reinforcement-learning, grpo, policy-optimization]
sources:
  - large-language-model-technical-reports-overview
  - rl-is-an-evolutionary-algorithm
  - 2607.07508
last_updated: 2026-10-13
knowledge_schema: synthesis-v1
---

## Definition
[[GroupRelativePolicyOptimization]] (GRPO) is a policy-optimization method that samples multiple outputs for the same prompt and estimates each output's advantage relative to group reward statistics instead of training a separate critic/value model.

## Current Synthesis
In the source's PPO comparison, PPO evaluates generated output with frozen reward and reference models, trains a critic to estimate value, and uses generalized advantage estimation to update the policy. GRPO removes the critic: it samples a response group, scores the responses, normalizes rewards relative to the group, and updates the policy while retaining a KL-style constraint against a reference model. This reduces model and training overhead, but it shifts importance toward prompt grouping, response diversity, reward reliability, and stable normalization rather than eliminating value estimation problems altogether.

The evolutionary essay interprets each response group as a small population whose variants exchange information only through relative reward normalization and the accumulated gradient. This is a useful intuition for selection among sampled behaviors, not part of GRPO's formal definition. Its broader prediction that diverse multi-domain training favors transferable behavior depends on stable optimization, genuinely varied tasks, and rewards that do not consistently select shortcuts.

The SAO paper adds an asynchronous boundary. A group baseline cannot be computed until every response finishes, so variable-length trajectories make completed samples wait and grow stale relative to a continuously updating learner. Direct importance masking stabilizes the paper's grouped comparison, showing that the synchronization problem and off-policy correction are separable; the proposed single-rollout alternative then removes the group barrier by restoring a trained critic. GRPO therefore remains attractive when grouped synchronous sampling is cheap and value-model overhead is undesirable, but it is structurally mismatched to one-trajectory feedback and can worsen policy lag in long-horizon asynchronous workloads.

## Key Claims
- GRPO replaces a learned critic baseline with relative reward statistics across responses to the same prompt.
- Removing the critic reduces memory, compute, and error from an inaccurate value model.
- Multiple sampled answers provide the comparison set needed to estimate relative advantage, but the full group becomes a completion barrier under asynchrony.
- A reference-policy or KL constraint still limits excessive policy drift.
- Rule-verifiable rewards can reduce dependence on a learned reward model for tasks with checkable answers and formats.
- GRPO remains sensitive to reward hacking, weak sample diversity, group composition, and tasks whose quality cannot be checked reliably.
- Population language can clarify within-group selection but should not replace the algorithm's probability, reward-normalization, gradient, and KL mechanics.

## Evidence
- Architecture: [[large-language-model-technical-reports-overview]] reproduces a PPO-versus-GRPO diagram showing the missing GRPO value model and grouped outputs, rewards, and advantages.
- Advantage computation: [[large-language-model-technical-reports-overview]] explains normalization using the group's reward mean and variance.
- Reward design: [[large-language-model-technical-reports-overview]] reproduces DeepSeek-R1-Zero's accuracy and format reward rules.
- Practical role: [[large-language-model-technical-reports-overview]] presents GRPO as the reasoning-oriented RL method used for DeepSeek-R1-Zero and the later R1 pipeline.
- Evolutionary analogy: [[rl-is-an-evolutionary-algorithm]] treats grouped responses as behavioral variants selected through relative reward and the aggregated gradient.
- Asynchronous limit: [[2607.07508]] shows vanilla GRPO collapsing near 160 steps, GRPO with direct importance sampling remaining stable, and grouped trajectories waiting for their slowest response before training.

## Counterevidence & Qualifications
The evidence combines a secondary technical explanation, a speculative practitioner analogy, and one primary comparison paper. The SAO study tests one Qwen3-30B-A3B backbone and bundles its alternative with direct masking and multiple critic changes; it therefore does not show that GRPO is generally inferior or that its group barrier dominates short synchronous workloads. Critic removal saves value-model training but requires multiple rollouts, and rule rewards fit mathematics, code, and constrained formats better than subjective or open-ended output. A relative score says which sampled answer is better within a group, not that any answer is objectively good. Calling the group a population does not make GRPO an evolutionary algorithm in the formal computational sense, and the essay explicitly uses nonstandard meanings for “agent” and “policy.”

## What Changed
- Added group completion as an explicit asynchronous synchronization and policy-staleness cost.
- Distinguished off-policy instability from the group barrier: direct masking stabilized the paper's grouped comparator without removing its wait.
- Limited the critique to long-horizon and one-trajectory settings rather than treating single-rollout actor-critic training as universally superior.

## Related Concepts
- [[ReinforcementLearning]] - broader framework within which GRPO optimizes a policy from reward.
- [[ChainOfThoughtReasoning]] - response trajectories whose relative quality GRPO can reinforce.
- [[DeepSeekR1]] - model family using GRPO for reasoning-oriented training.
- [[SearchR1]] - retrieval-policy project whose source also names GRPO as its actual optimizer.
- [[ReasoningModelDistillation]] - an alternative or complementary route to small-model reasoning capability.
- [[EvolutionaryOptimizationAnalogy]] - interprets grouped sampling and relative reward as variation and selection.
- [[InstructionRewardAlignment]] - determines whether group-relative optimization favors instructed or shortcut behavior.
- [[AsynchronousReinforcementLearning]] - setting where grouped completion can increase learner-policy lag.
- [[SingleRolloutAsynchronousOptimization]] - critic-based alternative designed to consume each completed trajectory immediately.
