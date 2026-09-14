---
title: "Code Review Practice"
type: concept
tags: [software-engineering, review, teamwork]
sources:
  - 7-best-practices-for-doing-code-reviews
  - blog-mahesh-balakrishnan-42-things-i-learned-from-building-a-production-database
last_updated: 2026-09-14
knowledge_schema: synthesis-v1
---

## Definition
[[CodeReviewPractice]] is the human workflow of inspecting, discussing, and approving code changes so teams improve shared understanding, change quality, and delivery flow.

## Current Synthesis
The Asana source frames code review as a team coordination and learning practice first. Reviewers and authors should agree on the purpose of review, because a review optimized for style enforcement, bug discovery, or knowledge transfer will produce different comments and different emotional effects.

The article's practical stance is execution-backed and flow-conscious. Reviewers should run the app, inspect the change in a real development environment, use breakpoints when lifecycle behavior is unclear, and read whole-file context rather than only textual diffs. At the same time, they should respond quickly, share partial understanding when blocked, and avoid requiring another review round for simple suggestions unless they can prove a behavioral bug.

Balakrishnan's production database source adds a critical-infrastructure qualification. For components where correctness failures are expensive, review speed is not the primary metric. Teams may need two accepts or even unanimous approval from a selected group, a culture where reviewers freely raise concerns, and author norms that treat critique with gratitude. The stricter stance is not a contradiction of flow-conscious review; it says review policy should scale with risk.

## Key Claims
- Teams should explicitly choose the goals of code review before relying on it.
- Code review is especially valuable for spreading codebase knowledge and helping engineers understand how teammates think.
- Running the app, using breakpoints, and checking local compiler or test feedback reveal behavior that diff reading may miss.
- Predicting expected changed files and visualizing call relationships turn reviewing into active learning.
- Prompt first-pass reviews and clear next steps reduce teammate blocking.
- Approval should not be withheld for simple style or refactoring preferences when no bug is proven.
- Critical infrastructure reviews may need stricter approval gates and longer review cycles than ordinary product diffs.

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

## Counterevidence & Qualifications
The sources are practitioner reflections rather than universal empirical studies. Asana's default-to-approval rule fits low-risk suggestions and simple cleanup better than safety-critical code, security-sensitive changes, migrations, unclear ownership boundaries, or changes without adequate verification. Balakrishnan's stricter review gates fit critical infrastructure better than routine low-risk changes, where excessive approval requirements could block useful cleanup and learning.

## What Changed
- Created the concept to capture code review as a team learning, feedback, and delivery-flow practice.
- Added the production-infrastructure qualification that critical components may justify slower review, multiple accepts, and discardable candidate code.

## Related Concepts
- [[PRReviewHygiene]] - review hygiene shapes code changes and feedback so human review remains usable.
- [[SoftwareVerification]] - tests and execution provide behavioral evidence that review alone may miss.
- [[WorkplaceLearning]] - active reviewing can teach codebase structure and teammate reasoning.
- [[HumanCodeResponsibility]] - reviewers and authors remain responsible for clear approval boundaries and follow-up.
- [[ProductionInfrastructureLeadership]] - infrastructure leads tune review norms to component criticality and correctness risk.
