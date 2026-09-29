---
title: "Home Assistant"
type: entity
tags: [home-automation, iot, integration]
sources:
  - how-i-turned-a-cheap-weather-station-into-a-personal-devops-dashboard
last_updated: 2026-09-29
knowledge_schema: synthesis-v1
---

## Overview
[[HomeAssistant]] is represented as the integration and entity layer between decoded household sensor messages and downstream storage or dashboards.

## Current Profile
In the weather-station project, Home Assistant OS runs Mosquitto, `rtl_433`, and an MQTT auto-discovery add-on. It receives discovery and observation messages from the broker, exposes weather values as entities, supports friendlier names and icons, derives converted speed and compass-direction entities, displays cards, and forwards events to [[InfluxDB]].

## Key Characteristics
- Hosts add-ons that receive radio data, broker MQTT messages, and publish discovery metadata.
- Represents decoded readings as named entities with units, device classes, icons, and friendly labels.
- Supports template entities for transformations such as km/h to mph and degrees to compass directions.
- Provides immediate home dashboards while forwarding events to a separate system for longer-lived analysis.

## Evidence
- Integration role: [[how-i-turned-a-cheap-weather-station-into-a-personal-devops-dashboard]] places Home Assistant between the RTL-SDR/MQTT acquisition path and InfluxDB storage.
- Entity model: [[how-i-turned-a-cheap-weather-station-into-a-personal-devops-dashboard]] shows discovered battery, wind, temperature, and humidity readings with unit and device attributes.
- Transformation and export: [[how-i-turned-a-cheap-weather-station-into-a-personal-devops-dashboard]] describes template entities plus native InfluxDB event forwarding.

## Qualifications
The source documents one historical Home Assistant OS installation and does not compare deployment modes, test failure recovery, audit access, secure the MQTT path, or establish that every event is delivered exactly once. Add-on availability and configuration can change across versions.

## What Changed
- Established Home Assistant as both the semantic normalization layer and forwarding boundary in a personal weather telemetry stack.

## Relationships
- [[Rtl433]] - produces decoded sensor observations consumed through MQTT and auto-discovery messages.
- [[InfluxDB]] - receives Home Assistant events for historical storage.
- [[Grafana]] - visualizes the resulting retained measurements outside Home Assistant's native cards.
- [[PersonalTelemetryPipeline]] - Home Assistant supplies entity normalization and integration in the demonstrated pipeline.
