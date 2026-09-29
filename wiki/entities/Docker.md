---
title: "Docker"
type: entity
tags: [containers, deployment, infrastructure]
sources:
  - 12-fractured-apps-kelsey-hightower-medium
  - 2018-nian-du-xiao-jie-ji-shu-fang-mian
  - bmpi-serverless-ying-yong-kai-fa-xiao-ji
  - improving-critical-infrastructure-rollouts-labs
last_updated: 2026-09-30
knowledge_schema: synthesis-v1
---

## Overview
[[Docker]] is the container platform used across the wiki to show the promise of twelve-factor deployment, the risks of packaging fragile applications, and the fleet-wide change hazards that emerge when a runtime becomes critical infrastructure.

## Current Profile
The sources present Docker as useful only when application behavior and delivery workflow are redesigned around containers. "12 Fractured Apps" shows Docker's fit with stdout logs, environment variables, and minimal artifacts, while warning against wrapper scripts and VM-like image sprawl. Wang Ziting's retrospective adds a later production view: Dockerfile tooling can make images more standardized and cache-friendly, but teams can still fall short of [[ContainerNativePractice]] when services rely on local storage, lack health checks, or mishandle shutdown signals.

The bmpi.dev case adds a dependency-build perspective. Its Python core needs native TA-Lib compilation, so the author rejects Alpine after slow, failure-prone builds and uses a Debian Buster-based Python image before pushing the artifact to ECR for Fargate execution. Image minimalism is therefore a tradeoff with dependency compatibility and build reliability, not an absolute goal.

Spotify adds the runtime-lifecycle boundary. Docker grew from a prototype substrate to a reported 80% of production backend services on thousands of hosts, so upgrades could no longer be treated as environment-wide maintenance. Version changes introduced hostname and command incompatibilities, orphaned containers and proxies, retained ports, routing errors, blocked starts, mass restarts, and reconnect storms. This makes gradual, representative production rollout part of operating the runtime, not merely part of packaging applications.

## Key Characteristics
- Makes [[TwelveFactorApp]] logging and environment-variable configuration concrete through container runtime behavior.
- Supports minimal artifact shipping through scratch-based images when applications do not need wrapper shells.
- Can enable superficial lift-and-shift migration or unsafe fleet-wide maintenance when application and rollout behavior remain unchanged.
- Exposes brittle application startup assumptions around config files, data directories, and external services.
- Encourages runtime configuration, but does not eliminate the need to design how runtime settings are supplied and validated.
- Benefits from deliberate base-image and Dockerfile choices that balance size, dependency compatibility, repeatability, and caching.
- Requires container-native operational behavior such as health checks, storage discipline, and graceful signal handling.

## Evidence
- Twelve-factor fit: [[12-fractured-apps-kelsey-hightower-medium]] connects Docker logs with stdout event streams and Docker runtime flags with environment-variable configuration.
- Minimal image example: [[12-fractured-apps-kelsey-hightower-medium]] builds a scratch image by copying only the Go application binary.
- Lift-and-shift warning: [[12-fractured-apps-kelsey-hightower-medium]] says Docker users often create large images based on full Linux distributions when they treat containers like VMs.
- Startup exposure: [[12-fractured-apps-kelsey-hightower-medium]] demonstrates failures from missing `/etc/config.json`, missing `/var/lib/data`, and a temporarily unreachable MySQL database.
- Wrapper-script cost: [[12-fractured-apps-kelsey-hightower-medium]] shows that adding a shell entrypoint requires an Alpine base image and moves logic outside the application.
- Dockerfile tooling: [[2018-nian-du-xiao-jie-ji-shu-fang-mian]] describes a Node.js DSL that stores Dockerfile sections as structured instruction data before generating standardized Dockerfiles.
- Container-native gap: [[2018-nian-du-xiao-jie-ji-shu-fang-mian]] says long-running production container use still left local storage dependencies, weak health checks, and poor signal handling.
- Native dependency build: [[bmpi-serverless-ying-yong-kai-fa-xiao-ji]] installs build tools, NumPy, and TA-Lib in a Python 3.8 Debian Buster image after the author found Alpine compilation slow and error-prone.
- Managed execution: [[bmpi-serverless-ying-yong-kai-fa-xiao-ji]] pushes the image to ECR and runs it as a scheduled ECS Fargate task.
- Upgrade regressions: [[improving-critical-infrastructure-rollouts-labs]] reports hostname and command changes, orphaned containers retaining ports, and orphaned `docker-proxy` processes across three upgrade periods.
- Fleet criticality: [[improving-critical-infrastructure-rollouts-labs]] reports thousands of instances and 80% of Spotify production backend services running as containers by February 2017.
- Restart risk: [[improving-critical-infrastructure-rollouts-labs]] says upgrading an instance restarts its containers and concentrated critical-service restarts can trigger user harm and downstream reconnect storms.
- Rollout response: [[improving-critical-infrastructure-rollouts-labs]] describes using Tsunami to distribute Docker versions gradually across representative production services.

## Qualifications
The sources are practitioner reflections, not comprehensive Docker ecosystem evaluations. The 2015 essay focuses on startup design, the 2018 retrospective on one organization's production container practice, and the bmpi.dev note on one Python native-dependency build and Fargate deployment. Spotify's first-party account documents several failures and a control design but supplies no comparative incident, detection, or recovery measurements; its rollout chart could not be retrieved.

## What Changed
- Added base-image compatibility and managed Fargate execution from the bmpi.dev Python/TA-Lib case.
- Added Dockerfile DSL and container-native operational gaps from Wang Ziting's 2018 retrospective.
- Added fleet-scale upgrade regressions, restart coupling, and progressive infrastructure rollout from Spotify.

## Relationships
- [[KelseyHightower]] - author uses Docker as the practical demonstration environment.
- [[TwelveFactorApp]] - Docker operationalizes several twelve-factor conventions.
- [[ContainerApplicationStartup]] - Docker exposes startup assumptions that the application should handle.
- [[RuntimeConfiguration]] - Docker supplies runtime env vars but does not by itself design configuration semantics.
- [[Kubernetes]] - both are container-infrastructure layers represented in the wiki, though this source predates and does not discuss Kubernetes directly.
- [[ContainerNativePractice]] - Docker packaging must be paired with health, storage, and lifecycle behavior.
- [[ServerlessComputing]] - Fargate runs the Dockerized core as managed event-triggered compute.
- [[Spotify]] - production operator whose Docker adoption made runtime changes a fleet-wide reliability concern.
- [[Helios]] - orchestration tool affected by orphaned-container port conflicts.
- [[Tsunami]] - desired-state service used to roll Docker versions out gradually.
- [[ProgressiveInfrastructureRollout]] - practice for bounding exposure to runtime upgrades and configuration changes.
