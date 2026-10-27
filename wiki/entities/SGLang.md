---
title: "SGLang"
type: entity
tags: [ai, inference, serving, open-source]
sources:
  - modal-multimodal-dictionary
  - rl-r3-best-implementation
last_updated: 2026-10-27
knowledge_schema: synthesis-v1
---

## Overview
[[SGLang]] is an open-source inference engine represented here through two data paths: multimodal request preparation through a single-threaded scheduler and capture of per-token routing or sparse-attention choices for [[RolloutTrainingStateReplay]].

## Current Profile
In the multimodal architecture, tokenizer processes prepare tensors while the scheduler forms batches and dispatches GPU work. The scheduler is therefore both a coordination point and a system-wide latency gate: repeated host bookkeeping in request preparation can idle the GPU and delay every in-flight request. SGLang v0.5.10 includes an optional CUDA IPC pool-handle cache that reconstructs each stable pool storage once and reuses it across tensor offsets.

In the RL account, SGLang is also the replay producer. Per-layer choices first land in device buffers; speculative-decoding verification can overwrite an in-memory tail; stable prefixes are chunked to shared storage under byte-level backpressure; and response metadata carries references rather than the full record. Only one owner rank writes objects so every stored object has a reachable key and reclamation path.

## Key Characteristics
- Separates server I/O, tokenization, scheduling, detokenization, and GPU forward passes across processes.
- Uses one scheduler thread to process requests, form batches, and dispatch GPU work.
- Shares large on-device multimodal tensors across processes through CUDA IPC pool handles and offsets.
- Supports mixed-chunk scheduling in which prefill and decode tokens can share a batch.
- Includes a pool-handle cache intended to remove repeated PyTorch shared-storage reconstruction.
- Can capture per-token discrete model choices in device buffers for later rollout-training replay.
- Separates a mutable speculative-decoding tail from stable, immutable chunks written by one owner rank under backpressure.

## Evidence
- Architecture: [[modal-multimodal-dictionary]] diagrams the CPU processes, IPC links, and scheduler-to-GPU dispatch boundary.
- Hot path: [[modal-multimodal-dictionary]] attributes 12.94% of scheduler samples to input processing and 3.43% to repeated `_new_shared_cuda` calls before optimization.
- Cache behavior: [[modal-multimodal-dictionary]] shows the old per-tensor open path and the new one-open-per-pool dictionary lookup.
- Outcome: [[modal-multimodal-dictionary]] reports throughput rising from 22.2 to 25.7 requests/s and mean end-to-end latency falling from 1,979 to 1,768 ms on one Qwen2.5-VL-3B-Instruct/H100 workload.

Replay capture:
- [[rl-r3-best-implementation]] describes device-buffer recording, speculative-tail overwrite, asynchronous chunk writes, owner-rank selection, and reference-only response metadata for sparse-attention replay.

## Qualifications
Both sources are first-party practitioner accounts. The multimodal benchmark covers one model, one H100 setup, and one workload; it does not compare engines, isolate every system factor, report repeated-run variance, or establish gains for text-only serving. The replay source gives no SGLang version, released implementation, correctness audit, hardware configuration, or component-level timing, so its reported end-to-end result should not be attributed to SGLang alone.

## What Changed
- Added SGLang's role as the producer of chunked rollout-replay state.
- Added speculative-tail handling, write backpressure, and single-rank object ownership.
- Qualified replay performance as a whole-pipeline result rather than an engine-only benchmark.

## Relationships
- [[InferenceHostOverhead]] - SGLang's scheduler exposes host work as a GPU-dispatch bottleneck.
- [[Modal]] - Modal engineers profiled, benchmarked, and upstreamed the pool-handle cache.
- [[PyTorchTransformers]] - PyTorch shared-storage reconstruction was the immediate hot-path implementation cost.
- [[HighThroughputIOOptimization]] - SGLang applies the same invariant-bookkeeping elimination principle to interprocess GPU storage.
- [[RolloutTrainingStateReplay]] - SGLang captures discrete choices and publishes stable payload chunks plus lightweight references.
- [[Mooncake]] - receives the immutable replay objects written by SGLang in the RL account.
