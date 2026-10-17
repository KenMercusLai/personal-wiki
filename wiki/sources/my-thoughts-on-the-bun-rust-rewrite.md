---
title: "My Thoughts on the Bun Rust Rewrite"
type: source
tags: [bun, zig, rust, software-quality, open-source, management]
date: 2026-07-09
source_file: "/mnt/ken_personal_wiki/Articles/My Thoughts on the Bun Rust Rewrite.md"
---

## Summary
[[AndrewKelley]] argues that [[Bun]]'s rewrite from [[Zig]] to Rust is better explained by organizational incentives, engineering practice, and the breakdown between Bun and the [[ZigSoftwareFoundation]] than by a simple language-feature comparison. He disputes several technical implications in Bun's announcement, welcomes the separation between the projects, and makes serious allegations about [[JarredSumner]]'s management and employment practices; those allegations are presented as Kelley's claims based partly on unnamed sources, not as independently verified findings.

## Key Claims
- [[OrganizationalEngineeringIncentives]] shape code quality because feature pressure, staffing, leadership, review, and time allocated to defect removal can matter more than a language-level safety mechanism.
- Kelley says Bun's rapid feature expansion accumulated hacks, assertion misuse, bugs, and technical debt despite repeated guidance from the Zig community.
- He challenges Bun's rewrite rationale by asking how its test suite can justify roughly one million lines of unreviewed translated code if that suite did not prevent the bugs attributed to the Zig implementation.
- He argues that reported LTO and binary-size improvements do not isolate a Rust effect because Zig supported LTO and much of the size work could have been performed before the rewrite.
- He says the published comparison omits a corresponding post-rewrite compilation-speed measurement and disputes the implication that Bun had already been fuzzing its Zig code.
- Kelley describes a values and relationship breakdown involving venture-backed urgency, Bun's engineering practices, the end of its annualized US$60,000 donation, its acquisition by [[Anthropic]], and the subsequent Rust rewrite.
- Kelley alleges, on the basis of firsthand accounts from two unnamed early-career programmers, that Sumner withheld wages and used bait-and-switch employment practices; the article withholds further detail to protect the alleged victims.

## Key Quotes
> "The main issue here had nothing to do with the language features of Zig vs Rust" - Kelley's central interpretation of the rewrite.

> "by dedicating engineering resources to it" - the mechanism Kelley says the language-versus-style-guide framing obscures.

## Connections
- [[AndrewKelley]] - author and Zig project leader presenting the retrospective.
- [[Bun]] - JavaScript toolchain whose Zig implementation and Rust rewrite are being assessed.
- [[Zig]] - original implementation language and community context for the dispute.
- [[JarredSumner]] - Bun founder and manager criticized throughout the account.
- [[ZigSoftwareFoundation]] - organization whose technical, financial, and community relationship with Bun ended.
- [[Anthropic]] - acquirer whose ownership precedes the rewrite in Kelley's account.
- [[InternalSoftwareQuality]] - the article argues that sustained engineering attention, not language choice alone, determines defect and maintenance outcomes.
- [[OrganizationalEngineeringIncentives]] - concept capturing the interaction among ownership, financing pressure, management, staffing, and engineering practice.
- [[TechnicalDebt]] - accumulated shortcuts and inadequate cleanup are presented as central causes of Bun's quality problems.
- [[HumanCodeResponsibility]] - the critique of a large unreviewed rewrite challenges the idea that tests alone transfer responsibility away from code review and engineering judgment.

## Contradictions
- The article directly disputes Bun's framing of its Rust rewrite, especially claims or implications concerning test sufficiency, fuzzing, LTO, binary size, and whether language choice explains the prior defect burden.
- Kelley's account is an openly resentful retrospective from the leader of the language project being left behind. It supplies no repository analysis, benchmark protocol, defect comparison, employment records, responses from Sumner or Anthropic, or named corroborating witnesses.
- The managerial and employment allegations are serious but not independently verified within the source. They should not be converted into settled biographical facts.
- The article does not establish whether the Rust rewrite improved correctness, maintainability, compilation speed, employee conditions, or long-run project outcomes; it primarily challenges Bun's causal explanation.
- The supplied Markdown contains no effective image references, so no visual evidence or retained asset was required.
