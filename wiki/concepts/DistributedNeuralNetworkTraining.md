---
title: "Distributed Neural Network Training"
type: concept
tags: [machine-learning, distributed-systems, parallel-computing]
sources:
  - jeff-dean-on-large-scale-deep-learning-at-google-high-scalability
  - mai-thinking-1-continuous
last_updated: 2026-10-17
knowledge_schema: synthesis-v1
---

## Definition
[[DistributedNeuralNetworkTraining]] divides the computation or data of neural-network optimization across accelerators or machines so that larger models and datasets can be trained, or experiments completed, more quickly.

## Current Synthesis
The sources trace distributed training from parameter-server-era model and data parallelism to a modern sparse-MoE stack. Model parallelism partitions computation when a model is too large, while data parallelism gives replicas different examples and coordinates their updates. Asynchronous replicas maximize independent progress but may apply stale gradients; synchronous coordination reduces that inconsistency while introducing coordination and straggler costs. The operational purpose is faster, trustworthy research feedback, not merely a larger one-off run.

The [[MAIThinking1]] report expands the systems boundary. YOLO combines ZeRO optimizer sharding, tensor and sequence parallelism, Ulysses context parallelism, expert parallelism, activation checkpointing and offloading, dropless variable-size all-to-all communication, deterministic kernels and collectives, asynchronous distributed checkpoints, and hot-standby recovery. Architecture and topology are co-designed: expert traffic stays within NVLink rack domains while data-parallel communication crosses racks, and new architecture generations repeatedly expose new bottlenecks. At cluster scale, goodput—not peak FLOPs alone—accounts for MFU loss, recomputation, checkpointing, recovery, placement, and hardware health.

## Key Claims
- Model parallelism divides a model's computation across devices and pays communication cost at partition boundaries.
- Data parallelism gives replicas different training examples while coordinating updates to shared parameters.
- Asynchronous updates improve concurrency but can use gradients computed from older parameter states.
- Synchronous updates trade stale-gradient risk for coordination and slow-worker sensitivity.
- Shorter training cycles improve research productivity by allowing more experiments and faster correction.
- Sparse MoE and long-context training require parallelism choices to follow communication topology, memory pressure, and variable expert load.
- Determinism, checkpoint completeness, fault recovery, health certification, and goodput are part of training correctness and iteration speed.

## Evidence
- Model partitioning: [[jeff-dean-on-large-scale-deep-learning-at-google-high-scalability]] describes neurons as substantially independent and says work can be split across machines or GPU cards.
- Replica training: [[jeff-dean-on-large-scale-deep-learning-at-google-high-scalability]] describes replicas reading different random examples, computing gradients, and sending adjustments to centralized parameter servers.
- Scale example: [[jeff-dean-on-large-scale-deep-learning-at-google-high-scalability]] reports that Google sometimes used 500 model copies on 500 machines.
- Consistency tradeoff: [[jeff-dean-on-large-scale-deep-learning-at-google-high-scalability]] says asynchronous training can return a gradient after parameters have moved, while synchronous training uses a controller.
- Research cadence: [[jeff-dean-on-large-scale-deep-learning-at-google-high-scalability]] contrasts one-day training with six weeks on a single GPU and argues for minutes-or-hours experiment cycles.
- Modern hybrid parallelism: [[mai-thinking-1-continuous]] describes custom ZeRO 1-3, tensor/sequence, Ulysses context, and dropless expert parallelism for a 35B-active, roughly 1T-total-parameter model.
- Reliability and utilization: [[mai-thinking-1-continuous]] reports bitwise determinism, asynchronous checkpointing, hot-standby restart, topology-aware placement, 20% or higher MFU across reported architecture generations after optimization, and 90% goodput on the final 8K-GPU pretraining run.

## Counterevidence & Qualifications
The older article gives a 2016 conceptual description, not benchmark-normalized results, communication topology, fault model, convergence analysis, or cost comparison. Its claim that stale gradients were acceptable up to roughly 50 to 100 replicas is model- and system-dependent, not a universal threshold. The MAI report supplies far richer topology and recovery detail but remains a first-party account without released code, full telemetry, equal-hardware framework comparisons, energy accounting, or independent reproduction. Its GB200/GB300, Azure Blob Storage, NVLink, InfiniBand, Ray, Kubernetes, and sparse-MoE choices are workload- and platform-specific rather than universal prescriptions.

## What Changed
- Added hybrid parallelism, topology-aware sparse-MoE placement, and activation memory management.
- Added bitwise determinism, distributed checkpointing, hot-standby recovery, and hardware certification as training-system properties.
- Added goodput as an end-to-end complement to local MFU and theoretical peak throughput.

## Related Concepts
- [[DeepLearningScaling]] - distinguishes training-resource growth from broad capability growth.
- [[NeuralNetworkTraining]] - supplies the optimization loop being distributed.
- [[ParallelProgramming]] - broader family of techniques for dividing computational work.
- [[EndToEndLearning]] - often creates large training workloads that benefit from distributed execution.
- [[StochasticGradientDescent]] - optimization family whose gradients replicas estimate and coordinate.
- [[MAIThinking1]] - frontier-scale case combining sparse pretraining and asynchronous RL infrastructure.
- [[HillClimbingMachine]] - uses reliable distributed execution to make model-development feedback loops trustworthy.
- [[MixtureOfExpertsLoadBalancing]] - couples expert-routing quality to communication volume, memory use, and execution balance.
