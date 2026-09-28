---
title: "Backup and Recovery"
type: concept
tags: [reliability, operations, disaster-recovery, data]
sources:
  - gitlab-com-database-incident-gitlab
last_updated: 2026-09-28
knowledge_schema: synthesis-v1
---

## Definition
[[BackupAndRecovery]] is the operational discipline of creating independent, usable copies of state and repeatedly proving that they can restore the required data, scope, and point in time after failure.

## Current Synthesis
The GitLab incident shows why backup inventory is not recovery capability. The organization could name five backup or replication mechanisms, yet scheduled database dumps were missing or invalid, the S3 destination was empty, Azure disk snapshots did not cover database servers, replication was stalled, and the recovery procedure itself was fragile and poorly documented.

A usable recovery system therefore needs more than nominal redundancy. It needs validated artifacts, independent failure boundaries, known retention and recovery windows, correct tooling versions, monitored job outcomes, practiced restoration procedures, and controls that keep troubleshooting commands from destroying the remaining good copy. GitLab recovered only because a manual staging snapshot happened to have been taken six hours earlier.

## Key Claims
- Backup jobs must be judged by successfully restored data, not job existence, file creation, or configured destinations.
- Replication supports availability but is not an independent backup when operator error or destructive commands can reach both copies.
- Recovery-point and recovery-time objectives must be reflected in snapshot frequency, retention, tooling, and practiced procedures.
- Destructive recovery work needs explicit host verification, bounded permissions, reversible steps, and protection of the last known good copy.
- Monitoring must detect silent failures such as tiny dump files, empty object-storage buckets, excluded disks, and replication lag.

## Evidence
- Restore proof: [[gitlab-com-database-incident-gitlab]] reports that regular dumps were only a few bytes or absent because the wrong PostgreSQL binaries may have failed silently.
- Independence: [[gitlab-com-database-incident-gitlab]] shows replication stopping before an operator accidentally deleted the primary while attempting to rebuild the secondary.
- Coverage and frequency: [[gitlab-com-database-incident-gitlab]] says Azure snapshots excluded the database servers and the usable manual snapshot was six hours old.
- Recovery procedure: [[gitlab-com-database-incident-gitlab]] describes fragile shell scripts, poor documentation, and a `pg_basebackup` wait that looked like a hang.
- Outcome: [[gitlab-com-database-incident-gitlab]] records permanent loss of database changes within the six-hour recovery window.

## Counterevidence & Qualifications
This source documents one unusually candid incident and was written during recovery, before the formal postmortem. It establishes failure modes but does not compare backup products, prescribe universal recovery objectives, or show which later remediations proved effective. Replication remains valuable for availability and failover; the narrower conclusion is that it should not be treated as the sole independently recoverable backup.

## What Changed
- Created the concept from GitLab's distinction between nominal backup mechanisms and demonstrated recoverability.

## Related Concepts
- [[SystemReliability]] - backup and recovery are the state-restoration layer of service dependability.
- [[ChangeSafety]] - destructive recovery operations require verified targets, bounded blast radius, and reversibility.
- [[ServiceObservability]] - backup success, replication lag, artifact size, and restore tests need actionable signals.
- [[CloudHighAvailability]] - availability replicas reduce some outages but do not replace independent recovery copies.
