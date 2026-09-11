---
title: "HTTP"
type: concept
tags: [networking, protocol, web]
sources:
  - chen-hao-http-de-qian-shi-jin-sheng
last_updated: 2026-09-11
knowledge_schema: synthesis-v1
---

## Definition
[[HTTP]] is the Hypertext Transfer Protocol: the web's application-layer protocol for transferring hypertext and other resources between clients and servers.

## Current Synthesis
The source presents HTTP as a protocol family that evolved by separating concerns and absorbing performance lessons. Early HTTP was a simple request-response mechanism; HTTP/1.0 added versioning, headers, status codes, and content types; [[HTTP11]] added persistent connections and richer negotiation; [[HTTP2]] improved throughput through binary framing and multiplexing; [[HTTP3]] moved transport onto [[QUIC]] over UDP to reduce TCP-level blocking.

The article's broader judgment is that HTTP became not just a document-transfer protocol but a general application communication standard. Its improvements made it easier for organizations to build on shared tooling and conventions rather than maintain private protocols for problems HTTP already solved.

## Key Claims
- HTTP's evolution is a sequence of engineering separations: protocol versioning, metadata headers, status codes, and content typing.
- HTTP/1.0 made the protocol more general but suffered from one new TCP connection per resource.
- [[HTTP11]] expanded HTTP into a more capable application-layer protocol with persistent connections, caching, negotiation, Host routing, CORS support, and WebSocket-era patterns.
- [[HTTP2]] improved performance by replacing textual request sequencing with binary framing, multiplexing, header compression, and server push.
- [[HTTP3]] changes the transport foundation by using [[QUIC]] over UDP rather than TCP.
- Standard HTTP adoption is treated as an architectural advantage because it increases compatibility with industry tooling and open-source ecosystems.

## Evidence
- Early engineering maturity: [[chen-hao-http-de-qian-shi-jin-sheng]] identifies versioning, headers, status codes, and content types as the changes that made HTTP/1.0 more disciplined.
- HTTP/1.0 limitation: [[chen-hao-http-de-qian-shi-jin-sheng]] says each resource request needed a new TCP connection and remained serial.
- HTTP/1.1 expansion: [[chen-hao-http-de-qian-shi-jin-sheng]] lists persistent connections, pipelining, chunked responses, cache control, negotiation headers, Host, and OPTIONS.
- HTTP/2 performance: [[chen-hao-http-de-qian-shi-jin-sheng]] describes binary transfer, concurrent requests on one TCP connection, HPACK header compression, and server push.
- HTTP/3 transport shift: [[chen-hao-http-de-qian-shi-jin-sheng]] explains HTTP/3 as HTTP/2 plus [[QUIC]], with UDP replacing TCP underneath.
- Standardization benefit: [[chen-hao-http-de-qian-shi-jin-sheng]] argues that internal architectures benefit when they follow industry standards.

## Counterevidence & Qualifications
The source is an explanatory technical essay, not a standards document or benchmark. Some adoption claims and browser-support references are time-bound to the article's publication date of 2019-10-01.

## What Changed
- Created the HTTP concept page as the parent protocol thread for the new networking source.
- Added the source's standardization and performance-evolution framing.

## Related Concepts
- [[HTTP11]] - HTTP/1.1 extends HTTP with persistent connections and richer application-protocol features.
- [[HTTP2]] - HTTP/2 changes HTTP's framing and multiplexing model.
- [[HTTP3]] - HTTP/3 changes HTTP's transport foundation through QUIC.
- [[QUIC]] - QUIC supplies the UDP-based transport layer for HTTP/3.
- [[HeadOfLineBlocking]] - transport and pipeline blocking are a recurring HTTP performance problem.
