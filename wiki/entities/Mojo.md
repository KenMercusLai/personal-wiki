---
title: "Mojo"
type: entity
tags: [programming-language, gpu, simd, portability]
sources:
  - scaling-elections
last_updated: 2026-10-18
knowledge_schema: synthesis-v1
---

## Overview
[[Mojo]] is represented here as a systems programming language used to implement one blocked strongest-path algorithm across CPUs and Nvidia and AMD GPUs.

## Current Profile
In [[scaling-elections]], Ash Vardanian reports that an AI-assisted Mojo port of his Numba and CUDA implementations compiled into a usable starting point, then ran the same GPU source on Nvidia and AMD hardware. The language exposes explicit device contexts, buffers, kernel dimensions, address spaces, stack allocation, move syntax, compile-time parameters, and architecture-independent SIMD. This is one practitioner experiment, not a general proof of performance portability or ecosystem maturity.

## Key Characteristics
- Targets CPU and GPU execution from one language and source base.
- Exposes GPU orchestration, memory, launch geometry, and synchronization through typed APIs.
- Provides width-parameterized SIMD used by the author across AVX-512-class CPU execution.
- Uses LLVM-style address spaces and explicit stack allocation for low-level memory control.
- Was amenable to a language-model-generated initial port, but still required expert review and optimization.

## Evidence
Cross-vendor execution:
- [[scaling-elections]] says the Nvidia-oriented Mojo source ran on AMD MI300 and MI355X without modification, while the comparable CUDA-to-HIP adaptation required more than 200 changed lines.

Measured execution:
- [[scaling-elections]] reports near-CUDA H100 throughput at several sizes, higher results on the tested AMD accelerators, and a sizable SIMD improvement on the tested 384-core Intel machine.

Programming model:
- [[scaling-elections]] shows typed device buffers and kernel enqueue operations, explicit synchronization, parameterized SIMD loads and stores, address spaces, stack allocation, and move syntax.

## Qualifications
The evidence comes from one author, one algorithm, a hackathon-derived codebase, and heterogeneous machines. Hardware generations, tuning effort, compiler versions, power, cost, memory limits, and numerical validation are not controlled as a language comparison. The author also reports difficulty feature-gating GPU code from CPU-only builds and calls for better packaging and distribution, indicating an immature cross-compilation and deployment surface.

## What Changed
- Created a source-scoped profile of Mojo's CPU, GPU, orchestration, and SIMD roles.
- Added the reported zero-change Nvidia-to-AMD port and its CUDA/HIP comparison.
- Preserved compiler-maturity, packaging, benchmark-control, and optimization-effort limits.

## Relationships
- [[SchulzeMethod]] - benchmark algorithm implemented in Mojo.
- [[ParallelProgramming]] - execution model exposed through tiled GPU kernels and CPU SIMD.
- [[Nvidia]] - H100 platform used for the Mojo comparison.
- [[LLVM]] - address-space model cited as a design influence.
