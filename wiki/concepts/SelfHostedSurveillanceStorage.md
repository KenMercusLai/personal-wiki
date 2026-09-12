---
title: "Self-Hosted Surveillance Storage"
type: concept
tags: [surveillance, data-ownership, infrastructure]
sources:
  - shi-yong-ffmpeg-yuan-cheng-du-qu-rtsp-jian-kong-shi-pin-liu
last_updated: 2026-09-13
knowledge_schema: synthesis-v1
---

## Definition
[[SelfHostedSurveillanceStorage]] is the storage pattern of keeping camera footage on infrastructure controlled by the user rather than in a vendor cloud or bundled recorder.

## Current Synthesis
The source's hardware and networking decisions are guided by storage ownership. The author rejects consumer WiFi cameras that require paid cloud storage, avoids analog cameras because they require a separate recorder, and does not choose PoE because of extra equipment cost. The eventual design uses a directly reachable network camera, [[FRP]] tunneling, and [[FFmpeg]] recording so the video lands on the author's server.

## Key Claims
- Storage ownership can dominate surveillance hardware selection.
- Vendor cloud services may be cheap upfront but constrain where footage can be stored.
- A network camera with direct RTSP access can reduce dependence on proprietary camera ecosystems.
- Self-hosting shifts operational burden to the user: networking, scheduling, security, storage, and monitoring must be handled outside the vendor package.
- Low-cost surveillance setups trade polish and integration for control.

## Evidence
- Motivation: [[shi-yong-ffmpeg-yuan-cheng-du-qu-rtsp-jian-kong-shi-pin-liu]] says the author wants camera footage saved to their own server rather than handed to domestic vendors.
- Hardware filter: [[shi-yong-ffmpeg-yuan-cheng-du-qu-rtsp-jian-kong-shi-pin-liu]] rejects cloud-dependent WiFi cameras, analog camera/NVR setups, and PoE equipment for cost or storage-control reasons.
- Implemented path: [[shi-yong-ffmpeg-yuan-cheng-du-qu-rtsp-jian-kong-shi-pin-liu]] combines a network camera, FRP, RTSP, FFmpeg, and cron.

## Counterevidence & Qualifications
The source is motivated by personal control but does not supply a full security, privacy, retention, or legal framework for operating surveillance footage. Self-hosting can reduce vendor dependence while increasing responsibility for exposed services and stored sensitive video.

## What Changed
- Created the concept page for self-hosted surveillance storage.

## Related Concepts
- [[RemoteVideoRecording]] - remote recording is the operational method used to store footage on the server.
- [[RTSPStreaming]] - direct stream access is what makes vendor-independent recording possible.
- [[NATTraversal]] - a tunnel is used to bridge the camera to the recording host.
- [[RemoteAdministrationExposure]] - camera and management ports become sensitive exposure surfaces.
- [[InternetOfThingsData]] - surveillance video is a sensor data stream whose value depends on capture and storage architecture.
