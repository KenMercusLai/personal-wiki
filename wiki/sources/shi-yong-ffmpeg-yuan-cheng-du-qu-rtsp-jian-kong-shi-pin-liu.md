---
title: "使用 FFmpeg 远程读取 rtsp 监控视频流"
type: source
tags: [ffmpeg, rtsp, surveillance, networking]
date: 2019-09-09
source_file: /mnt/ken_personal_wiki/Articles/使用 FFmpeg 远程读取 rtsp 监控视频流.md
---

## Summary
This Chinese technical diary explains how the author avoided vendor cloud storage for an IP surveillance camera by exposing the camera's RTSP service through [[FRP]] and recording clips on a remote server with [[FFmpeg]]. The source combines hardware selection, [[OpenWrt]] tunnel configuration, vendor VMS camera setup, RTSP URL discovery, and cron-based one-minute recording into a compact [[SelfHostedSurveillanceStorage]] workflow.

## Key Claims
- [[SelfHostedSurveillanceStorage]] is the source's practical motivation: the author wants surveillance footage saved to a personally controlled server instead of paying for vendor cloud storage.
- A wired network camera with direct browser/VMS access is preferred over consumer WiFi cameras, analog cameras, and PoE kits when the goal is low-cost remote recording without a proprietary recorder.
- [[RTSPStreaming]] can be reached through [[FRP]] by forwarding the camera's internal RTSP port `554` from an [[OpenWrt]] router to a remote server.
- The camera's vendor software identifies an [[Xiongmai]]/XM device at `192.168.0.241`, with management port `8080`, HTTP port `80`, ONVIF port `8899`, and RTSP enabled on `554`.
- [[FFmpeg]] can copy the H.264 RTSP stream into MP4 segments with `-rtsp_transport tcp`, `-vcodec copy`, `-r`, `-t`, and timestamped output filenames.
- Cron can approximate continuous remote recording by running a one-minute FFmpeg capture every minute, but this reconnects to the RTSP stream for every clip.
- The article closes by situating [[FFmpeg]] in [[FabriceBellard]]'s broader body of systems work and in open-source licensing disputes around commercial media players.

## Key Quotes
> "我需要的是将监控视频远程保存到服务器上，保存到自己的服务器上" - on why local/vendor cloud storage was rejected.

> "将摄像头 rtsp 协议的端口 554 内网穿透到服务器上" - on the FRP tunneling target.

> "选择每一分钟录制一分钟的是视频" - on the cron-based recording strategy and its reconnect cost.

## Connections
- [[FFmpeg]] - command-line tool used to ingest the RTSP stream and write MP4 clips.
- [[FRP]] - TCP tunnel used to expose the camera's internal RTSP and web ports to a server.
- [[OpenWrt]] - router environment where `frpc.ini` forwards the camera's local ports.
- [[Xiongmai]] - vendor ecosystem behind the VMS tool and XM camera configuration shown in screenshots.
- [[FabriceBellard]] - developer credited for FFmpeg and adjacent systems projects.
- [[RTSPStreaming]] - protocol-level path used by PotPlayer, VLC, and FFmpeg to read the camera stream.
- [[RemoteVideoRecording]] - operational workflow of recording remote RTSP footage into periodic clips.
- [[SelfHostedSurveillanceStorage]] - ownership motivation behind avoiding vendor cloud recording.
- [[NATTraversal]] - networking pattern represented by FRP forwarding from a private camera address to a public server.
- [[RemoteAdministrationExposure]] - security-adjacent concern implied by exposing camera web/RTSP ports outside the LAN.

## Contradictions
- No direct contradictions with existing wiki content were found. The source adds a practical small-network video-streaming case to the wiki's networking and infrastructure material.
