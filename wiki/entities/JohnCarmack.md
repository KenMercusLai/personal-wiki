---
title: "John Carmack"
type: entity
tags: [programmer, software-engineering, game-development]
sources:
  - being-a-versatile-hacker-is-becoming-more-important-than-knowing-frameworks-christian-maioli-m
  - john-carmack-on-inlined-code
last_updated: 2026-10-01
knowledge_schema: synthesis-v1
---

## Overview
[[JohnCarmack]] is represented as a programmer whose advice joins technical curiosity with explicit control over state, execution order, and reliability.

## Current Profile
Christian Maioli M. cites Carmack as an authority connecting antifragility to hacker-style programming. Carmack's own 2007 email supplies the technical substance missing from that citation: he argues that stateful, sequential real-time work can be easier to reason about when its ordering and mutations are visible, while pure functions are the safer form of reusable decomposition. His 2014 preface makes that position evolutionary rather than dogmatic by favoring functional programming more strongly and limiting execute-and-inhibit advice in power-constrained environments.

## Key Characteristics
- Connects programmer reliability to awareness of actual execution, dependencies, and state mutation.
- Advocates source-level inlining for some single-use stateful helpers, not removal of calls for performance.
- Prefers pure functions and explicit inputs when work can be separated cleanly from permanent state.
- Uses real-time game loops and aerospace anecdotes to reason about control-flow clarity and testing.
- Revises earlier judgments when later experience, such as a nearly shipped frame of latency, supplies contrary evidence.

## Evidence
- Authority and curiosity: [[being-a-versatile-hacker-is-becoming-more-important-than-knowing-frameworks-christian-maioli-m]] cites Carmack as the route through which Maioli encountered the antifragile-programmer idea.
- Visible execution and state: [[john-carmack-on-inlined-code]] argues that inline sequential code can expose ordering, repeated assignments, hidden work, and skipped state updates.
- Functional boundary: [[john-carmack-on-inlined-code]] says pure functions with explicit inputs are safe from the state-assumption errors motivating much of the inlining advice.
- Learning from failure risk: [[john-carmack-on-inlined-code]] reports that a predicted one-frame input-latency bug later nearly shipped in Doom 3 BFG Edition.

## Qualifications
The two sources do not provide a full biography or a representative sample of Carmack's engineering work. The inlining essay is practitioner guidance rather than controlled evidence, its strongest aerospace claim is secondhand, and its recommendations are explicitly conditional on execution shape, reuse, modularity, performance, and power constraints.

## What Changed
- Expanded Carmack from a brief authority citation into a source-grounded programming profile.
- Added his qualified preference for visible stateful execution and pure functional extraction.
- Added evidence that his 2014 commentary revised and narrowed the 2007 position.

## Relationships
- [[HackerStyleTechnicalCuriosity]] - Carmack is cited as an authority supporting this working posture.
- [[Antifragile]] - Maioli uses Carmack as the intermediary for applying antifragility to programmers.
- [[ExecutionPathTransparency]] - Carmack argues that visible execution order can improve reliability in stateful loops.
- [[FunctionalProgramming]] - Carmack later presents purity as the more direct answer to hidden dependency and mutation.
- [[IdSoftware]] - Carmack applies the coding-style argument to Id's real-time game code.
- [[ChristianMaioliM]] - Maioli cites Carmack while building a broader software-learning argument.
