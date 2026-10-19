---
title: "Chain-of-Thought Reasoning"
type: concept
tags: [ai, reasoning, inference-time-compute, language-models]
sources:
  - large-language-model-technical-reports-overview
  - controlling-reasoning-effort
last_updated: 2026-10-19
knowledge_schema: synthesis-v1
---

## Definition
[[ChainOfThoughtReasoning]] is the use of intermediate generated steps before a language model produces its final answer, allowing decomposition, checking, correction, and alternate approaches while consuming additional inference time and tokens.

## Current Synthesis
The sources treat extended reasoning as both learned behavior and controllable inference work. OpenAI o1 supplies the early scaling claim: reproduced plots show AIME accuracy rising with training and test-time compute. DeepSeek-R1-Zero shows that intermediate explanations, backtracking, and self-correction can emerge under verifiable outcome rewards even when the training signal ignores whether individual trace steps are correct. DeepSeek-R1 then adds cold-start supervision and language consistency for usability.

Newer hybrid models make the trace optional or variable. Qwen3 mixes thinking and non-thinking examples; GPT-OSS conditions one checkpoint on effort labels; Inkling changes token penalties with a continuous effort value; and other systems combine specialists, hard budgets, truncation examples, and distillation. This makes trace length an operating control, not a direct measure of reasoning quality. Delimiters merely mark trace boundaries, hidden or fluent traces remain difficult to audit, and longer output can encode confusion or redundancy as readily as useful computation.

## Key Claims
- Intermediate reasoning can help a model decompose difficult tasks, detect mistakes, and change strategy before answering.
- Outcome-verifiable reinforcement learning can induce extended reasoning without step-by-step correctness labels in the reported DeepSeek-R1-Zero setup.
- Training-time optimization and additional inference-time computation are distinct levers that can both improve selected reasoning benchmarks.
- Usable traces may require cold-start examples, language controls, format training, or later supervised stages even when the underlying behavior emerges through RL.
- Hybrid post-training can teach one checkpoint to omit, shorten, extend, or recover from interrupted reasoning in response to explicit controls.
- Trace delimiters and trace length are interface and budget signals, not proof that the trace is faithful or causally responsible for the answer.
- Longer reasoning is not automatically better because cost, latency, readability, redundancy, and diminishing benchmark returns bound its value.

## Evidence
- Compute scaling: [[large-language-model-technical-reports-overview]] reproduces o1 AIME plots rising with training-time and test-time compute.
- Emergent behavior: [[large-language-model-technical-reports-overview]] and [[controlling-reasoning-effort]] report reflection and self-correction arising during DeepSeek-R1-Zero's pure-RL training.
- Reward boundary: [[controlling-reasoning-effort]] shows RLVR checking final-answer correctness and output format while ignoring intermediate reasoning correctness.
- Readability intervention: [[large-language-model-technical-reports-overview]] describes DeepSeek-R1's cold-start data and language-consistency reward.
- Length efficiency: [[large-language-model-technical-reports-overview]] describes Kimi's shortest-correct selection, DPO, and length-penalized RL.
- Mode control: [[controlling-reasoning-effort]] compares mixed-mode SFT, effort-conditioned RL, specialists, distillation, and hard-budget recovery across open-weight models.
- Cost boundary: [[controlling-reasoning-effort]] retains GPT-OSS, GPT-5.6, and Inkling evidence linking higher effort to more tokens and generally higher but flattening performance.

## Counterevidence & Qualifications
The evidence is heavily vendor-reported and concentrated in mathematics, programming, science, and other verifiable domains. More tokens can encode confusion as well as useful work; benchmark accuracy does not establish trace faithfulness; and a hidden or fluent chain of thought is not proof that the stated steps caused the answer. Similar effort labels can represent different training and serving mechanisms, while several proprietary details remain inferred or undisclosed. The sources do not establish a universal scaling curve, best trace length, or automatic effort router across models and open-ended tasks.

## What Changed
- Added the distinction between outcome-rewarded trace emergence and direct supervision of intermediate steps.
- Added learned on/off and graded effort controls across SFT, RL, specialist, and distillation recipes.
- Separated trace delimiters and hard budgets from reasoning capability.
- Added direct evidence for diminishing returns at higher effort.

## Related Concepts
- [[ReasoningEffort]] - controls whether and how extensively a trained model emits intermediate reasoning.
- [[ReinforcementLearning]] - supplies outcome signals that can encourage useful reasoning trajectories.
- [[GroupRelativePolicyOptimization]] - estimates which sampled reasoning trajectories are better within a prompt group.
- [[ReasoningModelDistillation]] - transfers or consolidates stronger reasoning behavior into another checkpoint.
- [[OpenAIo1]] - illustrates hidden reasoning and reported test-time scaling.
- [[DeepSeekR1]] - distinguishes emergent pure-RL reasoning from a readable multi-stage model.
- [[KimiK15]] - illustrates long-context reasoning and explicit length control.
