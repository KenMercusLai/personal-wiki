---
title: "Bare Metal Check"
type: entity
tags: [infrastructure, inspection, offline-tools, automation]
sources:
  - self-contained-dist-tools
last_updated: 2026-10-13
knowledge_schema: synthesis-v1
---

## Overview
[[BareMetalCheck]] is a self-contained, offline server-inspection tool described by [[ChaneyZorn]] for Ubuntu 22.04 and 24.04 environments.

## Current Profile
The control CLI and [[Ansible]] are packaged into one shiv-built Python zipapp, while native inspection commands and active-test programs travel as separately built archives inside the final delivery package. The controller selects archives by node properties and role, verifies their integrity, transfers them over SSH only when required, and installs them idempotently under `/opt/` without using the target's package manager. Results are joined into a self-contained HTML report that works from `file://` and can also be served temporarily over HTTP.

The retained screenshot makes the report model concrete: five CPU or GPU nodes appear in a matrix covering operating system, CPU, memory, disk, drivers, container runtime, GPU, and network checks. Statuses distinguish pass, fail, error, and skipped work, while a node drill-down ties a failed memory check to an observed 188.7 GiB value and a 240 GiB requirement.

## Key Characteristics
- Requires a compatible system Python but installs no Python packages on the target.
- Reuses its `.pyz` as both the default CLI and the `ansible-playbook` executable environment.
- Carries relocatable native binaries and selected libraries in versioned archives.
- Selects and distributes tools by OS, architecture, node role, prerequisites, and permission for active tests.
- Verifies checksums and skips transfers when the installed digest already matches.
- Produces an offline single-file HTML report with batch and per-node evidence.

## Evidence
- Python and Ansible packaging: [[self-contained-dist-tools]] documents shiv construction and `SHIV_CONSOLE_SCRIPT` entry switching.
- Native-tool portability: [[self-contained-dist-tools]] describes dependency collection and `$ORIGIN`-relative rpaths applied with `patchelf`.
- Conditional installation: [[self-contained-dist-tools]] describes manifest filtering, separate checksum data, temporary transfer, verification, and digest-based skipping.
- Report behavior: [[self-contained-dist-tools]] explains the base64 JSON data island and retains a screenshot of the matrix and failure drill-down.

## Qualifications
The system is self-contained only within a declared compatibility envelope. It still relies on Python 3.10+, SSH, glibc and selected base libraries, suitable hardware and drivers, and architecture-specific wheels and binaries. The article does not provide the implementation, archive sizes, security threat model, benchmark data, checksum format, signature or provenance mechanism, failure-recovery tests, or cross-host compatibility results. The screenshot is an illustrative run, not evidence of production detection accuracy.

## What Changed
- Established the tool as a layered offline delivery system rather than a literally dependency-free executable.
- Made prerequisite gating and report evidence part of the profile, not just packaging details.

## Relationships
- [[ChaneyZorn]] - author and reported implementer of the tool.
- [[SelfContainedToolDistribution]] - operating pattern used across its code, utilities, and report.
- [[Ansible]] - embedded orchestration entry point for SSH-based multi-node checks.
- [[Python]] - pre-existing runtime that executes the zipapp.
- [[DeploymentAutomation]] - governs selection, transfer, verification, and idempotent installation.
