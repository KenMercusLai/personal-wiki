---
title: "Upgrading GitHub from Rails 3.2 to 5.2"
type: source
tags: [github, ruby-on-rails, framework-upgrade, continuous-delivery, technical-debt]
date: 2018-09-28
source_file: "/mnt/ken_personal_wiki/Articles/Upgrading GitHub from Rails 3.2 to 5.2 - The GitHub Blog.md"
---

## Summary
[[GitHub]] describes an eighteen-month upgrade of its main application from [[RubyOnRails|Rails]] 3.2 to 5.2.1 without stopping feature work or taking the site down. The team used dual-boot dependency locks, conditional compatibility code, sequential required CI jobs, manual testing, percentage production rollouts, and exception and performance monitoring, turning a volunteer effort into a staffed [[IncrementalFrameworkUpgrade]].

## Key Claims
- A large application can avoid a long-running upgrade branch by running its current and next framework versions from separate dependency lockfiles and conditionally loading version-specific code.
- Each intermediate framework version should become a required CI target once green, preventing regressions while work advances to the next version.
- Incremental version steps expose deprecations and create clear milestones even when only selected supported milestones are deployed to production.
- Production rollout should move from a test environment and team-by-team click testing to off-hours percentage exposure, with exceptions and performance compared against the previous version.
- GitHub merged each deployed upgrade only after the new version ran across full production for thirty minutes at peak traffic with no visible impact; Rails 4.2 and 5.2 were deployed with no downtime.
- The project took one year from Rails 3.2 to 4.2 and five months from 4.2 to 5.2, reflecting both improved Rails upgrade support and learning accumulated by a team that grew from one to four full-time engineers plus volunteers.
- Frequent upgrades, retained compatibility infrastructure, upstream contributions, avoidance of private APIs, routine technical-debt reduction, shared ownership, and an expectation of breakage reduce future upgrade cost.

## Key Quotes
> "Upgrade early and upgrade often." - the central maintenance recommendation.

> "Expect things to break." - on planning for failures beyond CI and click testing.

## Connections
- [[GitHub]] - company whose main application completed the upgrade.
- [[RubyOnRails]] - framework upgraded from version 3.2 to 5.2.1.
- [[IncrementalFrameworkUpgrade]] - dual-boot, compatibility, CI, and staged-rollout method demonstrated by the project.
- [[ContinuousDelivery]] - required multi-version CI and routine deployment kept the upgrade integrated with ongoing feature work.
- [[DeploymentAutomation]] - separate dependency locks and conditional boot logic made old and next framework versions deployable from one evolving codebase.
- [[ChangeSafety]] - test-environment checks, percentage exposure, monitoring, and a peak-traffic acceptance gate bounded production risk.
- [[ServiceObservability]] - exception and performance data determined whether each rollout was safe to expand.

## Contradictions
- No direct contradiction found. The source complements rollback-skeptical material by emphasizing compatibility, progressive exposure, measurement, and repeated correction rather than claiming that a framework rollout is safely reversible in all system state.
