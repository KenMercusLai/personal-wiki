---
title: "CuttleFS"
type: entity
tags: [file-system, fault-injection, testing, open-source]
sources:
  - atc20-rebello
last_updated: 2026-10-19
knowledge_schema: synthesis-v1
---

## Overview
[[CuttleFS]] is a FUSE-based testing filesystem created by the authors of [[atc20-rebello]] to emulate selected `fsync` failure reactions beneath unmodified data-intensive applications.

## Current Profile
CuttleFS keeps a user-space page cache separate from the kernel page cache. In trace mode it identifies which blocks an application's repeated writes eventually flush; in fault mode it can fail a configured write to a selected sector or block. After the injected fault, testers can choose whether a page stays dirty or becomes clean, whether it keeps the latest content or reverts, and whether the error appears immediately or on the next `fsync`.

The paper configures those controls to approximate the observed data-block reactions of ext4 ordered mode and XFS, ext4 data mode, and Btrfs. It also lets tests evict selected clean pages, making cache state and application restart separate experimental dimensions. This makes CuttleFS a durability-test harness, not a full behavioral replica of each filesystem.

## Key Characteristics
- Implements a FUSE filesystem with an independent user-space page cache.
- Traces effective flushed blocks rather than only application write calls.
- Injects deterministic faults into selected block or sector writes.
- Configures post-failure page cleanliness, content, and error-report timing.
- Supports targeted clean-page eviction for recovery experiments.
- Emulates selected failure characteristics rather than complete filesystem implementations.

## Evidence
- Architecture: [[atc20-rebello]] describes write and read handling through CuttleFS's user-space pages and synchronization to an underlying filesystem on `fsync`.
- Fault controls: [[atc20-rebello]] reports configurable block or sector failure, page state, retained content, and immediate or delayed reporting.
- Filesystem profiles: [[atc20-rebello]] defines configurations corresponding to observed ext4-ordered/XFS, ext4-data, and Btrfs data-failure reactions.
- Application use: [[atc20-rebello]] runs Redis, LMDB, LevelDB, SQLite, and PostgreSQL workloads across restart and eviction combinations.
- Reproducibility: [[atc20-rebello]] says CuttleFS, the device-mapper module, and experiment materials were open sourced.

## Qualifications
CuttleFS models selected reactions identified by the paper, especially page cleanliness, page content, and error timing after a single data-block fault. It does not reproduce all allocation, journaling, checkpoint, metadata, hardware, concurrency, performance, or availability behavior of ext4, XFS, or Btrfs. The reported experiments use 2020-era application versions and simple single-key workloads, so passing them would not prove complete durability.

## What Changed
- Created the entity from the paper's architecture, controls, and experimental role.
- Distinguished characteristic emulation from full filesystem equivalence.

## Relationships
- [[FsyncFailureSemantics]] - behavior contract that CuttleFS makes configurable for testing.
- [[DataDurability]] - guarantee whose failure paths the tool probes.
- [[ChaosEngineering]] - broader controlled-failure discipline that includes related but less storage-specific experiments.
- [[PostgreSQL]] - one of five applications tested over CuttleFS profiles.
- [[SQLite]] - tested in both rollback-journal and WAL modes.
