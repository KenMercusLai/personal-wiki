---
title: "Backup and Recovery"
type: concept
tags: [reliability, operations, disaster-recovery, data]
sources:
  - gitlab-com-database-incident-gitlab
  - hacker-puts-hosting-service-code-spaces-out-of-business-threatpost
last_updated: 2026-09-29
knowledge_schema: synthesis-v1
---

## Definition
[[BackupAndRecovery]] is the operational discipline of creating independent, usable copies of state and repeatedly proving that they can restore the required data, scope, and point in time after failure.

## Current Synthesis
The GitLab and Code Spaces incidents show why backup inventory is not recovery capability. GitLab could name five backup or replication mechanisms, yet scheduled database dumps were missing or invalid, the S3 destination was empty, Azure disk snapshots did not cover database servers, replication was stalled, and the recovery procedure itself was fragile and poorly documented. Code Spaces reported a different common-mode failure: a compromised AWS control plane could delete production resources, snapshots, object storage, machine images, configurations, and nominally offsite backups within the same administrative scope.

A usable recovery system therefore needs more than nominal redundancy. It needs validated artifacts, independent technical and administrative failure boundaries, known retention and recovery windows, correct tooling versions, monitored job outcomes, practiced restoration procedures, and controls that keep operators or compromised credentials from destroying the remaining good copy. GitLab recovered only because a manual staging snapshot happened to have been taken six hours earlier; Code Spaces said the remaining fragments were insufficient to preserve the service as a viable business.

## Key Claims
- Backup jobs must be judged by successfully restored data, not job existence, file creation, or configured destinations.
- Replication or geographic duplication is not an independent backup when one operator, account, or control plane can delete every copy.
- Recovery-point and recovery-time objectives must be reflected in snapshot frequency, retention, tooling, and practiced procedures.
- Destructive recovery work and cloud administration need explicit target verification, bounded permissions, separate recovery authority, reversible steps, and protection of the last known good copy.
- Monitoring must detect silent failures such as tiny dump files, empty object-storage buckets, excluded disks, and replication lag.

## Evidence
- Restore proof: [[gitlab-com-database-incident-gitlab]] reports that regular dumps were only a few bytes or absent because the wrong PostgreSQL binaries may have failed silently.
- Independence: [[gitlab-com-database-incident-gitlab]] shows replication stopping before an operator accidentally deleted the primary while attempting to rebuild the secondary.
- Coverage and frequency: [[gitlab-com-database-incident-gitlab]] says Azure snapshots excluded the database servers and the usable manual snapshot was six hours old.
- Recovery procedure: [[gitlab-com-database-incident-gitlab]] describes fragile shell scripts, poor documentation, and a `pg_basebackup` wait that looked like a hang.
- Outcome: [[gitlab-com-database-incident-gitlab]] records permanent loss of database changes within the six-hour recovery window.
- Administrative independence: [[hacker-puts-hosting-service-code-spaces-out-of-business-threatpost]] reports that an attacker with AWS control-panel access deleted EBS snapshots and volumes, S3 buckets, AMIs, instances, configurations, and most backups.
- Business continuity: [[hacker-puts-hosting-service-code-spaces-out-of-business-threatpost]] says Code Spaces ceased trading after the loss made recovery, refunds, and restored customer confidence financially untenable.

## Counterevidence & Qualifications
The sources document two unusually severe incidents rather than comparing backup products or prescribing universal recovery objectives. GitLab's live account was written during recovery, before the formal postmortem. The Threatpost report relies heavily on Code Spaces' own statement, does not establish how the attacker obtained control-panel access, and does not independently verify which safeguards were configured. Replication and geographic duplication remain valuable for availability; the narrower conclusion is that neither is an independently recoverable backup while the same destructive authority can reach every copy.

## What Changed
- Created the concept from GitLab's distinction between nominal backup mechanisms and demonstrated recoverability.
- Expanded independence from storage and replication topology to include administrative authority and control-plane blast radius.

## Related Concepts
- [[SystemReliability]] - backup and recovery are the state-restoration layer of service dependability.
- [[ChangeSafety]] - destructive recovery operations require verified targets, bounded blast radius, and reversibility.
- [[ServiceObservability]] - backup success, replication lag, artifact size, and restore tests need actionable signals.
- [[CloudHighAvailability]] - availability replicas reduce some outages but do not replace independent recovery copies.
- [[CloudAccountSegmentation]] - separate administrative boundaries can keep a production-account compromise from deleting every recovery copy.
