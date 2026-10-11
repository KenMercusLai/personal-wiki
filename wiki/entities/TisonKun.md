---
title: "Tison Kun"
type: entity
tags: [person, software-engineering, open-source, databases]
sources:
  - ye-tian-zhi-shu-121-when-code-is-cheap
last_updated: 2026-10-11
knowledge_schema: synthesis-v1
---

## Overview
[[TisonKun]] is a software engineer and open-source practitioner represented here through a first-person account of using coding agents across database, infrastructure, and Rust library work.

## Current Profile
The available source presents Tison as an experienced maintainer working across ScopeDB and projects including Cronexpr, Apache DataSketches Rust, HawkEye, Asyncband, Fastrace, and Logforth. He delegates increasingly large implementation and optimization tasks to [[Codex]] while retaining control over scope, naming, interfaces, core technical decisions, verification strategy, and the threshold for accepting results.

His workflow is neither exhaustive line review nor unconditional delegation. Well-covered, bounded refactors may be accepted from regression evidence and sampled inspection; ambiguous rewrites, public interfaces, error behavior, and designs that merely look plausible receive closer review and iterative correction.

## Key Characteristics
- Uses coding agents for refactoring, dependency removal, performance work, tests, documentation, examples, and large rewrites.
- Treats clear goals, technical decision paths, and acceptance criteria as the highest-leverage human inputs.
- Adjusts review depth according to scope, test coverage, user-visible behavior, and design ambiguity.
- Maintains multiple concurrent workstreams but identifies human cognitive energy as a harder constraint than implementation time.
- Favors readable, explicit, well-tested Rust designs and is willing to inline simple logic rather than retain unnecessary dependencies.

## Evidence
- Agent use: [[ye-tian-zhi-shu-121-when-code-is-cheap]] describes Codex-assisted work on Cronexpr, DataSketches Rust, HawkEye, Asyncband, and ScopeDB.
- Verification boundary: [[ye-tian-zhi-shu-121-when-code-is-cheap]] reports accepting bounded refactors under comprehensive tests and snapshots while reading less of the implementation.
- Design authority: [[ye-tian-zhi-shu-121-when-code-is-cheap]] shows the author correcting an implausible error format and unnecessary serialization helpers despite passing checks.
- Review method: [[ye-tian-zhi-shu-121-when-code-is-cheap]] describes reviewing the HawkEye rewrite from external contracts inward and refining names, modules, and responsibilities.
- Bottleneck shift: [[ye-tian-zhi-shu-121-when-code-is-cheap]] identifies goal clarity, core decisions, health, and reasoning effort as the constraints after code becomes cheap.

## Qualifications
This profile comes from one self-authored essay and selected successful project examples. It does not provide controlled productivity comparisons, escaped-defect rates, maintenance outcomes, or independent evidence that the same low-review workflow is safe outside the author's expertise and test-rich projects.

## What Changed
- Established the entity from the first available source.

## Relationships
- [[Codex]] - primary coding agent in the reported refactoring, optimization, and rewrite workflows.
- [[AICodingPractice]] - Tison contributes a test-conditioned and design-centered review model.
- [[BottleneckAwareAICoding]] - his account moves the constraint from implementation toward goals, judgment, verification, and energy.
- [[SoftwareVerification]] - regression suites, snapshots, benchmarks, CI, and downstream use support his acceptance decisions.
- [[OpenSourceProjectMaintenance]] - his examples concern maintaining, simplifying, optimizing, and migrating public Rust projects.
