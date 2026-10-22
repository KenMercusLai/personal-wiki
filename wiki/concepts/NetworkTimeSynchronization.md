---
title: "Network Time Synchronization"
type: concept
tags: [ntp, distributed-systems, clocks, production-engineering]
sources:
  - ntp-service
last_updated: 2026-10-22
knowledge_schema: synthesis-v1
---

## Definition
[[NetworkTimeSynchronization]] is the distribution and correction of clock time across computers over variable-latency networks using reference clocks, timestamp exchanges, clock-control software, and a hierarchy of serving systems.

## Current Synthesis
Useful precision is an end-to-end property, not simply a daemon's displayed offset. Reference quality, stratum architecture, network-path symmetry, packet timestamp location, operating-system scheduling, oscillator conditions, hardware support, and leap-second policy all contribute to the gap between a reported estimate and real clock error.

The Facebook case separates reference, policy, and scale. GNSS satellites discipline an atomic-clock appliance; a second tier applies a common leap smear; a broader serving tier distributes already-smeared time. Independent 1PPS or GNSS/atomic-clock measurements are needed to calibrate the daemon's error window because an NTP exchange observes packet timing through assumptions that production networks and general-purpose operating systems do not perfectly satisfy.

## Key Claims
- A layered stratum design separates primary reference clocks from policy application and large-scale serving load.
- Daemon offsets are model-based estimates whose accuracy depends on path symmetry, timestamp placement, scheduling, and oscillator behavior.
- Independent 1PPS or GNSS-disciplined packet measurement provides a stronger reference for validating real offset.
- Network-interface timestamps can reduce software-path uncertainty but cannot eliminate network and reference-clock error.
- Multiple geographically distinct endpoints can improve path locality and failure independence, but their benefit remains client-location-dependent.

## Evidence
- Layered architecture: [[ntp-service]] shows GNSS Stratum 0, an atomic-clock Stratum 1 appliance, leap-smearing Stratum 2 servers, and scaled Stratum 3 servers.
- Estimate boundary: [[ntp-service]] contrasts ntpd and chrony output with external observations and highlights assumptions about symmetry and prompt dispatch.
- Physical validation: [[ntp-service]] describes direct 1PPS phase comparison and a portable GNSS/atomic-clock NTP client with nanosecond-scale timestamping error.
- Public routing: [[ntp-service]] retains two endpoint traces with distinct routes and latency, plus a provider comparison whose results vary by path.

## Counterevidence & Qualifications
One first-party deployment does not establish universal ntpd-versus-chrony performance or the correct architecture for every scale. The source supplies selected traces rather than raw long-duration distributions, failure cases, holdover behavior, security analysis, configuration, or fleet-wide reliability. Public endpoint diversity shown from one vantage point does not prove global independence, and the NTP approach remains limited when applications require stronger precision than variable-latency packet exchange can reliably provide.

## What Changed
- Established time synchronization as a measured end-to-end service rather than a daemon configuration problem.
- Added separation among reference, leap policy, serving scale, and independent validation.

## Related Concepts
- [[HardwareTimestamping]] - moves packet timing closer to the network interface to reduce software-path uncertainty.
- [[LeapSecondSmearing]] - changes clock rate around a leap event to preserve monotonic application time.
- [[CentralizedLogging]] - depends on sufficiently aligned clocks when events from different nodes are compared by timestamp.
- [[Chrony]] - NTP implementation used in the source's measured production design.
