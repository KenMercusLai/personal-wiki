---
title: "FastNetMon"
type: entity
tags: [network-monitoring, ddos, traffic-analysis]
sources:
  - fastnetmon-grafana-jian-kong-wang-duan-liu-liang-ji-ddos-yu-jing
last_updated: 2026-09-28
knowledge_schema: synthesis-v1
---

## Overview
[[FastNetMon]] is represented as a network-traffic analyzer that detects per-host threshold crossings and can trigger notification or routing actions.

## Current Profile
The source configures FastNetMon on CentOS 7 to monitor CIDR ranges, ingest mirrored packets or flow telemetry, calculate traffic rates, and evaluate packet-per-second, bandwidth, and flow thresholds. A simulated UDP load shows its detection and callback path, while Graphite export connects its measurements to [[InfluxDB]] and [[Grafana]].

## Key Characteristics
- Monitors configured networks and reports inbound, outbound, internal, and other traffic by host.
- Supports multiple traffic inputs, including PF_RING, AF_PACKET, NetFlow, sFlow, netmap, and pcap, with different performance and deployment tradeoffs.
- Evaluates packet-rate, bandwidth, and optional flow thresholds to place a target in its internal ban state.
- Calls an external script for ban, unban, and attack-detail events, making enforcement dependent on the integration behind that callback.
- Exports metric hierarchies through Graphite and exposes optional BGP, FlowSpec, Redis, MongoDB, and API integrations in the historical configuration.

## Evidence
- Detection path: [[fastnetmon-grafana-jian-kong-wang-duan-liu-liang-ji-ddos-yu-jing]] reports an `iperf` UDP test exceeding lowered thresholds and appearing in the client ban list.
- Callback path: [[fastnetmon-grafana-jian-kong-wang-duan-liu-liang-ji-ddos-yu-jing]] records a generated ban message after the configured notification script ran.
- Telemetry path: [[fastnetmon-grafana-jian-kong-wang-duan-liu-liang-ji-ddos-yu-jing]] configures Graphite output to InfluxDB and shows the resulting Grafana dashboard.
- Extension surface: [[fastnetmon-grafana-jian-kong-wang-duan-liu-liang-ji-ddos-yu-jing]] includes disabled ExaBGP, FlowSpec, GoBGP, Redis, MongoDB, and API options in its sample configuration.

## Qualifications
The evidence is a 2019 practitioner walkthrough using historical software versions and one synthetic UDP load test. It verifies threshold detection and script invocation, not detection accuracy under diverse attacks, false-positive behavior, sustained throughput, packet blocking, route propagation, scrubbing capacity, or production recovery.

## What Changed
- Established FastNetMon as the detection and metric-emission component in a small DDoS monitoring stack.
- Distinguished its internal ban decision from enforcement performed by an external callback or routing integration.

## Relationships
- [[DDoSTrafficMonitoring]] - FastNetMon supplies traffic measurement, threshold evaluation, and response hooks.
- [[InfluxDB]] - receives FastNetMon's Graphite-formatted time-series metrics in the demonstrated stack.
- [[Grafana]] - visualizes FastNetMon-derived traffic rates and top talkers.
- [[TimeSeriesDatabase]] - provides the storage model used for historical traffic measurements.
