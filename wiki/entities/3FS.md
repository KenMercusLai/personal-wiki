---
title: "3FS"
type: entity
tags: [deepseek, distributed-filesystem, rdma, storage]
sources:
  - rdma-buffer-safe-reuse
last_updated: 2026-10-24
knowledge_schema: synthesis-v1
---

## Overview
[[3FS]] is a distributed file system used in the source as the production setting for RDMA chunk reads, chunk writes, registered-buffer pooling, and timeout recovery.

## Current Profile
The original 3FS contract made the server initiate every one-sided transfer: chunk reads used server-to-client RDMA Write and chunk writes used server-side RDMA Read from client memory. A client timeout closed the RDMA connection so no later remote operation could silently touch or consume a recycled client buffer.

The reported rollout preserves buffer safety while avoiding routine disconnects. Writes add a client request-status query that the server calls after RDMA Read. Reads replace server push with a reverse pull RPC that makes the client issue RDMA Read; only a read still in flight beyond a short grace period retains forced connection teardown as the last recovery mechanism.

## Key Characteristics
- Uses registered buffers and one-sided RDMA for chunk data movement.
- Previously coupled request timeout to connection closure as the buffer-revocation mechanism.
- Validates write-buffer ownership by querying whether the original `msgid` remains pending.
- Converts the read path from server RDMA Write to a client-side pull service and RDMA Read.
- Deploys the new write behavior behind a client feature flag after server rollout.

## Evidence
- Original contract: [[rdma-buffer-safe-reuse]] says the server initiated both chunk-read writes and chunk-write reads, while client timeout closed the connection.
- Write migration: [[rdma-buffer-safe-reuse]] diagrams RDMA Read followed by a reverse `msgid` query and conditional success.
- Read migration: [[rdma-buffer-safe-reuse]] diagrams a reverse pull RPC, transfer ID, RDMA Read, ACK, and timeout/error branches.
- Residual recovery: [[rdma-buffer-safe-reuse]] says the client briefly waits for an in-flight read after timeout and closes the connection if ownership still cannot be recovered.

## Qualifications
This profile comes from one contributor's design account. It does not document cluster scale, released code for the full change, rollout dates, quantitative effects, failure rates, or independent verification. The article describes one deployment strategy rather than the whole 3FS architecture, and the claim that receiver-driven control prevents observed congestion is not accompanied by measurements.

## What Changed
- Established 3FS as a canonical entity through its RDMA buffer-lifecycle design.
- Recorded the shift from timeout-triggered teardown toward request validation and receiver-driven pull.

## Relationships
- [[RDMABufferLifecycleSafety]] - 3FS is the production case for explicit post-read ownership validation.
- [[ReceiverDrivenFlowControl]] - the revised chunk-read path lets the client pull server data.
- [[HighThroughputIOOptimization]] - 3FS uses registered RDMA buffers in a performance-sensitive storage path.
