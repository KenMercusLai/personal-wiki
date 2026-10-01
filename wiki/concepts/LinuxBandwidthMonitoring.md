---
title: "Linux Bandwidth Monitoring"
type: concept
tags: [linux, networking, observability, bandwidth]
sources:
  - monitor-internet-bandwidth-usage-on-linux-baeldung-on-linux
last_updated: 2026-10-01
knowledge_schema: synthesis-v1
---

## Definition
[[LinuxBandwidthMonitoring]] is the measurement, retention, aggregation, and interpretation of received and transmitted traffic on Linux network interfaces for quota control, capacity awareness, troubleshooting, or alerting.

## Current Synthesis
The source contrasts two layers of measurement. `vnstat` runs a daemon that turns interface counters into persistent hourly, daily, monthly, and yearly history, exposes RX, TX, total, rate, and estimates through its CLI, and can render images or signal threshold crossings. `/proc/net/dev` exposes the lower-level cumulative counters directly without extra software, but those values belong to an interface lifecycle and can reset on reboot or interface recreation.

The practical monitoring problem is therefore not just reading a byte count. Operators must choose the interface and traffic direction that match the question, preserve timestamps and counter continuity, distinguish totals from rates and forecasts, and reconcile host-visible traffic with any provider billing boundary. Periodic subtraction is valid only within a continuous counter epoch; a maintained collector is preferable when durable period totals and automated quota alerts matter.

## Key Claims
- Persistent accounting requires a collector or reset-aware snapshot history; a current kernel counter alone cannot reconstruct an earlier period.
- Interface and direction selection are semantic choices because host-visible RX, TX, and total may not match a provider's charging rule or the intended internet path.
- Cumulative counters, interval deltas, average rates, and forecasts answer different operational questions and should not be treated as interchangeable.
- Threshold checks become operationally useful when their exit status is connected to a scheduled and observable response.
- Visual summaries can combine long-window totals with recent rate shape, but they do not explain the traffic's applications, destinations, or billing treatment.

## Evidence
- Persistent history: [[monitor-internet-bandwidth-usage-on-linux-baeldung-on-linux]] enables the `vnstat` daemon and demonstrates monthly, daily, and estimated per-interface traffic.
- Raw counters: [[monitor-internet-bandwidth-usage-on-linux-baeldung-on-linux]] reads RX bytes from column 2 and TX bytes from column 10 of `/proc/net/dev`, while noting that values reset at boot.
- Alert automation: [[monitor-internet-bandwidth-usage-on-linux-baeldung-on-linux]] uses `vnstat --alert` with interval, direction, limit, and unit arguments in a scheduled shell-script pattern.
- Visual interpretation: [[monitor-internet-bandwidth-usage-on-linux-baeldung-on-linux]] retains one inspected monthly report and one vertical summary with daily, monthly, all-time, and hourly-rate information.

## Counterevidence & Qualifications
The source demonstrates commands on one 2022-era system rather than validating current behavior across distributions or `vnstat` versions. Its CSV subtraction works only while counters remain monotonic; reboot, interface recreation, wrap, namespace changes, or missed samples require explicit handling. Host interface totals may include local, virtual, retransmitted, encapsulated, or otherwise non-billable traffic and may omit traffic observed at another gateway. Neither method provides per-process attribution, packet contents, destination analysis, or proof that an alert was delivered and acted upon.

## What Changed
- Created a reset-aware distinction between persistent accounting and direct cumulative interface counters.
- Separated totals, interval deltas, rates, forecasts, and provider-billing measurements.
- Added interface and direction choice as part of the monitoring question rather than a command-only detail.

## Related Concepts
- [[DDoSTrafficMonitoring]] - uses traffic rates and thresholds for attack detection rather than ordinary quota and usage accounting.
- [[TimeSeriesDatabase]] - generalizes timestamped retention, windowing, aggregation, and interpretation of monitored measurements.
- [[NetworkAutomation]] - connects scheduled collection or threshold outcomes to repeatable operational responses.
- [[NetworkSegmentation]] - defines traffic boundaries whose interfaces and paths affect what a host-level counter represents.
