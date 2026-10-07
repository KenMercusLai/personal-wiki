---
title: "Chain-of-Thought Reasoning"
type: concept
tags: [ai, reasoning, inference-time-compute, language-models]
sources:
  - large-language-model-technical-reports-overview
last_updated: 2026-10-07
knowledge_schema: synthesis-v1
---

## Definition
[[ChainOfThoughtReasoning]] is the use of intermediate reasoning steps before a language model produces its final answer, allowing decomposition, checking, correction, and alternate approaches while consuming additional inference time and tokens.

## Current Synthesis
The source treats extended reasoning as both a learned behavior and a controllable compute budget. OpenAI o1 supplies the clearest scaling claim: reproduced plots show AIME accuracy rising as training compute and test-time compute increase. DeepSeek-R1-Zero shows that reflective, self-verifying trajectories can emerge under outcome-based reinforcement learning, while DeepSeek-R1 adds supervised cold-start examples and language consistency to make them readable. Kimi k1.5 then highlights the efficiency boundary: longer trajectories can help difficult tasks, but Long2Short training and explicit length rewards try to retain correctness without paying for unnecessary tokens.

## Key Claims
- Intermediate reasoning can let a model decompose difficult tasks, detect mistakes, and change strategy before answering.
- Reasoning quality can scale with both training-time optimization and additional test-time computation.
- Outcome-verifiable reinforcement learning can induce extended reasoning without step-by-step labels, at least in the reported DeepSeek-R1-Zero setup.
- Usable reasoning traces may still require cold-start examples, language controls, or later supervised stages.
- Longer reasoning is not automatically better; token cost, latency, readability, and redundant steps create an efficiency tradeoff.
- Hidden chains of thought limit direct auditability even when a system exposes a summary.

## Evidence
- Compute scaling: [[large-language-model-technical-reports-overview]] reproduces o1 AIME plots rising with train-time and test-time compute.
- Emergent behavior: [[large-language-model-technical-reports-overview]] reports reflection and self-verification arising during DeepSeek-R1-Zero's pure-RL training.
- Readability intervention: [[large-language-model-technical-reports-overview]] describes DeepSeek-R1's cold-start data and language-consistency reward.
- Efficiency intervention: [[large-language-model-technical-reports-overview]] describes Kimi's shortest-correct selection, DPO, and length-penalized RL.
- Visibility boundary: [[large-language-model-technical-reports-overview]] states that o1 reveals summaries rather than its raw reasoning process.

## Counterevidence & Qualifications
The evidence is vendor-reported and task-heavy in mathematics, programming, science, and other verifiable domains. More tokens can encode confusion as well as useful work, benchmark accuracy does not establish faithfulness of the reasoning trace, and a hidden or fluent chain of thought is not proof that the stated steps caused the answer. The source does not establish a universal scaling curve across models or open-ended tasks.

## What Changed
- Created a synthesis connecting inference-time scaling, pure-RL emergence, readability interventions, and length efficiency.

## Related Concepts
- [[ReinforcementLearning]] - supplies outcome signals that can encourage useful reasoning trajectories.
- [[GroupRelativePolicyOptimization]] - estimates which sampled reasoning trajectories are better within a prompt group.
- [[ReasoningModelDistillation]] - transfers stronger-model reasoning behavior into smaller models.
- [[OpenAIo1]] - illustrates hidden reasoning and reported test-time scaling.
- [[DeepSeekR1]] - distinguishes emergent pure-RL reasoning from a readable multi-stage model.
- [[KimiK15]] - illustrates long-context reasoning and explicit length control.
