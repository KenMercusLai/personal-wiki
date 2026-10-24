---
title: "Network Time Synchronization"
type: concept
tags: [ntp, distributed-systems, clocks, production-engineering]
sources:
  - ntp-service
  - telestra-outage-report
last_updated: 2026-10-24
knowledge_schema: synthesis-v1
---

## Definition
[[NetworkTimeSynchronization]] is the distribution and correction of clock time across computers over variable-latency networks using reference clocks, timestamp exchanges, clock-control software, and a hierarchy of serving systems.

## Current Synthesis
Useful precision is an end-to-end property, not simply a daemon's displayed offset. Reference quality, stratum architecture, network-path symmetry, packet timestamp location, operating-system scheduling, oscillator conditions, hardware support, and leap-second policy all contribute to the gap between a reported estimate and real clock error.

The Facebook case separates reference, policy, and scale. GNSS satellites discipline an atomic-clock appliance; a second tier applies a common leap smear; a broader serving tier distributes already-smeared time. Independent 1PPS or GNSS/atomic-clock measurements are needed to calibrate the daemon's error window because an NTP exchange observes packet timing through assumptions that production networks and general-purpose operating systems do not perfectly satisfy.

The Telstra case adds a failure-topology boundary. A nominal hierarchy is not dependable when migration removes independent source paths, symmetric peering lets a server select one of its former clients, a failover reference can become wrong after restart, or operators cannot enumerate the real source relationships. In that incident, activating GPS promoted Melbourne to Stratum 1 and its clients to Stratum 2; after a later chassis restart moved the GPS date back 19.7 years, a shared client carried incorrect time into Sydney. Stratum numbers described apparent distance from a reference, but did not prove that references were independent or correct.

Time error can also outlive clock repair. Telstra's wrong date reset mobile control-plane instances, reduced capacity, and caused about 30,000 IP-prefix records to be written with invalid timestamps. Correcting the reference clock therefore had to be followed by application-state repair.

## Key Claims
- A layered stratum design separates primary reference clocks from policy application and large-scale serving load.
- Daemon offsets are model-based estimates whose accuracy depends on path symmetry, timestamp placement, scheduling, and oscillator behavior.
- Independent 1PPS or GNSS-disciplined packet measurement provides a stronger reference for validating real offset.
- Network-interface timestamps can reduce software-path uncertainty but cannot eliminate network and reference-clock error.
- Multiple geographically distinct endpoints can improve path locality and failure independence, but their benefit remains client-location-dependent.
- Source diversity is real only when dependency paths are independent, documented, and unable to form timing loops through shared clients.
- Failover references need restart, rollover, and bad-time-containment tests because an apparently higher-quality source can spread a coherent but false date.

## Evidence
- Layered architecture: [[ntp-service]] shows GNSS Stratum 0, an atomic-clock Stratum 1 appliance, leap-smearing Stratum 2 servers, and scaled Stratum 3 servers.
- Estimate boundary: [[ntp-service]] contrasts ntpd and chrony output with external observations and highlights assumptions about symmetry and prompt dispatch.
- Physical validation: [[ntp-service]] describes direct 1PPS phase comparison and a portable GNSS/atomic-clock NTP client with nanosecond-scale timestamping error.
- Public routing: [[ntp-service]] retains two endpoint traces with distinct routes and latency, plus a provider comparison whose results vary by path.
- Redundancy erosion: [[telestra-outage-report]] shows how Telstra's 2020 chassis migration removed local Stratum 3-to-Stratum 2 paths in Sydney and Melbourne.
- Loop formation: [[telestra-outage-report]] reports that Melbourne became Stratum 5 through an unidentified Stratum 4 client after losing its intended Sydney source.
- Failover promotion: [[telestra-outage-report]] shows GPS failover making Melbourne Stratum 1 and its clients Stratum 2, changing which peers appeared authoritative.
- Bad-time propagation: [[telestra-outage-report]] reconstructs incorrect Melbourne time passing through a shared client into Sydney after the GPS card restarted with a 19.7-year date rollback.
- Persistent consequences: [[telestra-outage-report]] says wrong time reset mobile control-plane instances and corrupted about 30,000 IP-prefix records that required repair after correct time returned.

## Counterevidence & Qualifications
One first-party deployment does not establish universal ntpd-versus-chrony performance or the correct architecture for every scale. The Facebook source supplies selected traces rather than raw long-duration distributions, failure cases, holdover behavior, security analysis, configuration, or fleet-wide reliability. Public endpoint diversity shown from one vantage point does not prove global independence, and the NTP approach remains limited when applications require stronger precision than variable-latency packet exchange can reliably provide.

The Telstra evidence is a secondary reconstruction whose author explicitly lacks telecom expertise and marks several topology and product details as assumptions. It does not supply complete configuration, packet captures, raw telemetry, Perth behavior, or an independently verified causal model. The incident nevertheless supports the narrower conclusion that hierarchy metadata alone cannot establish source independence, reference correctness, or containment of bad time.

## What Changed
- Established time synchronization as a measured end-to-end service rather than a daemon configuration problem.
- Added separation among reference, leap policy, serving scale, and independent validation.
- Added source-dependency topology, loop prevention, and restart-tested failover as correctness requirements.
- Added downstream poisoned-state repair as a consequence that can survive restoration of correct time.

## Related Concepts
- [[HardwareTimestamping]] - moves packet timing closer to the network interface to reduce software-path uncertainty.
- [[LeapSecondSmearing]] - changes clock rate around a leap event to preserve monotonic application time.
- [[CentralizedLogging]] - depends on sufficiently aligned clocks when events from different nodes are compared by timestamp.
- [[Chrony]] - NTP implementation used in the source's measured production design.
- [[SystemReliability]] - time-service dependability includes redundancy, failover, containment, and downstream recovery.
- [[SSU2000]] - timing chassis whose topology limit and GPS rollover behavior shaped the Telstra case.
