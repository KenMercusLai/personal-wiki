---
title: "RDMA Buffer Lifecycle Safety"
type: concept
tags: [rdma, memory, rpc, distributed-systems, correctness]
sources:
  - rdma-buffer-safe-reuse
last_updated: 2026-10-24
knowledge_schema: synthesis-v1
---

## Definition
[[RDMABufferLifecycleSafety]] is the protocol discipline that keeps registered memory contents, remote access authority, request identity, completion, timeout, and buffer reuse consistent across one-sided RDMA operations.

## Current Synthesis
RDMA completion and application ownership are different facts. After a process shares a buffer address and key, a remote RDMA Write can mutate that memory without a local application event, while a remote RDMA Read can consume contents after the owner has timed out, recycled the buffer, and written unrelated data. A buffer pool is therefore safe only when reuse is synchronized with every peer that may still exercise its access authority.

The source presents two ways to create that synchronization. A portable application protocol avoids remote writes, uses RDMA Read, and follows completion with an RPC that checks whether the original request still owns the buffer. A hardware path binds a request-scoped Type 2 Memory Window and invalidates its RKey so late reads fail. The first trades an extra RTT for weak hardware assumptions; the second shortens the normal path but depends on Memory Window support and can force QP recovery after a late access.

## Key Claims
- Local timeout does not prove that a remote NIC has stopped using an advertised buffer.
- RDMA Write requires revoking remote mutation authority before reuse; RDMA Read requires detecting whether the source contents changed before accepting them.
- Request identity can act as a generation check when the owner reports whether the original operation still holds the buffer.
- Type 2 Memory Windows can turn buffer authority into a revocable, request-scoped RKey.
- Safe recovery still needs an exceptional path when completion, validation, or invalidation cannot establish exclusive ownership.

## Evidence
- Write-versus-read hazard: [[rdma-buffer-safe-reuse]] distinguishes silent remote mutation from a remote read consuming repurposed contents.
- Application validation: [[rdma-buffer-safe-reuse]] diagrams a reverse RPC after RDMA Read that accepts the result only if the exposed buffer has not been reused.
- Revocable hardware authority: [[rdma-buffer-safe-reuse]] diagrams Bind MW, an authorized RKey, RDMA Read, and asynchronous invalidation.
- Production adaptation: [[rdma-buffer-safe-reuse]] describes 3FS checking a request `msgid` after writes and using a reverse pull service for reads.
- Recovery boundary: [[rdma-buffer-safe-reuse]] retains connection teardown when an in-flight read outlives the client's short ownership-recovery wait.

## Counterevidence & Qualifications
The proposal is a first-party design account, not a proof or comparative evaluation. The application path adds an RPC round trip and creates a correctness dependency on request-state retention, identity uniqueness, ordering, and failure handling. The Memory Window path is hardware-dependent, and a late access after invalidation can fail the QP. Avoiding RDMA Write also changes dataflow and may not suit every workload. The source reports no implementation measurements, failure-injection matrix, reconnect rate, throughput, tail latency, or formal model.

## What Changed
- Established buffer reuse as a distributed ownership and authority problem rather than a local pool operation.
- Distinguished portable post-read validation from hardware RKey revocation and preserved both recovery costs.
- Added the production 3FS write-check and reverse-pull adaptations.

## Related Concepts
- [[ReceiverDrivenFlowControl]] - receiver-issued reads couple safe ownership with application-controlled traffic admission.
- [[AdaptiveBackpressure]] - supplies the wider principle of propagating local capacity and completion state upstream.
- [[HighThroughputIOOptimization]] - registered buffers improve data-path efficiency but create lifecycle obligations that performance tuning must preserve.
- [[SystemReliability]] - requires explicit timeout, failure, and recovery semantics around the fast path.
