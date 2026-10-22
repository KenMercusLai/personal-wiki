---
title: "Chrony"
type: entity
tags: [software, ntp, time-synchronization, linux]
sources:
  - ntp-service
last_updated: 2026-10-22
knowledge_schema: synthesis-v1
---

## Overview
[[Chrony]] is an NTP implementation represented through Facebook's reported migration from ntpd and its use in an internal and public time service.

## Current Profile
In the tested Facebook environment, chrony produced smaller offset variation and tighter error estimates than ntpd while using similar CPU and slightly less memory. Its extended exchange between chrony peers, hardware-timestamp support, source diagnostics, and leap handling made it the serving foundation for a multi-stratum design. The strongest result is practical rather than absolute: external reference instrumentation usually found hundreds-of-microseconds accuracy, not the nanosecond-sized adjusted offset that one daemon sample displayed.

## Key Characteristics
- Implements NTP synchronization and exposes measured offset, adjusted offset, reachability, and estimated error through `chronyc`.
- Supports compatible network-interface hardware timestamps to reduce user-space and scheduler delay in packet timing.
- Supports leap-second smearing driven by the GNSS leap indicator.
- Scaled through separate reference, smear, and serving tiers in Facebook's deployment.

## Evidence
- Daemon comparison: [[ntp-service]] reports microsecond-range chrony estimates after millisecond-range ntpd behavior on the tested servers.
- Independent validation: [[ntp-service]] shows chrony mostly within plus or minus 200 microseconds and hardware-timestamped chrony often within plus or minus 100 microseconds on one lab trace.
- Timestamp mechanism: [[ntp-service]] explains why timestamping at the network interface avoids much of the Linux scheduling interval between userspace processing and wire transmission.
- Leap policy: [[ntp-service]] describes a smooth approximately 18-hour post-event smear applied by Stratum 2 chrony servers.

## Qualifications
The evidence is a first-party 2020 deployment account, not a controlled cross-platform benchmark or complete protocol analysis. Results depend on hardware, network path, reference clocks, configuration, traffic, oscillator conditions, and chrony version. A nanosecond-scale adjusted offset in `chronyc` does not override its wider estimated-error window or independent measurements.

## What Changed
- Established chrony as a measured production time-service component rather than only an NTP daemon.
- Separated displayed offset precision from externally validated accuracy.

## Relationships
- [[NetworkTimeSynchronization]] - service objective chrony implements over packet networks.
- [[HardwareTimestamping]] - optional precision mechanism supported by chrony and compatible interfaces.
- [[LeapSecondSmearing]] - continuity policy performed by chrony in the described Stratum 2 tier.
- [[Facebook]] - operator whose deployment supplies the current evidence.
