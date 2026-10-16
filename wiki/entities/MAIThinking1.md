---
title: "MAI-Thinking-1"
type: entity
tags: [large-language-model, reasoning-model, mixture-of-experts, microsoft]
sources:
  - mai-thinking-1-continuous
last_updated: 2026-10-17
knowledge_schema: synthesis-v1
---

## Overview
[[MAIThinking1]] is a [[MicrosoftAI]] reasoning model with 35B active and roughly 1T total parameters, a 256K context window, sparse 8-of-512 expert routing, and post-training for STEM reasoning, agentic coding and tool use, helpfulness, and safety.

## Current Profile
The model is built from the MAI-Base-1 checkpoint after 30T pretraining tokens, 3.55T mid-training tokens, three specialist RL climbs, SFT consolidation, and a final RL stage. The team reports 97.0% on AIME 2025, 94.5% on AIME 2026, 87.7% on LiveCodeBench v6, 73.5% on SWE-bench Verified, and 52.8% on SWE-Bench Pro. Its strongest public case is broad competence for its active size plus unusually explicit training-system detail, while its limits include first-party evaluation, high output budgets, proprietary data and infrastructure, and incomplete safety coverage.

## Key Characteristics
- Decoder-only sparse MoE with 35B active and about 1T total parameters, alternating dense and sparse feed-forward blocks.
- Periodic local and global attention and a progressively extended 256K context window.
- Trained from scratch on human-generated public and licensed data without third-party model distillation.
- Post-trained through separate STEM, agentic, and helpfulness-and-safety climbs before consolidation.
- Uses tool-calling loops with bash and string-replacement tools for software-engineering tasks.
- Evaluated across STEM, coding, tool use, long context, instruction following, safety, honesty, and health.

## Evidence
Architecture and training:
- [[mai-thinking-1-continuous]] specifies model size, sparse routing, 30T-token pretraining, 3.55T-token mid-training, and progressive context extension.

Post-training behavior:
- [[mai-thinking-1-continuous]] describes modified GRPO, self-distillation, specialist consolidation, verifiable rewards, agentic environments, preference rewards, and safety signals.

Evaluation:
- [[mai-thinking-1-continuous]] reports public benchmark results averaged across four runs, a 1,276-task English human evaluation, internal safety testing, and red-team outcomes.

## Qualifications
The checkpoint, complete training corpus, private evaluations, and training code are not available for independent reproduction. External scores and in-house reruns use different harnesses and budgets; STEM outputs may use up to 256K tokens, and some general capability and safety metrics depend on LLM judges. Human comparison covers English text tasks and excludes several tool, multimodal, and custom-environment cases.

## What Changed
- Created the model profile with its architecture, training path, reported strengths, and evaluation limits.

## Relationships
- [[MicrosoftAI]] - developer and evaluator of the model.
- [[HillClimbingMachine]] - integrated process used to produce the model.
- [[ReinforcementLearning]] - post-training framework for its learned reasoning and tool behavior.
- [[MixtureOfExpertsLoadBalancing]] - controls token routing across its sparse experts.
- [[ReasoningModelDistillation]] - self-distillation transfers progress between its own checkpoints.
- [[AgenticSandboxInfrastructure]] - supplies isolated stateful environments for tool-use training and evaluation.
