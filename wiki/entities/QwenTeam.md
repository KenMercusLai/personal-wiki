---
title: "Qwen Team"
type: entity
tags: [ai-research, language-models, mixture-of-experts, alibaba]
sources:
  - 2609.39137
last_updated: 2026-10-13
knowledge_schema: synthesis-v1
---

## Overview
[[QwenTeam]] is the Alibaba research team credited in the available source with developing and evaluating [[IDBalancing]] for extremely sparse mixture-of-experts language models.

## Current Profile
In this source, the Qwen Team is situated within Alibaba Token Hub and Alibaba Group. Its represented work treats sparse-expert routing as a feedback-control problem, compares auxiliary loss with two loss-free baselines, and evaluates an integral-derivative expert-bias update across model sizes and training conditions.

## Key Characteristics
- Develops large-language-model training methods in an Alibaba research context.
- Studies decoder-only hybrid-attention MoE models with 256 or 768 routed experts.
- Evaluates load balance jointly with LM loss, downstream tasks, training dynamics, and inference expert activity.
- Frames existing loss-free routing updates through generalized PID control.

## Evidence
Organizational attribution:
- [[2609.39137]] lists Qwen Team, Alibaba Token Hub, and Alibaba Group as the author affiliation.

Technical work:
- [[2609.39137]] attributes the PID framing, ID Balancing algorithm, and experiments through 69.9B total parameters to the author team.

## Qualifications
This profile is bounded to one paper and does not describe the team's full product portfolio, organization, membership, model releases, or independent evaluation record. The reported results are first-party and specific to the tested model family.

## What Changed
- Created a source-bounded organizational profile for the ID Balancing study.

## Relationships
- [[PengJin]] - equal-contribution team author represented by the source.
- [[ZihanQiu]] - equal-contribution team author represented by the source.
- [[ZekunWang]] - equal-contribution team author represented by the source.
- [[BoZheng]] - equal-contribution team author represented by the source.
- [[DayihengLiu]] - corresponding team author represented by the source.
- [[IDBalancing]] - load-control method developed in the represented research.
- [[MixtureOfExpertsLoadBalancing]] - technical problem addressed by the represented work.
