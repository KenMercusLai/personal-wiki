---
title: "The differences between QEMU microvm and Cloud Hypervisor"
type: source
tags: [virtualization, microvm, qemu, cloud-hypervisor]
date: 2026-02-18
source_file: /mnt/ken_personal_wiki/Articles/qemu-cloud-hypervisor.md
---

## Summary
[[PeterHaskoNagy]] compares [[QEMU]]'s microvm machine type with [[CloudHypervisor]] for platform builders choosing a lightweight virtual-machine monitor. Both target fast, isolated cloud workloads, but Cloud Hypervisor offers a REST API, direct VFIO device passthrough, and hotplug, while QEMU microvm fits the broader QEMU ecosystem and exposes QMP or libvirt at the cost of more integration work and important device-model limits.

## Key Claims
- [[MicroVM]] systems reduce startup and resource overhead through paravirtualized devices, minimal guest kernels, lightweight init, and a smaller legacy-device surface, making them attractive for dense ephemeral workloads.
- [[CloudHypervisor]] is a Rust VMM for KVM and Microsoft Hypervisor whose primary management interface is a per-process REST API over a Unix socket or file descriptor.
- [[QEMU]] microvm is a Linux/KVM machine type inspired by [[Firecracker]]; it uses virtio-mmio by default and can be managed through QMP or libvirt rather than a native REST API.
- Cloud Hypervisor supports VFIO PCI-device passthrough, including compatible GPUs, while QEMU microvm does not provide direct GPU passthrough in its default no-PCI configuration even though PCIe can be enabled.
- Both systems support snapshots and live migration with format, device, I/O, and version-compatibility caveats; neither provides portable live migration between different VMMs.
- Cloud Hypervisor supports x86 vCPU, memory, and PCI-device hotplug, while QEMU microvm does not support hotplug.
- VMM selection should follow workload and platform requirements rather than a universal ranking: Cloud Hypervisor favors REST-oriented control and dynamic devices, while QEMU microvm can favor compatibility with an existing QEMU operating model.

## Key Quotes
> "microVMs are lightweight virtual machines with strong isolation guarantees, a reduced attack surface, and usually pretty fast boot times." - on the category's intended operating profile.

> "collect information, capture your requirements, and make an educated decision." - on treating the comparison as a requirements exercise rather than declaring a winner.

## Connections
- [[PeterHaskoNagy]] - author of the comparison.
- [[MicroVM]] - lightweight virtualization category whose density, startup, and isolation goals frame the comparison.
- [[QEMU]] - provides the Linux-only microvm machine type discussed in the article.
- [[CloudHypervisor]] - Rust VMM compared against QEMU microvm.
- [[Firecracker]] - influenced both compared designs.
- [[VMSnapshotCloning]] - related prepared-state technique; this source focuses on operational snapshot capture and restoration rather than cloning many initialized workers.
- [[SessionScopedMicroVMIsolation]] - an existing lifecycle pattern that can be implemented on top of a suitable microVM runtime.

## Contradictions
- No direct contradiction with existing wiki content. The article qualifies broad microVM interchangeability: snapshot, migration, passthrough, hotplug, API, transport, host-platform, and version constraints differ materially between VMMs.
