---
title: "Rolling Deployment"
type: concept
tags: [deployment, load-balancing, availability, web-infrastructure]
sources:
  - nick-craver-stack-overflow-how-we-do-deployment-2016-edition
last_updated: 2026-10-01
knowledge_schema: synthesis-v1
---

## Definition
[[RollingDeployment]] is an incremental release pattern that removes a bounded subset of serving capacity, updates and verifies it, restores it to traffic, and repeats until the target fleet runs the new version.

## Current Synthesis
Stack Overflow's 2016 web deployment used [[HAProxy]] as an explicit traffic-state controller around each IIS update. The script drained new traffic, waited for active requests, stopped the site, marked the server down, copied the new files, restarted the site, and marked it ready. HAProxy then required three successful checks before returning that server to rotation. A tunable pause separated server updates, and the reported nine-server production pass usually still had seven servers serving when the step ended.

The same case exposes a second ordering problem outside server health. Seven-day caching meant new HTML could refer to a new static-asset hash while another web server still held old bytes. Stack Overflow therefore rolled out static assets to the CDN-serving IIS site before deploying application code that emitted the new hashes. The safer failure direction was new bytes under an old hash, which corrected on reload once the application rollout caught up, rather than old bytes cached under a new hash.

## Key Claims
- A rolling deployment needs explicit traffic withdrawal, in-flight request drainage, update, restart, health verification, and traffic restoration.
- Readiness should be demonstrated after startup rather than assumed from process launch.
- Capacity and spacing must be planned so the fleet can serve demand while members are unavailable or warming.
- Mixed-version compatibility extends beyond server code to databases, APIs, caches, and static assets.
- Dependency rollout order should choose the failure direction that is bounded and self-correcting.
- Automation can preserve a human promotion decision between deployment tiers without making every host update manual.

## Evidence
- Server sequence: [[nick-craver-stack-overflow-how-we-do-deployment-2016-edition]] shows the PowerShell drain, delay, stop, down, copy, start, and ready workflow.
- Readiness gate: [[nick-craver-stack-overflow-how-we-do-deployment-2016-edition]] says HAProxy waited for three successful polls before restoring traffic.
- Capacity snapshot: [[nick-craver-stack-overflow-how-we-do-deployment-2016-edition]] reports that seven of nine production web servers were typically serving when the roughly two-minute step completed.
- Static ordering: [[nick-craver-stack-overflow-how-we-do-deployment-2016-edition]] describes deploying CDN assets before code to avoid caching old content under a new cache-breaking hash.

## Counterevidence & Qualifications
The source is a first-party 2016 snapshot without load, error, tail-latency, or failure-rate measurements. Draining and three passing polls do not prove that warmed application behavior is correct under real traffic; the author notes that premature traffic can stress thread-pool growth. Rolling updates also create a mixed-version window and can progressively spread a subtle defect through the whole fleet. State migration, client compatibility, rollback, stop conditions, and automated outcome verification require controls beyond this server-copy loop.

## What Changed
- Created the concept from Stack Overflow's HAProxy-coordinated IIS rollout.
- Added static-asset publication order as a mixed-version deployment constraint.
- Distinguished process startup from demonstrated readiness under repeated health checks.

## Related Concepts
- [[DeploymentAutomation]] - implements the repeatable drain, update, verify, and restore loop.
- [[DeploymentPipeline]] - places rolling rollout after build and tier validation.
- [[DeploymentReleaseSeparation]] - traffic state can be controlled independently from installed code.
- [[ProgressiveInfrastructureRollout]] - both bound initial exposure, though fleet replacement and traffic exposure are not identical.
- [[NetworkLoadBalancing]] - the load balancer removes and restores serving capacity.
- [[ServiceHealthChecks]] - readiness polling gates return to traffic.
- [[ForwardOnlyDatabaseMigration]] - compatible schema sequencing supports mixed application versions.
