---
title: "Alex Watson"
type: entity
tags: [person, ai, security, formal-methods]
sources:
  - agent-policy-prover
last_updated: 2026-10-30
knowledge_schema: synthesis-v1
---

## Overview
[[AlexWatson]] is an OpenShell team author at [[Nvidia]] represented here through a technical introduction to formal verification of agent-policy changes.

## Current Profile
Watson explains why human and model permission review can miss capabilities created by composing binaries, credentials, protocols, endpoints, and policy rules. His article develops a counterexample-driven [[Z3]] containment query and connects it to [[OpenShell]]'s runtime policy prover and expert security checks.

## Key Characteristics
- Works with the OpenShell team at Nvidia.
- Writes about formal methods for controlling long-running AI agents.
- Frames solver output as deterministic evidence for, rather than a semantic replacement of, human or model review.

## Evidence
- Affiliation and topic: [[agent-policy-prover]] identifies Watson as an OpenShell team author at Nvidia and presents his policy-prover introduction.
- Technical contribution: [[agent-policy-prover]] explains candidate-versus-maximum containment, counterexample witnesses, and expert security queries.
- Review boundary: [[agent-policy-prover]] states that formal checks lack deployment context and should complement contextual reviewers.

## Qualifications
The wiki has one authored technical source for Watson and does not establish his broader role, biography, authorship of the underlying implementation, or independent security results.

## What Changed
- Created a source-bounded profile of Watson's OpenShell policy-verification work.

## Relationships
- [[OpenShell]] - project team and policy-prover subject of Watson's article.
- [[Nvidia]] - stated organizational affiliation.
- [[FormalPolicyVerification]] - method Watson introduces for agent-policy containment.
- [[Z3]] - solver used in the worked examples and runtime design.
