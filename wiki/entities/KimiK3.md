---
title: "Kimi K3"
type: entity
tags: [ai, reasoning-model, mixture-of-experts, kimi]
sources:
  - controlling-reasoning-effort
  - latent-moe
  - whos-afraid-of-chinese-models
last_updated: 2026-10-26
knowledge_schema: synthesis-v1
---

## Overview
[[KimiK3]] is a Chinese open-weight Kimi reasoning model described by the available secondary sources as operating at roughly 2.8-trillion-parameter scale, consolidating multiple domain-and-effort specialists, and using a system named Stable LatentMoE.

## Current Profile
The wiki has only a partial architectural, post-training, and economic profile. One comparative explainer says Kimi K3 distills nine specialists spanning domains and reasoning-effort levels into one checkpoint. A separate systems article says its launch material names Stable LatentMoE and presents this as a likely variant of latent expert compression, but explicitly awaits a technical report. Thompson's strategy essay uses Kimi K3 as a near-frontier open-weight competitor and reports a lower API token price than a U.S. frontier alternative, while arguing that heavier reasoning-token use may erase that apparent advantage at the level of a correct answer. Together the sources point toward co-design across sparse capacity, communication, controllable reasoning, and serving cost, but do not disclose an equal-quality unit-cost comparison.

## Key Characteristics
- Described as a roughly 2.8T-parameter-scale model rather than an independently documented exact configuration.
- Reported to consolidate nine domain-and-effort specialist models into one checkpoint.
- Reported to use Stable LatentMoE, whose exact relationship to the published LatentMoE pattern is not established by the available sources.
- Used as an example of why open weights and low token prices do not by themselves establish low task-level inference cost.

## Evidence
Reasoning-effort consolidation:
- [[controlling-reasoning-effort]] contrasts Kimi K3's nine-specialist domain-and-effort distillation with Kimi Toggle's alternating budget-limited and unconstrained training.

Sparse architecture and scale:
- [[latent-moe]] describes Kimi K3 as a 2.8T-parameter-scale deployment and says its launch blog names Stable LatentMoE.

Economic positioning:
- [[whos-afraid-of-chinese-models]] presents Kimi K3 as a near-frontier Chinese open-weight model but argues that token efficiency and serving cost must be compared at equal task quality.

## Qualifications
All three sources are secondary explainers or strategy analysis rather than the Kimi K3 technical report. The parameter figure is a scale description, not a fully specified total-versus-active parameter accounting. The quoted API prices do not reveal provider subsidy, hardware, utilization, token-to-solution efficiency, latency, or equal-quality cost. The wiki lacks controlled evaluations, architecture tables, training details, serving measurements, and independent reproduction. Stable LatentMoE may differ materially from the generic diagram, so its mechanism should remain provisional.

## What Changed
- Added Kimi K3's open-weight competitive position and the distinction between token price and equal-task inference cost.

## Relationships
- [[LatentMoE]] - likely architecture family behind the named Stable LatentMoE system, pending technical documentation.
- [[ReasoningEffort]] - training dimension represented across the nine reported specialists.
- [[ReasoningModelDistillation]] - consolidation mechanism reported to merge specialist behavior into one checkpoint.
- [[MixtureOfExpertsLoadBalancing]] - routing constraint for any sparse expert implementation at this scale.
- [[ProductCommoditization]] - Kimi K3 tests whether bounded intelligence is becoming substitutable across providers.
