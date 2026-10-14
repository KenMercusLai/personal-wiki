---
title: "SGLang"
type: entity
tags: [ai, inference, serving, open-source]
sources:
  - modal-multimodal-dictionary
last_updated: 2026-10-14
knowledge_schema: synthesis-v1
---

## Overview
[[SGLang]] is an open-source inference engine whose multimodal request path uses tokenizer workers, a single-threaded scheduler, GPU model execution, and CUDA IPC for cross-process tensor access.

## Current Profile
In the reported architecture, tokenizer processes prepare multimodal tensors while the scheduler forms batches and dispatches GPU work. The scheduler is therefore both a coordination point and a system-wide latency gate: repeated host bookkeeping in request preparation can idle the GPU and delay every in-flight request. SGLang v0.5.10 includes an optional CUDA IPC pool-handle cache that reconstructs each stable pool storage once and reuses it across tensor offsets.

## Key Characteristics
- Separates server I/O, tokenization, scheduling, detokenization, and GPU forward passes across processes.
- Uses one scheduler thread to process requests, form batches, and dispatch GPU work.
- Shares large on-device multimodal tensors across processes through CUDA IPC pool handles and offsets.
- Supports mixed-chunk scheduling in which prefill and decode tokens can share a batch.
- Includes a pool-handle cache intended to remove repeated PyTorch shared-storage reconstruction.

## Evidence
- Architecture: [[modal-multimodal-dictionary]] diagrams the CPU processes, IPC links, and scheduler-to-GPU dispatch boundary.
- Hot path: [[modal-multimodal-dictionary]] attributes 12.94% of scheduler samples to input processing and 3.43% to repeated `_new_shared_cuda` calls before optimization.
- Cache behavior: [[modal-multimodal-dictionary]] shows the old per-tensor open path and the new one-open-per-pool dictionary lookup.
- Outcome: [[modal-multimodal-dictionary]] reports throughput rising from 22.2 to 25.7 requests/s and mean end-to-end latency falling from 1,979 to 1,768 ms on one Qwen2.5-VL-3B-Instruct/H100 workload.

## Qualifications
The evidence is a first-party benchmark of one model, one H100 setup, and one multimodal workload. It does not compare SGLang with other inference engines, isolate every changed system factor, report repeated-run variance, or establish gains for text-only serving. The authors expect benefits to scale with multimodal inputs, but that expectation is not independently tested here.

## What Changed
- Created the entity profile around SGLang's scheduler and multimodal CUDA IPC path.

## Relationships
- [[InferenceHostOverhead]] - SGLang's scheduler exposes host work as a GPU-dispatch bottleneck.
- [[Modal]] - Modal engineers profiled, benchmarked, and upstreamed the pool-handle cache.
- [[PyTorchTransformers]] - PyTorch shared-storage reconstruction was the immediate hot-path implementation cost.
- [[HighThroughputIOOptimization]] - SGLang applies the same invariant-bookkeeping elimination principle to interprocess GPU storage.
