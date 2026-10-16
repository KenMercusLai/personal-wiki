---
title: "GeminiFS"
type: entity
tags: [gpu, file-system, nvme, machine-learning-systems]
sources:
  - geminifs
last_updated: 2026-10-17
knowledge_schema: synthesis-v1
---

## Overview
[[GeminiFS]] is a research companion file system that lets GPU programs issue file-based reads and writes directly to NVMe storage while a conventional host file system remains responsible for file creation and namespace management.

## Current Profile
GeminiFS splits a file system along processor strengths. CPU code pre-allocates a GVDK file and embeds its attributes plus a two-level logical-to-physical block map; GPU code caches that metadata, translates offsets, and submits requests through GPU-resident NVMe queues registered by a shared host driver. libGemini exposes a deliberately small interface, and a software-defined GPU page cache can be shared across processes.

The result sits between CPU-orchestrated file I/O and raw-device GPU storage. It preserves a host-managed file boundary while shortening the per-request control and data paths, but it does so by narrowing semantics to predictable ML data, explicit synchronization, pre-allocation, and a subset of file operations rather than implementing a general POSIX file system on the GPU.

## Key Characteristics
- Coexists with the host file system instead of replacing its namespace and management functions.
- Uses GVDK to embed file-specific metadata and a GPU-friendly two-level NVMe block map inside each pre-allocated file.
- Extends the NVMe driver with GPU-resident I/O queue pairs while retaining host admin and I/O queues.
- Provides host-side initialization, open, and close plus GPU-side read, write, and sync through libGemini.
- Shares a configurable GPU-memory page cache across processes and manages it at warp granularity.
- Targets predictable, mostly read-only or append-only DNN, GNN, and LLM storage workloads.

## Evidence
- Responsibility split: [[geminifs]] shows the host file system and GVDK Helper managing file construction while the GPU storage-volume layer performs cached offset translation and I/O.
- Metadata path: [[geminifs]] describes a first-block header, L1/L2 mapping tables, dirty bitmap, and reported 0.2% mapping overhead for 4 KiB blocks.
- Shared device control: [[geminifs]] registers GPU memory for DMA, creates GPU I/O queue pairs alongside host queues, and uses GPU polling for completion.
- Programming surface: [[geminifs]] documents the six init/open/close/read/write/sync calls and the removal of a host bounce buffer from device reads and writes.
- Performance: [[geminifs]] reports near-BaM uncached 4 KiB I/O, more than 640 GB/s in one cache-scaling microbenchmark, and large gains in a three-step activation-offload experiment.

## Qualifications
The evidence is one author-run FAST 2025 prototype evaluation on one host, GPU, NVMe device, file system, and selected workloads. GeminiFS depends on Nvidia peer-memory and CUDA IPC facilities, does not yet provide complete POSIX semantics or multi-GPU operation, and leaves crash consistency to explicit application synchronization. Its embedded physical mapping and direct I/O boundary therefore require careful validation under file relocation, failure, concurrent access, security, kernel, device, and deployment conditions not tested in the paper.

## What Changed
- Created the entity from the FAST 2025 paper's architecture, programming interface, measurements, and stated limitations.

## Relationships
- [[GPUCentricStorageAccess]] - implements GPU-initiated NVMe I/O while retaining a host-managed file abstraction.
- [[GPUMemoryHierarchy]] - adds an NVMe-backed tier below HBM and a GPU-resident page cache between them.
- [[HighThroughputIOOptimization]] - applies queue placement, CPU bypass, parallel request submission, caching, and prefetching to the GPU storage path.
- [[StoragePerformanceBenchmarking]] - supplies the discipline needed to distinguish raw SSD, software-stack, cache, and application results.
