---
title: "Parallel Running"
type: concept
tags: [software-architecture, migration, testing, observability]
sources:
  - blog-ian-cartwright-rob-horn-james-lewis-martinfowler-com-divert-the-flow
last_updated: 2026-09-25
knowledge_schema: synthesis-v1
---

## Definition
[[ParallelRunning]] is a migration-validation technique that operates old and replacement implementations concurrently and reconciles their outputs before, during, or after a staged cutover.

## Current Synthesis
For a replaced [[CriticalAggregator]], parallel running makes disagreement observable while business knowledge is still available to interpret it. The source recommends building reports in slices, taking each to a production-like environment, comparing known inputs and worked outputs where possible, and using beta cohorts before full cutover.

Exact equality is not the objective by itself because legacy outputs can contain bugs or off-system manual adjustments. Teams need tolerances, explained differences, and a judgment about which result is correct. Automated feed and output monitoring can keep selective comparison in place after cutover without turning reconciliation into permanent manual work.

## Key Claims
- Concurrent execution reduces cutover uncertainty by exposing differences before the legacy path is removed.
- Known test inputs and worked expected outputs make mismatches more diagnosable.
- Legacy and replacement outputs should not be assumed correct merely because they agree or differ.
- Reconciliation needs thresholds, ownership, alerting, and a finite migration purpose.
- Staged user cohorts can combine technical comparison with early usability feedback.

## Evidence
- Delivery sequence: [[blog-ian-cartwright-rob-horn-james-lewis-martinfowler-com-divert-the-flow]] recommends implementing each report through a production-like environment and monitoring it while remaining reports are built.
- Test design: [[blog-ian-cartwright-rob-horn-james-lewis-martinfowler-com-divert-the-flow]] recommends known injected data and expected outputs, ideally through both implementations.
- Interpretation: [[blog-ian-cartwright-rob-horn-james-lewis-martinfowler-com-divert-the-flow]] warns that old reports often contain undiscovered issues, so mismatches need investigation.
- Operational extension: [[blog-ian-cartwright-rob-horn-james-lewis-martinfowler-com-divert-the-flow]] recommends alerting when old and new implementations diverge beyond tolerance.

## Counterevidence & Qualifications
The source notes that legacy test environments and data injection may be unavailable or too complex, leaving only the replacement system testable. Parallel operation also adds compute, data, reconciliation, privacy, and operational cost, and its value declines if the comparison lacks authoritative expectations or responsible reviewers.

## What Changed
- Created the concept from the source's iterative delivery, testing, cutover, and monitoring guidance.

## Related Concepts
- [[DivertTheFlow]] - migration strategy whose outputs are validated through parallel operation.
- [[CriticalAggregator]] - common target where business-critical figures require reconciliation.
- [[TransitionalArchitecture]] - temporary old/new coexistence that makes parallel running possible.
- [[LegacyDisplacement]] - broader migration process whose cutover risk is being reduced.
- [[EventInterception]] - can provide comparable activity to the replacement during transition.
