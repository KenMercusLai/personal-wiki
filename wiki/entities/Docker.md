---
title: "Docker"
type: entity
tags: [containers, deployment, infrastructure]
sources:
  - 12-fractured-apps-kelsey-hightower-medium
last_updated: 2026-09-12
knowledge_schema: synthesis-v1
---

## Overview
[[Docker]] is the container platform used in "12 Fractured Apps" to show both the promise of twelve-factor deployment practices and the risks of packaging fragile applications without fixing their startup assumptions.

## Current Profile
The source presents Docker as a strong fit for applications that log to stdout, accept environment-variable configuration, and ship minimal runtime artifacts. It also warns that Docker can make brittle applications easier to package without making them easier to operate, especially when teams replace application-level startup behavior with image variants, bind mounts, custom entrypoint scripts, or deployment-order procedures.

## Key Characteristics
- Makes [[TwelveFactorApp]] logging and environment-variable configuration concrete through container runtime behavior.
- Supports minimal artifact shipping through scratch-based images when applications do not need wrapper shells.
- Can enable superficial lift-and-shift migration that treats containers like virtual machines.
- Exposes brittle application startup assumptions around config files, data directories, and external services.
- Encourages runtime configuration, but does not eliminate the need to design how runtime settings are supplied and validated.

## Evidence
- Twelve-factor fit: [[12-fractured-apps-kelsey-hightower-medium]] connects Docker logs with stdout event streams and Docker runtime flags with environment-variable configuration.
- Minimal image example: [[12-fractured-apps-kelsey-hightower-medium]] builds a scratch image by copying only the Go application binary.
- Lift-and-shift warning: [[12-fractured-apps-kelsey-hightower-medium]] says Docker users often create large images based on full Linux distributions when they treat containers like VMs.
- Startup exposure: [[12-fractured-apps-kelsey-hightower-medium]] demonstrates failures from missing `/etc/config.json`, missing `/var/lib/data`, and a temporarily unreachable MySQL database.
- Wrapper-script cost: [[12-fractured-apps-kelsey-hightower-medium]] shows that adding a shell entrypoint requires an Alpine base image and moves logic outside the application.

## Qualifications
The source is a 2015 practitioner essay focused on application startup design. It does not evaluate Docker's later ecosystem, orchestration practices, security model, or production platform history.

## What Changed
- Created the Docker entity page for the container deployment argument.

## Relationships
- [[KelseyHightower]] - author uses Docker as the practical demonstration environment.
- [[TwelveFactorApp]] - Docker operationalizes several twelve-factor conventions.
- [[ContainerApplicationStartup]] - Docker exposes startup assumptions that the application should handle.
- [[RuntimeConfiguration]] - Docker supplies runtime env vars but does not by itself design configuration semantics.
- [[Kubernetes]] - both are container-infrastructure layers represented in the wiki, though this source predates and does not discuss Kubernetes directly.
