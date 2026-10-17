---
title: "Pranjal Shankhdhar"
type: entity
tags: [person, gpu, cuda, performance-engineering]
sources:
  - outperforming-cublas-nvfp4
last_updated: 2026-10-18
knowledge_schema: synthesis-v1
---

## Overview
[[PranjalShankhdhar]] is a GPU performance writer and implementer represented here by a 2026 account of building a GB300 NVFP4 GEMM that reportedly exceeds cuBLASLt on a selected matrix shape.

## Current Profile
The available source presents Shankhdhar through one detailed optimization worklog. He reasons from Blackwell tensor-core shapes, TMA and TMEM capacities, compiler lowering, cache policy, tail arithmetic, reverse-engineered L2 topology, and controlled microbenchmarks, publishing the associated code in the `fast.cu` repository. The source also says Claude generated the kernels, while Shankhdhar supplies the architecture, experiments, measurements, interpretations, and public explanation; it does not expose enough process evidence to divide implementation authorship more precisely.

## Key Characteristics
- Develops GPU kernels in plain CUDA and inline PTX without a framework dependency.
- Uses dataflow diagrams and resource accounting to make warp roles, buffer ownership, and synchronization explicit.
- Optimizes through measured steps spanning compiler behavior, pipeline structure, local storage, store paths, tails, and hardware-aware scheduling.
- Treats benchmark protocol and power state as part of the result rather than one fixed neutral measurement.
- Publishes first-person performance claims with source code while acknowledging shape-specific losses and portability limits.

## Evidence
Kernel architecture and optimization:
- [[outperforming-cublas-nvfp4]] derives a two-CTA NVFP4 kernel and reports the progression from 3.271 to 7.653 PFLOP/s.

Hardware investigation:
- [[outperforming-cublas-nvfp4]] reports dependent-latency tests, physical-address mapping, observed SM-side splits, and an owned-side L2 scheduling strategy.

Evaluation and disclosure:
- [[outperforming-cublas-nvfp4]] publishes four benchmark protocols, acknowledges shapes where the kernel loses, links the code, and attributes kernel generation to Claude without a full development trace.

## Qualifications
This profile is bounded to one self-authored technical article. The benchmark, hardware-topology interpretation, code provenance, and Claude contribution are not independently reproduced in the wiki, and the source provides no broader biography, employment history, complete project record, or controlled productivity comparison.

## What Changed
- Created a bounded profile of the article's author, GPU optimization method, and evidence limits.

## Relationships
- [[FoundationModelKernelOptimization]] - broader co-design practice instantiated by the reported kernel work.
- [[Nvidia]] - supplies the GB300, CUDA, PTX, and cuBLASLt environment used in the experiment.
- [[Claude]] - credited with generating the kernel code under an undocumented collaboration process.
- [[GPUMemoryHierarchy]] - hardware substrate investigated and scheduled by the kernel.
