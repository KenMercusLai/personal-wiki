---
title: "HTTP/3"
type: concept
tags: [networking, protocol, web, quic]
sources:
  - chen-hao-http-de-qian-shi-jin-sheng
  - robin-marx-head-of-line-blocking-in-quic-and-http-3-the-details
last_updated: 2026-10-02
knowledge_schema: synthesis-v1
---

## Definition
[[HTTP3]] is the HTTP version that maps HTTP semantics onto [[QUIC]] streams over UDP rather than multiplexing HTTP streams inside TCP's single ordered byte stream.

## Current Synthesis
HTTP/3 changes the transport foundation beneath the HTTP/2-style application model. QUIC integrates TLS and reliable stream transport above UDP, moves stream identity into transport, and tracks byte ranges separately for each stream. A lost packet therefore blocks only streams that have a byte gap instead of withholding later data from every HTTP stream on the connection.

That is a narrower claim than eliminating [[HeadOfLineBlocking]]. Ordering remains inside each QUIC stream, and connection-wide congestion control still couples all streams. Page-load benefit requires multiple active streams, a scheduling pattern that leaves useful data unblocked, and resources that benefit from interleaving; sequential delivery can complete critical JavaScript, CSS, or fonts sooner. The loss of total cross-stream ordering also required QPACK and a simpler priority design because HTTP/2's HPACK and priority operations relied on deterministic delivery order.

Deployment adds a separate constraint. QUIC connection IDs can preserve identity across network changes, but NATs, load balancers, and other devices that understand UDP four-tuples rather than QUIC semantics can interfere with routing.

## Key Claims
- HTTP/3 uses QUIC streams over UDP to avoid TCP's cross-stream ordered-byte constraint.
- QUIC stream identity replaces HTTP/2's separate application-level stream layer.
- Packet loss blocks only streams with missing byte ranges, while unaffected streams can continue.
- Intra-stream ordering, connection-wide congestion control, and some cross-stream dependencies remain.
- QPACK and simplified prioritization replace HTTP/2 mechanisms that assumed total cross-stream delivery order.
- Practical performance depends on scheduling, loss placement, resource type, and concurrency rather than protocol version alone.
- Connection-ID semantics improve mobility but create deployment work for four-tuple-oriented infrastructure.

## Evidence
- Transport change and identity: [[chen-hao-http-de-qian-shi-jin-sheng]] describes QUIC over UDP and connection IDs; [[robin-marx-head-of-line-blocking-in-quic-and-http-3-the-details]] shows stream identity moving into QUIC STREAM frames.
- Loss boundary: [[robin-marx-head-of-line-blocking-in-quic-and-http-3-the-details]] shows per-stream byte tracking and immediate delivery for a stream without a gap after packet loss.
- Remaining coupling: [[robin-marx-head-of-line-blocking-in-quic-and-http-3-the-details]] explains intra-stream blocking, connection-wide congestion control, and the scheduler-dependent effect of burst loss.
- HTTP mechanism redesign: [[chen-hao-http-de-qian-shi-jin-sheng]] and [[robin-marx-head-of-line-blocking-in-quic-and-http-3-the-details]] explain QPACK's response to reordered stream delivery; the latter also notes the removal of HTTP/2's priority-tree mechanism.
- Infrastructure friction: [[chen-hao-http-de-qian-shi-jin-sheng]] gives NAT and load-balancer examples that do not understand QUIC identity.

## Counterevidence & Qualifications
Neither source provides a controlled, current browser benchmark. Marx's 2020 argument is explicitly skeptical that cross-stream blocking removal alone materially improves most page loads, because loss is often rare and aggressive multiplexing can delay critical resource completion. Chen Hao's 2019 adoption and infrastructure discussion is historical. Current deployment support and implementation behavior require current evidence.

## What Changed
- Narrowed “solves head-of-line blocking” to removing TCP-style cross-stream ordering while preserving intra-stream blocking.
- Added scheduling, resource-completion, burst-loss, and shared congestion-control qualifications.
- Explained why cross-stream reordering required QPACK and a changed priority model.

## Related Concepts
- [[HTTP]] - HTTP/3 is part of HTTP's protocol lineage.
- [[HTTP2]] - HTTP/3 retains framed HTTP semantics but changes stream ownership and transport.
- [[QUIC]] - QUIC provides HTTP/3's stream-aware reliable transport.
- [[HeadOfLineBlocking]] - HTTP/3 narrows blocking to affected dependencies and streams rather than eliminating it.
- [[HTTP11]] - HTTP/1.1's response serialization is an earlier, application-layer form of the problem.
