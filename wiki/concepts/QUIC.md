---
title: "QUIC"
type: concept
tags: [networking, protocol, transport, udp]
sources:
  - chen-hao-http-de-qian-shi-jin-sheng
last_updated: 2026-09-11
knowledge_schema: synthesis-v1
---

## Definition
[[QUIC]] is a UDP-based transport protocol used by [[HTTP3]] to provide reliable delivery behavior, TLS integration, multiplexing, congestion control, and connection identity above UDP.

## Current Synthesis
The source presents QUIC as the key transport innovation behind HTTP/3. QUIC uses UDP as its substrate but rebuilds many TCP-like responsibilities above it: retransmission, congestion control, connection establishment, TLS integration, and stream multiplexing. This design is meant to avoid TCP's transport-level [[HeadOfLineBlocking]] and reduce connection setup overhead.

The article also emphasizes that QUIC's strength creates infrastructure challenges. Existing network devices often route, map, or balance traffic using IP and port tuples; QUIC's connection ID gives applications a better identity mechanism, but devices that cannot understand it may split a connection across backends or mishandle UDP traffic.

## Key Claims
- QUIC is the transport foundation that lets [[HTTP3]] run over UDP instead of TCP.
- QUIC avoids TCP-level [[HeadOfLineBlocking]] by managing streams above UDP.
- QUIC includes its own retransmission and congestion-control behavior.
- QUIC can reduce HTTPS connection setup by integrating transport and TLS handshakes.
- QUIC connection IDs support continuity across IP or network-interface changes.
- QUIC deployment is constrained by network infrastructure that only understands UDP packets and four-tuples.

## Evidence
- HTTP/3 foundation: [[chen-hao-http-de-qian-shi-jin-sheng]] says QUIC entered the standardization path as the basis for [[HTTP3]].
- Blocking behavior: [[chen-hao-http-de-qian-shi-jin-sheng]] says UDP avoids TCP's ordered-delivery blocking, while QUIC supplies its own reliability.
- Congestion control: [[chen-hao-http-de-qian-shi-jin-sheng]] discusses QUIC using CUBIC and potentially BBR-style congestion control.
- Handshake integration: [[chen-hao-http-de-qian-shi-jin-sheng]] contrasts TCP plus TLS handshakes with QUIC's integrated setup.
- Connection identity: [[chen-hao-http-de-qian-shi-jin-sheng]] describes connection ID as a way to keep a connection through mobile/Wi-Fi changes.
- Infrastructure constraints: [[chen-hao-http-de-qian-shi-jin-sheng]] explains how NATs and four-tuple load balancers can fail to preserve QUIC's intended routing.

## Counterevidence & Qualifications
The source is conceptually favorable toward QUIC but does not present production measurements. It also notes significant deployment risk from network devices and backend routing behavior that were not designed around QUIC connection IDs.

## What Changed
- Created the QUIC concept page as the transport-protocol foundation for HTTP/3.

## Related Concepts
- [[HTTP3]] - HTTP/3 uses QUIC as its transport layer.
- [[HTTP2]] - QUIC carries an HTTP/2-like multiplexing model while avoiding TCP constraints.
- [[HeadOfLineBlocking]] - QUIC is presented as a response to TCP-level blocking.
- [[HTTP]] - QUIC changes the transport layer beneath the HTTP family.
