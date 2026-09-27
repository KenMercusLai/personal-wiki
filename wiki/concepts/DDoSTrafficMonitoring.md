---
title: "DDoS Traffic Monitoring"
type: concept
tags: [network-monitoring, ddos, observability, incident-response]
sources:
  - fastnetmon-grafana-jian-kong-wang-duan-liu-liang-ji-ddos-yu-jing
last_updated: 2026-09-28
knowledge_schema: synthesis-v1
---

## Definition
[[DDoSTrafficMonitoring]] is the measurement and interpretation of network traffic to identify attack-like volume or rate changes, notify operators, and supply evidence for a separately controlled mitigation action.

## Current Synthesis
The source presents a small pipeline: [[FastNetMon]] observes defined CIDR ranges and evaluates per-host thresholds; a callback records a detection event; Graphite-formatted measurements enter [[InfluxDB]]; and [[Grafana]] shows aggregate direction, packet rate, bandwidth, trends, and top talkers. This separates observation, detection, notification, visualization, and enforcement into distinct stages, even though the article sometimes uses “ban” as shorthand for the detector's internal state.

## Key Claims
- Effective monitoring starts with an explicit scope of protected networks and an understood packet, mirror, or flow input.
- Packet-rate, bandwidth, and flow thresholds capture different attack shapes and require calibration against normal traffic.
- A synthetic load test can verify metric flow, threshold crossing, and callback wiring, but cannot establish production detection quality.
- Time-series dashboards help operators distinguish direction, magnitude, trend, and responsible hosts after or during a threshold event.
- Detection does not itself mitigate traffic; blocking, route announcements, FlowSpec, diversion, or scrubbing require a working and governed enforcement path.

## Evidence
- Scope and inputs: [[fastnetmon-grafana-jian-kong-wang-duan-liu-liang-ji-ddos-yu-jing]] configures monitored CIDRs and enumerates PF_RING, AF_PACKET, NetFlow, sFlow, netmap, and pcap options.
- Detection and notification: [[fastnetmon-grafana-jian-kong-wang-duan-liu-liang-ji-ddos-yu-jing]] reports a deliberately low-threshold UDP test entering FastNetMon's ban list and invoking the notification script.
- Historical analysis: [[fastnetmon-grafana-jian-kong-wang-duan-liu-liang-ji-ddos-yu-jing]] sends hierarchical traffic metrics to InfluxDB and shows them in Grafana.
- Mitigation boundary: [[fastnetmon-grafana-jian-kong-wang-duan-liu-liang-ji-ddos-yu-jing]] discusses BGP while its supplied ExaBGP and FlowSpec options remain disabled and untested.

## Counterevidence & Qualifications
The walkthrough uses one host, one UDP generator, manually reduced thresholds, and no background-traffic baseline, so it does not measure precision, recall, time to detect, or false positives. A five-second dashboard refresh is not equivalent to alert delivery, and successful callback logging is not evidence that an upstream network accepted a route or that attack capacity was absorbed. The versions and commands are historical, and the appended configuration mixes alternatives that should be selected deliberately rather than enabled together without validation.

## What Changed
- Added a staged model separating traffic capture, threshold detection, notification, metric storage, visualization, and mitigation.
- Added synthetic testing as a wiring check with a clear boundary against claims of production effectiveness.
- Clarified that FastNetMon's internal ban state requires an external enforcement integration to change packet handling.

## Related Concepts
- [[TimeSeriesDatabase]] - stores direction- and host-specific traffic measurements across time for later query and visualization.
- [[NetworkAutomation]] - can implement controlled routing or filtering actions after a detection event.
- [[NetworkSegmentation]] - defines protected boundaries and can limit exposure, while traffic monitoring observes behavior across those boundaries.
- [[NetworkLoadBalancing]] - also depends on packet direction, rate, and routing behavior, but targets service distribution rather than attack detection.
