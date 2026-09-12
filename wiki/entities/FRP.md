---
title: "FRP"
type: entity
tags: [networking, tunneling, remote-access]
sources:
  - shi-yong-ffmpeg-yuan-cheng-du-qu-rtsp-jian-kong-shi-pin-liu
last_updated: 2026-09-13
knowledge_schema: synthesis-v1
---

## Overview
[[FRP]] is the tunneling tool used in the source to forward a private IP camera's local web and RTSP ports from an [[OpenWrt]] router to a remote server.

## Current Profile
In the article, FRP makes a camera at `192.168.0.241` reachable from outside the local network. The router-side `frpc.ini` defines TCP forwards for the camera's web interface and RTSP service: local port `80` becomes remote port `2418`, and local port `554` becomes remote port `554`. This makes [[RTSPStreaming]] available to tools such as PotPlayer, VLC, and [[FFmpeg]] on the server side.

## Key Characteristics
- Runs on the router as an FRP client configuration.
- Forwards TCP services from a private LAN device to a remote server.
- Maps the camera web interface separately from the RTSP media stream.
- Acts as a [[NATTraversal]] mechanism for devices without direct public reachability.
- Enables remote recording while keeping the camera itself on a private address.

## Evidence
- Router configuration: [[shi-yong-ffmpeg-yuan-cheng-du-qu-rtsp-jian-kong-shi-pin-liu]] shows `/etc/frpc.ini` with `monweb` and `monrtsp` TCP forwards.
- RTSP access path: [[shi-yong-ffmpeg-yuan-cheng-du-qu-rtsp-jian-kong-shi-pin-liu]] says forwarding local port `554` allows the server to read the RTSP stream.
- Web access path: [[shi-yong-ffmpeg-yuan-cheng-du-qu-rtsp-jian-kong-shi-pin-liu]] maps the camera's local web port `80` to remote port `2418`.

## Qualifications
The source focuses on reachability, not hardening. It does not describe authentication strength, firewall rules, TLS, access control, or retention policies for the exposed ports.

## What Changed
- Created the entity page for FRP.

## Relationships
- [[OpenWrt]] - FRP runs from the OpenWrt router in the source.
- [[NATTraversal]] - FRP provides the tunnel across the LAN/public boundary.
- [[RTSPStreaming]] - FRP exposes the camera's RTSP service.
- [[RemoteAdministrationExposure]] - forwarding camera services creates a management and media exposure surface that must be secured.
