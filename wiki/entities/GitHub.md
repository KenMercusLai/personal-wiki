---
title: "GitHub"
type: entity
tags: [company, software-development, hosting]
sources:
  - upgrading-github-from-rails-3-2-to-5-2-the-github-blog
  - democratic-databases-science-on-github-nature-news-comment
  - firing-people
last_updated: 2026-09-28
knowledge_schema: synthesis-v1
---

## Overview
[[GitHub]] is a version-controlled collaboration platform represented here through software operations, scientific-data collaboration, and a former early employee's account of termination and alumni culture.

## Current Profile
In this source, GitHub appears as the operator of a large, highly trafficked, decade-old Rails application that had to keep accepting feature and bug-fix work during a major framework migration. Its upgrade practice combined shared-code compatibility, required multi-version CI, manual product-area testing, progressive production rollout, and production measurement.

The project began with one full-time engineer and volunteers, then became an organizational priority staffed by four full-time engineers plus volunteers. GitHub also reports backporting security fixes to Rails 3.2 while declining to deploy unsupported intermediate Rails versions.

As research infrastructure, GitHub lets scientific teams use repository history, attribution, forks, review, merging, and rollback to curate machine-readable datasets and processing code. The Ebola, Open Tree of Life, Open Exoplanet Catalogue, and ZiBRA cases show that this can widen contribution and accelerate draft release, especially for smaller text-based datasets. That collaborative role does not make GitHub a permanent archive: mutable publication snapshots still need a repository such as Zenodo or Figshare for durable citation.

[[ZachHolman]] supplies a sharply different, employee-side view of the company. He describes joining as employee number nine, becoming publicly identified with GitHub, experiencing burnout and a sabbatical, and then being dismissed in 2015 without a rationale he found clear. His account also describes prompt access removal, contested separation and option-window pressure, coworker support, and a self-organized alumni network. These are attributed experiences, not a complete or independently adjudicated account of GitHub's personnel decision.

## Key Characteristics
- Operates a large and heavily used Rails application while keeping normal feature and bug-fix delivery active during framework migration.
- Used dual-boot dependency locks, conditional compatibility code, mandatory intermediate-version CI, and measured progressive rollout instead of a long-running upgrade branch.
- Treated framework modernization as an opportunity to remove technical debt and move custom behavior upstream.
- Supports distributed scientific-data contribution through version history, forks, review, merging, and rollback.
- Fits actively maintained text data better than large or binary datasets and does not replace permanent scholarly archiving.
- Appears in Holman's account as both a deeply identity-forming workplace and the context for a contested termination experience.
- Produced a self-organized alumni community that Holman describes as emotional support, professional networking, and cultural continuity.

## Evidence
- Application scale and continuity: [[upgrading-github-from-rails-3-2-to-5-2-the-github-blog]] describes the main application as large and heavily trafficked and says feature development and bug fixes could not stop for the upgrade.
- Compatibility strategy: [[upgrading-github-from-rails-3-2-to-5-2-the-github-blog]] describes separate current and next lockfiles, conditional framework-version code, and required CI jobs for completed version milestones.
- Rollout discipline: [[upgrading-github-from-rails-3-2-to-5-2-the-github-blog]] reports test-environment checks, team volunteers, percentage production deployment, exception and performance monitoring, and a full-production peak-traffic gate.
- Organizational investment: [[upgrading-github-from-rails-3-2-to-5-2-the-github-blog]] says staffing grew from one to four full-time engineers plus volunteers as the work became a priority.
- Modernization benefit: [[upgrading-github-from-rails-3-2-to-5-2-the-github-blog]] reports a more vanilla test suite, replacement of StateMachine with Active Record enums, and initial replacement of a job runner with Active Job.
- Scientific collaboration: [[democratic-databases-science-on-github-nature-news-comment]] describes Ebola, phylogeny, exoplanet, and Zika projects using GitHub to share, update, review, and disseminate data and code.
- Working-format fit: [[democratic-databases-science-on-github-nature-news-comment]] says text formats expose useful diffs while binary and large files remain awkward.
- Archive boundary: [[democratic-databases-science-on-github-nature-news-comment]] says GitHub repositories can change or disappear and recommends DOI-bearing snapshots in dedicated scientific archives.
- Employment experience: [[firing-people]] describes Holman's 2010-2015 tenure, burnout, sabbatical, dismissal, access removal, separation negotiations, and uncertainty about the decision's rationale.
- Alumni continuity: [[firing-people]] describes former GitHub employees' private community as a mix of support, social connection, and networking.

## Qualifications
The application profile is based on GitHub's own 2018 engineering retrospective. It reports process, milestones, and outcomes but does not provide comparative productivity data, total engineering cost, detailed incident counts, or enough evidence to generalize the same staffing and rollout model to every application. The scientific profile comes from a 2016 journalistic overview of selected projects, so its user, download, price, storage-limit, and adoption figures are historical and it does not measure data quality or research outcomes. Nature later corrected the article's claim about Git's storage model: Git maintains multiple file versions rather than literally storing line-by-line changes. The employment material is Holman's retrospective account; GitHub's rationale and perspective are not supplied, and the source cannot independently establish disputed facts or causation.

## What Changed
- Expanded the profile from GitHub's own application engineering to scientific-data collaboration.
- Added repository history, forks, review, and contribution as research-workflow capabilities.
- Added the format, scale, usability, mutability, and permanent-archiving boundaries.
- Added Holman's attributed employee-side account of dismissal and the self-organized alumni network, with explicit evidentiary limits.

## Relationships
- [[RubyOnRails]] - framework used by GitHub's main application and upgraded from 3.2 to 5.2.1.
- [[IncrementalFrameworkUpgrade]] - GitHub provides the central operating case for this migration pattern.
- [[ContinuousDelivery]] - ongoing releases and required CI kept upgrade work integrated with normal delivery.
- [[ChangeSafety]] - progressive traffic exposure and production measurement constrained rollout risk.
- [[DeploymentAutomation]] - multi-version boot infrastructure kept the migration deployable without a long-lived branch.
- [[VersionControlledScientificData]] - GitHub supplies the hosted collaboration workflow in the article's scientific cases.
- [[CaitlinRivers]] - used GitHub to turn Ebola reports into a distributed machine-readable dataset.
- [[DataScienceEngineeringPractice]] - version control, validation scripts, and text formats connect the platform to reproducible analytical work.
- [[ZachHolman]] - early employee whose account adds termination and alumni-culture evidence.
- [[EmployeeTermination]] - process illustrated by Holman's attributed experience leaving GitHub.
