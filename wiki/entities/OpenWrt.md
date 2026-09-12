---
title: "OpenWrt"
type: entity
tags: [networking, routers, linux]
sources:
  - shi-yong-ffmpeg-yuan-cheng-du-qu-rtsp-jian-kong-shi-pin-liu
last_updated: 2026-09-13
knowledge_schema: synthesis-v1
---

## Overview
[[OpenWrt]] is the router operating system shown in the source as the place where [[FRP]] is configured to forward an IP camera's local services.

## Current Profile
The article uses an OpenWrt shell prompt to show `/etc/frpc.ini`. In that configuration, the router bridges a private camera address, `192.168.0.241`, to a remote server by forwarding web and RTSP TCP ports. OpenWrt is not analyzed as a general router platform here; it appears as a practical always-on edge device close to the camera and therefore able to perform [[NATTraversal]] for [[RemoteVideoRecording]].

## Key Characteristics
- Hosts the FRP client configuration.
- Has LAN reachability to the camera's private IP address.
- Forwards camera port `80` and RTSP port `554` to a server.
- Serves as the practical edge device in a self-hosted surveillance setup.

## Evidence
- Configuration host: [[shi-yong-ffmpeg-yuan-cheng-du-qu-rtsp-jian-kong-shi-pin-liu]] shows `root@OpenWrt` reading `/etc/frpc.ini`.
- LAN bridge: [[shi-yong-ffmpeg-yuan-cheng-du-qu-rtsp-jian-kong-shi-pin-liu]] configures `local_ip = 192.168.0.241` for both forwarded services.
- Power and placement: [[shi-yong-ffmpeg-yuan-cheng-du-qu-rtsp-jian-kong-shi-pin-liu]] photos show the router and camera installed together, with the author sharing a power-adapter arrangement.

## Qualifications
This source does not discuss OpenWrt package management, firewall configuration, router security, or whether the same FRP setup is durable under IP changes or service restarts.

## What Changed
- Created the entity page for OpenWrt.

## Relationships
- [[FRP]] - OpenWrt runs the FRP client configuration.
- [[NATTraversal]] - OpenWrt participates in bridging private and remote network paths.
- [[SelfHostedSurveillanceStorage]] - the router-side tunnel supports the storage workflow.
- [[RTSPStreaming]] - OpenWrt forwards the camera's RTSP service.
