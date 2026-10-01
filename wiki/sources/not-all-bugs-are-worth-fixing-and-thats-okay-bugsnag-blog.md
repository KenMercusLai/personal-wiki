---
title: "Not all bugs are worth fixing and that's okay"
type: source
tags: [bugs, application-stability, agile, software-quality]
date: 2018-08-01
source_file: "/mnt/ken_personal_wiki/Articles/Not all bugs are worth fixing and that's okay - Bugsnag Blog.md"
---

## Summary
This [[Bugsnag]] article argues that defect work should be allocated by observed user impact and an achievable [[ApplicationStability]] target rather than by an impossible goal of defect-free software. It connects crash-free sessions, release-level feedback, and environment segmentation to explicit choices between feature work and bug repair, while acknowledging that browser and mobile fragmentation produce rare edge cases. The piece supports the fix-or-close boundary in [[ZeroBugsPolicy]], but its claims are vendor-authored, historically bounded, and unsupported by comparative outcome data.

## Key Claims
- No production application is literally bug-free, so a 100% stability target can impose diminishing returns and displace higher-value feature work.
- [[ApplicationStability]] can be expressed as the percentage of successful or crash-free application sessions in a release and used as a team accountability target.
- Fast release cycles make post-launch correction easier, while reduced traditional QA time can also increase the chance that defects reach production.
- Client-side browser, extension, version, device, and configuration fragmentation creates many edge cases that affect only a small share of users.
- Teams should distinguish frequently encountered, high-impact defects from rare issues and use a monitoring feedback loop to decide when stability work should interrupt the roadmap.
- An achievable stability target can turn the feature-versus-fix tradeoff into a data-informed resource decision rather than an automatic demand to repair every known defect.

## Key Quotes
> “There's no such thing as a bug free application” — premise for choosing a stability target rather than promising perfection.

> “It's not worth it to spend hours fixing a bug that only impacts a few users.” — the article's user-impact allocation rule.

## Connections
- [[Bugsnag]] - company publishing the article and offering the monitoring approach it recommends.
- [[ApplicationStability]] - crash-free interaction metric and target used to allocate engineering attention.
- [[ZeroBugsPolicy]] - complementary fix-or-close rule for avoiding an indefinitely deferred defect inventory.
- [[InternalSoftwareQuality]] - quality investment is bounded by lifecycle value, user impact, and opportunity cost rather than perfection.
- [[AgileSoftwareDevelopment]] - fast iteration and continuous deployment create both quicker correction loops and additional production-escape risk.
- [[SystemReliability]] - application stability is a user-session view of reliable operation rather than a complete reliability model.

## Contradictions
- Qualifies any literal reading of “zero bugs”: the article argues that rare, low-impact defects may rationally remain unfixed, while [[ZeroBugsPolicy]] already permits explicit closure rather than indefinite deferral.
- Qualifies blanket advice to fix defects as early as possible by adding user reach, impact, repair cost, and feature opportunity cost to the decision.
- The article defines stability mainly through crashes or unhandled errors; non-crashing corruption, security, accessibility, privacy, performance, and workflow failures may be severe without lowering that metric.
- The exact publication day and author are absent from the captured Markdown and were not recoverable from the original URL; the date records the independently indexed August 2018 publication window rather than a verified day.
