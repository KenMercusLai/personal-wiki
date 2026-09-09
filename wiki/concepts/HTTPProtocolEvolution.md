---
title: "HTTP Protocol Evolution"
type: concept
tags: [http, networking, protocol-history]
sources:
  - chen-hao-http-de-qian-shi-jin-sheng
last_updated: 2026-09-09
knowledge_schema: synthesis-v1
---

## Definition

HTTP protocol evolution is the progression of the Web's application protocol from a minimal document request mechanism toward a versioned, metadata-rich, multiplexed system whose performance depends on its interaction with the transport layer.

## Current Synthesis

The current source presents HTTP's history as repeated removal of bottlenecks. HTTP/1.0 added versioning, headers, status codes, and content typing but commonly paid connection setup per resource. HTTP/1.1 added persistent connections and broader control semantics, yet pipelining retained ordering constraints. HTTP/2 introduced binary framing, multiplexed streams, HPACK, and server push on one TCP connection, improving concurrency while exposing all streams to TCP-level head-of-line blocking after packet loss. HTTP/3 shifts that multiplexing onto [[QUIC]], where loss recovery is stream-aware and connection identity can survive a network-path change.

## Key Claims

- Versioning, headers, status codes, and content types gave HTTP explicit control and metadata boundaries.
- Persistent connections reduce repeated transport setup, but HTTP/1.1 pipelining does not eliminate response-order blocking.
- HTTP/2 separates messages into binary frames and multiplexes streams over one TCP connection.
- TCP loss recovery can stall every HTTP/2 stream sharing the affected connection.
- HTTP/3 uses [[QUIC]] to move stream multiplexing, reliability, encryption, and connection management into a UDP-based transport.
- Each performance gain introduces new implementation or deployment complexity.

## Evidence

### Engineering structure and connection reuse

- [[chen-hao-http-de-qian-shi-jin-sheng]] traces version markers, headers, status codes, content negotiation, `Host`, caching, persistent connections, and pipelining across HTTP/1.0 and HTTP/1.1.

### Multiplexing and transport interaction

- [[chen-hao-http-de-qian-shi-jin-sheng]] contrasts HTTP/2 binary framing and concurrent streams with HTTP/1.1 request ordering, then explains why TCP packet loss can stall all multiplexed streams.

### HTTP/3 deployment tradeoffs

- [[chen-hao-http-de-qian-shi-jin-sheng]] links HTTP/3 to QUIC and identifies connection IDs, middlebox behavior, load balancing, congestion control, and QPACK as parts of the deployment problem.

## Counterevidence & Qualifications

- The article is a 2019 technical overview, so its adoption percentages and implementation-support claims are historical snapshots.
- It sometimes compresses distinct mechanisms: chunked transfer encoding is not itself generic server push, and HTTP/2 server push is a separate feature.
- Its TCP-plus-TLS handshake count is illustrative rather than universal because TLS version, resumption, and transport setup affect round trips.
- HTTP/3's maturation and any claim that QUIC threatens to replace TCP require evidence beyond this source.
- The source argues for standards adoption on architectural grounds but provides no comparative organizational outcomes.

## What Changed

- Established the wiki's first version-by-version synthesis of HTTP.
- Identified head-of-line blocking at both HTTP/1.1 pipeline and HTTP/2 transport layers.
- Connected HTTP/3 performance goals to QUIC's stream-aware transport and deployment constraints.

## Related Concepts

- [[QUIC]] - provides the transport and security substrate used by HTTP/3.
