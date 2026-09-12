---
title: "Deep Learning Scaling"
type: concept
tags: [ai, machine-learning, scaling]
sources:
  - ai-winter-is-well-on-its-way-piekniewskis-blog
last_updated: 2026-09-13
knowledge_schema: synthesis-v1
---

## Definition
[[DeepLearningScaling]] is the claim or practice that increasing compute, data, model size, or training effort can produce stronger deep-learning capabilities.

## Current Synthesis
The source challenges a simple scaling story. It reads the OpenAI compute chart, whose y-axis shows petaflops per day on a log scale and whose points run from AlexNet through AlphaGo Zero and AlphaZero, as evidence that compute use exploded without yielding proportional general capability. Piekniewski accepts that compute can make specific systems bigger or faster, but argues that image-classification gains saturated, game-oriented reinforcement-learning systems relied on simulated data, and more compute did not automatically solve real-world vision or driving.

## Key Claims
- Compute scaling and capability scaling are different claims and should not be conflated.
- Vision benchmarks can saturate while real-world vision remains unsolved.
- Additional compute helps most when matched with suitable data, architecture, and domain structure.
- Reinforcement-learning game successes can require large simulated experience that does not transfer directly to open-world applications.
- Treating a compute-growth chart as proof of deep-learning scalability can invert the lesson if capability gains are narrow or benchmark-bound.

## Evidence
- Compute chart: [[ai-winter-is-well-on-its-way-piekniewskis-blog]] includes a chart from AlexNet to AlphaGo Zero showing roughly 300,000x growth in training compute.
- Vision saturation: [[ai-winter-is-well-on-its-way-piekniewskis-blog]] argues that ImageNet classification improvements after AlexNet required more compute and architecture tuning without solving vision generally.
- Data dependence: [[ai-winter-is-well-on-its-way-piekniewskis-blog]] says additional compute buys little without far more data samples, which are easiest to obtain in simulation.
- Game limitation: [[ai-winter-is-well-on-its-way-piekniewskis-blog]] treats AlphaGo Zero, AlphaZero, and Dota-style agents as impressive but domain-bound because games provide simulators and clear rewards.

## Counterevidence & Qualifications
The source predates later foundation-model and LLM scaling results, so its critique should be read as a 2018 assessment of deep learning in vision, games, and autonomous driving. It does not disprove all scaling laws; instead, it warns that compute curves alone do not establish broad, robust, real-world intelligence.

## What Changed
- Created the concept page for distinguishing compute growth from transferable capability growth.

## Related Concepts
- [[DeepLearning]] - scaling is one contested claim about deep-learning progress.
- [[ReinforcementLearning]] - game-focused reinforcement learning appears as a compute-heavy but simulator-dependent case.
- [[AIWinter]] - disappointment with scaling claims contributes to winter risk.
- [[AutonomousDrivingSafety]] - driving is the application where the source argues scaling failed to deliver reliable capability.
- [[StatisticalModelThinking]] - both encourage distinguishing proxies and measurements from the underlying phenomenon.
