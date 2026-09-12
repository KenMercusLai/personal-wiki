---
title: "Xiongmai"
type: entity
tags: [surveillance, camera-vendor, configuration]
sources:
  - shi-yong-ffmpeg-yuan-cheng-du-qu-rtsp-jian-kong-shi-pin-liu
last_updated: 2026-09-13
knowledge_schema: synthesis-v1
---

## Overview
[[Xiongmai]] is the camera-vendor ecosystem referenced by the source's VMS configuration tool and visible as vendor `XM` in the screenshots.

## Current Profile
The author asks the seller how to configure the camera and is directed to search for Xiongmai and download the supporting software. The VMS screenshots show a device at `192.168.0.241` with vendor `XM`, management port `8080`, HTTP port `80`, ONVIF port `8899`, and RTSP enabled on port `554`. The camera packaging identifies the unit as a Smart265 EXIR infrared network camera supporting H.265, H.264, and JPEG, with IP67 weather resistance and a dome-like infrared layout.

## Key Characteristics
- Provides the VMS software path used to discover and configure the camera.
- Appears in the screenshots as vendor `XM`.
- Exposes network settings for static IP, gateway, DNS, management, HTTP, ONVIF, and RTSP ports.
- Supports RTSP access through a vendor-specific URL template.
- The hardware shown supports H.265/H.264/JPEG and infrared surveillance use.

## Evidence
- Software setup: [[shi-yong-ffmpeg-yuan-cheng-du-qu-rtsp-jian-kong-shi-pin-liu]] says the seller told the author to search Xiongmai and download the matching configuration software.
- Device discovery: [[shi-yong-ffmpeg-yuan-cheng-du-qu-rtsp-jian-kong-shi-pin-liu]] screenshots show the camera as `192.168.0.241`, vendor `XM`, and group `默认组`.
- Port configuration: [[shi-yong-ffmpeg-yuan-cheng-du-qu-rtsp-jian-kong-shi-pin-liu]] screenshots show TCP `8080`, HTTP `80`, ONVIF `8899`, and enabled RTSP `554`.
- Hardware evidence: [[shi-yong-ffmpeg-yuan-cheng-du-qu-rtsp-jian-kong-shi-pin-liu]] photos show Smart265 EXIR infrared network camera packaging and mounted installation.

## Qualifications
The source does not independently verify manufacturer identity beyond seller guidance, the Xiongmai download page, and the VMS screenshots. It is a practical setup account, not a vendor audit.

## What Changed
- Created the entity page for Xiongmai.

## Relationships
- [[RTSPStreaming]] - Xiongmai/XM camera settings expose the RTSP service.
- [[RemoteVideoRecording]] - the configured camera becomes the remote recording source.
- [[SelfHostedSurveillanceStorage]] - the camera is selected partly because it can be used without vendor cloud storage.
