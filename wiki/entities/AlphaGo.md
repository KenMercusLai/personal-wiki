---
title: "AlphaGo"
type: entity
tags: [ai, deep-learning, reinforcement-learning, games]
sources:
  - from-2016-why-deep-learning-is-suddenly-changing-your-life-fortune
  - gamasutra-ben-webers-blog-deepmind-challenges-for-starcraft
last_updated: 2026-09-28
knowledge_schema: synthesis-v1
---

## Overview
[[AlphaGo]] is presented as [[DeepMind]]'s Go-playing system that combined learned policy and evaluation components, reinforcement learning, and Monte Carlo tree search to defeat Lee Sedol in March 2016.

## Current Profile
The sources use AlphaGo to show that deep learning can be combined with other AI methods rather than used alone. The Fortune feature says it learned from professional games and extensive self-play, reportedly playing a million games against itself. Weber adds Monte Carlo tree search to the account and uses the Lee Sedol match as the departure point for a harder proposed challenge: [[StarCraftAITestbed]], where state is hidden, actions are numerous, strategies evolve, and execution is real time. That contrast makes AlphaGo a demonstrated bounded-game milestone rather than evidence that the same system design transfers unchanged to richer environments.

## Key Characteristics
- Combined deep neural methods with reinforcement learning.
- Learned from professional game records and self-play rather than only hand-authored evaluation rules.
- Used Monte Carlo tree search to evaluate possible board states in Weber's high-level account.
- Defeated a champion Go player in March 2016.
- Served as a public landmark for learned sequential decision making.
- Became a comparison point for harder partially observable, real-time environments.

## Evidence
- Method combination: [[from-2016-why-deep-learning-is-suddenly-changing-your-life-fortune]] explicitly attributes AlphaGo to deep learning plus reinforcement learning.
- Training route: [[from-2016-why-deep-learning-is-suddenly-changing-your-life-fortune]] says it learned from professional games and played a million self-play games during training.
- Public milestone: [[from-2016-why-deep-learning-is-suddenly-changing-your-life-fortune]] identifies the March 2016 champion defeat as a landmark AI achievement.
- Search and match context: [[gamasutra-ben-webers-blog-deepmind-challenges-for-starcraft]] names Monte Carlo tree search and identifies Lee Sedol as the professional opponent.
- Transfer boundary: [[gamasutra-ben-webers-blog-deepmind-challenges-for-starcraft]] contrasts fully observable Go with hidden-state, real-time StarCraft.

## Qualifications
Both accounts are short secondary explanations rather than technical specifications. The Fortune feature omits the opponent, architecture, evaluation conditions, compute cost, and distinction among imitation learning, search, value estimation, and reinforcement learning. Weber names Lee Sedol and Monte Carlo tree search but compresses DeepMind's methods into a loose description that includes Q-learning and autoencoders. Mastery of a bounded board game does not by itself demonstrate open-world reasoning, expert real-time strategy play, or general intelligence.

## What Changed
- Added Lee Sedol, Monte Carlo tree search, and the contrast between fully observable Go and real-time partially observable StarCraft.
- Strengthened the boundary between a landmark bounded-game result and claims about transfer or general intelligence.

## Relationships
- [[ReinforcementLearning]] - supplies trial-and-error policy improvement through self-play.
- [[DeepLearning]] - supplies learned representations and evaluation components in the article's account.
- [[NeuralNetworkTraining]] - turns professional games and self-play trajectories into learned behavior.
- [[StarCraftAITestbed]] - exposes uncertainty, action complexity, adaptation, and timing challenges absent from the source's Go comparison.
- [[AndrewNg]] - appears in the same history of Google-linked deep-learning research and industrial application.
