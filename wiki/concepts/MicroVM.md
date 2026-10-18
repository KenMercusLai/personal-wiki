---
title: "MicroVM"
type: concept
tags: [virtualization, isolation, ephemeral-compute]
sources:
  - qemu-cloud-hypervisor
last_updated: 2026-10-18
knowledge_schema: synthesis-v1
---

## Definition
A [[MicroVM]] is a lightweight virtual machine that reduces emulated hardware and guest startup work to combine hardware-backed isolation with low overhead, fast boot, and high host density for cloud and ephemeral workloads.

## Current Synthesis
MicroVM performance comes from a system of related choices rather than size alone. Paravirtualized devices let virtualization-aware guests use optimized interfaces; minimal kernels avoid loading unused components; lightweight init replaces a general-purpose service manager; and VMMs omit legacy architectures and devices that the target workload does not need. Lower per-VM overhead can improve density, especially with CPU overcommit, and makes short-lived CI, sandbox, and serverless-style execution practical.

The category does not imply uniform capabilities. [[QEMU]] microvm and [[CloudHypervisor]] share Linux/KVM roots and [[Firecracker]] influence, yet differ in control protocols, host coverage, PCI transport, GPU passthrough, hotplug, snapshot mechanics, migration limits, and ecosystem fit. A microVM platform therefore requires explicit decisions about device access, dynamic resource changes, state capture, version compatibility, and the higher-level control plane.

## Key Claims
- Reduced legacy emulation and guest initialization can lower startup time, attack surface, and per-instance resource overhead.
- Paravirtualized devices, purpose-built kernels, and lightweight init are complementary rather than interchangeable optimization layers.
- Lower overhead can increase workload density, particularly when many ephemeral guests share overcommitted CPU capacity.
- Hardware-backed isolation does not make all microVM VMMs operationally interchangeable.
- API shape, device transport, passthrough, hotplug, snapshot, migration, host support, and existing ecosystem are first-class selection criteria.
- Snapshot and migration capabilities remain bounded by device state, storage format, I/O activity, and VMM-version compatibility.

## Evidence
- Category and workload: [[qemu-cloud-hypervisor]] defines microVMs through strong isolation, reduced attack surface, fast boot, high density, and short-lived workload fit.
- Optimization layers: [[qemu-cloud-hypervisor]] identifies paravirtualization, minimalist kernels, and lightweight init as the main startup and overhead techniques.
- Implementation divergence: [[qemu-cloud-hypervisor]] compares QEMU microvm's QMP/libvirt and virtio-mmio defaults with Cloud Hypervisor's REST interface and PCI/VFIO support.
- Lifecycle limits: [[qemu-cloud-hypervisor]] records different snapshot mechanisms, incomplete device-state capture, external-I/O migration limits, absent cross-VMM migration, and cross-version risk.
- Dynamic operation: [[qemu-cloud-hypervisor]] contrasts Cloud Hypervisor's CPU, memory, and PCI hotplug with QEMU microvm's lack of hotplug.

## Counterevidence & Qualifications
The source explains intended properties but supplies no boot-time, density, memory, attack-surface, or overcommit measurements. Strong isolation is a design goal rather than an independently tested security result, and smaller device surfaces do not remove kernel, VMM, firmware, configuration, or control-plane risk. Feature support can change across versions and configurations; in particular, QEMU microvm can enable PCIe despite its default virtio-mmio emphasis. Snapshot formats are not necessarily portable across VMMs, and the article's suggestion that cross-VMM restoration might be possible is speculative and format-dependent.

## What Changed
- Created the general microVM concept and separated shared design goals from VMM-specific operational capabilities.

## Related Concepts
- [[SessionScopedMicroVMIsolation]] - applies a microVM boundary to one interaction session and makes teardown a state boundary.
- [[VMSnapshotCloning]] - uses captured VM state to accelerate creation of prepared microVM workers.
- [[AgenticSandboxInfrastructure]] - may use microVMs when agent workloads need stronger isolation or Linux compatibility.
- [[ServerlessComputing]] - shares demand-driven, ephemeral execution goals while leaving the isolation mechanism open.
- [[Firecracker]] - influential microVM monitor emphasizing a small device model and fast disposable execution.
