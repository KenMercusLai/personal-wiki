---
title: "Mooncake"
type: entity
tags: [ai, inference, kv-cache, data-transfer]
sources:
  - qiong-ren-ban-pd-fen-li-zai-xiao-fei-ji-xian-ka-shang-ba-tts-tui-li-chai-cheng-liang-ban
  - rl-r3-best-implementation
last_updated: 2026-10-27
knowledge_schema: synthesis-v1
---

## Overview
[[Mooncake]] is a data-transfer and shared-storage system represented here in two roles: moving KV cache between prefill and decode workers and holding immutable, layer-sharded rollout-replay payloads between inference and training.

## Current Profile
In the reported environment, the pinned wheel omitted NVLink transport, a newer configuration could silently fall back to TCP, and upstream same-host NVLink worked only while both sides shared a container-visible GPU context. The team therefore forked Mooncake for two hardware-specific paths: B300 prefill imported decode's FABRIC allocation and gathered scattered source rows directly into it, while RTX 5090 workers registered memory with a per-unit `nvlink_proxy` that opened both CUDA IPC handles and performed PCIe P2P copies.

The fork also became the boundary for fragmentation and correctness fixes. It added gather support, multithreaded TCP, and protocol changes that attach request identity and remaining-time metadata, reject late chunks at the receiver, and expose a batch-quiescence result only when terminal state can be proved. These are source-specific extensions, not evidence that the upstream project provides the same behavior.

The RL source reuses Mooncake as shared storage rather than describing another KV handoff. Stable Top-K record chunks are written once, addressed by UUID, and divided by model layer so each training pipeline stage can retrieve only what it consumes. Lightweight object-and-range references cross the control path; the account does not specify whether this storage behavior is upstream, fork-specific, or tied to a particular Mooncake version.

## Key Characteristics
- Transfers KV state between prefill and decode workers through selectable transport paths.
- Depends on build contents, protocol selection, driver capabilities, IMEX configuration, and container-visible devices.
- Was extended with B300 FABRIC direct-write and RTX 5090 proxy-mediated P2P paths.
- Uses gather operations to avoid thousands of inefficient small copies from paged KV pools.
- Was extended with request-aware terminal-state semantics to prevent late writes into recycled pages.
- Stores write-once, UUID-addressed replay chunks whose layer partitioning supports stage-selective reads.
- Lets lightweight manifests travel separately from payloads that are materialized only at the training consumer.

## Evidence
Transport discovery:
- [[qiong-ren-ban-pd-fen-li-zai-xiao-fei-ji-xian-ka-shang-ba-tts-tui-li-chai-cheng-liang-ban]] reports a missing wheel transport, silent TCP fallback, IMEX-related `cuMemCreate` failure, and cross-Pod CUDA visibility errors.

Hardware-specific fork:
- [[qiong-ren-ban-pd-fen-li-zai-xiao-fei-ji-xian-ka-shang-ba-tts-tui-li-chai-cheng-liang-ban]] describes B300 FABRIC import and direct gather writes, plus an RTX 5090 sidecar that imports both workers' CUDA IPC handles for P2P transfer.

Fragmentation behavior:
- [[qiong-ren-ban-pd-fen-li-zai-xiao-fei-ji-xian-ka-shang-ba-tts-tui-li-chai-cheng-liang-ban]] observes transfer expansion from 72 to 105,660 fragments and uses contiguous staging to recover millisecond-scale handoff.

Failure semantics:
- [[qiong-ren-ban-pd-fen-li-zai-xiao-fei-ji-xian-ka-shang-ba-tts-tui-li-chai-cheng-liang-ban]] reports that an older peer could write more than 2 MiB after apparent quiescence, motivating request IDs, late-block rejection, and terminal acknowledgement in TCP protocol v3.

Rollout-training storage:
- [[rl-r3-best-implementation]] describes immutable layer-sharded objects, UUID-and-range handles, asynchronous writes with backpressure, stage-selective reads, and deletion from the batch manifest after consumption.

## Qualifications
This profile comes from two practitioner deployments rather than upstream documentation or an independent audit. Exact throughput, storage latency, and supported handles depend on GPU, topology, driver, container runtime, build, and object-store configuration. The proxy's ability to see every GPU expands its authority and should not be treated as a general isolation recommendation. Silent fallback, protocol compatibility, quiescence behavior, and replay-object storage are reported without precise Mooncake versions; the sources do not establish that every described extension exists upstream.

## What Changed
- Expanded the profile from KV handoff to shared storage for rollout-training replay objects.
- Added write-once UUID addressing, layer sharding, reference-only control flow, and consumer-side materialization.
- Preserved uncertainty about which reported capabilities are upstream versus deployment-specific.

## Relationships
- [[PrefillDecodeDisaggregation]] - Mooncake carries KV state across the source's separated inference phases.
- [[KVCacheAwareRouting]] - both operate on reusable KV state, while Mooncake handles transfer rather than route selection.
- [[MicroserviceFailureContainment]] - terminal acknowledgement and bounded restart prevent a failed transfer from silently corrupting another request.
- [[RolloutTrainingStateReplay]] - Mooncake stores heavy replay payloads while manifests and token handles traverse the training control path.
- [[SGLang]] - produces the stable replay chunks stored by Mooncake in the RL account.
