---
title: "Castform"
type: entity
tags: [ai, reinforcement-learning, model-post-training, agentic-retrieval]
sources:
  - training-100x-cheaper-retrieval-models-neon-and-castform
last_updated: 2026-10-13
knowledge_schema: synthesis-v1
---

## Overview
[[Castform]] is a model post-training platform presented as turning an organization's existing corpus into synthetic tasks and reinforcement-learning an open-weights model to use retrieval tools.

## Current Profile
In the joint case study with [[Neon]], Castform manages task generation, tool configuration, reward definition, parallel rollouts, and run inspection. Its target is a specialized retrieval agent that can outperform a base small model and, in the vendor's reported evaluation, rival or exceed several frontier models at lower inference cost.

## Key Characteristics
- Converts corpus documents into synthetic questions and inferred ground-truth answers.
- Runs reinforcement-learning post-training around developer-specified tools and rewards.
- Trains retrieval, citation, and final-answer behavior together in the worked example.
- Exposes aggregate reward progress and individual rollout traces for debugging.
- Uses the same Neon search interface during training and production inference.

## Evidence
- Dataset creation: [[training-100x-cheaper-retrieval-models-neon-and-castform]] shows a policy document transformed into an inferred answer and a paraphrased user question.
- Training contract: [[training-100x-cheaper-retrieval-models-neon-and-castform]] specifies a hybrid-search tool and a reward composed of retrieval, citation, and correctness signals.
- Reported outcome: [[training-100x-cheaper-retrieval-models-neon-and-castform]] charts the fine-tune at 1.447 mean reward and $0.000920 per rollout, above the displayed base and comparison models on reward.
- Observability: [[training-100x-cheaper-retrieval-models-neon-and-castform]] says users can inspect both the reward curve and individual tasks for broken tools or reward hacking.

## Qualifications
The only evidence is a promotional joint case study. It does not disclose the evaluation dataset, model and training configuration, sample counts, uncertainty, equivalent tool budgets, token usage, hardware, or independent reproduction, so neither general frontier-model superiority nor a universal 100x cost reduction is established.

## What Changed
- Created the Castform profile as a corpus-to-task and reinforcement-learning platform for specialized retrieval agents.
- Recorded the vendor-reported cost/reward result while narrowing it to the displayed comparison and missing methodology.

## Relationships
- [[Neon]] - supplies the shared storage, search, and elastic database environment used across training and inference.
- [[AgenticRAG]] - is the retrieval-control behavior Castform trains in this case study.
- [[ReinforcementLearning]] - supplies the trial-and-reward optimization loop managed by Castform.
- [[RetrievalAugmentedGeneration]] - provides the corpus and retrieval baseline that the trained agent extends.
