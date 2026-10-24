---
title: "Receiver-Driven Flow Control"
type: concept
tags: [rdma, networking, congestion-control, flow-control, distributed-systems]
sources:
  - rdma-buffer-safe-reuse
last_updated: 2026-10-24
knowledge_schema: synthesis-v1
---

## Definition
[[ReceiverDrivenFlowControl]] is an application-level transfer policy in which the data receiver decides when to pull data, letting its buffer ownership and processing capacity govern admission into the network.

## Current Synthesis
In the source's RDMA setting, replacing sender-initiated RDMA Write with receiver-initiated RDMA Read solves more than one problem. The receiver controls when each transfer begins, so it can coordinate registered-buffer ownership and limit concurrent traffic before congestion appears in the fabric. RPC carries the request, authority, validation, and error semantics that one-sided data movement does not supply by itself.

This is complementary to network congestion control rather than a general replacement for it. The application sees request identity, available buffers, processing state, and acceptable concurrency, while the network sees queues and transport signals. The source reports that receiver-driven control helped workloads where network mechanisms alone did not prevent congestion, but provides no measurements that isolate the contribution.

## Key Claims
- Pull-based RDMA gives the receiver an explicit admission point for each large transfer.
- The same control point can coordinate buffer lifetime and limit transfer concurrency.
- Two-sided RPC can carry application state and recovery semantics around one-sided payload movement.
- Application control complements rather than proves the inadequacy of all network-layer congestion control.

## Evidence
- Direction choice: [[rdma-buffer-safe-reuse]] rejects remote RDMA Write and makes the destination issue RDMA Read.
- Ownership coupling: [[rdma-buffer-safe-reuse]] checks request or buffer validity after the read before accepting the result.
- Production flow: [[rdma-buffer-safe-reuse]] diagrams a 3FS reverse pull RPC whose client-side handler issues and acknowledges RDMA Read.
- Operational observation: [[rdma-buffer-safe-reuse]] reports congestion in 3FS and KV-cache storage that the author says network-layer algorithms alone did not avoid.

## Counterevidence & Qualifications
The congestion claim lacks workload traces, topology, queue telemetry, transport settings, controlled alternatives, fairness analysis, or quantitative improvement. Pull control can add RPCs, scheduling work, and latency, and poor receiver policy can underutilize the network or shift queues elsewhere. Some workloads may require push semantics or benefit from hardware and transport controls unavailable to the described environment.

## What Changed
- Established receiver-issued RDMA Read as a joint lifecycle and traffic-admission mechanism.
- Kept application and network congestion control as complementary layers rather than universal substitutes.

## Related Concepts
- [[RDMABufferLifecycleSafety]] - supplies the ownership constraint that the receiver must preserve while admitting reads.
- [[AdaptiveBackpressure]] - generalizes the use of local capacity feedback to delay, redirect, or reject upstream work.
- [[HighThroughputIOOptimization]] - evaluates receiver control alongside buffer registration, CPU, storage, and NIC throughput.
- [[DataCenterNetworkFabric]] - supplies the shared network whose path diversity does not by itself guarantee congestion-free operation.
