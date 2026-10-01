---
title: "HTTP/2"
type: concept
tags: [networking, protocol, web]
sources:
  - chen-hao-http-de-qian-shi-jin-sheng
  - building-a-shop-with-sub-second-page-loads-lessons-learned
  - nick-craver-https-on-stack-overflow-the-end-of-a-long-road
  - robin-marx-head-of-line-blocking-in-quic-and-http-3-the-details
last_updated: 2026-10-02
knowledge_schema: synthesis-v1
---

## Definition
[[HTTP2]] is the HTTP version that uses binary frames, stream identifiers, header compression, and scheduling to multiplex resource transfers over one TCP connection.

## Current Synthesis
HTTP/2 responds to [[HTTP11]]'s response serialization by placing HEADERS or DATA frames with stream identity and length before resource chunks. Those frames let a receiver separate interleaved resources and let a sender schedule bandwidth across streams. HPACK reduces repeated headers, and server push was designed to send dependencies before separate client requests.

This application-layer concurrency does not remove transport-layer [[HeadOfLineBlocking]]. TCP sees one opaque, ordered byte stream: if a packet is lost, later bytes remain buffered even when their HTTP/2 frames belong to an unaffected stream. The practical penalty is conditional. Loss is often rare, and HTTP/2 is generally competitive through lower connection overhead, but several HTTP/1.1 or HTTP/2 connections can isolate some loss and congestion effects that a single connection concentrates.

For webshop performance, protocol efficiency is only one lever. Caching and CDNs can matter more because avoiding a round trip beats optimizing it. HTTPS was also the practical browser deployment gate for HTTP/2 in Stack Overflow's 2017 case, where shared edge IPs and certificate coverage enabled cross-origin connection reuse while preserving HTTP/1.1 sharding.

## Key Claims
- HTTP/2 standardized ideas developed through Google's SPDY work.
- Binary HEADERS and DATA frames identify streams and chunk lengths, enabling multiplexing over one TCP connection.
- HPACK reduces repeated header overhead, while stream scheduling distributes shared connection bandwidth.
- HTTP/2 still inherits TCP-level [[HeadOfLineBlocking]] because TCP cannot deliver later bytes across a loss gap.
- A single connection reduces setup overhead but concentrates congestion response and packet-loss impact; parallel connections trade more overhead for partial isolation.
- HTTP/2 can reduce page-load overhead, especially with caching and CDN delivery, but protocol features do not replace those systems.
- HTTPS, certificate coverage, origin co-location, and browser behavior shaped practical deployment and cross-origin reuse.

## Evidence
- Framing and multiplexing: [[chen-hao-http-de-qian-shi-jin-sheng]] describes binary framing and concurrent streams; [[robin-marx-head-of-line-blocking-in-quic-and-http-3-the-details]] shows stream IDs and lengths separating interleaved resource chunks.
- TCP mismatch and loss: [[chen-hao-http-de-qian-shi-jin-sheng]] and [[robin-marx-head-of-line-blocking-in-quic-and-http-3-the-details]] explain that HTTP/2 sees independent streams while TCP tracks one byte sequence; the latter's inspected diagram makes the mapping explicit.
- Performance context: [[building-a-shop-with-sub-second-page-loads-lessons-learned]] recommends HTTP/2 among several network optimizations, while the Marx source explains why multiple connections can sometimes outperform one under loss.
- HTTPS and origin coordination: [[nick-craver-https-on-stack-overflow-the-end-of-a-long-road]] describes browser encryption requirements, shared edge IPs, and a combined certificate for connection reuse and planned push.
- Compression, push, and complexity: [[chen-hao-http-de-qian-shi-jin-sheng]] covers HPACK, server push, and priority-tree complexity.

## Counterevidence & Qualifications
The sources do not supply controlled protocol benchmarks. The Baqend account treats HTTP/2 as one optimization among caching, CDN placement, and backend design; the Stack Overflow account describes planned rather than measured server-push benefit. Marx argues that TCP-level blocking is real but often smaller than HTTP/1.1 application-layer serialization because packet loss is comparatively rare. Current browser connection-coalescing, server-push, priority, and deployment behavior require current documentation.

## What Changed
- Added packet-level framing and the mismatch between independent HTTP streams and TCP's single byte stream.
- Qualified single-connection efficiency with concentrated loss and congestion-control effects.
- Distinguished protocol capability from measured page-load benefit under real scheduling and loss.

## Related Concepts
- [[HTTP]] - HTTP/2 is a performance-oriented version in the HTTP family.
- [[HTTP11]] - HTTP/2 adds stream framing to overcome HTTP/1.1 response serialization.
- [[HTTP3]] - HTTP/3 retains framed HTTP semantics while moving stream handling into QUIC.
- [[QUIC]] - QUIC addresses the cross-stream transport constraint that HTTP/2 cannot remove over TCP.
- [[HeadOfLineBlocking]] - TCP-level blocking is HTTP/2's central remaining ordering problem.
- [[WebPerformanceOptimization]] - HTTP/2 is one network-performance lever among caching, CDN, frontend, and backend work.
- [[HTTPSMigration]] - HTTPS deployment enabled practical browser use of HTTP/2 in the Stack Overflow case.
- [[Fastly]] - edge provider involved in certificate placement and planned cross-origin push support.
