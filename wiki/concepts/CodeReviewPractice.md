---
title: "Code Review Practice"
type: concept
tags: [software-engineering, review, teamwork]
sources:
  - 7-best-practices-for-doing-code-reviews
  - blog-mahesh-balakrishnan-42-things-i-learned-from-building-a-production-database
  - 3-strategies-for-picking-your-battles-as-a-software-developer
  - wei-shen-me-ai-xie-dai-ma-geng-kuai-dan-jiao-fu-mei-bian-yi-ji-wo-zen-me-ba-ta-ban-hui-lai-de
last_updated: 2026-09-15
knowledge_schema: synthesis-v1
---

## Definition
[[CodeReviewPractice]] is the human workflow of inspecting, discussing, and approving code changes so teams improve shared understanding, change quality, and delivery flow.

## Current Synthesis
The Asana source frames code review as a team coordination and learning practice first. Reviewers and authors should agree on the purpose of review, because a review optimized for style enforcement, bug discovery, or knowledge transfer will produce different comments and different emotional effects.

The article's practical stance is execution-backed and flow-conscious. Reviewers should run the app, inspect the change in a real development environment, use breakpoints when lifecycle behavior is unclear, and read whole-file context rather than only textual diffs. At the same time, they should respond quickly, share partial understanding when blocked, and avoid requiring another review round for simple suggestions unless they can prove a behavioral bug.

Balakrishnan's production database source adds a critical-infrastructure qualification. For components where correctness failures are expensive, review speed is not the primary metric. Teams may need two accepts or even unanimous approval from a selected group, a culture where reviewers freely raise concerns, and author norms that treat critique with gratitude. The stricter stance is not a contradiction of flow-conscious review; it says review policy should scale with risk.

Head adds an interpersonal triage layer. In ordinary review disagreement, a reviewer should ask whether the issue is a real codebase standard, a non-trivial performance concern, or a readability problem before turning preference into pressure. When a teammate is ramping into project standards, conversation is more likely to work than tearing apart a review line by line. This turns review judgment into both a quality decision and a morale decision.

AI-heavy work adds a capacity-management layer. When AI doubles or triples local code production, review can become the real constraint: larger PRs and more queued PRs make feedback slower, context switching worse, and delivery no better. In this practice, code review is not only a quality gate or learning ritual; it is a scarce system resource that must be protected through PR sizing, pre-review verification, WIP limits, and risk-based escalation.

## Key Claims
- Teams should explicitly choose the goals of code review before relying on it.
- Code review is especially valuable for spreading codebase knowledge and helping engineers understand how teammates think.
- Running the app, using breakpoints, and checking local compiler or test feedback reveal behavior that diff reading may miss.
- Predicting expected changed files and visualizing call relationships turn reviewing into active learning.
- Prompt first-pass reviews, clear next steps, non-blocking treatment of simple preferences, and WIP-aware PR sizing reduce teammate blocking.
- Critical infrastructure reviews may need stricter approval gates and longer review cycles than ordinary product diffs.
- Reviewers should separate project standards, material performance, and readability concerns from personal style preferences.

## Evidence
- Review purpose: [[7-best-practices-for-doing-code-reviews]] recommends a team conversation about whether reviews are meant for style, bug catching, shared understanding, or knowledge spread.
- Knowledge sharing: [[7-best-practices-for-doing-code-reviews]] values review for learning coworkers' thinking and ensuring more than one teammate can diagnose changed areas.
- Execution-backed review: [[7-best-practices-for-doing-code-reviews]] recommends running the app, using breakpoints, pulling the change locally, and checking compile errors, warnings, and test failures.
- Active reviewing: [[7-best-practices-for-doing-code-reviews]] recommends visualizing method calls and predicting changed files before reading the diff.
- Review flow: [[7-best-practices-for-doing-code-reviews]] recommends quick first passes, timeboxing difficult reviews, and clear communication when a reviewer is not ready or qualified to approve.
- Approval norm: [[7-best-practices-for-doing-code-reviews]] argues that simple renames or refactors usually should not block approval when the reviewer cannot prove a bug.
- Critical component gates: [[blog-mahesh-balakrishnan-42-things-i-learned-from-building-a-production-database]] suggests two accepts or unanimous approval from selected ICs for critical components.
- Review depth over speed: [[blog-mahesh-balakrishnan-42-things-i-learned-from-building-a-production-database]] says time to landing a diff is not the key metric for critical components.
- Throwaway culture: [[blog-mahesh-balakrishnan-42-things-i-learned-from-building-a-production-database]] says teams should be willing to discard candidate code when review reveals the design is wrong.
- Preference triage: [[3-strategies-for-picking-your-battles-as-a-software-developer]] recommends letting a good PR go when feedback is not a codebase best practice, material performance issue, or readability problem.
- Conversation over critique: [[3-strategies-for-picking-your-battles-as-a-software-developer]] says standards mismatch with someone ramping into a project is better handled through conversation than exhaustive line-by-line critique.
- AI review bottleneck: [[wei-shen-me-ai-xie-dai-ma-geng-kuai-dan-jiao-fu-mei-bian-yi-ji-wo-zen-me-ba-ta-ban-hui-lai-de]] argues that AI can increase PR count and PR size faster than reviewer bandwidth, leaving organizational delivery unchanged.
- WIP control: [[wei-shen-me-ai-xie-dai-ma-geng-kuai-dan-jiao-fu-mei-bian-yi-ji-wo-zen-me-ba-ta-ban-hui-lai-de]] recommends limiting review-stage work in progress so parallel agent output does not recreate downstream accumulation.

## Counterevidence & Qualifications
The sources are mostly practitioner reflections rather than universal empirical studies, though the AI coding bottleneck source cites industry telemetry for review latency and PR growth. Asana's default-to-approval rule fits low-risk suggestions and simple cleanup better than safety-critical code, security-sensitive changes, migrations, unclear ownership boundaries, or changes without adequate verification. Balakrishnan's stricter review gates fit critical infrastructure better than routine low-risk changes, where excessive approval requirements could block useful cleanup and learning. Head's advice to let some issues go assumes the code is already good enough; it should not be used to avoid raising genuine maintainability, security, accessibility, or correctness concerns.

## What Changed
- Created the concept to capture code review as a team learning, feedback, and delivery-flow practice.
- Added the production-infrastructure qualification that critical components may justify slower review, multiple accepts, and discardable candidate code.
- Added the AI coding bottleneck view: review bandwidth, PR size, and WIP limits determine whether generated code becomes delivered value.

## Related Concepts
- [[PRReviewHygiene]] - review hygiene shapes code changes and feedback so human review remains usable.
- [[SoftwareVerification]] - tests and execution provide behavioral evidence that review alone may miss.
- [[WorkplaceLearning]] - active reviewing can teach codebase structure and teammate reasoning.
- [[HumanCodeResponsibility]] - reviewers and authors remain responsible for clear approval boundaries and follow-up.
- [[ProductionInfrastructureLeadership]] - infrastructure leads tune review norms to component criticality and correctness risk.
- [[WorkplaceCollaboration]] - review comments affect team trust, pride, and willingness to keep improving shared code.
- [[BottleneckAwareAICoding]] - treats review as the likely downstream constraint after AI accelerates coding.
