---
title: "StarCraft"
type: entity
tags: [games, real-time-strategy, artificial-intelligence]
sources:
  - gamasutra-ben-webers-blog-deepmind-challenges-for-starcraft
last_updated: 2026-09-28
knowledge_schema: synthesis-v1
---

## Overview
[[StarCraft]] is represented as a real-time strategy game and a demanding artificial-intelligence research environment.

## Current Profile
In Weber's 2016 account, Brood War requires simultaneous economic, strategic, and tactical control over many units while much of the opponent's state remains hidden. Seasonal map rotation and an evolving meta-game change which plans work, while surprise all-in strategies punish systems that cover only typical play. The closed-source environment also limits the large simulation loops associated with reinforcement learning.

## Key Characteristics
- Partially observable because fog of war hides unscouted areas and opponent actions.
- Real-time, requiring timely parallel control rather than alternating turns.
- High-dimensional, with hundreds of heterogeneous units and possible actions.
- Strategically nonstationary because maps, build orders, and counters change over time.
- Adversarially varied, including rare exploitative or all-in tactics.
- Deterministic at the engine level in Weber's task-environment classification.

## Evidence
- Hidden information: [[gamasutra-ben-webers-blog-deepmind-challenges-for-starcraft]] describes scouting limits and the need to infer builds and attacks.
- Control scale: [[gamasutra-ben-webers-blog-deepmind-challenges-for-starcraft]] connects large unit counts to squads, build orders, and abstraction.
- Adaptation: [[gamasutra-ben-webers-blog-deepmind-challenges-for-starcraft]] describes rotating maps, changing strategies, counters, and surprise tactics.
- Execution constraints: [[gamasutra-ben-webers-blog-deepmind-challenges-for-starcraft]] identifies real-time timing, high action rates, and restricted simulation access.

## Qualifications
The profile reflects one 2016 Brood War commentary, not the complete design of the franchise or the current state of competitive play. The source's claim that the environment is deterministic does not eliminate uncertainty caused by hidden state or opponent behavior.

## What Changed
- Created a research-oriented profile of the game's observable, strategic, and control properties.

## Relationships
- [[StarCraftAITestbed]] - interprets the game's properties as a combined AI research benchmark.
- [[BenWeber]] - researcher and competition founder supplying the source account.
- [[DeepMind]] - proposed developer of an expert-level system in the 2016 essay.
- [[ReinforcementLearning]] - possible training method constrained by simulation and state-space demands.
