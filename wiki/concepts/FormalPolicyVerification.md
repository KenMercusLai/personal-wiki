---
title: "Formal Policy Verification"
type: concept
tags: [formal-methods, ai, agents, security, permissions]
sources:
  - agent-policy-prover
last_updated: 2026-10-30
knowledge_schema: synthesis-v1
---

## Definition
[[FormalPolicyVerification]] encodes actions and policy rules as logic, then searches for a counterexample showing that a candidate grant permits something outside a reviewed authority envelope.

## Current Synthesis
The useful question is precise and directional: does there exist an action for which the candidate policy allows access and the maximum policy does not? With [[Z3]], `sat` means such an action exists and can be returned as a witness; `unsat` means no counterexample exists inside the model; `unknown` means the system did not establish either outcome and should fail closed.

This makes policy review compositional. Binary, host, port, protocol layer, HTTP method, path, credential scope, and other action attributes can be reasoned about together rather than inspected as independent rules. The OpenShell case shows why: a clone-capable binary, raw network reach, and a broad GitHub credential jointly created write authority that REST inspection did not see.

Formal containment is not semantic approval. The solver cannot decide whether a repository is temporary, a database is production-critical, or a human intended a broad exception. Its value is deterministic evidence, fast repeated checks, concrete counterexamples, and an auditable complement to probabilistic or human judgment.

## Key Claims
- Policy safety questions must be translated into explicit predicates over a bounded action domain.
- Candidate-minus-maximum emptiness is a reusable containment property for proposed authority changes.
- A satisfying model is operationally useful because it exposes the exact binary, endpoint, protocol, method, or path that escapes the envelope.
- An unsatisfiable result is relative to the policy encoding and cannot establish safety outside modeled surfaces.
- Once a policy language is encoded, specialized expert checks can reuse the same logic for known risk classes.
- Formal checks complement contextual review by supplying deterministic, token-free evidence without claiming to understand business intent.

## Evidence
- Containment property: [[agent-policy-prover]] defines the query as candidate permission conjoined with the negation of maximum permission.
- Concrete witnesses: [[agent-policy-prover]] returns a POST path for an over-broad REST rule and a raw layer-4 action for an inspection-bypass rule.
- Narrowness proof: [[agent-policy-prover]] returns `unsat` when one exact GET request is contained by the reviewed maximum.
- Runtime encoding: [[agent-policy-prover]] describes Rust translation of policy rules, Boolean rule composition, and glob compilation into regular languages.
- Reusable expert formulas: [[agent-policy-prover]] lists checks for link-local reach, layer-7 bypass with credentials, credentialed endpoint expansion, and added HTTP methods.
- Operational role: [[agent-policy-prover]] reports millisecond-scale, token-free checks that provide evidence to human or agent reviewers.

## Counterevidence & Qualifications
The source is a first-party explanation and demonstration, not an independent audit. A proof can be sound relative to a model while the model omits a binary, protocol, redirect, DNS behavior, policy interaction, implementation bug, or deployed configuration. Regular-language policy fragments also deliberately exclude some language features. A pre-reviewed maximum can itself be too broad or semantically inappropriate, and formal containment cannot infer intent, asset criticality, recovery cost, or social authorization. No comparative detection rate, solver-load benchmark, maintenance cost, false-positive analysis, or end-to-end reproduction is supplied.

## What Changed
- Created a counterexample-driven model of formal verification for agent permission changes, with explicit modeling and semantic-review boundaries.

## Related Concepts
- [[AgentPermissionModel]] - supplies the authority envelope whose later changes can be checked for containment.
- [[AgentSecurityLayering]] - formal reasoning detects dangerous capability composition across binaries, protocols, credentials, and inspection layers.
- [[SoftwareVerification]] - places formal policy checks among external mechanisms for judging machine-generated or autonomous behavior.
- [[ProductionAgentInfrastructure]] - uses fast deterministic checks when agent scale makes universal human review infeasible.
- [[CapabilityGateway]] - can enforce the scoped actions that the verified policy describes.
- [[AccountabilityInfrastructure]] - preserves counterexamples, decisions, and policy versions as audit evidence.
