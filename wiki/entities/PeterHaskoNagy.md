---
title: "Peter Hasko-Nagy"
type: entity
tags: [virtualization, technical-writing]
sources:
  - qemu-cloud-hypervisor
last_updated: 2026-10-18
knowledge_schema: synthesis-v1
---

## Overview
[[PeterHaskoNagy]] is the author of a platform-oriented comparison of QEMU microvm and Cloud Hypervisor.

## Current Profile
Hasko-Nagy explains microVM selection through operational capabilities rather than declaring one VMM universally superior. His comparison emphasizes API shape, device passthrough, snapshots, live migration, hotplug, and fit with an existing virtualization stack.

## Key Characteristics
- Writes about lightweight virtualization from a platform-builder perspective.
- Compares VMMs through concrete operational requirements and integration costs.
- Treats technology choice as conditional on workload, host, device, and ecosystem needs.

## Evidence
- Authorship: [[qemu-cloud-hypervisor]] identifies Peter Hasko-Nagy as the article's author.
- Comparison method: [[qemu-cloud-hypervisor]] organizes the decision around API support, GPU passthrough, snapshotting, live migration, and hotplug.
- Decision framing: [[qemu-cloud-hypervisor]] explicitly avoids naming a universal winner and recommends matching requirements to tradeoffs.

## Qualifications
The wiki currently has one article by Hasko-Nagy. It supplies no broader biography, role history, independent benchmark work, or evidence that the comparison generalizes beyond the versions and documented behavior available to the author.

## What Changed
- Created the profile from the QEMU microvm and Cloud Hypervisor comparison.

## Relationships
- [[QEMU]] - one virtualization system compared in Hasko-Nagy's article.
- [[CloudHypervisor]] - the other VMM evaluated in the comparison.
- [[MicroVM]] - the workload and isolation category framing the article.
