---
title: "Write less code, be more responsible"
type: source
tags: [ai, software-engineering, open-source, responsibility]
date: 2026-04-11
source_file: "/mnt/ken_personal_wiki/Articles/Write less code, be more responsible - Orhun's Blog.md"
---

## Summary
[[OrhunParmaksiz]] argues that AI-assisted programming changes how code is produced without transferring responsibility for the resulting product. His preferred [[AICodingPractice]] mixes AI for tedious or difficult work with manual implementation of enjoyable parts, followed by a human quality pass; the essay treats unreviewed [[VibeCoding]] as a maintainability and user-safety risk rather than rejecting AI use itself. It also raises unresolved licensing and FOSS-ethics questions without claiming a legal answer.

## Key Claims
- [[HumanCodeResponsibility]] remains with the person who publishes software, regardless of whether they or an AI agent typed the implementation.
- A commit-by-commit workflow in which every generated line is reviewed and understood improves control, but can turn programming into continuous code review and reduce the enjoyment of craft.
- A mixed workflow can reserve AI for tedious or slow tasks, preserve personally meaningful coding, and use a final human pass to enforce the desired quality bar.
- Faster AI-assisted production increases the supply of software without guaranteeing maintainability, safe future releases, or trustworthy open-source stewardship.
- Developers should experiment openly with AI workflows and choose a balance that fits their goals rather than treating tool use as a shameful secret.
- AI-generated code creates unsettled licensing and FOSS-ethics questions; the author explicitly offers no legal conclusion.

## Key Quotes
> "you are still responsible for the end product" — on accountability surviving a change in tools.

> "read everything to the last semicolon" — on the author's initial quality-control rule for AI-generated commits.

> "don't vibe code and commit" — the essay's compressed warning against publishing unreviewed output.

## Connections
- [[OrhunParmaksiz]] — author reflecting on AI-assisted programming from an open-source maintainer's perspective.
- [[Codex]] — coding agent used in the author's cargo-tree-tui workflow experiment.
- [[AICodingPractice]] — the essay compares unrestricted delegation, exhaustive commit review, and a mixed human–AI workflow.
- [[HumanCodeResponsibility]] — central principle that the publisher owns quality, maintainability, and user consequences.
- [[VibeCoding]] — criticized when fast generation is allowed to bypass understanding and review.
- [[CodeReviewPractice]] — exhaustive review restores control but can become the dominant and less enjoyable form of work.
- [[OpenSourceProjectMaintenance]] — public contribution creates continuing quality and release-safety obligations.
- [[AIDependencySkillAtrophy]] — the author's feeling of becoming lost and “illiterate” under unrestricted delegation echoes skill and understanding risks.

## Contradictions
- Partly qualifies strongly automation-positive [[AICodingPractice]] accounts: faster implementation can preserve output while replacing enjoyable construction with review labor and leaving maintainability risk with the human.
- The licensing discussion is an open question, not evidence that AI-generated code has one settled license or that all LLM use is incompatible with FOSS.
