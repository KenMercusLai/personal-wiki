---
title: "Refiner-Bench"
type: entity
tags: [benchmark, video-generation, video-refinement, evaluation]
sources:
  - 2609.37969
last_updated: 2026-10-13
knowledge_schema: synthesis-v1
---

## Overview
[[RefinerBench]] is a 150-video benchmark introduced with [[SoLRefiner]] to compare generated-video refiners on aligned shared inputs from multiple base generators.

## Current Profile
The benchmark contains 50 outputs each from WAN 2.1 1.3B, SANA-Video 2B, and LTX-2 Stage 1. Its labels span 12 content groups, three motion levels, and six camera-motion types. The main comparison resizes aligned inputs to 1024×576, evaluates most outputs at 2048×1152, and reports VBench and UniPercept components and averages.

## Key Characteristics
- Separates refiner comparison from the upstream generator by sharing aligned inputs.
- Mixes two out-of-distribution generators with the in-distribution LTX-2 source.
- Covers people, animals, scenes, objects, stylized content, three motion levels, and six camera motions.
- Uses VBench for consistency, motion, dynamism, aesthetics, and imaging quality.
- Uses UniPercept for aesthetics, image quality, structure, and texture on eight sampled frames.
- Contains generated videos rather than camera-captured degradation or general editing tasks.

## Evidence
Composition:
- [[2609.37969]] documents 50 videos from each of three generators, 12 content groups, 50/64/36 low/medium/high-motion clips, and camera-motion counts.

Protocol:
- [[2609.37969]] specifies generator-dependent alignment, one shared main input size, output resolutions, competing refiners, and reported metric components.

## Qualifications
The benchmark and evaluated model share authors, and no independent replication is supplied. LingBot outputs use 1920×1088 while other main outputs use 2048×1152. Automated frame and video metrics do not fully measure human preference or long-range temporal consistency, and 150 generated clips cannot establish behavior on broader degradation and editing distributions.

## What Changed
- Created the benchmark profile and recorded its composition, comparison protocol, and external-validity limits.

## Relationships
- [[SoLRefiner]] - model introduced and evaluated on the benchmark.
- [[VideoRefinement]] - task isolated by its shared-input protocol.
- [[DiffusionModelSampling]] - inference family whose refiner step counts are compared.
- [[Nvidia]] - organization behind the benchmark and paper.
