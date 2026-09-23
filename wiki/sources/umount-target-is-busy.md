---
title: "umount: /: target is busy"
type: source
tags: [linux, filesystems, troubleshooting, lvm]
date: 2017-01-04
source_file: "/mnt/ken_personal_wiki/Articles/umount target is busy.md"
---

## Summary
An Ask Ubuntu question reports that an attempt to unmount the active LVM-backed root filesystem returned `target is busy`, even after unsuccessful experiments with `lsof` and `fuser`. The accepted answer proposes lazy unmounting with `umount -l` and reserves `umount -f` for a busy NFS mount, while later comments warn that lazy unmounting only detaches the mount and can remove a filesystem from underneath active users. A second, unaccepted answer proposes deactivating the logical volume before unmounting it, but its low score, command typo, and questionable operation order make it weak evidence rather than a reliable procedure. All four referenced images were inspected and identified as an Ask Ubuntu logo or user avatars, so they were omitted as decorative.

## Key Claims
- A mounted root filesystem on a running system is expected to be busy because the operating system and processes actively depend on it.
- `lsof` and `fuser` are suggested as ways to identify processes using a device, but the question does not document the attempted commands or why they failed.
- `umount -l` performs a lazy detachment: it can remove the mount from the namespace before all active references have gone away, so apparent success does not mean immediate cleanup or safe device removal.
- The answer scopes `umount -f` to busy NFS mounts rather than presenting force as a general remedy for local filesystems.
- A separate answer suggests LVM deactivation with `lvchange -an`, but it proposes deactivation before unmounting and supplies no successful result, recovery plan, or safety analysis.

## Key Quotes
> "umount: /: target is busy" - the reported failure when attempting to unmount the active root filesystem.

> "umount -l does not actually unmount the filesystem." - a comment warning that lazy detachment has important deferred-cleanup semantics.

## Connections
- [[FilesystemUnmounting]] - diagnosing active filesystem users and distinguishing ordinary, lazy, and forced unmount behavior.
- [[DatabaseServiceExposure]] - the force option is discussed specifically for NFS, a network file service with different failure conditions from a local root filesystem.
- [[SelfHostedSurveillanceStorage]] - persistent self-hosted storage likewise requires coordination with active writers before detachment or maintenance.

## Contradictions
- No direct contradiction with an existing wiki page. Internally, however, the source's second answer is in tension with normal dependency ordering because it proposes deactivating an LVM logical volume before unmounting the filesystem that uses it; the source provides no evidence that this sequence worked.
