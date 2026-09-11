---
title: "HTTP/3"
type: concept
tags: [networking, protocol, web, quic]
sources:
  - chen-hao-http-de-qian-shi-jin-sheng
last_updated: 2026-09-11
knowledge_schema: synthesis-v1
---

## Definition
[[HTTP3]] is the HTTP version that runs HTTP semantics over [[QUIC]] and UDP rather than TCP, primarily to address transport-level blocking and connection-setup costs.

## Current Synthesis
The source frames HTTP/3 less as a new application protocol and more as HTTP/2 moved onto a different transport foundation. [[HTTP2]] multiplexes streams over TCP, but TCP cannot distinguish those streams; packet loss can therefore stall all streams on the connection. HTTP/3 addresses that by using QUIC over UDP, where stream recovery, congestion control, TLS integration, and connection identity are handled above UDP.

The article is optimistic about QUIC's power but cautious about deployment speed. Because HTTP/3 changes the lower transport layer, network equipment, NAT behavior, load-balancer hashing, and header-compression synchronization create adoption and implementation challenges.

## Key Claims
- HTTP/3 is motivated by [[HeadOfLineBlocking]] that remains when HTTP/2 multiplexes streams over TCP.
- HTTP/3 changes HTTP's transport from TCP to UDP through [[QUIC]].
- QUIC combines reliable transport behavior, TLS setup, and HTTP/2-like multiplexing above UDP.
- QUIC connection IDs allow continuity across network changes better than TCP's four-tuple identity.
- HTTP/3 faces deployment friction from NATs, load balancers, and network devices that understand UDP but not QUIC.
- HTTP/3 required QPACK because HPACK-style dynamic-table synchronization is harder over QUIC's transport model.

## Evidence
- Blocking motivation: [[chen-hao-http-de-qian-shi-jin-sheng]] explains that HTTP/2 packet loss on one TCP connection can block all HTTP streams.
- Transport change: [[chen-hao-http-de-qian-shi-jin-sheng]] says HTTP/3 replaces TCP underneath HTTP with UDP through QUIC.
- QUIC stack role: [[chen-hao-http-de-qian-shi-jin-sheng]] describes QUIC as pseudo-TCP plus TLS plus HTTP/2-style multiplexing over UDP.
- Connection identity: [[chen-hao-http-de-qian-shi-jin-sheng]] says QUIC connection IDs can preserve a connection across mobile and Wi-Fi changes.
- Infrastructure friction: [[chen-hao-http-de-qian-shi-jin-sheng]] gives NAT and four-tuple load-balancing examples that can break QUIC routing assumptions.
- Header compression change: [[chen-hao-http-de-qian-shi-jin-sheng]] explains why HPACK had to be redesigned as QPACK for QUIC.

## Counterevidence & Qualifications
The article was written in 2019 and treats HTTP/3 support and adoption as emergent at that time. Its deployment outlook should be read as publication-date context rather than a current adoption measurement.

## What Changed
- Created the HTTP/3 concept page as the wiki's QUIC-based HTTP transport node.

## Related Concepts
- [[HTTP]] - HTTP/3 is part of HTTP's protocol lineage.
- [[HTTP2]] - HTTP/3 reuses much of the HTTP/2 model while changing transport.
- [[QUIC]] - QUIC is HTTP/3's UDP-based transport foundation.
- [[HeadOfLineBlocking]] - reducing TCP-level blocking is the article's main reason for HTTP/3.
