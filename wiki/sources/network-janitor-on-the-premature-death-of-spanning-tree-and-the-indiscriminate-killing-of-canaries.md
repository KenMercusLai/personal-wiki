---
title: "On the Premature Death of Spanning Tree and the Indiscriminate Killing of Canaries"
type: source
tags: [networking, spanning-tree, data-center, loop-prevention]
date: 2012-12-06
source_file: "/mnt/ken_personal_wiki/Articles/Network Janitor - On the Premature Death of Spanning Tree and the Indiscriminate Killing of Canaries.md"
---

## Summary
[[NetworkJanitor]] argues that [[DataCenterNetworkFabric|data-center fabrics]] can legitimately remove [[SpanningTreeProtocol|Spanning Tree Protocol]] from fabric-core links without making it safe to disable STP indiscriminately at the edge. End stations, VoIP phones, users, and virtual machines can still bridge ports or VLANs, so edge networks need explicit detection and containment controls. The article treats BPDU Guard as an early-warning “canary” and presents storm control, MAC-address limits, MAC-flap dampening, and CPU monitoring as partial alternatives rather than complete substitutes.

## Key Claims
- Fabric architectures can provide multipath Layer 2 forwarding and justify disabling STP on core-facing links, but that architectural boundary does not remove edge-loop risk.
- Many historical STP failures reflect weak design or configuration; MSTP requires more planning but can avoid per-VLAN instance limits and later redesign.
- BPDU Guard can detect an unexpected BPDU on an access port, report the condition, and disable the port before a bridging loop persists.
- BPDU Filter suppresses the signal that BPDU Guard needs, so using it on a port attached to a system capable of bridging networks can hide a loop rather than make the topology safe.
- A virtual machine bridging vNICs on different VLANs can carry a BPDU across a host and create an external Layer 2 loop; the author's VMware incident was contained when BPDU Guard disabled the host port.
- Networks that retire STP must replace its edge-loop detection and mitigation functions deliberately, potentially using storm control, MAC-count limits, MAC-flap dampening, and high-CPU alerts.

## Key Quotes
> “calling it dead today is premature” — on claims that fabric networking had already made STP obsolete.

> “ask yourself how you will detect loops in the edge networks and how you will mitigate them” — the operational test proposed before disabling STP.

## Connections
- [[NetworkJanitor]] - pseudonymous author presenting the argument and a firsthand virtualized-loop incident.
- [[SpanningTreeProtocol]] - loop-prevention protocol whose scope, configuration, and premature retirement are the article's central concern.
- [[DataCenterNetworkFabric]] - architecture that can remove STP from core-facing links without eliminating edge hazards.
- [[EdgeNetworkLoopProtection]] - layered detection and containment controls needed wherever accidental bridging remains possible.
- [[VMware]] - virtualization context for the author's anecdote about a guest bridging vNICs across VLANs and for an attributed BPDU Filter recommendation.

## Contradictions
- The article contradicts blanket claims that fabric adoption makes STP unnecessary everywhere, while agreeing that STP may be unnecessary inside a correctly bounded fabric core.
- The VMware guidance and incident are reported from one practitioner's experience without configuration records, vendor documentation, dates, product versions, or an independent account; they should not be generalized to every VMware deployment.
- BPDU Guard can contain an offending port but may also disconnect every workload behind a host, while the listed non-STP signals are indirect and can produce false positives or react only after traffic or control-plane impact begins.
- The sole embedded image is a decorative canary photograph. It was inspected and omitted because it adds no technical evidence.
