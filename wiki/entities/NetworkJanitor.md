---
title: "Network Janitor"
type: entity
tags: [networking, infrastructure, author]
sources:
  - network-janitor-on-the-premature-death-of-spanning-tree-and-the-indiscriminate-killing-of-canaries
last_updated: 2026-10-01
knowledge_schema: synthesis-v1
---

## Overview
[[NetworkJanitor]] is the pseudonymous networking practitioner who wrote the 2012 article “On the Premature Death of Spanning Tree and the Indiscriminate Killing of Canaries.”

## Current Profile
The source presents Network Janitor as an experienced designer and operator of enterprise or data-center Layer 2 networks. The author favors deliberate [[SpanningTreeProtocol|STP]] design, including MSTP where its planning cost avoids instance limits, and evaluates new fabric architectures by whether their failure detection and containment cover both core and edge behavior.

The article also draws on a firsthand incident in which a virtual machine bridged vNICs in separate VLANs and BPDU Guard disabled the attached host port. That anecdote supports the author's operational caution but does not establish a broader deployment study or identify the network, products, versions, or configuration.

## Key Characteristics
- Writes from a network-design and operations perspective.
- Prefers explicit failure analysis over categorical claims that a protocol is obsolete.
- Treats detection and containment mechanisms as part of architecture, not optional operational add-ons.
- Supports MSTP when its up-front planning avoids later per-VLAN scaling problems.
- Uses a firsthand virtualization-loop incident to argue for preserving edge-loop warning signals.

## Evidence
- Design position: [[network-janitor-on-the-premature-death-of-spanning-tree-and-the-indiscriminate-killing-of-canaries]] argues for planned MSTP use and describes rebuilding networks that exceeded STP-instance limits.
- Fabric boundary: [[network-janitor-on-the-premature-death-of-spanning-tree-and-the-indiscriminate-killing-of-canaries]] accepts disabling STP on fabric-core interfaces but rejects extending that conclusion automatically to edge ports.
- Incident experience: [[network-janitor-on-the-premature-death-of-spanning-tree-and-the-indiscriminate-killing-of-canaries]] recounts BPDU Guard containing a loop caused by a guest bridging VLAN-connected vNICs.

## Qualifications
This profile comes from one polemical 2012 article and the author name appears pseudonymous. The source provides no verified biography, employer, certification history, topology diagrams, device configurations, incident records, or comparative outcome data.

## What Changed
- Created the profile from the author's STP, fabric-boundary, and edge-loop argument.

## Relationships
- [[SpanningTreeProtocol]] - protocol the author argues should be scoped and configured rather than declared universally dead.
- [[DataCenterNetworkFabric]] - architectural context in which the author accepts removing STP from core links.
- [[EdgeNetworkLoopProtection]] - operational discipline illustrated through BPDU Guard and alternative loop signals.
- [[VMware]] - virtualization context named in the author's loop anecdote and vendor-guidance criticism.
