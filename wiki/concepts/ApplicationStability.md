---
title: "Application Stability"
type: concept
tags: [reliability, crashes, monitoring, software-quality]
sources:
  - not-all-bugs-are-worth-fixing-and-thats-okay-bugsnag-blog
last_updated: 2026-10-01
knowledge_schema: synthesis-v1
---

## Definition
[[ApplicationStability]] is a release- and user-centered measure of successful application interactions, commonly operationalized as the share of sessions that do not end in a crash or unhandled error and compared with an explicit target.

## Current Synthesis
The Bugsnag article makes stability a resource-allocation signal rather than a promise of perfect software. Teams select an achievable target, observe crash or error experience across real sessions, and use the gap from that target to decide whether engineering capacity should move from the product roadmap toward defect repair.

This framing is especially useful in client applications whose operating conditions vary across browsers, versions, extensions, mobile devices, and settings. Segmentation can separate widespread failures from rare environmental edge cases, while frequent delivery shortens the correction loop after launch. The same cadence can allow more defects into production when it compresses traditional testing, so deployment speed does not replace feedback.

Crash-free sessions remain a partial proxy for software quality. A stable score can miss incorrect results, data loss, security or privacy exposure, accessibility failures, severe slowness, and recoverable errors that still block a user's goal. The target therefore needs risk classes and qualitative escalation rules rather than acting as the sole repair threshold.

## Key Claims
- Stability targets can make feature-versus-fix allocation explicit and accountable.
- Real-session crash or unhandled-error rates provide a user-impact signal that raw defect counts do not.
- Browser and device fragmentation makes reach and environment segmentation important to defect priority.
- Fast release cycles strengthen correction feedback but can also increase production escape risk when testing is compressed.
- A target below 100% acknowledges diminishing returns without excusing high-consequence failures.
- Crash-free sessions are an incomplete quality measure and require additional risk signals.

## Evidence
- Target and allocation rule: [[not-all-bugs-are-worth-fixing-and-thats-okay-bugsnag-blog]] recommends an achievable stability target to decide whether sprint capacity should favor the roadmap or defect repair.
- User-session measurement: [[not-all-bugs-are-worth-fixing-and-thats-okay-bugsnag-blog]] defines stability through successful interactions and the percentage of users experiencing crashes in a release.
- Environmental segmentation: [[not-all-bugs-are-worth-fixing-and-thats-okay-bugsnag-blog]] points to browser, extension, version, device, and setting variance as a source of low-reach client-side edge cases.
- Feedback-loop tradeoff: [[not-all-bugs-are-worth-fixing-and-thats-okay-bugsnag-blog]] argues that continuous deployment enables quicker post-launch repair while reduced traditional QA time can raise escape risk.

## Counterevidence & Qualifications
The evidence is a vendor-authored practitioner article promoting stability monitoring, not a comparative study. It reports no target-selection method, before-and-after outcomes, repair-cost distribution, retention effect, or evidence that teams using the metric allocate capacity better.

Its crash-centered definition is too narrow for a complete quality or reliability judgment. Rare failures can still demand immediate repair when they affect safety, security, privacy, data integrity, accessibility, contractual obligations, or regulation. Conversely, a widespread but low-consequence handled error may need a different response from a crash. Targets should therefore be segmented by product, workflow, release, environment, and consequence where possible.

## What Changed
- Established stability as a user-impact signal for feature-versus-fix allocation.
- Bounded crash-free targets with non-crash quality signals and high-consequence risk classes.

## Related Concepts
- [[ZeroBugsPolicy]] - adds an explicit fix-or-close inventory decision around the stability signal.
- [[SystemReliability]] - provides the broader system behavior and recovery context that session stability only partially measures.
- [[ServiceObservability]] - supplies the telemetry and alerting needed to detect stability changes.
- [[InternalSoftwareQuality]] - affects the cost and safety of repairing defects and changing the product.
- [[AgileSoftwareDevelopment]] - short delivery cycles create the feedback cadence in which stability targets guide planning.
- [[ChangeSafety]] - limits the chance that rapid fixes or releases create new failures.
