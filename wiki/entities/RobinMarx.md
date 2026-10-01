---
title: "Robin Marx"
type: entity
tags: [researcher, networking, web-performance]
sources:
  - robin-marx-head-of-line-blocking-in-quic-and-http-3-the-details
last_updated: 2026-10-02
knowledge_schema: synthesis-v1
---

## Overview
[[RobinMarx]] is represented here as a web-performance and network-protocol researcher whose work focuses on [[QUIC]] and [[HTTP3]].

## Current Profile
The source presents Marx as a researcher at Hasselt University and a developer of qlog and qvis tooling for inspecting QUIC and HTTP/3 behavior. His article combines layered protocol explanation with packet-level diagrams and a deliberately qualified performance judgment: removing TCP's cross-stream [[HeadOfLineBlocking]] is technically important, but its page-load value depends on resource scheduling, concurrency, and loss patterns.

## Key Characteristics
- Researches QUIC, HTTP/3, and web-performance behavior.
- Explains protocol mechanisms through packetization, byte-range, stack, and sequence diagrams.
- Distinguishes protocol capability from measured end-user performance benefit.
- Develops qlog and qvis tools for protocol analysis and visualization.

## Evidence
- Research focus and tooling: [[robin-marx-head-of-line-blocking-in-quic-and-http-3-the-details]] identifies Marx with Hasselt University, QUIC and HTTP/3 performance research, and qlog/qvis development.
- Explanatory method: [[robin-marx-head-of-line-blocking-in-quic-and-http-3-the-details]] uses inspected diagrams to compare framing, stream identity, byte tracking, packet loss, scheduling, and pipelining across protocol layers.
- Qualified judgment: [[robin-marx-head-of-line-blocking-in-quic-and-http-3-the-details]] argues that QUIC's narrower blocking domain probably has limited effect for many web page loads unless multiple useful streams are active under favorable loss and scheduling conditions.

## Qualifications
The profile is based on one 2020 article and its short author biography. It does not establish Marx's current affiliation, complete publication record, or the present status and adoption of qlog and qvis.

## What Changed
- Created Robin Marx's profile around his protocol-research focus, tooling, and qualified analysis of QUIC performance.

## Relationships
- [[QUIC]] - primary transport protocol in Marx's analyzed performance problem.
- [[HTTP3]] - application protocol whose stream behavior the article explains.
- [[HeadOfLineBlocking]] - central mechanism Marx separates across application, transport, stream, and TLS layers.
