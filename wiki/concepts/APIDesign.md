---
title: "API Design"
type: concept
tags: [api, developer-experience, usability, software-engineering]
sources:
  - notes-to-myself-on-software-engineering-featured-stories-medium
last_updated: 2026-10-01
knowledge_schema: synthesis-v1
---

## Definition
[[APIDesign]] is the deliberate shaping of a software interface so users can understand its concepts, complete real workflows, recover from failures, and reach advanced capability without carrying unnecessary implementation detail or cognitive load.

## Current Synthesis
[[FrancoisChollet]] treats an API as a user experience rather than a neutral inventory of callable features. Good design begins with actual use cases and domain practitioners' mental models, then chooses objects, data structures, argument names, defaults, and feedback that make the common path understandable. Implementation details should not leak into user decisions merely because they exist internally.

This workflow-first frame also constrains extensibility. Simple tasks should stay simple while complex tasks remain possible, but niche flexibility should not tax common use. New requests therefore need interpretation: the best response may be to extend an existing concept rather than add a disconnected option. Modular, hierarchical concepts can preserve a simple high-level path while exposing precision progressively.

Documentation, examples, error messages, and naming are part of the interface itself. End-to-end examples should show users how to accomplish real tasks, while consistent domain language and actionable feedback reduce the distance between intention and recovery. The resulting standard is not minimal surface area for its own sake, but a coherent interface whose complexity follows the problem rather than the implementation.

## Key Claims
- APIs have users, so usability and empathy are core design responsibilities.
- Common workflows should minimize unnecessary choices and reflect domain experts' mental models.
- End-to-end use cases should shape atomic capabilities, arguments, data structures, and defaults.
- Simple tasks should remain simple while modular and hierarchical structure progressively supports advanced work.
- Naming, error messages, feedback, documentation, and examples are part of the API contract.
- Feature requests should be interpreted within a coherent product model rather than implemented literally by default.

## Evidence
- User and cognition frame: [[notes-to-myself-on-software-engineering-featured-stories-medium]] defines an API as a user experience and asks designers to minimize avoidable action, choice, and conceptual burden.
- Domain fit: [[notes-to-myself-on-software-engineering-featured-stories-medium]] says public objects, arguments, and data structures should match practitioner concepts rather than expose implementation details.
- Workflow design: [[notes-to-myself-on-software-engineering-featured-stories-medium]] recommends starting from use cases and optimal action sequences before adding atomic options.
- Progressive expressiveness: [[notes-to-myself-on-software-engineering-featured-stories-medium]] favors modular, hierarchical models that remain approachable at a high level and precise in depth.
- Communication surfaces: [[notes-to-myself-on-software-engineering-featured-stories-medium]] treats consistent naming, deliberate error feedback, documentation, and end-to-end code examples as parts of interface quality.

## Counterevidence & Qualifications
The evidence is one experienced practitioner's design checklist, not a measured comparison of API learnability, task success, error rate, compatibility, or maintenance outcomes. Low cognitive load is context-dependent: automation and defaults can hide consequential behavior, while some domains require explicit consent, safety controls, accessibility settings, expert options, or detailed configuration. Domain experts can disagree on concepts and terminology, and optimizing for their existing mental models can disadvantage novices or constrain genuinely new abstractions. Workflow coherence must also coexist with performance, security, versioning, observability, and backward-compatibility requirements that the source does not address.

## What Changed
- Created API design as a workflow-, mental-model-, and user-experience-centered software practice.

## Related Concepts
- [[DeveloperExperience]] - API usability is a major part of a developer's experience with a system.
- [[MentalModels]] - domain concepts should shape public objects, arguments, and workflows.
- [[CognitiveOverheadInProductDesign]] - unnecessary options and implementation leakage increase comprehension burden.
- [[DeveloperDocumentation]] - examples and task guidance form part of the usable interface.
- [[APIErrorHandling]] - failure feedback should help users understand responsibility and recover.
- [[ProductFlowFriction]] - the goal is meaningful, legible work rather than the fewest visible steps.
- [[APIBackwardCompatibility]] - interface improvement must account for existing users and versioned behavior.
