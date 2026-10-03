---
title: "Docker"
type: entity
tags: [containers, deployment, infrastructure]
sources:
  - 12-fractured-apps-kelsey-hightower-medium
  - 2018-nian-du-xiao-jie-ji-shu-fang-mian
  - bmpi-serverless-ying-yong-kai-fa-xiao-ji
  - improving-critical-infrastructure-rollouts-labs
  - increasing-attacker-cost-using-immutable-infrastructure
  - docker-qing-li-zuo-bi-shou-ce
last_updated: 2026-10-03
knowledge_schema: synthesis-v1
---

## Overview
[[Docker]] is the container platform used across the wiki to show the promise of twelve-factor deployment, the risks of packaging fragile applications, and the fleet-wide change hazards that emerge when a runtime becomes critical infrastructure.

## Current Profile
The sources present Docker as useful only when application behavior and delivery workflow are redesigned around containers. "12 Fractured Apps" shows Docker's fit with stdout logs, environment variables, and minimal artifacts, while warning against wrapper scripts and VM-like image sprawl. Wang Ziting's retrospective adds a later production view: Dockerfile tooling can make images more standardized and cache-friendly, but teams can still fall short of [[ContainerNativePractice]] when services rely on local storage, lack health checks, or mishandle shutdown signals.

The bmpi.dev case adds a dependency-build perspective. Its Python core needs native TA-Lib compilation, so the author rejects Alpine after slow, failure-prone builds and uses a Debian Buster-based Python image before pushing the artifact to ECR for Fargate execution. Image minimalism is therefore a tradeoff with dependency compatibility and build reliability, not an absolute goal.

Spotify adds the runtime-lifecycle boundary. Docker grew from a prototype substrate to a reported 80% of production backend services on thousands of hosts, so upgrades could no longer be treated as environment-wide maintenance. Version changes introduced hostname and command incompatibilities, orphaned containers and proxies, retained ports, routing errors, blocked starts, mass restarts, and reconnect storms. This makes gradual, representative production rollout part of operating the runtime, not merely part of packaging applications.

Diogo Mónica's compromise demonstration adds the filesystem and response boundary. Docker images remain unchanged while normal containers record runtime writes in a copy-on-write layer that `docker diff` can inspect and `docker commit` can preserve. Launching a fresh container restores the packaged application, while `--read-only` separately blocks writes to the root filesystem. These mechanisms improve restoration and constrain persistence, but they do not neutralize remote code execution or protect credentials, databases, external systems, and explicitly writable mounts.

The cleanup cheat sheet adds a local resource-lifecycle boundary. Stopped containers remain until removed unless they were launched with `--rm`; dangling images are a narrower category than all images unused by containers; and volumes and networks have their own prune commands. Cleanup is reference- and order-sensitive: deleting containers first can make every local image eligible for `docker image prune -a`, so disk reclamation must be treated as a scoped destructive operation rather than a consequence-free maintenance step.

## Key Characteristics
- Makes [[TwelveFactorApp]] logging and environment-variable configuration concrete through container runtime behavior.
- Supports minimal artifact shipping and read-only root filesystems that can reduce post-compromise tools and persistence paths.
- Can enable superficial lift-and-shift migration or unsafe fleet-wide maintenance when application and rollout behavior remain unchanged.
- Exposes brittle application startup assumptions around config files, data directories, and external services.
- Encourages runtime configuration, but does not eliminate the need to design how runtime settings are supplied and validated.
- Benefits from deliberate base-image and Dockerfile choices that balance size, dependency compatibility, repeatability, and caching.
- Requires container-native lifecycle discipline across health checks, writable paths, storage, graceful signal handling, and reference-aware cleanup of retained resources.

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
- Writable-layer visibility: [[increasing-attacker-cost-using-immutable-infrastructure]] uses `docker diff` to expose a changed web page and an added PHP shell after compromise.
- Restore and preserve: [[increasing-attacker-cost-using-immutable-infrastructure]] commits the compromised layer for inspection and launches a fresh container from the original application image.
- Read-only boundary: [[increasing-attacker-cost-using-immutable-infrastructure]] shows `--read-only` blocking the demonstrated defacement while acknowledging continued code execution and data-exfiltration risk.
- Resource-specific cleanup: [[docker-qing-li-zuo-bi-shou-ce]] distinguishes container, image, volume, and network prune commands and describes the narrower default scope of `docker system prune` in its 2019 context.
- Cleanup order: [[docker-qing-li-zuo-bi-shou-ce]] warns that removing all containers before `docker image prune -a` can make every local image eligible for deletion.

## Qualifications
The sources are practitioner reflections, not comprehensive Docker ecosystem evaluations. The 2015 essay focuses on startup design, the 2018 retrospective on one organization's production container practice, and the bmpi.dev note on one Python native-dependency build and Fargate deployment. Spotify's first-party account documents several failures and a control design but supplies no comparative incident, detection, or recovery measurements; its rollout chart could not be retrieved. Mónica's 2016 example is deliberately vulnerable and demonstrates filesystem behavior rather than complete containment or forensic procedure. The cleanup note is a short 2019 cheat sheet without a pinned Docker version, build-cache treatment, filters, recovery guidance, or a full account of persistent-volume risk. Image immutability does not imply that a normal container root is read-only, restoring a container does not restore or validate mutable external state, and current cleanup behavior must be verified against the execution environment.

## What Changed
- Added copy-on-write drift inspection and compromised-layer preservation as incident-response capabilities.
- Distinguished unchanged images, writable container layers, and the separate `--read-only` runtime control.
- Added the security limit that container replacement and read-only roots do not remediate code execution or mutable external state.
- Added object-specific cleanup rules for containers, images, volumes, and networks.
- Added the order-sensitive risk that removing containers can expand the images eligible for broad pruning.

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
- [[DiogoMonica]] - practitioner demonstrating Docker filesystem controls during a simulated compromise.
- [[ImmutableInfrastructure]] - known image artifacts support replacement while runtime controls determine permitted drift.
- [[IncidentManagement]] - Docker can preserve filesystem evidence and restore the packaged service as separate response steps.
- [[DockerResourceCleanup]] - object references and command order determine which local Docker resources can be reclaimed.
