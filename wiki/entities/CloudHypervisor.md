---
title: "Cloud Hypervisor"
type: entity
tags: [virtualization, microvm, rust, kvm]
sources:
  - qemu-cloud-hypervisor
last_updated: 2026-10-18
knowledge_schema: synthesis-v1
---

## Overview
[[CloudHypervisor]] is a Rust virtual-machine monitor focused on modern cloud workloads and designed without broad legacy architecture or device support.

## Current Profile
Cloud Hypervisor is inspired by [[Firecracker]], runs on KVM and Microsoft Hypervisor, and does not support macOS. Each binary invocation corresponds to one VMM process, primarily controlled through a REST API exposed over a Unix socket or file descriptor rather than through a built-in fleet-level control plane.

The source presents Cloud Hypervisor as the more capable of the two compared systems for dynamic platform operation. It uses VFIO for compatible PCI-device passthrough, including GPUs; snapshots paused VMs independently of disk format; supports live migration; and allows x86 vCPU, memory, and PCI-device hotplug. These features retain operational caveats around guest-side CPU onlining, memory-hotplug methods, omitted VFIO snapshot state, and version compatibility.

## Key Characteristics
- Implements a modern cloud-focused VMM in Rust with a deliberately reduced legacy-device surface.
- Runs on Linux KVM and Microsoft Hypervisor but not macOS.
- Uses a per-process REST API over a Unix socket or file descriptor as its primary control interface.
- Supports VFIO passthrough for compatible PCI devices, including GPUs.
- Supports snapshots and live migration with device-state and version boundaries.
- Supports x86 vCPU, memory, and PCI-device hotplug.

## Evidence
- Platform scope: [[qemu-cloud-hypervisor]] describes the Rust VMM, its Firecracker influence, reduced legacy support, and KVM/Microsoft Hypervisor host coverage.
- Control interface: [[qemu-cloud-hypervisor]] identifies its REST API as the primary VM-management path and notes that each process manages one VM without a fleet-level control plane.
- Device support: [[qemu-cloud-hypervisor]] reports VFIO PCI passthrough for GPUs and other compatible devices.
- State lifecycle: [[qemu-cloud-hypervisor]] describes pause-snapshot-restore-resume behavior, omitted VFIO device state, live migration, and cross-version limitations.
- Dynamic resources: [[qemu-cloud-hypervisor]] reports x86 vCPU, memory, and PCI-device hotplug with guest and method-specific caveats.

## Qualifications
The profile rests on one practitioner-authored documentation comparison without reproduced performance, density, failure, security, or compatibility tests. Snapshotting excludes VFIO device state, migration and snapshots are not guaranteed across versions, and some hotplug operations require guest cooperation. A per-VM REST API does not itself provide inventory, scheduling, health management, or a multi-VM control plane.

## What Changed
- Created the entity profile from its comparison with QEMU microvm.

## Relationships
- [[MicroVM]] - Cloud Hypervisor implements the lightweight VM operating model.
- [[QEMU]] - compared alternative with broader ecosystem continuity and different device constraints.
- [[Firecracker]] - architectural influence and component source for Cloud Hypervisor.
- [[VMSnapshotCloning]] - related snapshot-based lifecycle pattern, constrained here by device state and version compatibility.
