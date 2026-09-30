---
title: "Intention-Driven Software"
type: concept
tags: [ai, software-engineering, agents, interfaces]
sources:
  - intention-is-all-you-need
last_updated: 2026-09-30
knowledge_schema: synthesis-v1
---

## Definition
[[IntentionDrivenSoftware]] is software creation and interaction organized around the outcome a person wants, with an LLM translating high-level natural-language intent into implementation or coordinated action.

## Current Synthesis
The source treats intention as the reason all software exists and argues that capable LLMs sharply compress its historical translation through requirements, architecture, and code. This shifts the primary human interface from instructions about how a system should operate toward statements of what should become true. The same principle applies to agent frameworks: their visible primitives should be high-level, general, and cognitively natural enough to carry intent, as [[Slock]] attempts through group chat and channels.

Compression is not elimination. Intent can be incomplete, contradictory, underspecified, or revised after execution begins, while dependable software still needs verification, maintainability, security, permissions, recovery, and operational ownership. Intention-driven software therefore relocates engineering effort toward clarification, constraints, feedback, judgment, and assurance rather than making those functions obsolete.

## Key Claims
- Human intent is the originating purpose of software, while programming languages and engineering processes are translation mechanisms.
- LLMs can compress the path from desired outcome to executable behavior enough that natural-language intent becomes a practical development interface.
- Agent-native products should expose abstractions that match how people naturally coordinate goals rather than defaulting to low-level orchestration controls.
- A familiar surface such as group chat can carry high-level collaboration intent while infrastructure complexity remains behind it.
- Ambiguity, conflicting goals, reliability, maintenance, security, and recovery preserve a substantial engineering gap.

## Evidence
- Translation compression: [[intention-is-all-you-need]] argues that LLM emergence moves intention from the starting point of software development toward the development act itself.
- Interface alignment: [[intention-is-all-you-need]] presents [[Slock]] channels and messages as a natural coordination model for agents across machines.
- Complexity contrast: [[intention-is-all-you-need]] retains a screenshot of a conventional orchestration proposal to show how quickly designers and agents reach for task graphs, schedulers, event logs, artifact schemas, gates, and recovery paths.
- Remaining gap: [[intention-is-all-you-need]] explicitly states that reliable, maintainable, secure software still lies at an engineering distance from an initial wish.

## Counterevidence & Qualifications
The argument is a first-person practitioner thesis, not comparative evidence that intent-only workflows improve delivered value, defect rates, security, maintenance cost, or team coordination. GitHub contribution activity measures visible repository actions rather than product quality, and the source's claimed late-2025 model inflection is not benchmarked. High-level interfaces may hide necessary decisions, and users cannot reliably express constraints they do not yet understand. Safety-critical, regulated, shared, and long-lived systems may require more explicit specifications and approval boundaries than the essay's broad framing suggests.

## What Changed
- Created the concept page from the source's distinction between intention as software's origin and intention as an increasingly executable interface.

## Related Concepts
- [[VibeCoding]] - provides the AI-assisted development setting in which natural-language intent can directly drive implementation.
- [[AIAgentCollaboration]] - extends intent into coordination among human and machine participants.
- [[SoftwareEngineering]] - supplies the clarification, verification, maintenance, security, and operational disciplines that remain after translation is compressed.
- [[HumanCodeResponsibility]] - keeps accountability with the humans who choose goals, constraints, acceptance, and release.
- [[ConversationalUI]] - natural language becomes the surface through which outcomes are requested and refined.
- [[Slock]] - illustrates intent-aligned agent collaboration through ordinary group chat and channels.
