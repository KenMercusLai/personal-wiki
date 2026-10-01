---
title: "Rainforest QA"
type: entity
tags: [software, testing, infrastructure]
sources:
  - rainforest-qa-how-and-why-we-migrated-from-heroku-to-kubernetes
last_updated: 2026-10-01
knowledge_schema: synthesis-v1
---

## Overview
[[RainforestQA]] is a software-testing company represented here through its first-party account of migrating production applications and PostgreSQL databases from [[Heroku]] to Google Cloud and [[GoogleKubernetesEngine]].

## Current Profile
The 2019 retrospective portrays Rainforest QA as a heterogeneous, PostgreSQL-heavy application operator with a small operations team. Its infrastructure decision favored managed services, minimal simultaneous architectural change, established tools, private networking, custom autoscaling, and staged risk reduction. The migration took about six months and preserved Heroku as a rollback target until the final database transfer.

## Key Characteristics
- Operated Rails applications alongside Go, Elixir, Python, and Crystal services.
- Kept most customer data in a small number of large PostgreSQL databases during the migration.
- Preferred managed services because its operations team was small relative to its responsibilities.
- Used a temporary cross-cloud application stage to separate application cutover risk from database cutover risk.
- Accepted scheduled downtime when a simpler, rehearsable database migration was safer than fragile low-downtime replication.

## Evidence
- Workload shape: [[rainforest-qa-how-and-why-we-migrated-from-heroku-to-kubernetes]] describes a heterogeneous application estate, large PostgreSQL databases, and short-lived automation jobs.
- Operating principles: [[rainforest-qa-how-and-why-we-migrated-from-heroku-to-kubernetes]] names managed services, minimized change, and deliberately boring supporting technology as selection principles.
- Risk separation: [[rainforest-qa-how-and-why-we-migrated-from-heroku-to-kubernetes]] and its retained diagram show production traffic moving to GKE while applications still used Heroku Postgres before the final Cloud SQL cutover.
- Database execution: [[rainforest-qa-how-and-why-we-migrated-from-heroku-to-kubernetes]] reports a full rehearsal and a production maintenance window of about six hours.

## Qualifications
This profile comes from one company-authored 2019 retrospective and is not a current description of Rainforest QA's architecture, organization, products, or scale. Reported outcomes, timings, costs, and technical judgments are not independently verified.

## What Changed
- Created the company profile around its migration constraints, operating principles, staged topology, and database-cutover discipline.

## Relationships
- [[Heroku]] - Rainforest QA's original production application and PostgreSQL platform.
- [[GoogleKubernetesEngine]] - managed orchestration target for most migrated applications.
- [[Kubernetes]] - common runtime chosen for heterogeneous web and batch workloads.
- [[PostgreSQL]] - critical state layer and highest-risk portion of the migration.
- [[Terraform]] - infrastructure definition tool used for clusters, projects, and permissions.
- [[ChangeSafety]] - rollback, rehearsal, and scoped phases shaped the migration plan.
