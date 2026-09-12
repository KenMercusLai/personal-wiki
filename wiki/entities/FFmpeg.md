---
title: "FFmpeg"
type: entity
tags: [media, open-source, command-line]
sources:
  - shi-yong-ffmpeg-yuan-cheng-du-qu-rtsp-jian-kong-shi-pin-liu
last_updated: 2026-09-13
knowledge_schema: synthesis-v1
---

## Overview
[[FFmpeg]] is an open-source cross-platform audio and video toolkit used in this source as a command-line recorder for [[RTSPStreaming]] camera footage.

## Current Profile
The source treats FFmpeg as the practical bridge between a network camera and server-side archival storage. After [[FRP]] forwards the camera's RTSP port to a server, FFmpeg reads the RTSP URL over TCP and writes timestamped MP4 clips without re-encoding the H.264 video. The article also frames FFmpeg as part of [[FabriceBellard]]'s larger systems-programming output and as a project whose license obligations affected commercial media-player vendors.

## Key Characteristics
- Reads RTSP network streams from IP cameras.
- Can force RTSP over TCP for more predictable remote capture.
- Can copy H.264 video into MP4 segments without transcoding.
- Supports scriptable parameters for duration, frame rate, overwrite behavior, and timestamped filenames.
- Fits cron-based recurring recording because it is command-line friendly.
- Carries open-source license obligations that downstream commercial users may violate.

## Evidence
- RTSP ingest: [[shi-yong-ffmpeg-yuan-cheng-du-qu-rtsp-jian-kong-shi-pin-liu]] installs FFmpeg on the server and reads the camera's forwarded RTSP URL.
- TCP transport and copy mode: [[shi-yong-ffmpeg-yuan-cheng-du-qu-rtsp-jian-kong-shi-pin-liu]] uses `-rtsp_transport tcp` and `-vcodec copy` to capture the stream.
- Segment recording: [[shi-yong-ffmpeg-yuan-cheng-du-qu-rtsp-jian-kong-shi-pin-liu]] runs a one-minute command from cron and writes filenames generated from the current date.
- Project context: [[shi-yong-ffmpeg-yuan-cheng-du-qu-rtsp-jian-kong-shi-pin-liu]] credits [[FabriceBellard]] with creating FFmpeg and quotes a discussion of LGPL/GPL license compliance conflicts.

## Qualifications
The source shows one 2019 Ubuntu 18.04-era FFmpeg command and one camera stream. It does not compare modern FFmpeg options, streaming protocols, security settings, retention policies, or long-running recorder architectures.

## What Changed
- Created the entity page for FFmpeg.

## Relationships
- [[FabriceBellard]] - Bellard is credited in the source as FFmpeg's creator.
- [[RTSPStreaming]] - FFmpeg reads the camera stream over RTSP.
- [[RemoteVideoRecording]] - FFmpeg performs the server-side recording step.
- [[SelfHostedSurveillanceStorage]] - FFmpeg enables the author's vendor-independent storage workflow.
