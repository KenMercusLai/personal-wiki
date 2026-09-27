---
title: "Cisco NX-OS"
type: entity
tags: [networking, network-operating-system, automation, data-center]
sources:
  - enabling-devops-approach-with-cisco-nx-os-and-ansible-cisco-blog
last_updated: 2026-09-27
knowledge_schema: synthesis-v1
---

## Overview
[[CiscoNXOS]] is Cisco's network operating system for Nexus data-center switches, represented here through a 2016 account of automation with [[Ansible]].

## Current Profile
The source exposes NX-OS through concrete automation surfaces rather than through a general platform review. Ansible 2.0's `nxos_command`, `nxos_config`, and `nxos_template` modules could send CLI commands or configuration files using SSH or NX-API, while linked examples covered provisioning and later operational work.

This establishes NX-OS as a programmable network target, but not the breadth, reliability, or present state of its automation support. The evidence is Cisco-authored, tied to early Ansible releases, and supplies no comparative outcomes.

## Key Characteristics
- Runs on the [[CiscoNexus]] data-center switching platform in the source's framing.
- Exposes CLI-driven automation through Ansible's `nxos_command` module.
- Supports configuration and template workflows through `nxos_config` and `nxos_template`.
- Can be reached through SSH or NX-API for the described automation tasks.
- Is presented across Day 0 provisioning and Day 1/Day 2 operational workflows.

## Evidence
- Module surface: [[enabling-devops-approach-with-cisco-nx-os-and-ansible-cisco-blog]] names three Ansible 2.0 core modules specific to Nexus devices.
- Transport surface: [[enabling-devops-approach-with-cisco-nx-os-and-ansible-cisco-blog]] says the modules send CLI commands or configuration files through SSH or NX-API.
- Operational span: [[enabling-devops-approach-with-cisco-nx-os-and-ansible-cisco-blog]] points to a demonstration covering Day 0, Day 1, and Day 2 automation.

## Qualifications
The evidence is a short 2016 Cisco promotional article, not a current compatibility matrix or an independent test of feature coverage, idempotence, security, reliability, or scale. The linked examples were written for Ansible 1.9 or announced with Ansible 2.0 and may not describe current modules or recommended practices.

## What Changed
- Established NX-OS as a canonical entity with explicit Ansible modules, transports, and lifecycle scope.

## Relationships
- [[Cisco]] - develops and markets NX-OS.
- [[CiscoNexus]] - hardware platform associated with NX-OS in this source.
- [[Ansible]] - supplies the named command, configuration, and template modules.
- [[NetworkAutomation]] - NX-OS is the device operating-system surface being automated.
- [[ConfigurationManagement]] - configuration files and templates are applied to running network devices.
