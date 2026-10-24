---
title: "Donge"
type: entity
tags: [software-engineer, ai-inference, ascend]
sources:
  - ds4-ascend
last_updated: 2026-10-24
knowledge_schema: synthesis-v1
---

## Overview
[[Donge]] is the practitioner-author of an Ascend port of [[DwarfStar]], used as a learning exercise in model-specific inference and accelerator optimization.

## Current Profile
The source presents Donge as a systems-optimization practitioner who reimplemented DwarfStar's backend interface with AscendCL for an Atlas 300i Duo. The work reaches CPU-aligned output but not practical speed, and the author identifies native IQ2_XXS dequantization, two-die weight placement, and batched prefill attention as unfinished work.

## Key Characteristics
- Approaches the port as a way to understand an inference stack rather than as a finished product claim.
- Works across model execution, quantized representation, explicit host-device memory movement, and accelerator kernels.
- Reports the slow result directly and separates functional alignment from performance readiness.

## Evidence
- Port scope: [[ds4-ascend]] describes adding an AscendCL backend implementing DwarfStar's existing GPU interface.
- Validation boundary: [[ds4-ascend]] reports CPU-path output alignment while supplying no detailed test protocol.
- Performance diagnosis: [[ds4-ascend]] attributes the reported 0.1–0.3 token/s primarily to CPU dequantization, repeated transfers, and use of only one 48 GB device.

## Qualifications
The profile rests on one self-authored project account. It does not establish Donge's broader employment, project history, independent benchmark results, or completion of the proposed kernels and dual-device work.

## What Changed
- Created the profile from the DwarfStar Ascend-port report.

## Relationships
- [[DwarfStar]] - inference engine Donge ported to Ascend.
- [[Huawei]] - vendor of the accelerator and programming stack used in the port.
- [[AcceleratorBackendPorting]] - engineering practice illustrated by the project.
