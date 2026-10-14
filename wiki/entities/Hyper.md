---
title: "hyper"
type: entity
tags: [rust, http, networking, open-source]
sources:
  - how-we-found-a-bug-in-the-hyper-http-library
last_updated: 2026-10-14
knowledge_schema: synthesis-v1
---

## Overview
[[Hyper]] is an open-source HTTP library for Rust. [[Cloudflare]] uses it on the Images service side of a socket connection to read requests and write processed image responses.

## Current Profile
The available source focuses on hyper's HTTP/1 connection lifecycle rather than its full API or architecture. Its `dispatch.rs` state machine reads, writes, flushes, decides whether more input is needed, and eventually shuts down the transport. In the reported failure, it treated response encoding into an internal buffer as complete even though the buffer had not fully drained to the kernel socket.

The dispatch loop discarded `Poll::Pending` from `poll_flush`. When a slow reader let the socket buffer fill, hyper could then conclude that the connection was finished and call shutdown with response bytes still buffered. Cloudflare reproduced this with a stream wrapper that accepted one 8 KB write and blocked later writes. The merged fix makes `poll_shutdown` await a complete flush before shutting down the socket.

## Key Characteristics
- Provides an asynchronous HTTP implementation for Rust services.
- Drives HTTP/1 connections through a state machine covering reads, writes, flushes, and shutdown.
- Separates response encoding into an internal buffer from transport-level delivery to a socket.
- Uses Rust `Poll` readiness to represent incomplete asynchronous I/O.
- Accepts upstream fixes and regression tests through the `hyperium/hyper` project.

## Evidence
- Service role: [[how-we-found-a-bug-in-the-hyper-http-library]] says Cloudflare Images uses hyper to manage the service side of client connections.
- Failure mechanism: [[how-we-found-a-bug-in-the-hyper-http-library]] traces a discarded `Poll::Pending` through connection completion and premature `SHUT_WR` with unsent buffered bytes.
- Deterministic reproduction: [[how-we-found-a-bug-in-the-hyper-http-library]] describes a constrained stream that accepts 8 KB and then blocks, exposing shutdown with most of a 500 KB response still buffered.
- Remediation: [[how-we-found-a-bug-in-the-hyper-http-library]] reports that PR #4018 moved the safety check to shutdown by awaiting `poll_flush` before closing the write side.

## Qualifications
The source is a Cloudflare incident account centered on one HTTP/1 lifecycle bug across the tested 0.14, 1.7, and 1.8 versions. It is not a general assessment of hyper's performance, protocol coverage, API stability, security, or reliability. Cloudflare's first dispatch-loop patch worked in its no-keepalive service but was not suitable as the general upstream design because it could reduce read polling and affect reusable connections. At publication time, the merged fix was scheduled for a future release and Cloudflare was running an internal patched fork.

## What Changed
- Created the project profile from Cloudflare's diagnosis, deterministic test, and upstream shutdown fix.

## Relationships
- [[Cloudflare]] - uses hyper in its Images service and contributed the reported fix.
- [[RaceCondition]] - the reported data loss depended on flush and shutdown timing.
- [[AdaptiveBackpressure]] - socket-buffer saturation caused the flush to return `Poll::Pending`.
- [[SystemReliability]] - transport completion must match the HTTP body's promised length.
- [[ServiceObservability]] - syscall traces revealed behavior invisible to application telemetry.
