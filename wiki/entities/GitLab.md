---
title: "GitLab"
type: entity
tags: [software-company, developer-tools, devops]
sources:
  - gitlab-com-database-incident-gitlab
last_updated: 2026-09-28
knowledge_schema: synthesis-v1
---

## Overview
[[GitLab]] is the company and software platform operating GitLab.com, represented here through its public account of a severe 2017 database incident.

## Current Profile
In this source, GitLab responds to a cascading production failure with unusually candid live documentation. It distinguishes database-backed application data from Git repositories and wikis, publishes operational details while recovery is active, acknowledges six hours of permanent data loss, and promises a later postmortem and preventive measures.

The account also exposes a large gap between nominal safeguards and operational recovery. Replication was fragile, several backups were missing or unusable, cloud snapshots did not cover the database servers, and recovery succeeded only because an engineer had manually created a recent staging snapshot for unrelated work.

## Key Characteristics
- Operates GitLab.com while also distributing self-hosted GitLab installations.
- Separates Git repository and wiki storage from database-backed projects, issues, merge requests, users, comments, and snippets.
- Published a candid live account of an operator-caused production-data loss event.
- Relied on a fragile and incompletely validated database backup and replication system during the incident.
- Restored service from a six-hour-old staging snapshot and accepted permanent loss inside that recovery window.

## Evidence
- Service boundary: [[gitlab-com-database-incident-gitlab]] states that Git repositories, wikis, and self-hosted instances were unaffected while GitLab.com database records were lost.
- Public accountability: [[gitlab-com-database-incident-gitlab]] explicitly calls the loss unacceptable, links live notes, and promises a full postmortem.
- Recovery weakness: [[gitlab-com-database-incident-gitlab]] reports that five backup or replication techniques were unreliable, unavailable, or not configured for the failed database.
- Recovery outcome: [[gitlab-com-database-incident-gitlab]] documents restoration from staging and a six-hour data-loss window.

## Qualifications
This profile is intentionally source-bounded to one 2017 live incident report. It does not describe GitLab's current architecture, present recovery controls, later remediation, product breadth, governance, or financial position. The live account was later superseded by a formal postmortem for deeper causal analysis.

## What Changed
- Created a source-bounded GitLab profile from its public 2017 database-incident account.

## Relationships
- [[PostgreSQL]] - GitLab.com used PostgreSQL for the failed and restored application database.
- [[SystemReliability]] - the incident exposed interacting load, replication, procedure, backup, and recovery failures.
- [[BackupAndRecovery]] - GitLab's restoration depended on the only sufficiently recent usable snapshot.
- [[ChangeSafety]] - a destructive command executed on the wrong host caused catastrophic data loss.
