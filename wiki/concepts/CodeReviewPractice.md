---
title: "Code Review Practice"
type: concept
tags: [software-engineering, review, teamwork]
sources:
  - 7-best-practices-for-doing-code-reviews
  - blog-mahesh-balakrishnan-42-things-i-learned-from-building-a-production-database
  - 3-strategies-for-picking-your-battles-as-a-software-developer
  - wei-shen-me-ai-xie-dai-ma-geng-kuai-dan-jiao-fu-mei-bian-yi-ji-wo-zen-me-ba-ta-ban-hui-lai-de
  - cyle-how-i-review-code
last_updated: 2026-09-23
knowledge_schema: synthesis-v1
---

## Definition
[[CodeReviewPractice]] is the human workflow of inspecting, discussing, and approving code changes so teams improve shared understanding, change quality, and delivery flow.

## Current Synthesis
The sources frame code review as a team coordination, explanation, and learning practice rather than a single-purpose bug hunt. Reviewers and authors should agree on the goal because review optimized for style enforcement, defect discovery, shared understanding, or risk control will produce different comments and gates. Cyle adds a long-term audience: a pull request should preserve enough motivation and context for someone investigating the code months or years later.

The practical stance is execution-backed and flow-conscious. Reviewers should run the app, inspect real development-environment feedback, use breakpoints when lifecycle behavior is unclear, and read whole-file context rather than only diffs. Automated style checks can remove mechanical work so human attention goes to intent, clarity, documentation, scope, and maintainability. Small pull requests, quick first passes, explicit deferred work, and follow-up after revisions keep the review loop moving.

Balakrishnan's production database source adds a critical-infrastructure qualification. For components where correctness failures are expensive, review speed is not the primary metric. Teams may need two accepts or even unanimous approval from a selected group, a culture where reviewers freely raise concerns, and author norms that treat critique with gratitude. The stricter stance is not a contradiction of flow-conscious review; it says review policy should scale with risk.

Head and Cyle add an interpersonal layer. A reviewer should distinguish codebase standards, material performance, and readability concerns from personal preference, then adapt help to the author's experience and familiarity with the codebase. Examples and references may help a junior engineer, while an experienced engineer may need a prompt to document an opaque abstraction. In every case, feedback should give the author the benefit of the doubt and remain safe for the wider team to read.

AI-heavy work adds a capacity-management layer. When AI doubles or triples local code production, review can become the real constraint: larger PRs and more queued PRs make feedback slower, context switching worse, and delivery no better. In this practice, code review is not only a quality gate or learning ritual; it is a scarce system resource that must be protected through PR sizing, pre-review verification, WIP limits, and risk-based escalation.

## Key Claims
- Teams should choose review goals and approval strictness according to the change's purpose and risk.
- Reviews should preserve motivation and decision context while spreading codebase knowledge to current and future engineers.
- Execution, tests, development tooling, and automated style checks should support human judgment rather than leaving every check to diff reading.
- Small changes, prompt first passes, explicit next steps, revision follow-up, and bounded review-stage work reduce blocking and queue growth.
- Reviewers should separate genuine standards, performance, readability, and correctness concerns from personal preference.
- Feedback should adapt to the author's experience while remaining respectful and useful to the wider team.
- Critical infrastructure may justify multiple accepts, slower review, and discarded candidate code that would be excessive for routine low-risk changes.

## Evidence
- Purpose and audience: [[7-best-practices-for-doing-code-reviews]] distinguishes review goals; [[cyle-how-i-review-code]] requires enough motivation and context for future engineers to understand an old change.
- Shared learning: [[7-best-practices-for-doing-code-reviews]] recommends predicting files and visualizing calls; [[cyle-how-i-review-code]] says engineers learn by reading other people's reviews.
- Tool-supported judgment: [[7-best-practices-for-doing-code-reviews]] recommends running the app and checking compiler, test, and runtime feedback; [[cyle-how-i-review-code]] says Tumblr automated coding-standard enforcement so reviewers could focus on clarity and documentation.
- Flow and scope: [[cyle-how-i-review-code]] favors small PRs, ticket-linked deferral, prompt review, and follow-up after revisions; [[wei-shen-me-ai-xie-dai-ma-geng-kuai-dan-jiao-fu-mei-bian-yi-ji-wo-zen-me-ba-ta-ban-hui-lai-de]] shows how oversized AI-generated queues can saturate reviewer capacity.
- Preference triage: [[3-strategies-for-picking-your-battles-as-a-software-developer]] recommends letting a good PR go when feedback is not about a standard, material performance, or readability; [[7-best-practices-for-doing-code-reviews]] similarly discourages blocking simple non-bug suggestions.
- Author-aware communication: [[cyle-how-i-review-code]] varies examples, references, documentation requests, and explanation by author context while insisting that comments remain kind and appropriate for any reader.
- Risk-scaled gates: [[blog-mahesh-balakrishnan-42-things-i-learned-from-building-a-production-database]] supports multiple accepts, slower landing, and throwing away wrong candidate code for critical components.

## Counterevidence & Qualifications
The sources are mostly practitioner reflections rather than universal empirical studies, though the AI coding bottleneck source cites industry telemetry for review latency and PR growth. Tumblr's reported workflow is a historical case from one large company, and author-sensitive feedback can become inconsistent or paternalistic if it substitutes assumptions about seniority for evidence in the change. Default-to-approval and ticketed deferral fit low-risk, traceable work better than unresolved safety, security, accessibility, migration, or correctness risk. Conversely, Balakrishnan's stricter gates fit critical infrastructure better than routine changes, where excessive approvals can block cleanup and learning.

## What Changed
- Review now includes durable decision context for future maintainers, not only immediate feedback and approval.
- Reviewer judgment now explicitly combines author-aware coaching with respectful, publicly readable communication.
- Flow guidance now includes small scope, traceable deferral, prompt response, revision follow-up, and WIP control.
- Risk remains the main qualification: critical components may justify slower review, multiple accepts, and discarded candidate code.

## Related Concepts
- [[PRReviewHygiene]] - review hygiene shapes code changes and feedback so human review remains usable.
- [[SoftwareVerification]] - tests and execution provide behavioral evidence that review alone may miss.
- [[WorkplaceLearning]] - active reviewing can teach codebase structure and teammate reasoning.
- [[HumanCodeResponsibility]] - reviewers and authors remain responsible for clear approval boundaries and follow-up.
- [[ProductionInfrastructureLeadership]] - infrastructure leads tune review norms to component criticality and correctness risk.
- [[WorkplaceCollaboration]] - review comments affect team trust, pride, and willingness to keep improving shared code.
- [[BottleneckAwareAICoding]] - treats review as the likely downstream constraint after AI accelerates coding.
