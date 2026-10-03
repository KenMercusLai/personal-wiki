---
title: "Docker Resource Cleanup"
type: concept
tags: [docker, operations, storage, cleanup]
sources:
  - docker-qing-li-zuo-bi-shou-ce
last_updated: 2026-10-03
knowledge_schema: synthesis-v1
---

## Definition
[[DockerResourceCleanup]] is the deliberate removal of unused Docker containers, images, volumes, and networks after identifying the object types, reference relationships, and deletion scope of each cleanup command.

## Current Synthesis
The 2019 cheat sheet treats cleanup as a family of object-specific operations rather than one interchangeable delete action. Stopped containers persist unless they were launched with `--rm` or are later pruned; dangling images are narrower than all images unused by containers; and volumes and networks have separate cleanup commands. `docker system prune` combines several categories, but the article does not present it as including volumes by default.

The main operational risk is order-dependent reachability. Removing containers first eliminates the references that protect their images, so a later `docker image prune -a` can expand from a selective cleanup to every local image. Safe use therefore depends on inspecting the current environment, distinguishing stopped from running and dangling from merely unused, and treating broad prune or command-substitution sequences as destructive changes rather than routine housekeeping.

## Key Claims
- Cleanup scope should be reasoned about separately for containers, images, volumes, and networks.
- Stopping a container and deleting it are different lifecycle transitions unless it was started with `--rm`.
- Dangling-image cleanup is narrower than pruning every image unused by a container.
- Cleanup order changes reachability: deleting containers can make more images eligible for later pruning.
- Broad system or all-object commands require inspection and deliberate confirmation because convenience increases deletion scope.

## Evidence
- Object-specific commands: [[docker-qing-li-zuo-bi-shou-ce]] lists `docker container prune`, `docker image prune`, `docker volume prune`, and `docker network prune` separately.
- Container lifecycle: [[docker-qing-li-zuo-bi-shou-ce]] says stopped containers remain until removed unless `--rm` was set at run time.
- Image scope: [[docker-qing-li-zuo-bi-shou-ce]] distinguishes dangling images from all images not used by a container through the `-a` option.
- Order-dependent reachability: [[docker-qing-li-zuo-bi-shou-ce]] warns that deleting all containers before `docker image prune -a` can make all images removable.
- Combined cleanup: [[docker-qing-li-zuo-bi-shou-ce]] describes `docker system prune` as removing stopped containers, dangling images, and unused networks.

## Counterevidence & Qualifications
This synthesis rests on one short 2019 practitioner note rather than a versioned Docker command reference or measured operations study. The source does not cover command filters, BuildKit build cache, Compose-managed resources, confirmation behavior, named-volume data loss, concurrent workloads, or recovery. Exact command semantics and eligible-object definitions can vary with Docker version and execution context, so the local CLI help and an inventory of affected resources remain authoritative for an actual cleanup.

## What Changed
- Established cleanup as an object- and reference-aware lifecycle operation rather than a single disk-reclamation command.
- Added the order-dependent risk that container removal expands the image-prune candidate set.
- Separated dangling-image pruning from removal of every image unused by containers.

## Related Concepts
- [[Docker]] - platform whose resource graph and CLI define the cleanup targets.
- [[ContainerNativePractice]] - operational lifecycle discipline includes knowing which container resources persist beyond a process.
- [[ImmutableInfrastructure]] - replaceable image artifacts still consume local storage and can become eligible for pruning when references disappear.
- [[IncidentManagement]] - cleanup should not destroy container layers or artifacts that must first be preserved as evidence.
