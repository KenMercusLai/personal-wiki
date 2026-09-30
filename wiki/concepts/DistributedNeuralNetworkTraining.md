---
title: "Distributed Neural Network Training"
type: concept
tags: [machine-learning, distributed-systems, parallel-computing]
sources:
  - jeff-dean-on-large-scale-deep-learning-at-google-high-scalability
last_updated: 2026-10-01
knowledge_schema: synthesis-v1
---

## Definition
[[DistributedNeuralNetworkTraining]] divides the computation or data of neural-network optimization across accelerators or machines so that larger models and datasets can be trained, or experiments completed, more quickly.

## Current Synthesis
The source separates two kinds of parallelism. Model parallelism partitions neurons or layers across machines when the model itself is too large or computationally expensive, with communication concentrated at partition boundaries. Data parallelism runs multiple model replicas on different examples and sends their gradients to shared parameter servers. Asynchronous replicas maximize independent progress but may apply stale gradients; synchronous coordination reduces that inconsistency while introducing coordination and straggler costs. The operational purpose is faster research feedback, not merely a larger one-off run.

## Key Claims
- Model parallelism divides a model's computation across devices and pays communication cost at partition boundaries.
- Data parallelism gives replicas different training examples while coordinating updates to shared parameters.
- Asynchronous updates improve concurrency but can use gradients computed from older parameter states.
- Synchronous updates trade stale-gradient risk for coordination and slow-worker sensitivity.
- Shorter training cycles improve research productivity by allowing more experiments and faster correction.

## Evidence
- Model partitioning: [[jeff-dean-on-large-scale-deep-learning-at-google-high-scalability]] describes neurons as substantially independent and says work can be split across machines or GPU cards.
- Replica training: [[jeff-dean-on-large-scale-deep-learning-at-google-high-scalability]] describes replicas reading different random examples, computing gradients, and sending adjustments to centralized parameter servers.
- Scale example: [[jeff-dean-on-large-scale-deep-learning-at-google-high-scalability]] reports that Google sometimes used 500 model copies on 500 machines.
- Consistency tradeoff: [[jeff-dean-on-large-scale-deep-learning-at-google-high-scalability]] says asynchronous training can return a gradient after parameters have moved, while synchronous training uses a controller.
- Research cadence: [[jeff-dean-on-large-scale-deep-learning-at-google-high-scalability]] contrasts one-day training with six weeks on a single GPU and argues for minutes-or-hours experiment cycles.

## Counterevidence & Qualifications
The article gives a 2016 conceptual description, not benchmark-normalized results, communication topology, fault model, convergence analysis, or cost comparison. Its claim that stale gradients were acceptable up to roughly 50 to 100 replicas is model- and system-dependent, not a universal threshold. Modern distributed training can use different collective, sharding, optimizer-state, and pipeline designs.

## What Changed
- Created the concept to separate distributed optimization mechanics from the broader claim that scaling produces capability.

## Related Concepts
- [[DeepLearningScaling]] - distinguishes training-resource growth from broad capability growth.
- [[NeuralNetworkTraining]] - supplies the optimization loop being distributed.
- [[ParallelProgramming]] - broader family of techniques for dividing computational work.
- [[EndToEndLearning]] - often creates large training workloads that benefit from distributed execution.
- [[StochasticGradientDescent]] - optimization family whose gradients replicas estimate and coordinate.
