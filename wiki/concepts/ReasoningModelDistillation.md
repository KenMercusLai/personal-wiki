---
title: "Reasoning-Model Distillation"
type: concept
tags: [ai, distillation, reasoning, model-compression]
sources:
  - large-language-model-technical-reports-overview
last_updated: 2026-10-07
knowledge_schema: synthesis-v1
---

## Definition
[[ReasoningModelDistillation]] transfers reasoning behavior from a stronger teacher model into a smaller model by training on teacher-generated solutions or preferences rather than requiring the smaller model to rediscover the behavior through equally large-scale reinforcement learning.

## Current Synthesis
The source presents distillation as an efficiency path for reasoning models. DeepSeek generates reasoning data from a strong R1 model and fine-tunes smaller Qwen and Llama models; the reproduced same-family comparison reports that distilled Qwen variants outperform Qwen models trained directly with the R1-Zero-style RL process. Kimi's Long2Short program addresses a related target—compact correct reasoning—through parameter merging, shortest-correct rejection sampling, length-oriented DPO, and additional RL with a length penalty. Together these methods suggest that capability discovery and capability deployment may be economically different stages.

## Key Claims
- Strong-model reasoning trajectories can supervise smaller models without repeating the full discovery-scale RL process.
- DeepSeek's reproduced comparison favors distillation over direct large-scale RL for smaller Qwen models.
- Distillation can reduce training compute and deployment size while retaining substantial benchmark capability.
- Long2Short methods add a second compression target: fewer reasoning tokens, not only fewer model parameters.
- Teacher errors, style, hidden shortcuts, and benchmark specialization can also transfer into the student.

## Evidence
- Same-family comparison: [[large-language-model-technical-reports-overview]] reproduces results where DeepSeek-R1-Distill-Qwen-32B and 7B outperform corresponding directly RL-trained Qwen variants across the listed reasoning benchmarks.
- Cross-family transfer: [[large-language-model-technical-reports-overview]] reports distilled models based on multiple Qwen and Llama sizes.
- Sequence compression: [[large-language-model-technical-reports-overview]] describes Kimi's shortest-correct rejection sampling, DPO preference pairs, and length-penalized RL.
- Compute claim: [[large-language-model-technical-reports-overview]] quotes the DeepSeek report's conclusion that direct RL on small models can require enormous compute and still underperform distillation.

## Counterevidence & Qualifications
The source does not independently reproduce the tables, compare equal total data and compute budgets, or measure how well distilled behavior transfers outside the selected benchmarks. Smaller students may imitate answer patterns without inheriting the teacher's full robustness, and selecting shortest correct traces can remove useful explanation or hide brittle shortcuts. Distillation also depends on access to a capable teacher and permission to use its outputs.

## What Changed
- Created a synthesis linking model-size distillation with Kimi's reasoning-length compression methods.

## Related Concepts
- [[ChainOfThoughtReasoning]] - behavior transferred or shortened by the distillation process.
- [[DeepSeekR1]] - teacher model family and source of the reported distilled checkpoints.
- [[KimiK15]] - uses Long2Short methods for compact reasoning.
- [[GroupRelativePolicyOptimization]] - direct RL alternative that the DeepSeek comparison finds less efficient for smaller models.
- [[PersonaDistillation]] - another lossy transfer concept, applied to a person's recorded outputs rather than model reasoning capability.
