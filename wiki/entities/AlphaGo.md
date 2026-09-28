---
title: "AlphaGo"
type: entity
tags: [ai, deep-learning, reinforcement-learning, games]
sources:
  - from-2016-why-deep-learning-is-suddenly-changing-your-life-fortune
last_updated: 2026-09-28
knowledge_schema: synthesis-v1
---

## Overview
[[AlphaGo]] is presented as DeepMind's Go-playing system that combined deep learning with reinforcement learning and defeated a champion player in March 2016.

## Current Profile
The article uses AlphaGo to show that deep learning can be combined with other AI methods rather than used alone. Unlike the rule and evaluation framing it assigns to IBM's Deep Blue, AlphaGo learned from professional games and extensive self-play, reportedly playing a million games against itself during training. The feature treats the victory as a landmark but uses DeepMind's later data-center work to argue that trial-and-error policy learning may also apply to operational control problems.

## Key Characteristics
- Combined deep neural methods with reinforcement learning.
- Learned from professional game records and self-play rather than only hand-authored evaluation rules.
- Defeated a champion Go player in March 2016.
- Served as a public landmark for learned sequential decision making.
- Inspired analogies to industrial control, though the article does not establish direct technical equivalence.

## Evidence
- Method combination: [[from-2016-why-deep-learning-is-suddenly-changing-your-life-fortune]] explicitly attributes AlphaGo to deep learning plus reinforcement learning.
- Training route: [[from-2016-why-deep-learning-is-suddenly-changing-your-life-fortune]] says it learned from professional games and played a million self-play games during training.
- Public milestone: [[from-2016-why-deep-learning-is-suddenly-changing-your-life-fortune]] identifies the March 2016 champion defeat as a landmark AI achievement.
- Transfer analogy: [[from-2016-why-deep-learning-is-suddenly-changing-your-life-fortune]] connects trial-and-error learning to DeepMind's reported data-center efficiency work.

## Qualifications
The magazine account omits the precise AlphaGo architecture, evaluation conditions, opponent, match score, compute cost, and distinction among imitation learning, search, value estimation, and reinforcement learning. Mastery of a bounded board game does not by itself demonstrate open-world reasoning or general intelligence.

## What Changed
- Created a source-bounded profile distinguishing a landmark game result from broader claims about general intelligence or real-world transfer.

## Relationships
- [[ReinforcementLearning]] - supplies trial-and-error policy improvement through self-play.
- [[DeepLearning]] - supplies learned representations and evaluation components in the article's account.
- [[NeuralNetworkTraining]] - turns professional games and self-play trajectories into learned behavior.
- [[AndrewNg]] - appears in the same history of Google-linked deep-learning research and industrial application.
