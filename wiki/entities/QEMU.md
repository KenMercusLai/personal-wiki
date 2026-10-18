---
title: "QEMU"
type: entity
tags: [virtualization, microvm, kvm]
sources:
  - qemu-cloud-hypervisor
last_updated: 2026-10-18
knowledge_schema: synthesis-v1
---

## Overview
[[QEMU]] is a broad machine emulator and virtualizer whose Linux/KVM microvm machine type removes much legacy-device machinery to target lightweight cloud workloads.

## Current Profile
The microvm machine type is a specialized configuration inside the wider QEMU ecosystem rather than a separate VMM. It is inspired by [[Firecracker]], runs on Linux with KVM, and defaults to virtio-mmio instead of PCI, trading device flexibility for a smaller and faster-booting platform. Operators manage it through QMP or an external layer such as libvirt rather than a native REST API.

For platform use, QEMU microvm supports snapshots through `savevm` and `loadvm` when a writable qcow2 disk is present, or state export through migration while disks are managed separately. Live migration appears available with qualifications, but ongoing external I/O is unsupported for this machine type and cross-version compatibility is not guaranteed. Hotplug is unsupported, and direct GPU passthrough is unavailable in the default no-PCI configuration even though PCIe can be enabled.

## Key Characteristics
- Provides a Linux/KVM microvm machine type within the larger QEMU tool and protocol ecosystem.
- Uses virtio-mmio by default and omits ordinary PCI-device support to reduce legacy surface.
- Exposes QMP and can be integrated through libvirt, but has no native REST management API.
- Supports more than one snapshot path, each with disk-format or state-management constraints.
- Has live-migration caveats for external I/O and version compatibility.
- Does not support resource or device hotplug in the microvm machine type.

## Evidence
- Scope and transport: [[qemu-cloud-hypervisor]] describes QEMU microvm as a Firecracker-inspired Linux/KVM machine type using virtio-mmio rather than PCI by default.
- Management: [[qemu-cloud-hypervisor]] identifies QMP as its JSON-over-Unix-socket control protocol and libvirt as an optional higher-level integration with distribution-dependent microvm compatibility.
- Snapshot paths: [[qemu-cloud-hypervisor]] distinguishes qcow2-backed `savevm`/`loadvm` from migration-to-file with separate disk handling.
- Migration boundary: [[qemu-cloud-hypervisor]] reports qualified live-migration support but no ongoing external-I/O migration and no cross-version guarantee.
- Dynamic-device boundary: [[qemu-cloud-hypervisor]] says the microvm type lacks hotplug and lacks direct GPU passthrough in its default no-PCI setup.

## Qualifications
The profile describes QEMU's microvm machine type, not full-system QEMU generally. The source is a practitioner comparison based largely on project documentation, gives no reproduced startup, density, migration, or snapshot measurements, and uses cautious inference for QEMU microvm live migration. PCIe can be configured, so the default no-PCI limitation should not be mistaken for an absolute property of every possible microvm configuration.

## What Changed
- Created the entity profile for QEMU's microvm machine type and its platform tradeoffs.

## Relationships
- [[MicroVM]] - QEMU supplies one implementation of the lightweight VM category.
- [[CloudHypervisor]] - compared alternative with a REST-first API and broader hotplug support.
- [[Firecracker]] - design influence on QEMU's microvm machine type.
- [[VMSnapshotCloning]] - related use of captured VM state, subject to QEMU-specific storage and compatibility rules.
