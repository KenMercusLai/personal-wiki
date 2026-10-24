---
title: "I don't want your PRs anymore"
type: source
tags: [open-source, software-engineering, ai-coding, pull-requests]
date: 2026-04-06
source_file: /mnt/ken_personal_wiki/Articles/i-dont-want-your-prs-anymore.md
---

## Summary
An unnamed open-source maintainer argues that AI-assisted implementation has made unsolicited pull requests less valuable than the security review, preference alignment, synchronization, and contributor back-and-forth they require. The article does not reject outside participation: it redirects contributors toward feedback, design discussion, investigated bug reports, illustrative prototypes and prompts, code review, and independent forks while placing the maintainer's bottleneck in understanding, design, and review rather than code production.

## Key Claims
- Unknown contributors create a distinct malicious-change risk, while their formatting, structure, dependency, and design preferences can make a patch slower to review than a maintainer-authored implementation.
- AI assistance lowers the cost of reproducing a requested change under the maintainer's existing instructions and allows rapid iteration without cross-time-zone coordination.
- Easier code generation shifts the scarce work in software development toward understanding an existing system, designing the right change, and reviewing whether an implementation matches intent.
- A contributed patch does not necessarily reduce those bottlenecks, so mergeable code should not be treated as the default or highest-value form of open-source participation.
- Feedback, idea discussion, reproducible and investigated bug reports, and review can improve the maintainer's judgment without transferring implementation ownership.
- A reference pull request can remain useful as an executable prototype, especially when accompanied by the prompt that produced it, even if the maintainer rewrites rather than merges it.
- Cheap customization makes a fork a legitimate endpoint: contributors can pursue their own use case and report what they learn without forcing consensus or upstream integration.

## Key Quotes
> "The code in your PR doesn't help me much with any of these." - on understanding, design, and review remaining the maintainer's bottlenecks.

> "A good bug report is 3/4 of the bug itself being fixed." - on investigation as a higher-value contribution than implementation alone.

## Connections
- [[OpenSourceProjectMaintenance]] - reframes unsolicited patch acceptance as a discretionary use of scarce maintainer attention rather than the default collaboration path.
- [[OpenSourceCollaborationModels]] - describes an AI-assisted maintainer model with public feedback and forking but concentrated upstream implementation authority.
- [[CodeReviewPractice]] - distinguishes reviewing trusted local agent output from assessing unknown external code, contributor intent, and preference mismatch.
- [[AICodingPractice]] - moves human effort from writing code toward system understanding, design, and acceptance judgment.
- [[BottleneckAwareAICoding]] - treats implementation speed as useful only when it reduces the actual constraint rather than adding review and coordination work.
- [[ExitAsGovernance]] - presents forking as a way to pursue divergent needs without prolonged consensus or permission seeking.

## Contradictions
- The source tensions [[OpenSourceProjectMaintenance]] advice to delegate early and welcome contributor patches by arguing that AI-assisted maintainer implementation can now cost less than reviewing unknown contributors. The disagreement is conditional rather than universal because the article gives no project size, team structure, risk model, contribution history, or comparative timing data.
- It narrows collaborative accounts of [[CodeReviewPractice]]: review can spread context and teach teammates, but an unknown outside contributor may add security and synchronization costs that do not apply to a trusted team.
- The preference for local agent output does not establish that model-generated code is safer overall. It reduces the author's concern about malicious human intent while leaving defects, dependency risk, prompt mistakes, compromised tooling, and inadequate verification unresolved.
