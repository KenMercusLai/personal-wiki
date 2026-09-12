---
title: "Docker"
type: entity
tags: [containers, deployment, infrastructure]
sources:
  - 12-fractured-apps-kelsey-hightower-medium
  - 2018-nian-du-xiao-jie-ji-shu-fang-mian
last_updated: 2026-09-12
knowledge_schema: synthesis-v1
---

## Overview
[[Docker]] is the container platform used across the wiki to show both the promise of twelve-factor deployment practices and the risks of packaging fragile applications without fixing their startup and runtime assumptions.

## Current Profile
The sources present Docker as useful only when application behavior and delivery workflow are redesigned around containers. "12 Fractured Apps" shows Docker's fit with stdout logs, environment variables, and minimal artifacts, while warning against wrapper scripts and VM-like image sprawl. Wang Ziting's retrospective adds a later production view: Dockerfile tooling can make images more standardized and cache-friendly, but teams can still fall short of [[ContainerNativePractice]] when services rely on local storage, lack health checks, or mishandle shutdown signals.

## Key Characteristics
- Makes [[TwelveFactorApp]] logging and environment-variable configuration concrete through container runtime behavior.
- Supports minimal artifact shipping through scratch-based images when applications do not need wrapper shells.
- Can enable superficial lift-and-shift migration that treats containers like virtual machines.
- Exposes brittle application startup assumptions around config files, data directories, and external services.
- Encourages runtime configuration, but does not eliminate the need to design how runtime settings are supplied and validated.
- Benefits from structured Dockerfile generation when teams need repeatable instruction ordering and cross-application caching.
- Requires container-native operational behavior such as health checks, storage discipline, and graceful signal handling.

## Evidence
- Twelve-factor fit: [[12-fractured-apps-kelsey-hightower-medium]] connects Docker logs with stdout event streams and Docker runtime flags with environment-variable configuration.
- Minimal image example: [[12-fractured-apps-kelsey-hightower-medium]] builds a scratch image by copying only the Go application binary.
- Lift-and-shift warning: [[12-fractured-apps-kelsey-hightower-medium]] says Docker users often create large images based on full Linux distributions when they treat containers like VMs.
- Startup exposure: [[12-fractured-apps-kelsey-hightower-medium]] demonstrates failures from missing `/etc/config.json`, missing `/var/lib/data`, and a temporarily unreachable MySQL database.
- Wrapper-script cost: [[12-fractured-apps-kelsey-hightower-medium]] shows that adding a shell entrypoint requires an Alpine base image and moves logic outside the application.
- Dockerfile tooling: [[2018-nian-du-xiao-jie-ji-shu-fang-mian]] describes a Node.js DSL that stores Dockerfile sections as structured instruction data before generating standardized Dockerfiles.
- Container-native gap: [[2018-nian-du-xiao-jie-ji-shu-fang-mian]] says long-running production container use still left local storage dependencies, weak health checks, and poor signal handling.

## Qualifications
The sources are practitioner reflections, not comprehensive Docker ecosystem evaluations. The 2015 essay focuses on startup design, while the 2018 retrospective focuses on one organization's production container practice and build tooling.

## What Changed
- Added Dockerfile DSL and container-native operational gaps from Wang Ziting's 2018 retrospective.

## Relationships
- [[KelseyHightower]] - author uses Docker as the practical demonstration environment.
- [[TwelveFactorApp]] - Docker operationalizes several twelve-factor conventions.
- [[ContainerApplicationStartup]] - Docker exposes startup assumptions that the application should handle.
- [[RuntimeConfiguration]] - Docker supplies runtime env vars but does not by itself design configuration semantics.
- [[Kubernetes]] - both are container-infrastructure layers represented in the wiki, though this source predates and does not discuss Kubernetes directly.
- [[ContainerNativePractice]] - Docker packaging must be paired with health, storage, and lifecycle behavior.
