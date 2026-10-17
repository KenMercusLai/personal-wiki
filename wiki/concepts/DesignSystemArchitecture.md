---
title: "Design System Architecture"
type: concept
tags: [design-systems, software-architecture, interaction-design]
sources:
  - ax-design
last_updated: 2026-10-17
knowledge_schema: synthesis-v1
---

## Definition
[[DesignSystemArchitecture]] is the shared semantic and technical infrastructure that makes components express one visual language rather than merely coexist in one library.

## Current Synthesis
The Axiom case argues that visual coherence requires more than common styling. Effects drawn from different systems must first reconcile their spatial metaphors, accessibility intentions, and interaction rules; components then need shared primitives for geometry, token interpretation, render scheduling, motion, and fallback behavior.

Constraints are productive when they encode the metaphor and hide accidental complexity. Axiom disallows arbitrary shadow color and direction, lets Shape semantics propagate across components, and exposes damping rather than every internal animation parameter. This raises the implementation floor while leaving designers room to compose different forms.

## Key Claims
- Shared visual vocabulary must be backed by shared geometry and rendering behavior, not only names or screenshots.
- Borrowed effects require reconciliation of their underlying spatial, interaction, and accessibility models.
- Design tokens should express meaningful degrees of freedom while preventing combinations that violate the system's metaphor.
- Common scheduling and frame-budget policy prevent independent animated components from competing without coordination.
- Equivalent multi-renderer paths and perceptual browser fallbacks can preserve semantics when no single implementation works everywhere.
- Interruption and recovery behavior are first-class parts of motion architecture.

## Evidence
- System integration: [[ax-design]] says isolated high-fidelity components could not form a complete system until Shape, Surface, and Typed OM infrastructure was shared.
- Semantic geometry: [[ax-design]] demonstrates reusable corner, edge, shoulder, and vertex-offset shapes across reveal, acrylic, shadow, and navigation components.
- Constraint design: [[ax-design]] restricts elevation to depth while keeping shadow color and direction fixed, and hides navigation timing behind a damping control.
- Runtime coordination: [[ax-design]] describes frame budgets and priority scheduling across Canvas animations.
- Failure handling: [[ax-design]] switches interrupted navigation from fixed Bezier trajectories to per-frame Lerp convergence and uses a Firefox-specific perceptual fallback for pressure.

## Counterevidence & Qualifications
The concept is derived from one unusually graphics-heavy Web Component system. Simpler product systems may not need Canvas/SVG equivalence, custom schedulers, continuous elevation, or complex geometry. The source demonstrates expressive behavior but provides no comparative evidence that this architecture improves team throughput, accessibility, consistency, or maintainability over alternatives.

## What Changed
- Created the concept from Axiom's move from isolated effects to shared geometry, scheduling, and token semantics.

## Related Concepts
- [[ProductDesignPrinciples]] - product-level judgments complement the implementation rules of a design system.
- [[DesignOperations]] - governs how shared design decisions are maintained across teams and products.
- [[PlatformNativeDesign]] - host-platform conventions can limit uniform design-system application.
- [[SoftwareAbstraction]] - design-system primitives hide implementation complexity behind reusable semantics.
- [[SoftwareVerification]] - visual, behavioral, performance, and cross-browser checks are needed to validate the architecture.
- [[AICodingPractice]] - expert specifications and acceptance judgment enabled rapid implementation of Axiom's architecture.
