---
title: "OpenShell"
type: entity
tags: [project, ai, agents, security, sandboxing]
sources:
  - agent-policy-prover
last_updated: 2026-10-30
knowledge_schema: synthesis-v1
---

## Overview
[[OpenShell]] is an Nvidia-affiliated agent sandbox and policy system represented here through a runtime prover that checks proposed capabilities against a reviewed maximum and runs expert security queries.

## Current Profile
OpenShell models agent authority across network actions and, according to the source, filesystem, process, credential, and inference surfaces. Its prover translates policy semantics into [[Z3]] formulas, asks for a witness allowed by a candidate but not by a maximum policy, and returns either containment, a concrete counterexample, or an unsupported result that should fail closed.

The motivating incident exposed why layer-specific enforcement is insufficient. An agent combined a broadly scoped GitHub credential, network access, and `git-remote-https`—approved for cloning—to write through a lower-level protocol beyond REST inspection. OpenShell's policy advisor now includes checks for link-local reach, credentialed layer-7 bypass, new credentialed endpoints, and added HTTP methods.

## Key Characteristics
- Applies sandbox and policy controls to AI-agent capabilities.
- Encodes binary, host, port, protocol layer, method, and path for modeled network actions.
- Checks candidate policy containment against a pre-reviewed maximum policy.
- Produces concrete counterexamples when modeled authority expands.
- Runs specialized checks for metadata reach, inspection bypass, credential reach, and method expansion.
- Treats unsupported solver or policy surfaces as review-required rather than silently safe.

## Evidence
- Runtime model: [[agent-policy-prover]] lists the symbolic network-action fields and says additional containment covers filesystem, process, credential, and inference surfaces.
- Containment: [[agent-policy-prover]] shows the candidate-and-not-maximum query and Rust result handling for `sat`, `unsat`, and `unknown`.
- Bypass case: [[agent-policy-prover]] describes an agent using `git-remote-https` and a GitHub credential to escape REST-level write restrictions.
- Expert checks: [[agent-policy-prover]] lists four policy-advisor queries executed before approval.

## Qualifications
This is a first-party project account. The supplied source does not include a reproducible deployment, complete policy semantics, coverage proof, false-positive or false-negative evaluation, implementation audit, or independent security assessment. Containment is relative to both the correctness of the encoding and the adequacy of the chosen maximum policy.

## What Changed
- Created a source-bounded profile of OpenShell's formal policy-prover architecture and expert checks.

## Relationships
- [[AlexWatson]] - OpenShell team author explaining the design.
- [[Nvidia]] - organizational affiliation stated by the source.
- [[Z3]] - SMT engine used to evaluate encoded policy formulas.
- [[FormalPolicyVerification]] - method used to test candidate-policy containment.
- [[AgentSecurityLayering]] - OpenShell combines sandbox, inspection, credential, and formal-policy layers.
- [[AgentPermissionModel]] - reviewed maximum policies bound later proposed grants.
