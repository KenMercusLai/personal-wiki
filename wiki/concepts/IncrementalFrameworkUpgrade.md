---
title: "Incremental Framework Upgrade"
type: concept
tags: [software-maintenance, framework-upgrade, compatibility, ci-cd]
sources:
  - upgrading-github-from-rails-3-2-to-5-2-the-github-blog
last_updated: 2026-09-23
knowledge_schema: synthesis-v1
---

## Definition
[[IncrementalFrameworkUpgrade]] is a migration strategy that keeps current and next framework versions runnable from one evolving codebase, advances through explicit compatibility milestones, and expands production exposure only as tests and operational evidence justify it.

## Current Synthesis
GitHub's Rails migration shows how a large application can modernize without freezing ordinary product work or hiding the upgrade in a long-running branch. Separate dependency lockfiles select the current or next Rails version, conditional code preserves temporary compatibility, and each completed minor-version CI target becomes required before the team advances.

The sequence separates compatibility progress from production deployment. GitHub tested every intermediate version in CI but deployed only Rails 4.2 and 5.2 because unsupported 4.0 and 4.1 releases did not fit its security constraints. For deployed milestones, team volunteers click-tested product areas before off-hours percentage rollouts supplied exception and performance evidence; full production at peak traffic became the final acceptance environment.

The method is partly organizational. Staffing and shared familiarity grew with momentum, while repeated milestones converted an uncertain volunteer project into a priority. Retaining the compatibility infrastructure, following upstream releases, reducing private-API use and technical debt, and contributing tooling upstream are presented as ways to make the next upgrade routine rather than exceptional.

## Key Claims
- Dual-booting current and future dependency sets can replace a long-running upgrade branch.
- Sequential framework-version CI gates keep completed compatibility milestones from regressing.
- Intermediate compatibility targets and production deployment targets may differ because support and security constraints matter.
- Progressive rollout should combine pre-production human testing with production exceptions, performance, and exposure controls.
- Repeated small version steps expose deprecations earlier and create clearer milestones than a single multi-version jump.
- Upgrade infrastructure and compatibility knowledge compound, so retaining them lowers the likely cost of future upgrades.
- Framework migration is also a chance to remove application-specific patches, adopt upstream capabilities, and clarify application/framework boundaries.

## Evidence
- Shared-code migration: [[upgrading-github-from-rails-3-2-to-5-2-the-github-blog]] describes `Gemfile.lock` and `Gemfile_next.lock` plus conditional Rails-version code in the main application.
- Compatibility ratchet: [[upgrading-github-from-rails-3-2-to-5-2-the-github-blog]] says each green minor-version CI job became required while the next version was brought up.
- Support-aware milestones: [[upgrading-github-from-rails-3-2-to-5-2-the-github-blog]] says Rails 4.2 and 5.2 were deployed, while 4.0 and 4.1 were not because GitHub had not backported security fixes to them.
- Staged evidence: [[upgrading-github-from-rails-3-2-to-5-2-the-github-blog]] describes test-environment click testing, off-hours percentage production rollout, and exception and performance collection.
- Acceptance gate: [[upgrading-github-from-rails-3-2-to-5-2-the-github-blog]] says the upgrade was merged after thirty minutes at full production during peak traffic with no visible impact.
- Learning curve: [[upgrading-github-from-rails-3-2-to-5-2-the-github-blog]] reports one year for Rails 3.2 to 4.2 and five months for 4.2 to 5.2 as the framework process and team experience improved.

## Counterevidence & Qualifications
The evidence is one company-authored retrospective about a particular monolithic Rails application. Dual-booting adds conditional code and test-matrix cost, while peak-traffic observation cannot prove that delayed, rare, data-specific, or client-specific regressions are absent. The article also reports CI, local-development, and slow-query failures that escaped automated and manual testing, so incremental compatibility narrows migration risk rather than eliminating it.

## What Changed
- Established shared-code dual booting and sequential CI gates as one coherent upgrade pattern.
- Distinguished compatibility milestones from versions safe and supported enough for production deployment.
- Added progressive production evidence and accumulated team learning to the framework-migration model.

## Related Concepts
- [[ContinuousDelivery]] - frequent integration keeps the upgrade compatible with ongoing feature development.
- [[DeploymentAutomation]] - selectable dependency sets and conditional boot logic make multiple framework versions deployable.
- [[ChangeSafety]] - staged traffic, monitoring, and explicit acceptance gates bound production migration risk.
- [[ServiceObservability]] - exceptions and performance signals govern rollout expansion.
- [[TechnicalDebtTracking]] - recurring debt visibility supports removal of code that blocks framework change.
- [[ToolFamiliarity]] - repeated version steps build team knowledge that accelerates later migration work.
