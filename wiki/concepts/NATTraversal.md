---
title: "NAT Traversal"
type: concept
tags: [networking, remote-access, tunneling]
sources:
  - shi-yong-ffmpeg-yuan-cheng-du-qu-rtsp-jian-kong-shi-pin-liu
last_updated: 2026-09-13
knowledge_schema: synthesis-v1
---

## Definition
[[NATTraversal]] is the set of techniques that let a service on a private network become reachable from another network despite address translation or firewall boundaries.

## Current Synthesis
This source shows NAT traversal through a concrete FRP tunnel. The IP camera remains on a private LAN address, `192.168.0.241`, while [[OpenWrt]] runs `frpc` rules that connect to a remote server and expose selected local TCP ports. The pattern is useful because the camera does not need a public IP address, but the article also implies the usual tradeoff: forwarding service ports makes private-device interfaces newly reachable and therefore security-sensitive.

## Key Claims
- NAT traversal can be implemented by a client on the private network initiating a tunnel to a reachable server.
- Port-level forwarding is enough for simple services such as camera web access and RTSP streaming.
- The tunnel decouples the private device address from the remote endpoint used by clients.
- Tunneling improves reachability but does not by itself solve authentication, authorization, encryption, or exposure risk.

## Evidence
- Private address: [[shi-yong-ffmpeg-yuan-cheng-du-qu-rtsp-jian-kong-shi-pin-liu]] configures `local_ip = 192.168.0.241` for the camera.
- Forwarded services: [[shi-yong-ffmpeg-yuan-cheng-du-qu-rtsp-jian-kong-shi-pin-liu]] maps local ports `80` and `554` to remote ports `2418` and `554`.
- Use case: [[shi-yong-ffmpeg-yuan-cheng-du-qu-rtsp-jian-kong-shi-pin-liu]] reads the forwarded RTSP stream from the server with FFmpeg.

## Counterevidence & Qualifications
The source presents FRP as a working tunnel, not a general taxonomy of NAT traversal. It does not discuss hole punching, relay tradeoffs, TLS, firewall scoping, credential rotation, or whether public port `554` should be exposed directly.

## What Changed
- Created the concept page for NAT traversal.

## Related Concepts
- [[RTSPStreaming]] - the RTSP service is the tunneled workload.
- [[RemoteVideoRecording]] - NAT traversal lets a remote server record a private camera.
- [[RemoteAdministrationExposure]] - newly reachable private services become exposure surfaces.
- [[NetworkLoadBalancing]] - both concern packet/service reachability, but NAT traversal focuses on crossing private/public boundaries rather than distributing traffic.
