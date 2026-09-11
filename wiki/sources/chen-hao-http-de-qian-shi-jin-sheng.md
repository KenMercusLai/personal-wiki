---
title: "陈皓 - HTTP的前世今生"
type: source
tags: [http, networking, protocol, web]
date: 2019-10-01
source_file: /mnt/ken_personal_wiki/Articles/陈皓 - HTTP的前世今生.md
---

## Summary
This article traces [[HTTP]] from its early request-response origins through [[HTTP11]], [[HTTP2]], and [[HTTP3]]. [[ChenHao]] frames the protocol's history as a series of engineering moves: separating metadata from payloads, standardizing errors through status codes, improving connection reuse and caching, then addressing performance limits through binary framing, multiplexing, and [[QUIC]]. The source argues that protocol standardization gives architecture teams practical leverage because widely adopted standards improve interoperability and access to open-source ecosystems.

## Key Claims
- Early [[HTTP]] became more engineering-friendly when versioning, headers, status codes, and content types separated control metadata from business data.
- [[HTTP11]] improved HTTP/1.0 by adding persistent connections, pipelining, chunked responses, cache control, negotiation headers, the Host header, and OPTIONS for CORS.
- The 2014 HTTP/1.1 RFC series broadened HTTP's role as a general application-layer protocol and reduced the case for private RPC reinvention.
- [[HTTP2]] addressed HTTP/1.1 performance constraints with binary framing, request multiplexing, HPACK header compression, and server push, while increasing protocol complexity.
- [[HeadOfLineBlocking]] remained a problem for HTTP/2 because multiple HTTP streams still shared one TCP connection.
- [[HTTP3]] moved HTTP over [[QUIC]] and UDP to reduce TCP-level head-of-line blocking, combine transport and TLS setup, and support connection identity across network changes.
- [[QUIC]] faces deployment challenges because many NATs, load balancers, and network devices understand UDP packets rather than QUIC's connection IDs and stream semantics.

## Key Quotes
> "一种工程文明" - on HTTP/1.0's versioning, headers, status codes, and content types.

> "HTTP/3破天荒地把HTTP底层的TCP协议改成了UDP" - on the protocol-stack shift in HTTP/3.

## Connections
- [[HTTP]] - the article's central protocol lineage.
- [[HTTP11]] - presented as the version that made HTTP persistent, cacheable, negotiable, and broadly useful for application APIs.
- [[HTTP2]] - presented as the major performance upgrade built from Google's SPDY work.
- [[HTTP3]] - presented as the QUIC-based successor intended to address TCP limitations.
- [[QUIC]] - described as the UDP-based transport foundation for HTTP/3.
- [[HeadOfLineBlocking]] - used to explain why HTTP/2 still had transport-level blocking.
- [[ChenHao]] - author of the article.
- [[TimBernersLee]] - credited as the inventor of HTTP and the WWW.
- [[Google]] - associated with SPDY, QUIC, Chrome, and congestion-control experimentation in the article.

## Contradictions
- No direct contradictions with existing wiki content. This source adds a networking-protocol thread to the technology portion of the wiki.
