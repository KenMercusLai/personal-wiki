---
title: "Loro"
type: entity
tags: [crdt, local-first, collaboration, synchronization]
sources:
  - sui-shi-sui-di-zhi-hui-ni-de-agent-tuan-dui-leon7hao
last_updated: 2026-10-15
knowledge_schema: synthesis-v1
---

## Overview
[[Loro]] is a high-performance CRDT framework for multi-device synchronization and collaborative editing under concurrent or offline operation.

## Current Profile
The source presents Loro as a business-independent merge layer that converges replicas once they receive the same operation set. It favors eventual over strong consistency, keeps user-device data primary, and combines synchronization with version history and claimed end-to-end encryption. Lody uses it as the data layer for current cross-device state and a planned versioned workspace-context system.

## Key Characteristics
- Merges concurrent or offline edits through CRDT operations without a central OT authority.
- Guarantees convergence from identical operation sets rather than intent-correct conflict resolution.
- Supports local-first storage in which the user's device holds the primary copy.
- Presents version history, business-independent synchronization, and end-to-end encryption as framework capabilities.
- Underlies [[Lody]]'s synchronized sessions and proposed structured context history.

## Evidence
- Convergence model: [[sui-shi-sui-di-zhi-hui-ni-de-agent-tuan-dui-leon7hao]] distinguishes eventual convergence from the possibility that an automatic merge violates real human intent.
- Local-first topology: [[sui-shi-sui-di-zhi-hui-ni-de-agent-tuan-dui-leon7hao]] includes an inspected diagram contrasting isolated local-only data and cloud-centralized clients with user-owned data synchronized across devices.
- Product use: [[sui-shi-sui-di-zhi-hui-ni-de-agent-tuan-dui-leon7hao]] says Lody builds multi-device, offline-first, collaborative synchronization and its context roadmap on Loro.

## Qualifications
This profile comes from a co-founder's product talk, not a protocol paper, audit, or comparative CRDT benchmark. It does not specify supported data types, conflict semantics, scaling limits, encryption and key management, recovery behavior, metadata leakage, or how local-first ownership interacts with any synchronization service.

## What Changed
- Established Loro's role as both a general CRDT framework and Lody's synchronization foundation.
- Made convergence-versus-intent correctness an explicit boundary.

## Relationships
- [[Lody]] - uses Loro for current synchronization and the planned versioned context layer.
- [[LeonZhao]] - co-founder presenting the framework's role and design principles.
- [[LocalFirstSoftware]] - Loro operationalizes local ownership with multi-device and collaborative synchronization.
- [[DistributedConsensus]] - CRDT convergence addresses replicated-state coordination under concurrent operations.
