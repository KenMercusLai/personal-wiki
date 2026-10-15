---
title: "Unknown Unknowns"
type: concept
tags: [uncertainty, product-development, validation]
sources:
  - unknown-unknowns-why-you-should-release-early-and-often
  - a-field-guide-to-fable-finding-your-unknowns
last_updated: 2026-10-15
knowledge_schema: synthesis-v1
---

## Definition
[[UnknownUnknowns]] are relevant questions, constraints, possibilities, or failure modes that a decision-maker does not yet recognize as missing from their understanding.

## Current Synthesis
The sources distinguish unrecognized gaps from uncertainty that is already visible. Karlsson focuses on product development: teams may treat assumptions about customers or behavior as facts, or lack enough domain knowledge to know which questions should be asked. Thariq places the same risk inside human-agent work, where a prompt or plan is a map and the codebase, users, domain, and constraints are the territory. Whenever that map omits a consequential choice, the agent must guess unless exploration makes the choice visible.

Discovery is therefore iterative rather than a one-time planning phase. Customer conversations, mockups, proofs of concept, blind-spot passes, alternative prototypes, expert references, and implementation work expose different unknowns. During implementation, deviation notes preserve newly discovered constraints; after implementation, explainers transfer the resulting context and quizzes test whether the human understands what was built. None of these artifacts eliminates hidden risk, but each can move some uncertainty into a cheaper, inspectable form before it hardens into product or code.

## Key Claims
- Assumptions treated as facts can be more dangerous than acknowledged gaps because teams do not investigate them.
- Domain novices cannot reliably enumerate everything they need to learn before acting, and coding agents cannot infer every local preference or constraint from a prompt.
- Different evidence surfaces reveal different gaps: conversations and releases expose market assumptions, while blind-spot passes, alternatives, prototypes, references, and implementation expose domain, taste, and technical constraints.
- Planning should identify consequential choices without pretending to eliminate surprises; some unknowns emerge only while implementation interacts with the real system.
- The cost of discovery usually rises as more implementation, coordination, or emotional commitment accumulates around an untested premise.
- Post-implementation explanation and questioning can reveal residual human-understanding gaps even after the artifact appears complete.

## Evidence
- False certainty: [[unknown-unknowns-why-you-should-release-early-and-often]] argues that foundational beliefs about customers and product behavior can make a team build the wrong product when reality disagrees.
- Domain gaps: [[unknown-unknowns-why-you-should-release-early-and-often]] uses bookkeeping to illustrate how a non-expert may research extensively without locating every gap; [[a-field-guide-to-fable-finding-your-unknowns]] recommends an explicit blind-spot pass when the user lacks the questions or quality bar for unfamiliar work.
- Tacit and technical discovery: [[a-field-guide-to-fable-finding-your-unknowns]] uses multiple prototypes for “know it when I see it” criteria, source code as a high-detail reference, interviews for consequential ambiguity, and implementation notes for constraints discovered while coding.
- Early exposure: [[unknown-unknowns-why-you-should-release-early-and-often]] recommends customer calls, paper mockups, and proofs of concept; [[a-field-guide-to-fable-finding-your-unknowns]] similarly treats brainstorms, prototypes, and decision-focused plans as cheap ways to change course before full implementation.
- Avoidance: [[unknown-unknowns-why-you-should-release-early-and-often]] links delayed release to perfectionism, fear of criticism, and the emotional safety of a product that has not yet visibly failed.
- Residual understanding: [[a-field-guide-to-fable-finding-your-unknowns]] recommends demo-led explainers for reviewers and quizzes for the implementer before merge, making unarticulated post-build gaps visible.

## Counterevidence & Qualifications
Both sources are practitioner essays rather than controlled comparisons. Early release reveals only what selected users and tests make observable, while an agent's blind-spot pass is constrained by its training, retrieved evidence, prompt framing, and access to the actual environment. Brainstorms can invent noise, prototypes can prematurely anchor the solution, references can import inappropriate design choices, and interviews can overfit the questions asked. Safety-critical, regulated, private, or reputation-sensitive work may need domain experts, simulation, staged exposure, formal review, and stronger behavioral verification; a quiz demonstrates articulated understanding, not production correctness. The four-quadrant vocabulary is a useful elicitation device, not proof that all uncertainty has been exhaustively classified.

## What Changed
- Extended the concept from early product validation into iterative human-agent collaboration.
- Added tacit “unknown knowns,” implementation-time discovery, deviation notes, explainers, and quizzes as qualified discovery surfaces.
- Preserved the boundary that artifacts reveal only the unknowns their evidence and framing make observable.

## Related Concepts
- [[StartupHypothesisTesting]] - turns recognized assumptions into explicit tests while unknown unknowns motivate early probing.
- [[IterativeProductShipping]] - repeated releases create opportunities for hidden constraints to become visible.
- [[MinimumViableProduct]] - a minimal test can expose missing knowledge before full buildout.
- [[CustomerLedProductDevelopment]] - customer contact supplies external evidence against internally coherent assumptions.
- [[BehavioralRiskJudgment]] - overconfidence and avoidance can prevent uncertainty from being examined.
- [[AIAgentCollaboration]] - agents and humans can jointly expose ambiguity while retaining human decision authority.
- [[PrototypeFirstProductDiscovery]] - tangible alternatives help reveal criteria that are difficult to articulate in advance.
- [[SpecDrivenAgentDevelopment]] - plans and specs externalize known intent but must remain revisable when implementation reveals new constraints.
