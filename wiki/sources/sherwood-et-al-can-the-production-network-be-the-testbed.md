---
title: "Can the Production Network Be the Testbed?"
type: source
tags: [networking, sdn, openflow, network-slicing, testbed]
date: 2010-10-06
source_file: "/mnt/ken_personal_wiki/Articles/Sherwood et al - Can the Production Network Be the Testbed.md"
---

## Summary
Sherwood and colleagues present [[FlowVisor]], a transparent proxy that partitions [[OpenFlow]] production hardware into isolated control domains so experimental and legacy traffic can share real switches, links, users, and line-rate forwarding. The design turns [[NetworkSlicing]] into a policy over topology, bandwidth, device CPU, forwarding-table capacity, and flowspace, with control-message filtering and rewriting enforcing each slice's authority. Their deployment and measurements support [[ProductionNetworkExperimentation]] as a promising bridge between isolated testbeds and operational networks, while switch-CPU isolation, incomplete hardware abstractions, control-path latency, and limited topology and packet-processing flexibility remain material constraints.

## Key Claims
- A testbed embedded in deployed hardware can inherit production scale, topology, traffic, users, and line-rate forwarding without requiring a parallel hardware network.
- FlowVisor interposes between OpenFlow switches and multiple controllers, presenting each controller with a transparent but policy-bounded view of the shared data plane.
- A usable network slice must isolate topology, link bandwidth, switch CPU, and finite forwarding-table entries rather than only separate traffic with VLANs.
- Flowspace rules let users opt selected traffic into an experiment, while message inspection, intersection, rewriting, rejection, quotas, queues, and rate limits constrain each controller to its allocation.
- The prototype added no steady-state data-plane overhead, but measured about 16 ms average overhead for new-flow messages and 0.48 ms for port-status responses.
- In the reported bandwidth test, an unfriendly constant-bit-rate slice reduced competing TCP traffic to 1.2% without isolation; 30/70 minimum reservations produced 28.5% and 64.2% shares respectively.
- A Stanford production deployment and six additional campus test deployments showed practical coexistence, but unexpected legacy-device behavior and switch-CPU exhaustion were the most important operational hazards.

## Key Quotes
> "the problem with testbeds is that they are testbeds" - on the realism and transfer gap created by separate experimental infrastructure.

> "FlowVisor appears as a switch (or a network of switches); from a switch's perspective, FlowVisor appears as a controller" - on the proxy's bidirectional transparency.

## Connections
- [[FlowVisor]] - prototype that partitions OpenFlow control and shared forwarding resources among production and experimental slices.
- [[OpenFlow]] - control/data-plane protocol and hardware abstraction used by the implementation.
- [[NetworkSlicing]] - resource and authority partitioning model spanning flowspace, topology, bandwidth, CPU, and forwarding entries.
- [[ProductionNetworkExperimentation]] - proposal to validate new network behavior with real users and equipment inside bounded production slices.
- [[NetworkResilienceTradeoffs]] - isolation gains depend on additional policy, proxy, control-path, and hardware failure surfaces.

## Contradictions
- The paper's own deployment was explicitly not bullet-proof: switch CPU was the most constrained resource, slow-path rules could drive utilization to 100%, and per-message costs varied by hardware and OpenFlow implementation.
- Transparency and line-rate forwarding do not imply zero overhead: FlowVisor remains on the control path, performs linear flowspace matching in the prototype, and added measurable new-flow setup latency.
- Minimum-bandwidth queues do not impose maximum shares, and the reported 64.2% TCP result fell below the nominal 70% reservation; the experiment supports substantial isolation rather than perfect allocation.
- The reported campus deployment, synthetic workloads, and selected experiments do not establish safety across arbitrary production networks, controllers, hardware, traffic mixes, adversaries, or failure combinations.
- OpenFlow's lowest-common-denominator abstraction excluded many hardware capabilities, arbitrary per-packet computation, and some virtual-topology constructions, limiting which experiments could use the production hardware directly.
- The supplied Markdown contains no effective image references, so no visual assets or manifest were required.
