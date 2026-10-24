---
title: "Huawei"
type: entity
tags: [networking, vendor, infrastructure]
sources:
  - ansible-charges-into-network-automation-with-cisco-juniper-the-register
  - ds4-ascend
last_updated: 2026-10-24
knowledge_schema: synthesis-v1
---

## Overview
[[Huawei]] appears in the sources as both a networking vendor absent from [[Ansible]]'s initial automation launch list and the supplier of the Ascend accelerator platform used for a model-inference port.

## Current Profile
The 2016 networking article uses Huawei only as a contrast: Ansible supported several competitors at launch but not Huawei. The newer implementation report concerns a different product domain. It describes an Atlas 300i Duo card based on the Ascend 310P family, exposed through CANN and AscendCL as two independent 48 GB devices, and records the consequences of porting a CUDA/Metal-oriented low-bit inference engine without a native IQ2_XXS kernel.

## Key Characteristics
- Was absent from Ansible's named initial network-automation targets.
- Supplies the Ascend accelerator hardware and CANN software stack used in a model-inference port.
- Exposes the Atlas 300i Duo's two physical dies as independent devices in the reported configuration.
- Provides dense GEMM support, while the port still requires custom normalization, positional, softmax, and low-bit paths.
- Is represented through source-scoped product behavior rather than a comprehensive company profile.

## Evidence
- Absence from support list: [[ansible-charges-into-network-automation-with-cisco-juniper-the-register]] says Huawei was notable by its absence.
- Launch list contrast: [[ansible-charges-into-network-automation-with-cisco-juniper-the-register]] lists Arista, Cisco, Juniper, Cumulus Networks, and OpenSwitch as supported.
- Accelerator programming: [[ds4-ascend]] uses CANN, AscendCL, and Ascend C as the platform layers for an Atlas 300i Duo port.
- Capacity and topology: [[ds4-ascend]] reports two independently enumerated 48 GB devices and uses only device 0 in the current implementation.
- Kernel boundary: [[ds4-ascend]] uses `aclblasGemmEx` for dense work but lacks a native IQ2_XXS path, causing CPU expansion and repeated transfers.

## Qualifications
The networking source does not explain why Huawei was absent or whether support arrived later. The inference source is one unfinished, self-reported port without an optimized baseline, profiler output, version matrix, independent reproduction, or evidence about other Ascend models and frameworks. Its 0.1–0.3 token/s result should not be generalized to the platform.

## What Changed
- Expanded the profile from a networking-support absence to a concrete Ascend hardware and programming-stack case.
- Preserved the port's implementation-specific performance boundary rather than treating it as a platform benchmark.

## Relationships
- [[Ansible]] - Huawei is absent from Ansible's named launch support.
- [[NetworkAutomation]] - Huawei's absence qualifies the multivendor automation claim.
- [[AcceleratorBackendPorting]] - the Ascend case exposes the difference between functional and performance portability.
- [[DwarfStar]] - inference engine ported to Huawei's accelerator stack.
