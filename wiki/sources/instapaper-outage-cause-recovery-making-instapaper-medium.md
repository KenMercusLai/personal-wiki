---
title: "Instapaper Outage Cause & Recovery"
type: source
tags: [instapaper, outage, mysql, rds, disaster-recovery]
date: 2017-02-14
source_file: "/mnt/ken_personal_wiki/Articles/Instapaper Outage Cause - Recovery - Making Instapaper - Medium.md"
---

## Summary
[[Instapaper]] explains how a legacy ext3-backed [[AmazonRDS]] MySQL instance inherited through a read-replica migration hit a 2 TB single-file limit, making its bookmarks table unwritable and leaving snapshot backups subject to the same constraint. With help from [[Pinterest]] SRE and [[AWS]] engineers, the team restored limited service after 31 hours, moved the data and indexes to ext4, replayed temporary-production changes, and completed recovery without losing user data. The incident shows [[BackupAndRecovery]] depending on known infrastructure lineage, observable limits, measured restore time, practiced degraded-service paths, and provider escalation rather than snapshot existence alone.

## Key Claims
- A pre-April 2014 RDS MySQL instance used ext3 and imposed a 2 TB file-size limit; a 2015 read replica inherited that filesystem even though the replica itself was created after the cutoff.
- RDS exposed no console signal, alert, or log that told Instapaper it had the legacy limit or was approaching it, so the bookmarks table crossed the boundary without advance warning.
- Ten days of automated filesystem snapshots did not provide a direct escape because every backup preserved the same ext3-backed limit.
- The absence of a tested disaster-recovery plan and realistic dump/restore timings delayed the decision to launch a limited-archive service; the first dump took 24 hours and a parallel attempt took 10.
- Recovery combined an ext4 filesystem mount and roughly eight-hour `rsync`, row-based replication from temporary production, and a final master promotion; the team reports no loss of old articles, recent changes, or newly saved articles.
- Instapaper planned immediate escalation to Pinterest SRE for system-wide outages and monthly rather than quarterly backup tests, while acknowledging that neither action would itself have prevented this filesystem-limit failure.
- The team retained RDS because its managed snapshots, failover, and replication had otherwise reduced operational work and AWS engineers were essential to the recovery.

## Key Quotes
> "all of our backups were also subject to" - on the production filesystem limit surviving into snapshot backups.

> "we didn't have a good disaster recovery plan" - on why diagnosis did not translate into a fast, rehearsed restore.

> "without losing any of our users' older articles" - on the final recovery outcome.

## Connections
- [[Instapaper]] - service whose bookmarks database, archives, and availability were affected.
- [[AmazonRDS]] - hosted MySQL service whose inherited ext3 storage boundary caused the failure and constrained snapshot recovery.
- [[AmazonAurora]] - low-friction parallel recovery target that completed a read replica in about 24 hours but had not been sufficiently tested against the application.
- [[Pinterest]] - owner whose SRE team helped diagnose the failure, guide the database dump, and shape a new escalation workflow.
- [[AWS]] - provider whose engineers supplied filesystem-level intervention, replication support, and expedited recovery.
- [[BackupAndRecovery]] - snapshots preserved the failing storage constraint, while full recovery required migration to a new filesystem and synchronization of interim writes.
- [[IncidentManagement]] - delayed escalation, uncertain restore duration, and late degraded-service activation extended the outage.
- [[IncidentCommunication]] - the retrospective says internal Pinterest and AWS communication could have mobilized recovery resources sooner.
- [[SystemReliability]] - legacy infrastructure state, invisible limits, common-mode backups, restore performance, and organizational readiness interacted in one failure.

## Contradictions
- [[10-years-of-instapaper]] describes the 2017 outage as 20 hours offline, while this detailed incident account reports 31 hours before limited service returned; the detailed timeline is more specific, but the discrepancy remains unresolved.
- The source labels February 9, 2017 as Wednesday and February 10 as Thursday, although those dates were Thursday and Friday. Its stated durations and recovery sequence remain usable, but the weekday labels should not be treated as reliable.
- Automated snapshots existed and the final recovery had no reported data loss, but those facts do not establish that the backups were independently recoverable from the ext3 failure without AWS's filesystem-level assistance.
