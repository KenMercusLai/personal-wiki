---
title: "Oleg Obleukhov"
type: entity
tags: [production-engineering, time-synchronization, author]
sources:
  - ntp-service
last_updated: 2026-10-22
knowledge_schema: synthesis-v1
---

## Overview
[[OlegObleukhov]] is represented as the Facebook production engineer who authored a 2020 account of the company's internal and public NTP service.

## Current Profile
Obleukhov presents precision timekeeping as an empirically validated production-systems problem. His account joins daemon selection, stratum architecture, reference-clock instrumentation, network-interface timestamping, path diversity, privacy, and leap-second policy rather than treating NTP configuration alone as sufficient.

## Key Characteristics
- Uses independent physical and packet-level measurements to test software-reported timing error.
- Connects sub-millisecond clock precision to ordering, logging, and distributed-database throughput requirements.
- Treats public time delivery as both a reliability and network-path design problem.

## Evidence
- Measurement discipline: [[ntp-service]] compares daemon estimates with oscilloscope, closed-loop 1PPS, and portable GNSS/atomic-clock observations.
- Production scope: [[ntp-service]] traces time from GNSS and an atomic-clock appliance through leap-smearing and scaled serving tiers.
- Public-service design: [[ntp-service]] describes five geographically distinct endpoints, no IP fingerprinting, and path-dependent external measurements.

## Qualifications
The wiki currently represents Obleukhov through one employer-published technical article. It does not independently establish his broader biography, precise role in each implementation decision, later work, or the current state of Facebook's NTP service.

## What Changed
- Established Obleukhov's source-bounded profile around measured production time synchronization.

## Relationships
- [[Facebook]] - employer and operator of the time service in his account.
- [[Chrony]] - daemon whose deployment and measured precision he explains.
- [[NetworkTimeSynchronization]] - primary engineering domain of the article.
- [[HardwareTimestamping]] - mechanism he evaluates with external reference instrumentation.
