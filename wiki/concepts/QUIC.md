---
title: "QUIC"
type: concept
tags: [quic, http3, networking, transport]
sources:
  - chen-hao-http-de-qian-shi-jin-sheng
last_updated: 2026-09-09
knowledge_schema: synthesis-v1
---

## Definition

QUIC is a secure, reliable, multiplexed transport built over UDP and used as the transport substrate for HTTP/3.

## Current Synthesis

The current source frames QUIC as a response to HTTP/2's dependence on TCP's single ordered byte stream. QUIC implements loss recovery and congestion control above UDP, integrates cryptographic setup, and exposes independent streams so loss affecting one stream need not block unrelated streams. Connection IDs decouple a logical connection from one network four-tuple, enabling connection migration, but network devices and load balancers that understand only conventional TCP/UDP flow keys can complicate deployment. [[HTTPProtocolEvolution]] supplies the application-protocol context for these choices.

## Key Claims

- Independent QUIC streams limit cross-stream head-of-line blocking caused by transport loss.
- QUIC supplies reliability and congestion control rather than inheriting them from UDP.
- Integrated secure setup can reduce connection-establishment latency relative to separate TCP and TLS setup.
- Connection IDs allow a connection to persist across some address or network changes.
- UDP-unfriendly middleboxes and four-tuple-based load balancers can impede deployment.
- HTTP/3 requires QPACK rather than directly reusing HTTP/2's order-dependent HPACK design.

## Evidence

### Stream independence and connection setup

- [[chen-hao-http-de-qian-shi-jin-sheng]] describes QUIC's own retransmission and congestion control, its integration with cryptographic setup, and its avoidance of connection-wide blocking between independent HTTP streams.

### Connection identity and infrastructure

- [[chen-hao-http-de-qian-shi-jin-sheng]] explains connection IDs through mobile-to-Wi-Fi migration and notes that four-tuple-based routing can send packets from one logical connection to different servers.

### Header compression

- [[chen-hao-http-de-qian-shi-jin-sheng]] presents QPACK as a redesign needed because HPACK's shared dynamic state assumes the ordering properties available over TCP.

## Counterevidence & Qualifications

- UDP itself does not remove head-of-line blocking; QUIC avoids connection-wide blocking through its stream and recovery design.
- NAT devices can and commonly do map UDP flows using tuples and timers, so the source's categorical NAT contrast is simplified.
- Faster setup depends on protocol version, prior connection state, address validation, and resumption conditions.
- The source predates mature HTTP/3 deployment and offers no measurements of loss recovery, migration success, or middlebox failure rates.
- Whether QUIC will displace TCP outside its current uses remains speculative in this corpus.

## What Changed

- Established QUIC as the wiki's first UDP-based reliable transport concept.
- Distinguished stream-aware loss recovery from UDP's native behavior.
- Added connection migration, middlebox compatibility, and QPACK synchronization as deployment considerations.

## Related Concepts

- [[HTTPProtocolEvolution]] - explains why HTTP/3 adopted QUIC after HTTP/2's TCP-level blocking limits.
