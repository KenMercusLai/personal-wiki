---
title: "Container Application Startup"
type: concept
tags: [software-engineering, containers, deployment, reliability]
sources:
  - 12-fractured-apps-kelsey-hightower-medium
last_updated: 2026-09-12
knowledge_schema: synthesis-v1
---

## Definition
[[ContainerApplicationStartup]] is the design of application initialization so a containerized service can start predictably while handling configuration, local directories, logging, and temporarily unavailable dependencies.

## Current Synthesis
The source argues that container startup should not depend on a perfect deployment order or on external shell scripts papering over application assumptions. An application should load optional config, apply sane defaults, accept environment-variable overrides, ensure its own working directories exist, log what it is doing, and retry transient dependency failures with backoff.

This is a small-code, high-leverage reliability point. The Go example shows that a scratch-based binary can stay small and simple when startup behavior lives in the application; moving those responsibilities into a Docker entrypoint script adds another artifact, another language boundary, and possible drift between wrapper behavior and the real application.

## Key Claims
- Startup design should handle ordinary missing-local-state cases such as absent optional config files or working directories.
- Runtime environment variables should be applied by the application rather than translated through a deployment-only wrapper when the team controls the code.
- External dependencies such as databases may be temporarily unavailable, so startup should retry with backoff instead of requiring strict service order.
- Entrypoint scripts add operational complexity and can drift away from application behavior.
- Keeping bootstrapping close to application code can preserve smaller, cleaner container images.

## Evidence
- Missing local state: [[12-fractured-apps-kelsey-hightower-medium]] demonstrates startup failures from missing `/etc/config.json` and `/var/lib/data`, then shows optional config defaults and `MkdirAll` as application fixes.
- Env overrides: [[12-fractured-apps-kelsey-hightower-medium]] shows application code reading `APP_DATADIR`, `APP_HOST`, `APP_PORT`, `APP_USERNAME`, `APP_PASSWORD`, and `APP_DATABASE`.
- Dependency retry: [[12-fractured-apps-kelsey-hightower-medium]] replaces immediate database failure with repeated `Ping` attempts and increasing sleep durations.
- Entrypoint cost: [[12-fractured-apps-kelsey-hightower-medium]] shows that adding a shell entrypoint requires a base image and doubles the example image size.
- Wrapper drift: [[12-fractured-apps-kelsey-hightower-medium]] warns that a wrapper script can get out of sync with the application.

## Counterevidence & Qualifications
Entrypoint scripts remain reasonable for third-party applications that the deploying team cannot change. The source also focuses on startup-time database availability; long-running dependency behavior, circuit breakers, health checks, and orchestration probes are outside its scope.

## What Changed
- Created the concept page for application-owned startup behavior in containers.

## Related Concepts
- [[RuntimeConfiguration]] - startup is where runtime config is loaded, defaulted, and overridden.
- [[TwelveFactorApp]] - twelve-factor conventions motivate env-driven and log-stream-friendly startup.
- [[DependencyDegradation]] - retry and backoff are one way to prevent dependency timing from breaking startup.
- [[SystemReliability]] - robust startup is one layer of broader reliability.
- [[GameServerCloudNativeDelivery]] - both treat containers as delivery architecture, though this source focuses on application initialization.
