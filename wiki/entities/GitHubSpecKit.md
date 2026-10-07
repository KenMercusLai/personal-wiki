---
title: "GitHub Spec Kit"
type: entity
tags: [github, software-development, specifications, ai-agents]
sources:
  - spec-driven-development-with-spec-kit
last_updated: 2026-10-07
knowledge_schema: synthesis-v1
---

## Overview
[[GitHubSpecKit]] is a [[GitHub]] project and command-line workflow for turning durable specifications into structured inputs for coding agents.

## Current Profile
In the reported [[LaMemoria]] case, Spec Kit initializes repository-resident governance and feature artifacts, then guides work through constitution, specification, clarification, technical planning, task decomposition, consistency analysis, implementation, and convergence. Its value is not automatic correctness but a repeatable, inspectable workflow whose files survive conversation boundaries and can coordinate different models across phases.

## Key Characteristics
- Separates non-functional project governance from functional and technical feature decisions.
- Stores specifications, plans, contracts, research, task state, and supporting artifacts in the repository.
- Uses analysis before implementation to find contradictions and missing requirements across artifacts.
- Uses convergence after implementation to compare the codebase with the spec, plan, and tasks and to add remediation work.
- Supports multiple coding-agent integrations and optional extensions, including an LLM-maintained wiki.
- Imposes meaningful setup, review, context, token, and monetary overhead.

## Evidence
- Workflow stages: [[spec-driven-development-with-spec-kit]] documents `constitution`, `specify`, `clarify`, `plan`, `tasks`, `analyze`, `implement`, and `converge` in a real greenfield project.
- Persistent coordination: [[spec-driven-development-with-spec-kit]] reports that checked task state and repository artifacts supported restarts, fresh chats, phased implementation, and model changes.
- Quality gates: [[spec-driven-development-with-spec-kit]] reports that analysis exposed three critical pre-implementation conflicts and convergence later found an incomplete test plus two smaller gaps.
- Cost boundary: [[spec-driven-development-with-spec-kit]] reports substantial document generation, roughly 7,000 subscription credits for the initial release, and an unmeasured estimate of 20–30% more tokens.

## Qualifications
This profile rests on one first-person greenfield case using a particular editor, subscription, model mix, and Spec Kit release. The resulting application still contained runtime and UI defects, so Spec Kit's artifact consistency checks do not replace executable verification, usability review, dependency maintenance, or human judgment. The source did not test brownfield adoption and explicitly questions who would reverse-engineer and review specifications for a large existing codebase.

## What Changed
- Established Spec Kit as a durable multi-stage agent workflow rather than a synonym for ordinary plan mode.
- Added practitioner evidence for pre-implementation analysis, post-implementation convergence, resumability, and cost.
- Bounded the project against residual implementation defects and uncertain brownfield adoption.

## Relationships
- [[SpecDrivenAgentDevelopment]] - Spec Kit operationalizes specification-centered agent work through repository artifacts and staged commands.
- [[LaMemoria]] - La Memoria is the greenfield application used to evaluate the workflow.
- [[GitHub]] - GitHub hosts and maintains the project described by the source.
- [[GitHubCopilot]] - Copilot in VS Code is the integration used in the case study.
- [[SoftwareVerification]] - analysis and convergence supplement but do not replace behavioral verification.
- [[VibeCoding]] - Spec Kit is presented as a more structured alternative to beginning with loosely governed agent generation.
