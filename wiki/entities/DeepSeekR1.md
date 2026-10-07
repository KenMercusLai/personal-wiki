---
title: "DeepSeek-R1"
type: entity
tags: [ai, reasoning-model, deepseek, reinforcement-learning]
sources:
  - large-language-model-technical-reports-overview
last_updated: 2026-10-07
knowledge_schema: synthesis-v1
---

## Overview
[[DeepSeekR1]] is a reasoning-model family whose report distinguishes the pure-reinforcement-learning R1-Zero experiment from a multi-stage R1 model designed for readability, general capability, and alignment.

## Current Profile
R1-Zero begins from DeepSeek-V3-Base without supervised fine-tuning and uses [[GroupRelativePolicyOptimization]] with rule-based correctness and format rewards, showing in the report that extended reasoning, reflection, and self-verification can emerge from outcome-driven RL. Its mixed-language, low-readability output and unstable early training motivate the practical R1 pipeline: cold-start long-chain SFT, reasoning RL, rejection-sampled reasoning plus general SFT data, and a final all-scenario RL phase. The report also finds distillation into smaller models more effective than directly applying its large-scale RL recipe to those models.

## Key Characteristics
- Separates a pure-RL research result from a more engineered production-oriented training pipeline.
- Uses GRPO to estimate relative advantage from grouped samples without a learned critic.
- Prefers rule-verifiable accuracy and format rewards during R1-Zero training.
- Adds cold-start data and a language-consistency reward to improve readability and reduce language mixing.
- Builds roughly 600,000 reasoning and 200,000 non-reasoning SFT examples before a final broad RL phase, as reported in the overview.
- Transfers reasoning capability to smaller Qwen and Llama models through distillation.

## Evidence
- Pure-RL result: [[large-language-model-technical-reports-overview]] describes R1-Zero training directly from a base model without initial SFT.
- Reward and optimization design: [[large-language-model-technical-reports-overview]] reproduces DeepSeek's rule-based reward description and PPO-versus-GRPO architecture.
- Usability pipeline: [[large-language-model-technical-reports-overview]] details the four stages added for R1 and the language-consistency reward.
- Distillation: [[large-language-model-technical-reports-overview]] reproduces the same-family comparison in which distilled Qwen models outperform direct RL variants.
- Negative results: [[large-language-model-technical-reports-overview]] reports practical difficulties with process reward models and MCTS.

## Qualifications
The evidence comes through a secondary technical explainer and vendor-authored report. Pure RL describes R1-Zero, not the final R1 pipeline; rule rewards require objectively checkable tasks; reported data counts, benchmark results, and compute comparisons are not independently replicated here; and negative PRM/MCTS results should not be universalized beyond the tested setup.

## What Changed
- Created a profile distinguishing R1-Zero's pure-RL experiment from DeepSeek-R1's cold-start, SFT, and multi-stage RL pipeline.

## Relationships
- [[GroupRelativePolicyOptimization]] - primary critic-free policy-optimization method described for the model family.
- [[ChainOfThoughtReasoning]] - target behavior that emerges in R1-Zero and is made more readable in R1.
- [[ReasoningModelDistillation]] - mechanism used to transfer R1 reasoning into smaller models.
- [[OpenAIo1]] - benchmark and capability comparison point.
- [[KimiK15]] - parallel reasoning-model program with a different multi-stage training design.
