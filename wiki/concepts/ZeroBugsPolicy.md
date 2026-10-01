---
title: "Zero Bugs Policy"
type: concept
tags: [bugs, agile, software-quality, backlog]
sources:
  - gal-zellermayer-0-bugs-policy
  - not-all-bugs-are-worth-fixing-and-thats-okay-bugsnag-blog
last_updated: 2026-10-01
knowledge_schema: synthesis-v1
---

## Definition
[[ZeroBugsPolicy]] is a defect-inventory rule under which each newly found bug is promptly fixed or explicitly closed as not worth fixing, rather than kept in an indefinitely deferred backlog.

## Current Synthesis
The policy separates defects found during feature development from later regression, customer, or post-completion defects. An in-sprint bug means the story is not done and must be repaired before acceptance. Other defects receive a bounded fix-or-close decision: repair now or in the next sprint when the value exceeds the effort, otherwise close them as “won't fix.”

The Bugsnag article strengthens the decision side of the policy by supplying a candidate impact signal. A release-level [[ApplicationStability]] target, based on successful or crash-free user sessions, can show when defect repair should displace roadmap work; environment and user reach can distinguish common failures from rare browser or device edge cases. “Zero bugs” therefore means zero unresolved queue, not 100% stability or defect-free software.

The economic argument concerns queue age as well as repair work. A delayed defect loses human context, test and development environments may disappear, surrounding code may change, and the item repeatedly consumes triage attention. Explicit closure avoids pretending that every known defect will eventually be repaired, but it must preserve enough traceability for later recurrence, support, audit, or risk review.

Neither defect count nor crash-free percentage is a complete priority rule. Low-frequency safety, security, data-integrity, privacy, accessibility, contractual, or regulatory failures can outrank common low-consequence crashes. The durable synthesis is prompt, recorded, risk-aware disposition informed by user impact—not automatic repair and not silent abandonment.

## Key Claims
- In-sprint defects keep a story from satisfying its definition of done.
- Every other new defect should receive a prompt fix-or-close decision rather than indefinite deferral.
- User reach and a stability target can inform when repair should displace feature work.
- Defect repair generally becomes harder as human, environmental, and code context decays.
- Retained bug inventories impose recurring triage and prioritization costs.
- Zero open bugs is an inventory state, not a claim of defect-free or perfectly stable software.
- High-consequence risk can override frequency, reach, and ordinary opportunity-cost thresholds.

## Evidence
- Completion and disposition rule: [[gal-zellermayer-0-bugs-policy]] distinguishes in-sprint defects from regressions, customer reports, and post-completion bugs, then prescribes prompt repair or explicit closure.
- Delay and queue cost: [[gal-zellermayer-0-bugs-policy]] attributes later repair cost to lost memory, unavailable environments, changed code, repeated triage, and feature displacement in a mixed backlog.
- Stability-based allocation: [[not-all-bugs-are-worth-fixing-and-thats-okay-bugsnag-blog]] recommends a below-100% stability target to decide when sprint capacity should shift between roadmap and bug repair.
- Reach and fragmentation: [[not-all-bugs-are-worth-fixing-and-thats-okay-bugsnag-blog]] argues that browser, extension, version, device, and setting variance creates edge cases that may affect very few users.
- Shared non-perfection boundary: both [[gal-zellermayer-0-bugs-policy]] and [[not-all-bugs-are-worth-fixing-and-thats-okay-bugsnag-blog]] explicitly reject the idea that every known defect must be repaired.

## Counterevidence & Qualifications
Both sources are practitioner arguments rather than controlled or comparative studies. Neither reports defect escape rate, severity, customer harm, throughput, time spent fixing, reopen rate, retention, or measured outcomes before and after adoption. The Bugsnag source also comes from a monitoring vendor and defines stability mainly through crashes or unhandled errors.

Closing a defect does not remove it from the product. A low-value cosmetic issue and a low-probability high-consequence issue cannot be judged by effort or reach alone. Some organizations must retain known-issue records, formal risk acceptance, customer disclosures, workarounds, or audit trails even when they choose not to repair immediately. Bounded deferral may also be necessary when dependencies, incident stabilization, coordinated releases, or insufficient reproduction evidence make immediate resolution unsafe or impossible.

## What Changed
- Added user-session stability and environmental reach as inputs to the fix-or-close decision.
- Clarified that zero open inventory neither requires 100% stability nor makes crash-free percentage a complete risk measure.
- Strengthened recorded non-repair and high-consequence override boundaries.

## Related Concepts
- [[ApplicationStability]] - supplies a user-impact metric for deciding when repair should displace roadmap work.
- [[AgileSoftwareDevelopment]] - definition-of-done and sprint planning provide the policy's operating context.
- [[InternalSoftwareQuality]] - defect decisions affect correctness, change cost, and lifecycle maintenance.
- [[TechnicalDebtTracking]] - both manage future engineering liabilities, but defects are observable product failures rather than all forms of debt.
- [[ProductBacklogBuilding]] - mixed product backlogs create the prioritization surface the policy seeks to avoid.
- [[ChangeSafety]] - repair timing should account for the risk of introducing or amplifying failure.
