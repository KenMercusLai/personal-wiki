---
title: "Preimplementation Feature Discovery"
type: concept
tags: [product-development, software-development, specification, user-flows]
sources:
  - kannan-chandrasegaran-your-app-is-an-onion-why-software-projects-spiral-out-of-control
last_updated: 2026-10-01
knowledge_schema: synthesis-v1
---

## Definition
[[PreimplementationFeatureDiscovery]] is the practice of translating a product objective into step-by-step user and operator flows, then interrogating those flows to expose necessary scope before committing to code.

## Current Synthesis
A concise feature description usually states an objective, not a buildable interaction. When a team walks through how people actually achieve that objective, it encounters screens, inputs, validation, information ordering, notifications, user-to-user interactions, external services, administrative controls, and failure cases. The source calls this depth fractal: detail emerges as the viewing scale moves from business intent toward use.

The proposed response is to move early iteration into cheap representations. Teams list user objectives, map every step or screen with an outline, mockup, or flowchart, then question each step across four dimensions: user inputs, information presented, interactions among system participants and services, and business-owner functionality. Newly exposed requirements return to the map for another pass. This is not a promise of complete prediction; it is a sequencing discipline intended to reveal foreseeable product decisions before they become slow build-review-rebuild loops.

## Key Claims
- Business-level feature statements conceal the interaction and operational decisions required for usable software.
- Hidden supporting capabilities can belong to the original product promise and therefore should not be mislabeled as [[FeatureCreep]].
- Step-by-step user-flow mapping exposes missing screens, transitions, data, roles, and service dependencies.
- Low-fidelity outlines, mockups, and flowcharts are valuable because they make revision fast and inexpensive.
- Questions about inputs, outputs, interactions, and operator needs provide a reusable discovery checklist.
- Preimplementation work changes when complexity is found; it does not remove technical, market, accessibility, security, or live-use uncertainty.

## Evidence
- Scope expansion: [[kannan-chandrasegaran-your-app-is-an-onion-why-software-projects-spiral-out-of-control]] expands a two-line local book-marketplace pitch into profiles, catalog search, proximity matching, notifications, chat, negotiation, payments, verification, and location functions.
- Scale analogy: [[kannan-chandrasegaran-your-app-is-an-onion-why-software-projects-spiral-out-of-control]] contrasts a straight map line with a viable street route to show how implementation-level constraints change a high-level plan.
- Cycle placement: [[kannan-chandrasegaran-your-app-is-an-onion-why-software-projects-spiral-out-of-control]] contrasts repeated month-long coded versions with day-scale revisions to a feature map before the first build.
- Representation method: [[kannan-chandrasegaran-your-app-is-an-onion-why-software-projects-spiral-out-of-control]] recommends objectives, every screen or step, and fast outlines, mockups, or flowcharts.
- Question framework: [[kannan-chandrasegaran-your-app-is-an-onion-why-software-projects-spiral-out-of-control]] groups prompts around user inputs, presented information, participant/service interactions, and owner or employee functions.

## Counterevidence & Qualifications
The concept currently rests on one practitioner essay and a hypothetical marketplace. Its week-versus-month comparison is illustrative, and no outcome data establishes how much rework the method avoids. Exhaustive-looking flows can create false confidence, prematurely freeze a solution, or waste effort when problem and market uncertainty dominate. Static representations also cannot fully reveal technical feasibility, accessibility, abuse, real user behavior, production load, or operational failures. Teams therefore need to combine specification discovery with appropriate prototypes, research, engineering spikes, testing, and post-release learning.

## What Changed
- Created the concept from Chandrasegaran's feature-depth diagnosis and structured pre-code discovery method.

## Related Concepts
- [[FeatureCreep]] - distinguishes unrelated capability accumulation from detail required to fulfill the original objective.
- [[PrototypeFirstProductDiscovery]] - uses tangible artifacts for early learning, often adding user behavior or technical possibility as evidence.
- [[ProductFlowFriction]] - examines the practical and cognitive burden revealed within a mapped user journey.
- [[OutsourcedProductDevelopment]] - benefits from explicit product decisions before requirements cross an organizational boundary.
- [[SoftwareVerification]] - tests the implemented system after specification work has framed expected behavior.
- [[UnknownUnknowns]] - bounds the method because some relevant conditions remain invisible until broader research or real use.
