---
title: "Kimi K3"
type: entity
tags: [ai, reasoning-model, mixture-of-experts, kimi]
sources:
  - controlling-reasoning-effort
  - latent-moe
last_updated: 2026-10-22
knowledge_schema: synthesis-v1
---

## Overview
[[KimiK3]] is a Kimi reasoning model described by the available secondary sources as operating at roughly 2.8-trillion-parameter scale, consolidating multiple domain-and-effort specialists, and using a system named Stable LatentMoE.

## Current Profile
The wiki has only a partial architectural and post-training profile. One comparative explainer says Kimi K3 distills nine specialists spanning domains and reasoning-effort levels into one checkpoint. A separate systems article says its launch material names Stable LatentMoE and presents this as a likely variant of latent expert compression, but explicitly awaits a technical report. These claims suggest co-design across sparse capacity, communication efficiency, and controllable reasoning, while leaving exact active parameters, routing, latent dimensions, training recipe, evaluations, and serving behavior undocumented here.

## Key Characteristics
- Described as a roughly 2.8T-parameter-scale model rather than an independently documented exact configuration.
- Reported to consolidate nine domain-and-effort specialist models into one checkpoint.
- Reported to use Stable LatentMoE, whose exact relationship to the published LatentMoE pattern is not established by the available sources.

## Evidence
Reasoning-effort consolidation:
- [[controlling-reasoning-effort]] contrasts Kimi K3's nine-specialist domain-and-effort distillation with Kimi Toggle's alternating budget-limited and unconstrained training.

Sparse architecture and scale:
- [[latent-moe]] describes Kimi K3 as a 2.8T-parameter-scale deployment and says its launch blog names Stable LatentMoE.

## Qualifications
Both sources are secondary explainers rather than the Kimi K3 technical report. The parameter figure is presented as a scale description, not a fully specified total-versus-active parameter accounting. The wiki lacks controlled evaluations, architecture tables, training details, serving measurements, and independent reproduction. Stable LatentMoE may differ materially from the generic diagram, so its mechanism should remain provisional.

## What Changed
- Created a bounded profile connecting reported model scale, specialist distillation, and the provisional Stable LatentMoE claim.

## Relationships
- [[LatentMoE]] - likely architecture family behind the named Stable LatentMoE system, pending technical documentation.
- [[ReasoningEffort]] - training dimension represented across the nine reported specialists.
- [[ReasoningModelDistillation]] - consolidation mechanism reported to merge specialist behavior into one checkpoint.
- [[MixtureOfExpertsLoadBalancing]] - routing constraint for any sparse expert implementation at this scale.
