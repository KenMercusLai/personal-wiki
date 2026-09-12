---
title: "HTTP"
type: concept
tags: [networking, protocol, web]
sources:
  - chen-hao-http-de-qian-shi-jin-sheng
  - 402-payment-required-david-humphrey-medium
last_updated: 2026-09-12
knowledge_schema: synthesis-v1
---

## Definition
[[HTTP]] is the Hypertext Transfer Protocol: the web's application-layer protocol for transferring hypertext and other resources between clients and servers.

## Current Synthesis
The sources present HTTP as a protocol family that evolved by separating concerns and absorbing performance lessons. Early HTTP was a simple request-response mechanism; HTTP/1.0 added versioning, headers, status codes, and content types; [[HTTP11]] added persistent connections and richer negotiation; [[HTTP2]] improved throughput through binary framing and multiplexing; [[HTTP3]] moved transport onto [[QUIC]] over UDP to reduce TCP-level blocking.

The article's broader judgment is that HTTP became not just a document-transfer protocol but a general application communication standard. Its improvements made it easier for organizations to build on shared tooling and conventions rather than maintain private protocols for problems HTTP already solved.

Humphrey's payment article adds a product-design angle to HTTP status semantics. It argues that [[HTTP402PaymentRequired]], reserved for future use, could become a browser-readable signal for paid access if sites returned enough metadata for a trusted [[BrowserPaymentBroker]] to offer purchase, rental, or subscription options.

## Key Claims
- HTTP's evolution is a sequence of engineering separations: protocol versioning, metadata headers, status codes, and content typing.
- HTTP/1.0 made the protocol more general but suffered from one new TCP connection per resource.
- [[HTTP11]] expanded HTTP into a more capable application-layer protocol with persistent connections, caching, negotiation, Host routing, CORS support, and WebSocket-era patterns.
- [[HTTP2]] improved performance by replacing textual request sequencing with binary framing, multiplexing, header compression, and server push.
- [[HTTP3]] changes the transport foundation by using [[QUIC]] over UDP rather than TCP.
- Standard HTTP adoption is treated as an architectural advantage because it increases compatibility with industry tooling and open-source ecosystems.
- HTTP status codes can be product-interface hooks, not only error labels, when browsers and sites agree on behavior around responses such as [[HTTP402PaymentRequired]].

## Evidence
- Early engineering maturity: [[chen-hao-http-de-qian-shi-jin-sheng]] identifies versioning, headers, status codes, and content types as the changes that made HTTP/1.0 more disciplined.
- HTTP/1.0 limitation: [[chen-hao-http-de-qian-shi-jin-sheng]] says each resource request needed a new TCP connection and remained serial.
- HTTP/1.1 expansion: [[chen-hao-http-de-qian-shi-jin-sheng]] lists persistent connections, pipelining, chunked responses, cache control, negotiation headers, Host, and OPTIONS.
- HTTP/2 performance: [[chen-hao-http-de-qian-shi-jin-sheng]] describes binary transfer, concurrent requests on one TCP connection, HPACK header compression, and server push.
- HTTP/3 transport shift: [[chen-hao-http-de-qian-shi-jin-sheng]] explains HTTP/3 as HTTP/2 plus [[QUIC]], with UDP replacing TCP underneath.
- Standardization benefit: [[chen-hao-http-de-qian-shi-jin-sheng]] argues that internal architectures benefit when they follow industry standards.
- Payment signaling: [[402-payment-required-david-humphrey-medium]] proposes using [[HTTP402PaymentRequired]] metadata so browsers can present paid-access options.

## Counterevidence & Qualifications
The protocol-history source is an explanatory technical essay, not a standards document or benchmark. Some adoption claims and browser-support references are time-bound to the article's publication date of 2019-10-01. The 402 source is a 2015 proposal rather than an implemented standard, so its payment claims should be read as design imagination.

## What Changed
- Created the HTTP concept page as the parent protocol thread for the new networking source.
- Added the 402 payment proposal as an example of HTTP status semantics becoming browser product infrastructure.

## Related Concepts
- [[HTTP11]] - HTTP/1.1 extends HTTP with persistent connections and richer application-protocol features.
- [[HTTP2]] - HTTP/2 changes HTTP's framing and multiplexing model.
- [[HTTP3]] - HTTP/3 changes HTTP's transport foundation through QUIC.
- [[QUIC]] - QUIC supplies the UDP-based transport layer for HTTP/3.
- [[HeadOfLineBlocking]] - transport and pipeline blocking are a recurring HTTP performance problem.
- [[HTTP402PaymentRequired]] - 402 is a reserved HTTP status code proposed as a payment signal.
- [[BrowserPaymentBroker]] - browser-mediated payment depends on clients interpreting the HTTP 402 response.
