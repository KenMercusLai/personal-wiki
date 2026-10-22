---
title: "Hardware Timestamping"
type: concept
tags: [networking, ntp, clocks, linux, precision]
sources:
  - ntp-service
last_updated: 2026-10-22
knowledge_schema: synthesis-v1
---

## Definition
[[HardwareTimestamping]] records packet timing at a compatible network interface rather than relying only on a userspace or kernel software timestamp taken earlier or later in the I/O path.

## Current Synthesis
For clock synchronization, moving the timestamp toward the wire removes much of the uncertain interval created by process scheduling, system calls, queueing, and neighbor discovery. The timestamp still does not coincide perfectly with physical transmission, but the source places the remaining network-card interval below 10 ns in its setup.

The important distinction is between timestamp precision and clock accuracy. One chrony sample showed an adjusted offset of 11 ns while retaining a 193 microsecond estimated-error window; an independent device observed a broader distribution, often within plus or minus 100 microseconds. Hardware timestamping therefore improves the measurement boundary without making every other error source disappear.

## Key Claims
- Software timestamps can include nondeterministic delay before a packet reaches or leaves the network interface.
- Compatible interface timestamps narrow that local delay and let chrony estimate packet timing closer to wire transmission.
- Capability must be verified for both hardware transmit and receive paths rather than assumed from the network-card model.
- Nanosecond-resolution timestamps do not guarantee nanosecond end-to-end synchronization accuracy.

## Evidence
- Delay mechanism: [[ntp-service]] diagrams Linux, chrony, other processes, and the network card between software timestamping and packet transmission.
- Capability check: [[ntp-service]] uses `ethtool -T eth0` to verify transmit, receive, and raw-clock timestamp support.
- External result: [[ntp-service]] reports hardware-timestamped chrony usually between -100 and +100 microseconds on the displayed lab run, compared with a wider chrony range and a 13 ms ntpd span.

## Counterevidence & Qualifications
The article does not specify the interface model, driver, clock discipline, chrony configuration, traffic conditions, sample distribution, or reproducible benchmark procedure. Hardware timestamps do not remove asymmetric network paths, queueing beyond the timestamp point, oscillator drift, reference-clock uncertainty, daemon modeling error, or unsupported hardware. The claimed sub-10 ns interface delay is setup-specific and is not independently validated in the source.

## What Changed
- Established hardware timestamping as a boundary shift in packet observation rather than an accuracy guarantee.
- Added the distinction between nanosecond timestamp resolution and microsecond-scale validated clock error.

## Related Concepts
- [[NetworkTimeSynchronization]] - uses packet timestamps to estimate and correct clock offset.
- [[Chrony]] - consumes supported hardware timestamps in the described deployment.
- [[HighThroughputIOOptimization]] - shares the broader principle that user-space observations can hide kernel, queue, and device-stage delay.
- [[LatencyHierarchy]] - situates software scheduling and device timing as distinct latency components.
