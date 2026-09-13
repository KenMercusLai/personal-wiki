---
title: "Investigate and Fix Flow"
type: concept
tags: [ux, developer-tools, product-design]
sources:
  - advocating-for-a-complete-product-redesign-google-design-medium
last_updated: 2026-09-13
knowledge_schema: synthesis-v1
---

## Definition
[[InvestigateAndFixFlow]] is the recurring Crashlytics user micro-journey in which a developer identifies a stability problem, investigates crash evidence, prioritizes the issue, and works toward a fix.

## Current Synthesis
The source presents the investigate-and-fix flow as the common structure beneath several Crashlytics use cases. Whether a developer is monitoring a new release, checking app stability, prioritizing crashes, or debugging a customer problem, the same core loop appears: notice stability information, inspect issue detail, understand affected versions/users/devices, and use diagnostic material such as stack traces, logs, keys, and data to resolve the crash. The inspected Firebase screenshots show the redesigned interface making that loop more visible through overview metrics, issue tables, device/version cards, sessions, and diagnostic tabs.

## Key Claims
- A mature product can contain repeated micro-journeys across otherwise distinct use cases.
- Finding the repeated flow helps a team choose which information deserves higher hierarchy.
- Crash debugging requires linking overview signals to issue detail and diagnostic evidence.
- The redesigned Firebase surface appears structured around moving from crash trends to specific issues and then to sessions and stack traces.
- The flow gave the team a shared foundation for redesign decisions.

## Evidence
- Recurring flow: [[advocating-for-a-complete-product-redesign-google-design-medium]] says mapping four user journeys revealed the investigate-and-fix flow across all of them.
- Use-case coverage: [[advocating-for-a-complete-product-redesign-google-design-medium]] names monitoring a new release, checking stability, prioritizing crashes, and debugging a customer problem as journeys tied to the flow.
- Interface evidence: [[advocating-for-a-complete-product-redesign-google-design-medium]] includes inspected images showing crash-free statistics, event trends, issues, affected users, versions, device and operating-system breakdowns, sessions, stack traces, keys, logs, and data.
- Alignment role: [[advocating-for-a-complete-product-redesign-google-design-medium]] says the shared flows aligned the team on how users use Crashlytics.

## Counterevidence & Qualifications
The term is source-specific and tied to Crashlytics. Other developer tools may have similar investigate-and-resolve loops, but this page should not generalize beyond crash-reporting workflows without additional sources.

## What Changed
- Created the concept page for the recurring Crashlytics investigate-and-fix journey.

## Related Concepts
- [[UserJourneyMapping]] - method that surfaced the recurring flow.
- [[ProductRedesign]] - the flow shaped redesign priorities.
- [[InformationHierarchy]] - the flow indicates which evidence belongs near the top of the interface.
- [[Crashlytics]] - product case where the flow appears.
- [[CLIApplicationDesign]] - both concern developer-tool UX organized around task flow.
