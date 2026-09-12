---
title: "Upstream Divergence Policy"
type: concept
tags: [software-engineering, migration, architecture, testing]
sources:
  - yong-claude-code-jiang-san-wan-hang-go-xiang-mu-yi-zhi-dao-rust-agent-team-shi-jian-yu-harness-xiao-lu-you-hua
last_updated: 2026-09-12
knowledge_schema: synthesis-v1
---

## Definition
[[UpstreamDivergencePolicy]] is an explicit rule set for deciding when a port or rewrite should preserve upstream behavior, warn about it, or reject it.

## Current Synthesis
The source presents upstream divergence as one of the hardest parts of a rewrite: copying an upstream bug may preserve compatibility, but it can also silently reproduce unsafe or misleading behavior. ADR-0002 handles this with a two-class decision framework. Class A differences affect safety, privacy, or routing intent and become hard load-time errors. Class B differences affect performance, compatibility, deprecated paths, or slower behavior and become warn-once behavior while continuing to run.

## Key Claims
- Ports need explicit divergence rules because upstream-compatible behavior is not automatically correct.
- Safety, privacy, and routing-intent differences should fail loudly rather than silently degrade.
- Performance or deprecated-compatibility differences can often warn once and continue.
- A default rule helps implementation agents proceed when a spec misses an edge case.
- Test cases should cite the divergence class so reviewers can see the intended policy.

## Evidence
- Class A definition: [[yong-claude-code-jiang-san-wan-hang-go-xiang-mu-yi-zhi-dao-rust-agent-team-shi-jian-yu-harness-xiao-lu-you-hua]] classifies VMess `cipher: zero`, sniffer peek IO errors, and `default-nameserver` bootstrap loops as hard errors.
- Class B definition: [[yong-claude-code-jiang-san-wan-hang-go-xiang-mu-yi-zhi-dao-rust-agent-team-shi-jian-yu-harness-xiao-lu-you-hua]] classifies `alterId > 0`, unknown cipher fallback, server-side mux ignoring, and deprecated field aliases as warn-and-continue behavior.
- Default rule: [[yong-claude-code-jiang-san-wan-hang-go-xiang-mu-yi-zhi-dao-rust-agent-team-shi-jian-yu-harness-xiao-lu-you-hua]] says uncertain cases should default to Class A and be marked in the PR description.
- Test intent: [[yong-claude-code-jiang-san-wan-hang-go-xiang-mu-yi-zhi-dao-rust-agent-team-shi-jian-yu-harness-xiao-lu-you-hua]] says QA tests can cite ADR-0002 classes so review intent is clear.

## Counterevidence & Qualifications
The two-class policy fits this proxy-core port, but other migrations may need more categories for legal, data-format, performance, UX, or ecosystem compatibility constraints. Defaulting to hard errors can also break users if applied without migration paths or clear messages.

## What Changed
- Created the concept page for explicit upstream-divergence handling in rewrite and porting projects.

## Related Concepts
- [[SpecDrivenAgentDevelopment]] - divergence tables are part of the source's spec template.
- [[SoftwareVerification]] - tests cite divergence classes to validate intended behavior.
- [[HarnessEngineering]] - the policy constrains agent decisions during implementation.
- [[AICodingPractice]] - explicit compatibility rules help keep AI-generated ports accountable.
