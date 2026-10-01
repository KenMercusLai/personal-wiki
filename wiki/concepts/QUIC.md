---
title: "QUIC"
type: concept
tags: [networking, protocol, transport, udp]
sources:
  - chen-hao-http-de-qian-shi-jin-sheng
  - how-nat-traversal-works
  - robin-marx-head-of-line-blocking-in-quic-and-http-3-the-details
last_updated: 2026-10-02
knowledge_schema: synthesis-v1
---

## Definition
[[QUIC]] is a UDP-based secure transport protocol that provides reliable independent streams, integrated TLS, congestion control, and connection identity for applications including [[HTTP3]].

## Current Synthesis
QUIC retains UDP's deployable datagram substrate while rebuilding reliable stream transport above it. For HTTP/3, STREAM frames carry stream IDs and byte ranges so loss creates a gap only inside affected streams rather than in one connection-wide TCP byte sequence. For peer-to-peer applications, the same UDP substrate lets traversal logic share and control the socket while the application receives stream semantics.

Independence is bounded. QUIC preserves ordering inside each stream, uses a single connection-wide congestion controller, and implementations often place one stream's data in a packet; burst loss can therefore block one or many streams depending on the scheduler. Per-packet encryption avoids TLS-record blocking but costs CPU. QUIC's connection IDs also support continuity across network changes while challenging NATs and load balancers built around IP-and-port tuples.

## Key Claims
- QUIC is the secure transport foundation that lets [[HTTP3]] run reliable streams over UDP.
- STREAM frames track byte ranges per stream, avoiding TCP-style cross-stream delivery blocking.
- Ordering and [[HeadOfLineBlocking]] remain within each stream, while congestion control remains shared across the connection.
- Scheduling and loss placement determine how many streams a packet-loss burst blocks.
- Integrated TLS and per-packet encryption change setup, recovery, and CPU tradeoffs relative to TCP plus TLS records.
- Connection IDs support continuity across address changes but require infrastructure that can route QUIC correctly.
- QUIC can provide streams while preserving the shared UDP socket needed for [[NATTraversal]].

## Evidence
- Stream-aware recovery: [[robin-marx-head-of-line-blocking-in-quic-and-http-3-the-details]] shows QUIC delivering an unaffected stream immediately while retaining data after a gap in another stream.
- Shared limits and encryption: [[robin-marx-head-of-line-blocking-in-quic-and-http-3-the-details]] describes intra-stream ordering, one congestion controller, scheduler-dependent loss, and per-packet encryption cost.
- HTTP/3, handshake, and connection identity: [[chen-hao-http-de-qian-shi-jin-sheng]] describes QUIC's HTTP role, integrated setup, congestion control, and network-change continuity.
- Infrastructure constraints: [[chen-hao-http-de-qian-shi-jin-sheng]] explains four-tuple NAT and load-balancer mismatches.
- Traversal fit: [[how-nat-traversal-works]] recommends QUIC when an application wants reliable streams while traversal logic controls the same UDP socket.

## Counterevidence & Qualifications
The sources are mechanism explanations rather than comparative production measurements. QUIC removes connection-wide delivery ordering across independent streams, not every form of blocking or coupling. UDP does not guarantee reachability: networks may block it, endpoint-dependent NAT may defeat learned mappings, and relays may still be required. Per-packet cryptography and user-space implementation can add CPU cost, while routing devices that ignore connection IDs can mishandle paths. Implementation and deployment claims from 2019-2020 are historical snapshots.

## What Changed
- Reframed QUIC's benefit as per-stream loss recovery rather than elimination of all head-of-line blocking.
- Added intra-stream ordering, connection-wide congestion control, scheduling, and encryption-cost boundaries.
- Connected packet-level stream identity to HTTP/3's removal of a duplicate HTTP stream layer.

## Related Concepts
- [[HTTP3]] - HTTP/3 maps HTTP semantics onto QUIC streams.
- [[HTTP2]] - QUIC removes the single TCP byte-stream constraint beneath HTTP/2-style multiplexing.
- [[HeadOfLineBlocking]] - QUIC narrows transport blocking to streams with missing byte ranges.
- [[HTTP]] - QUIC changes the transport foundation beneath the HTTP family.
- [[NATTraversal]] - QUIC preserves a UDP socket substrate that traversal logic can probe and map.
