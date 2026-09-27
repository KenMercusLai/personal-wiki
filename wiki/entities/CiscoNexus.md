---
title: "Cisco Nexus"
type: entity
tags: [networking, switches, data-center, automation]
sources:
  - enabling-devops-approach-with-cisco-nx-os-and-ansible-cisco-blog
last_updated: 2026-09-27
knowledge_schema: synthesis-v1
---

## Overview
[[CiscoNexus]] is Cisco's data-center switching platform, represented here as the hardware target for NX-OS automation through [[Ansible]].

## Current Profile
The 2016 source positions Nexus as a common automation surface across controller-led ACI deployment and do-it-yourself [[CiscoNXOS]] operation. Its practical evidence is narrower: Cisco points to Ansible playbooks, three NX-OS modules, SSH and NX-API transports, and a demonstration spanning initial provisioning through ongoing operations.

The page therefore records an automation target rather than a general assessment of Nexus architecture or product quality. The claim that only Nexus offered this flexibility is vendor marketing and is not established by comparison with other platforms.

## Key Characteristics
- Serves as the data-center switch family targeted by the named NX-OS Ansible modules.
- Is presented as supporting both ACI and direct NX-OS operational models.
- Shares the source's claimed automation model across provisioning and ongoing management.
- Is associated with SSH and NX-API automation through NX-OS.

## Evidence
- Automation target: [[enabling-devops-approach-with-cisco-nx-os-and-ansible-cisco-blog]] names Nexus devices as the target of Ansible's NX-OS core modules.
- Deployment flexibility: [[enabling-devops-approach-with-cisco-nx-os-and-ansible-cisco-blog]] contrasts ACI deployment with do-it-yourself NX-OS while claiming a common automation model.
- Lifecycle coverage: [[enabling-devops-approach-with-cisco-nx-os-and-ansible-cisco-blog]] points to examples covering Day 0, Day 1, and Day 2 operations.

## Qualifications
The source is a short Cisco-authored promotional post from 2016. It does not compare Nexus automation with competing platforms, define the limits of the claimed common model, measure operational outcomes, or establish current module and transport support.

## What Changed
- Established Nexus as a canonical entity with an explicitly bounded automation profile.

## Relationships
- [[Cisco]] - develops and markets the Nexus platform.
- [[CiscoNXOS]] - operating system and automation surface described for Nexus devices.
- [[Ansible]] - automation framework used in the linked playbooks and demonstrations.
- [[NetworkAutomation]] - Nexus is the platform target for the source's provisioning and management examples.
- [[DevOpsCulture]] - Cisco frames Nexus automation as enabling a DevOps approach for network operations.
