---
title: "fsync Failure Semantics"
type: concept
tags: [file-systems, durability, databases, recovery]
sources:
  - atc20-rebello
last_updated: 2026-10-19
knowledge_schema: synthesis-v1
---

## Definition
[[FsyncFailureSemantics]] are the rules governing what an application may infer about memory, filesystem metadata, persistent data, future error reports, and safe recovery after an `fsync` call fails.

## Current Synthesis
A failed `fsync` is an ambiguous cross-layer event, not merely a successful flush delayed until retry. In the tested Linux filesystems, a data or journal write may have failed after some state changed, and all three marked failed pages clean. Retrying could therefore return success without resubmitting the write. Ext4 and XFS sometimes kept the new contents in the page cache while disk retained older data; Btrfs reverted the cached contents; ext4 data-journal mode could surface the failure only on a later `fsync`.

Application recovery must consequently distinguish acknowledged logical state, application buffers, clean page-cache contents, journal or WAL contents, and actual disk state. Crash-restart alone is insufficient when restart reads a valid-looking cached log entry or when a delayed error lets an application discard its recovery log before damaged data is exposed. The safe general assumption after failure is narrow: persistence may be complete, partial, or absent, and recovery needs storage-grounded evidence plus a filesystem contract precise enough to interpret it.

## Key Claims
- A failed `fsync` does not imply that all target data is dirty, retryable, wholly persisted, or wholly absent.
- Clean page-cache contents can disagree with disk and can temporarily hide data loss or corruption.
- Error timing, page contents, metadata persistence, and post-failure availability vary by filesystem and mode.
- Application-level retry, rollback, checksum, crash-restart, or direct I/O is not universally sufficient without matching the underlying failure semantics.
- Recovery tests must exercise low-level faults, cache eviction, application restart, and continued post-failure operations.
- Claims are version-, configuration-, workload-, and fault-model-specific rather than permanent properties of a filesystem or database name.

## Evidence
- Clean-page ambiguity: [[atc20-rebello]] reports that ext4, XFS, and Btrfs all marked pages clean after injected data-write failures, preventing a simple `fsync` retry from resubmitting them.
- Divergent state: [[atc20-rebello]] finds ext4 and XFS retaining new cached contents over old disk data while Btrfs reverted cached state to match disk.
- Delayed reporting: [[atc20-rebello]] finds ext4 data-journal mode capable of returning success before a later checkpoint failure is reported by the next `fsync`.
- Recovery anomalies: [[atc20-rebello]] reports old values, false failures, corrupt keys or values, and missing keys across five applications, with manifestation depending on cache eviction and restart.
- Testing boundary: [[atc20-rebello]] uses deterministic block fault injection and [[CuttleFS]] because syscall-error mocks and immediate shutdown do not reproduce filesystem state transitions or later operations.

## Counterevidence & Qualifications
The study covers single transient write faults, two small update patterns, Linux kernel 5.2.11, three filesystems, and specific 2019–2020 application versions. It does not establish behavior for current releases, other kernels or operating systems, hardware power-loss behavior, multiple simultaneous faults, read faults, complex transactions, distributed replication, or every filesystem mount option. Btrfs was more corruption-resistant in the tested comparison but still produced holes and availability changes, so copy-on-write is not a universal recovery guarantee.

## What Changed
- Created the concept to separate failed-persistence semantics from ordinary successful durability guarantees.
- Established cache eviction and restart as independent dimensions of storage recovery testing.
- Recorded delayed error attribution and clean-page mismatch as cross-layer contract failures.

## Related Concepts
- [[DataDurability]] - defines the survival guarantee whose boundary becomes uncertain after a failed persistence barrier.
- [[BackupAndRecovery]] - handles restoration after failure, while fsync semantics govern the state from which recovery begins.
- [[ChaosEngineering]] - supplies the broader controlled-failure practice; fsync testing requires storage-specific injection and state inspection.
- [[DatabaseTransactionIsolation]] - governs concurrent visibility, whereas fsync semantics govern persistence and recovery after write failure.
- [[SystemReliability]] - treats precise failure contracts and exercised recovery paths as system-level reliability controls.
