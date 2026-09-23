---
title: "Filesystem Unmounting"
type: concept
tags: [linux, filesystems, system-administration, troubleshooting]
sources:
  - umount-target-is-busy
last_updated: 2026-09-24
knowledge_schema: synthesis-v1
---

## Definition
[[FilesystemUnmounting]] is the controlled removal of a mounted filesystem from a system's namespace after active process, directory, and kernel references have been identified or released.

## Current Synthesis
The source illustrates why `target is busy` is a dependency signal rather than merely a command failure. Its concrete case is the root filesystem of the running operating system, so active use is inherent: normal unmounting requires the references to disappear, which generally means operating from another boot or recovery environment when the root volume itself needs maintenance. Although the diagnostic names `lsof` and `fuser`, the question gives no reproducible commands or results from them.

The accepted answer offers two escape hatches with different scopes. A lazy unmount detaches the mount now and defers final cleanup until references are released; comments emphasize that this can hide continuing use and can pull a filesystem out from under active work. The force option is presented for NFS, not as a universal local-filesystem fix. A low-scored second answer suggests deactivating the LVM logical volume first, but the source neither validates that sequence nor addresses the normal need to stop filesystem use before removing its backing device.

## Key Claims
- A busy-unmount error means the mount still has active dependencies that should be understood before storage maintenance proceeds.
- A running root filesystem is structurally different from an incidental data mount because the operating system itself depends on it.
- `lsof` and `fuser` can help locate process users, but this source does not supply a successful diagnostic recipe.
- Lazy unmounting detaches first and cleans up later; it is not evidence that all I/O or references have ended.
- Forced unmounting is source-scoped to NFS and should not be generalized to local filesystems from this evidence.
- Backing-volume operations must respect filesystem dependencies; the source's deactivate-before-unmount suggestion is unverified and potentially backwards.

## Evidence
- Busy root mount: [[umount-target-is-busy]] reports `umount: /: target is busy` while targeting an LVM-backed root filesystem on the running system.
- Diagnostic direction: [[umount-target-is-busy]] names `lsof` and `fuser` as process-discovery tools but says the user's attempts had not worked.
- Lazy-versus-forced behavior: [[umount-target-is-busy]] recommends `umount -l` for a busy device, limits `umount -f` to busy NFS, and includes comments warning that lazy detachment is not immediate final unmounting.
- LVM ordering concern: [[umount-target-is-busy]] contains an unaccepted answer proposing `lvchange -an` before `umount`, without a successful outcome or explanation of how a mounted filesystem could safely remain above an inactive volume.

## Counterevidence & Qualifications
This is a short community Q&A rather than authoritative operational documentation. It does not distinguish every cause of a busy mount, provide exact diagnostic invocations, explain mount namespaces or nested mounts, show a safe root-volume resize workflow, or test the proposed commands. The accepted answer's popularity is not proof of safety, and the source comments themselves warn that lazy unmounting can conceal continuing references. The LVM answer should not be treated as a runbook because it is unverified, contains a `dmsetup` typo, and appears to reverse the safer dependency order.

## What Changed
- Created a scoped synthesis of busy-mount diagnosis and unmount escape hatches.
- Distinguished lazy detachment from completed cleanup and limited the force recommendation to the source's NFS context.
- Marked the deactivate-before-unmount LVM sequence as weak, unverified evidence.

## Related Concepts
- [[DatabaseServiceExposure]] - NFS is a network file service and is the only context in which the source recommends forced unmounting.
- [[SelfHostedSurveillanceStorage]] - storage maintenance must account for active writers such as ongoing video-recording processes.
- [[AgentFilesystem]] - contrasts host-level mount lifecycle with the agent-design use of files as durable intermediate artifacts.
