---
title: "Imgix"
type: entity
tags: [company, image-processing, distributed-systems]
sources:
  - health-checks-and-graceful-degradation-in-distributed-systems
last_updated: 2026-09-29
knowledge_schema: synthesis-v1
---

## Overview
[[Imgix]] is the real-time image-processing company used as the setting for a historical adaptive load-management case.

## Current Profile
The source describes Imgix as accepting image-transformation requests through a URL API, fetching and caching originals, performing work such as cropping, resizing, PDF processing, and GIF rendering, and serving results through a CDN. Highly variable request cost and non-asynchronous GPU transformation made fixed admission assumptions unsafe, so the internal Spillway layer coordinated workers and bounded overload.

## Key Characteristics
- Provided real-time image fetching and transformation behind a URL API.
- Served transformed output through a content-delivery layer.
- Handled request costs ranging from ordinary images to long PDFs and multi-frame GIFs.
- Used an internal broker and worker pool to adapt admission and routing to current load.

## Evidence
- Product and stack: [[health-checks-and-graceful-degradation-in-distributed-systems]] describes origin fetching, origin caching, image processing, load distribution, and content delivery.
- Workload variability: [[health-checks-and-graceful-degradation-in-distributed-systems]] identifies PDFs, GIFs, and ordinary images as materially different transformation workloads.
- Adaptive operation: [[health-checks-and-graceful-degradation-in-distributed-systems]] describes workers refusing work based on request metadata and local state before overload.

## Qualifications
The account is a former employee's historical description and does not establish Imgix's current architecture. It supplies no comparative performance or reliability data for the design.

## What Changed
- Established Imgix as the company context for the Spillway adaptive-load case.

## Relationships
- [[Spillway]] - internal reverse proxy and request broker coordinating image-processing workers.
- [[AdaptiveBackpressure]] - operating pattern used to handle unpredictable request cost.
- [[ServiceHealthChecks]] - worker capacity was treated as richer than binary process health.
