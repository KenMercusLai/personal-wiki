---
title: "Kimi k1.5"
type: entity
tags: [ai, reasoning-model, kimi, reinforcement-learning]
sources:
  - large-language-model-technical-reports-overview
last_updated: 2026-10-07
knowledge_schema: synthesis-v1
---

## Overview
[[KimiK15]] is a long-context reasoning model whose technical report combines long-chain supervised fine-tuning, reinforcement learning over a curated prompt set, critic-free policy optimization, and Long2Short compression methods.

## Current Profile
Unlike DeepSeek-R1-Zero's pure-RL experiment, Kimi k1.5 retains a staged pretraining-to-SFT-to-long-chain-SFT-to-RL process and extends the RL context window to 128K tokens. Its prompt set emphasizes diverse, objectively gradable, difficulty-balanced math, programming, STEM, and general-reasoning problems. A variant of online policy mirror descent uses sampled rewards and relative-entropy regularization without a critic, while curriculum and prioritized sampling manage difficulty; Long2Short methods then seek shorter correct reasoning through merging, rejection sampling, DPO, or length-penalized RL.

## Key Characteristics
- Supports reported 128K-token RL contexts for long reasoning trajectories.
- Uses a curated prompt set designed for diversity, objective evaluation, and balanced difficulty.
- Retains long-chain supervised fine-tuning before reinforcement learning.
- Applies critic-free online policy mirror descent with sampled relative rewards and policy regularization.
- Moves from easier tasks toward harder or lower-success tasks through curriculum and prioritized sampling.
- Uses four Long2Short methods to reduce response length while preserving correctness.

## Evidence
- Training sequence and context: [[large-language-model-technical-reports-overview]] contrasts Kimi's staged pipeline and 128K context with DeepSeek's pure-RL experiment.
- Prompt-set design: [[large-language-model-technical-reports-overview]] lists diversity, evaluability, difficulty balance, automatic filtering, tags, and guessability exclusion.
- Policy optimization: [[large-language-model-technical-reports-overview]] reproduces the online policy mirror descent objective and sampled-reward surrogate loss.
- Sampling: [[large-language-model-technical-reports-overview]] describes curriculum sampling followed by emphasis on harder, lower-success problems.
- Compression: [[large-language-model-technical-reports-overview]] describes model merging, shortest-correct rejection sampling, DPO, and length-penalized RL.

## Qualifications
The wiki profile is based on a secondary overview of Kimi's technical report, without independent benchmark reproduction, training code, or cost accounting. A 128K context permits longer traces but does not itself prove better reasoning, and length penalties can trade verbosity against omitted reasoning or answer quality if their reward design is poorly calibrated.

## What Changed
- Created a source-bounded profile of Kimi k1.5's long-context RL, prompt curation, policy optimization, sampling, and Long2Short methods.

## Relationships
- [[ChainOfThoughtReasoning]] - Kimi trains and then compresses long reasoning trajectories.
- [[ReinforcementLearning]] - optimizes reasoning behavior over verifiable prompt sets.
- [[ReasoningModelDistillation]] - Long2Short is a related capability-compression program.
- [[DeepSeekR1]] - reaches similar reasoning goals through a differently staged pipeline.
- [[OpenAIo1]] - another comparison point for inference-time reasoning.
