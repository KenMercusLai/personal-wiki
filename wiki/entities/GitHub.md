---
title: "GitHub"
type: entity
tags: [company, software-development, hosting]
sources:
  - upgrading-github-from-rails-3-2-to-5-2-the-github-blog
last_updated: 2026-09-23
knowledge_schema: synthesis-v1
---

## Overview
[[GitHub]] is the software-development platform whose engineering blog documents an eighteen-month upgrade of its main application from [[RubyOnRails|Rails]] 3.2 to 5.2.1.

## Current Profile
In this source, GitHub appears as the operator of a large, highly trafficked, decade-old Rails application that had to keep accepting feature and bug-fix work during a major framework migration. Its upgrade practice combined shared-code compatibility, required multi-version CI, manual product-area testing, progressive production rollout, and production measurement.

The project began with one full-time engineer and volunteers, then became an organizational priority staffed by four full-time engineers plus volunteers. GitHub also reports backporting security fixes to Rails 3.2 while declining to deploy unsupported intermediate Rails versions.

## Key Characteristics
- Operates a large and heavily used Rails application.
- Kept normal feature and bug-fix delivery active during a multi-version framework migration.
- Used dual-boot dependency locks and conditional compatibility code instead of a long-running upgrade branch.
- Made completed intermediate-version CI jobs mandatory to prevent regressions.
- Expanded production traffic only after testing, monitoring, and comparison with the prior version.
- Treated framework modernization as an opportunity to remove technical debt and move custom behavior upstream.

## Evidence
- Application scale and continuity: [[upgrading-github-from-rails-3-2-to-5-2-the-github-blog]] describes the main application as large and heavily trafficked and says feature development and bug fixes could not stop for the upgrade.
- Compatibility strategy: [[upgrading-github-from-rails-3-2-to-5-2-the-github-blog]] describes separate current and next lockfiles, conditional framework-version code, and required CI jobs for completed version milestones.
- Rollout discipline: [[upgrading-github-from-rails-3-2-to-5-2-the-github-blog]] reports test-environment checks, team volunteers, percentage production deployment, exception and performance monitoring, and a full-production peak-traffic gate.
- Organizational investment: [[upgrading-github-from-rails-3-2-to-5-2-the-github-blog]] says staffing grew from one to four full-time engineers plus volunteers as the work became a priority.
- Modernization benefit: [[upgrading-github-from-rails-3-2-to-5-2-the-github-blog]] reports a more vanilla test suite, replacement of StateMachine with Active Record enums, and initial replacement of a job runner with Active Job.

## Qualifications
The profile is based on GitHub's own 2018 engineering retrospective. It reports process, milestones, and outcomes but does not provide comparative productivity data, total engineering cost, detailed incident counts, or enough evidence to generalize the same staffing and rollout model to every application.

## What Changed
- Established GitHub as a large-application framework-upgrade case.
- Added its dual-boot, sequential-CI, and progressive-production practices.
- Added its reported staffing growth and technical-debt modernization outcomes.

## Relationships
- [[RubyOnRails]] - framework used by GitHub's main application and upgraded from 3.2 to 5.2.1.
- [[IncrementalFrameworkUpgrade]] - GitHub provides the central operating case for this migration pattern.
- [[ContinuousDelivery]] - ongoing releases and required CI kept upgrade work integrated with normal delivery.
- [[ChangeSafety]] - progressive traffic exposure and production measurement constrained rollout risk.
- [[DeploymentAutomation]] - multi-version boot infrastructure kept the migration deployable without a long-lived branch.
