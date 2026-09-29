---
title: "NAT Traversal"
type: concept
tags: [networking, remote-access, tunneling]
sources:
  - shi-yong-ffmpeg-yuan-cheng-du-qu-rtsp-jian-kong-shi-pin-liu
  - how-nat-traversal-works
last_updated: 2026-09-29
knowledge_schema: synthesis-v1
---

## Definition
[[NATTraversal]] is the set of direct-connect, mapping, coordination, and relay techniques that let peers communicate across address translation and stateful firewall boundaries.

## Current Synthesis
The evidence now spans two distinct strategies. An [[FRP]] client can initiate a durable tunnel from a private network to a reachable server, which is simple for selected TCP services but turns the public endpoint into an exposure and relay boundary. Direct peer-to-peer traversal instead uses UDP, a shared application socket, a coordination side channel, simultaneous outbound packets, endpoint discovery, and parallel candidate probing. Easy NAT mappings can often support a direct path; endpoint-dependent NAT, blocked UDP, failed CGNAT hairpinning, or path loss require a relay and recovery path.

The robust pattern is therefore not hole punching alone. Start with a working encrypted relay, gather LAN, IPv6, STUN-derived, port-mapped, and operator-provided endpoints, probe them concurrently, upgrade to the best authenticated direct route, send keepalives, and fall back before rediscovery when that route disappears. [[Tailscale]] supplies the source's concrete relay-first implementation, while IPv6 simplifies address reachability without removing stateful-firewall coordination.

## Key Claims
- NAT traversal includes both server-mediated tunnels and direct UDP paths; relay service remains the reliability floor when direct paths fail.
- Direct traversal depends on control of the application socket, coordinated simultaneous transmission, and discovery of candidate endpoints.
- NAT mapping behavior matters more than old cone labels: endpoint-independent mappings are reusable, while endpoint-dependent mappings can invalidate STUN observations.
- Port mapping, IPv6, NAT64 handling, and CGNAT hairpinning add candidates or remove barriers but are conditional rather than universal solutions.
- Candidate racing should select and continuously verify the best working route, with keepalive, downgrade, and rediscovery behavior.
- Dynamic paths require end-to-end authentication and encryption; reachability mechanisms do not establish application trust.

## Evidence
- Relay and tunnel patterns: [[shi-yong-ffmpeg-yuan-cheng-du-qu-rtsp-jian-kong-shi-pin-liu]] maps a camera's private ports `80` and `554` through FRP, while [[how-nat-traversal-works]] uses DERP or TURN-like relays when direct traversal fails.
- Firewall traversal: [[how-nat-traversal-works]] explains that matching outbound UDP state permits return traffic and that coordinated peers can open opposing stateful firewalls.
- Endpoint discovery and mapping: [[how-nat-traversal-works]] covers STUN, endpoint-independent versus endpoint-dependent mapping, UPnP IGD, NAT-PMP, PCP, CGNAT hairpinning, and NAT64/DNS64.
- Path selection and recovery: [[how-nat-traversal-works]] gathers multiple candidates, probes them concurrently, upgrades from relay to a better path, and falls back after failure.
- Exposure boundary: [[shi-yong-ffmpeg-yuan-cheng-du-qu-rtsp-jian-kong-shi-pin-liu]] exposes camera services through public server ports, while [[how-nat-traversal-works]] requires upper-layer end-to-end authentication and encryption across changing paths.

## Counterevidence & Qualifications
The Tailscale source is a first-party 2020 technical explanation rather than a representative device survey; its connectivity estimate, IPv6 snapshot, relay preference, and implementation details are historical and source-scoped. Direct traversal cannot defeat networks that block outbound UDP, and birthday-style probing can resemble a port scan or exhaust NAT session tables. The FRP source proves a small TCP tunnel works but does not cover authentication, TLS, firewall scoping, or whether exposing camera web and RTSP ports is acceptable.

## What Changed
- Expanded the judgment from one FRP tunnel to a layered direct-connect, relay, candidate-selection, and recovery model.
- Added NAT behavior, CGNAT/NAT64, and end-to-end security as explicit traversal boundaries.

## Related Concepts
- [[RTSPStreaming]] - the RTSP service is the tunneled workload.
- [[RemoteVideoRecording]] - NAT traversal lets a remote server record a private camera.
- [[RemoteAdministrationExposure]] - newly reachable private services become exposure surfaces.
- [[QUIC]] - supplies stream semantics above UDP while retaining a traversal-friendly transport substrate.
- [[SystemReliability]] - relay-first startup, health probes, fallback, and rediscovery treat path loss as recoverable state.
