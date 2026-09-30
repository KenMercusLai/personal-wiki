---
title: "Backup and Recovery"
type: concept
tags: [reliability, operations, disaster-recovery, data]
sources:
  - gitlab-com-database-incident-gitlab
  - hacker-puts-hosting-service-code-spaces-out-of-business-threatpost
  - instapaper-outage-cause-recovery-making-instapaper-medium
last_updated: 2026-09-30
knowledge_schema: synthesis-v1
---

## Definition
[[BackupAndRecovery]] is the operational discipline of creating independent, usable copies of state and repeatedly proving that they can restore the required data, scope, and point in time after failure.

## Current Synthesis
The GitLab and Code Spaces incidents show why backup inventory is not recovery capability. GitLab could name five backup or replication mechanisms, yet scheduled database dumps were missing or invalid, the S3 destination was empty, Azure disk snapshots did not cover database servers, replication was stalled, and the recovery procedure itself was fragile and poorly documented. Code Spaces reported a different common-mode failure: a compromised AWS control plane could delete production resources, snapshots, object storage, machine images, configurations, and nominally offsite backups within the same administrative scope.

A usable recovery system therefore needs more than nominal redundancy. It needs validated artifacts, independent technical and administrative failure boundaries, known retention and recovery windows, correct tooling versions, monitored job outcomes, practiced restoration procedures, and controls that keep operators or compromised credentials from destroying the remaining good copy. GitLab recovered only because a manual staging snapshot happened to have been taken six hours earlier; Code Spaces said the remaining fragments were insufficient to preserve the service as a viable business.

Instapaper adds a third common mode: backups can be intact and access-controlled yet still reproduce the production system's disabling constraint. Ten days of RDS filesystem snapshots retained the ext3 2 TB file limit, so recovery required moving a 2.5 TB database onto ext4, restoring indexes, and replaying writes from temporary production. The first dump took 24 hours rather than the estimated six to eight, showing that recovery-time confidence must come from representative tests and data-shape awareness. A separate degraded-service plan can reduce customer downtime while full restoration continues, but it must also preserve and reconcile interim writes.

## Key Claims
- Backup jobs must be judged by successfully restored data, not job existence, file creation, or configured destinations.
- Replication or geographic duplication is not an independent backup when one operator, account, or control plane can delete every copy.
- A backup is not independent when it preserves the same filesystem, format, corruption, encryption, or platform constraint that disabled production.
- Recovery-point and recovery-time objectives must be reflected in snapshot frequency, retention, data shape, measured throughput, tooling, and practiced procedures.
- Destructive recovery work and cloud administration need explicit target verification, bounded permissions, separate recovery authority, reversible steps, and protection of the last known good copy.
- Monitoring must detect silent failures such as tiny dump files, empty object-storage buckets, excluded disks, and replication lag.
- Degraded-service recovery needs an explicit scope plus a tested path for reconciling writes made before full restoration.

## Evidence
- Restore proof: [[gitlab-com-database-incident-gitlab]] reports that regular dumps were only a few bytes or absent because the wrong PostgreSQL binaries may have failed silently.
- Independence: [[gitlab-com-database-incident-gitlab]] shows replication stopping before an operator accidentally deleted the primary while attempting to rebuild the secondary.
- Coverage and frequency: [[gitlab-com-database-incident-gitlab]] says Azure snapshots excluded the database servers and the usable manual snapshot was six hours old.
- Recovery procedure: [[gitlab-com-database-incident-gitlab]] describes fragile shell scripts, poor documentation, and a `pg_basebackup` wait that looked like a hang.
- Outcome: [[gitlab-com-database-incident-gitlab]] records permanent loss of database changes within the six-hour recovery window.
- Administrative independence: [[hacker-puts-hosting-service-code-spaces-out-of-business-threatpost]] reports that an attacker with AWS control-panel access deleted EBS snapshots and volumes, S3 buckets, AMIs, instances, configurations, and most backups.
- Business continuity: [[hacker-puts-hosting-service-code-spaces-out-of-business-threatpost]] says Code Spaces ceased trading after the loss made recovery, refunds, and restored customer confidence financially untenable.
- Constraint independence: [[instapaper-outage-cause-recovery-making-instapaper-medium]] says RDS snapshots preserved the ext3 2 TB file-size limit that had made the production bookmarks table unwritable.
- Restore-time measurement: [[instapaper-outage-cause-recovery-making-instapaper-medium]] reports a 24-hour initial dump and a 10-hour parallel dump after an estimate based on row count missed uneven data distribution.
- Degraded service and reconciliation: [[instapaper-outage-cause-recovery-making-instapaper-medium]] describes a limited-archive production database whose binary logs were later replicated into the restored ext4 database.
- Recovery outcome: [[instapaper-outage-cause-recovery-making-instapaper-medium]] reports final promotion without loss of older articles, recent changes, or post-outage saves.

## Counterevidence & Qualifications
The sources document three unusually severe incidents rather than comparing backup products or prescribing universal objectives. GitLab's live account preceded its formal postmortem; Threatpost relies heavily on Code Spaces' statement; and Instapaper's no-loss outcome, timings, and causal explanation are first-party. Instapaper's snapshots were not useless—they retained the data and supported provider-assisted migration—but they could not independently escape the filesystem constraint through the customer's normal interface. Replication, snapshots, and geographic duplication remain valuable; the narrower conclusion is that recovery independence must be tested against the actual failure model.

## What Changed
- Expanded recovery independence to include inherited filesystem and platform constraints, not only storage location or administrative authority.
- Added representative restore-time measurement and degraded-service write reconciliation as recovery capabilities.

## Related Concepts
- [[SystemReliability]] - backup and recovery are the state-restoration layer of service dependability.
- [[ChangeSafety]] - destructive recovery operations require verified targets, bounded blast radius, and reversibility.
- [[ServiceObservability]] - backup success, replication lag, artifact size, and restore tests need actionable signals.
- [[CloudHighAvailability]] - availability replicas reduce some outages but do not replace independent recovery copies.
- [[CloudAccountSegmentation]] - separate administrative boundaries can keep a production-account compromise from deleting every recovery copy.
- [[IncidentManagement]] - early choice of degraded service versus full restoration depends on rehearsed escalation and credible recovery timing.
