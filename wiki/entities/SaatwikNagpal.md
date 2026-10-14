---
title: "Saatwik Nagpal"
type: entity
tags: [ai, inference, performance]
sources:
  - modal-multimodal-dictionary
last_updated: 2026-10-14
knowledge_schema: synthesis-v1
---

## Overview
[[SaatwikNagpal]] is a co-author of a [[Modal]] engineering account about removing host-side overhead from [[SGLang]] multimodal inference.

## Current Profile
The source associates Nagpal with profiling SGLang's scheduler, identifying repeated CUDA IPC shared-storage reconstruction, implementing or explaining a pool-handle cache, and measuring its end-to-end effect on a Qwen2.5-VL-3B-Instruct workload.

## Key Characteristics
- Works on multimodal inference performance in the reported account.
- Uses sampling profiles to connect host-side work to GPU dispatch stalls.
- Reports an upstreamed SGLang optimization with workload-level measurements.

## Evidence
- Authorship: [[modal-multimodal-dictionary]] names Saatwik Nagpal as a co-author.
- Engineering scope: [[modal-multimodal-dictionary]] presents scheduler profiling, CUDA IPC cache design, and before-and-after benchmark results.

## Qualifications
The source provides no broader biography, precise individual contribution breakdown, independent evaluation, or evidence about work beyond this optimization. Claims are therefore limited to authorship and the technical account presented.

## What Changed
- Created the entity page from the co-authored SGLang performance account.

## Relationships
- [[CharlesFrye]] - co-authored the reported multimodal inference optimization.
- [[Modal]] - published the engineering account.
- [[SGLang]] - inference engine optimized in the account.
- [[InferenceHostOverhead]] - performance problem analyzed in the account.
