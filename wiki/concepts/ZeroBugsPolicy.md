---
title: "Zero Bugs Policy"
type: concept
tags: [bugs, agile, software-quality, backlog]
sources:
  - gal-zellermayer-0-bugs-policy
last_updated: 2026-09-28
knowledge_schema: synthesis-v1
---

## Definition
[[ZeroBugsPolicy]] is a defect-inventory rule under which each newly found bug is promptly fixed or explicitly closed as not worth fixing, rather than kept in an indefinitely deferred backlog.

## Current Synthesis
The policy separates defects found during feature development from later regression, customer, or post-completion defects. An in-sprint bug means the story is not done and must be repaired before acceptance. Other defects receive a bounded fix-or-close decision: repair now or in the next sprint when the value exceeds the effort, otherwise close them as “won't fix.”

Its economic argument is about queue age as well as repair work. A delayed defect loses human context, test and development environments may disappear, surrounding code may change, and the item repeatedly consumes triage attention. The retained planning sequence supplies a plausible displacement mechanism: even highly ranked bugs fall below sprint capacity when critical and desired features are promoted, then meet more features and defects in the next backlog.

“Zero bugs” therefore means zero open defect inventory, not flawless software. Closing a known low-value defect preserves the observable behavior while eliminating the promise to reconsider it. That clarity may reduce recurring coordination cost, but it also requires explicit risk judgment and must not erase records needed for safety, security, contracts, regulation, customer communication, or later analysis.

## Key Claims
- In-sprint defects keep a story from satisfying its definition of done.
- Every other new defect should receive a prompt fix-or-close decision rather than indefinite deferral.
- Defect repair generally becomes harder as human, environmental, and code context decays.
- Retained bug inventories impose recurring triage and prioritization costs.
- Mixed backlogs can structurally favor visible new features over lower-priority defects.
- Zero open bugs is an inventory state, not a claim that the software contains no defects.

## Evidence
- Decision rule and categories: [[gal-zellermayer-0-bugs-policy]] distinguishes in-sprint defects from regressions, customer reports, and bugs found after feature completion, then prescribes fix or close.
- Delay cost: [[gal-zellermayer-0-bugs-policy]] attributes later repair cost to lost memory, unavailable environments, and changed code.
- Queue overhead: [[gal-zellermayer-0-bugs-policy]] describes repeated multi-role triage and reporting as work created by the retained backlog itself.
- Feature displacement: [[gal-zellermayer-0-bugs-policy]] uses a five-frame planning example in which two bugs fall below sprint capacity as feature stories move upward, then reappear beside an additional bug next sprint.
- Reported culture effect: [[gal-zellermayer-0-bugs-policy]] says developers pursued higher quality when bugs could no longer be deferred, but provides no measurement.

## Counterevidence & Qualifications
The evidence is a 2016 practitioner essay based on the author's experience across several Scrum teams, not a controlled or comparative study. It does not report defect escape rate, severity, customer harm, throughput, time spent fixing, reopen rate, or outcomes before and after adoption. The planning images illustrate a mechanism rather than measured prevalence.

Closing a defect does not remove it from the product. A low-value cosmetic issue and a low-probability safety, security, data-integrity, accessibility, contractual, or regulatory issue cannot be judged by effort alone. Some organizations must retain known-issue records, formal risk acceptance, customer disclosures, or audit trails even when they choose not to repair immediately. Teams may also need bounded deferral when dependencies, incident stabilization, coordinated releases, or unavailable reproduction evidence make immediate resolution unsafe or impossible.

## What Changed
- Created the concept and distinguished zero open inventory from defect-free software.
- Preserved the source's fix-or-close economics while adding traceability and risk-governance boundaries.

## Related Concepts
- [[AgileSoftwareDevelopment]] - definition-of-done and sprint planning provide the policy's operating context.
- [[InternalSoftwareQuality]] - defect decisions affect correctness, change cost, and lifecycle maintenance.
- [[TechnicalDebtTracking]] - both manage future engineering liabilities, but defects are observable product failures rather than all forms of debt.
- [[ProductBacklogBuilding]] - mixed product backlogs create the prioritization surface the policy seeks to avoid.
- [[ChangeSafety]] - repair timing should account for the risk of introducing or amplifying failure.
