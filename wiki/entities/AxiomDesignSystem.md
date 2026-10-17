---
title: "Axiom Design System"
type: entity
tags: [design-system, web-components, graphics]
sources:
  - ax-design
last_updated: 2026-10-17
knowledge_schema: synthesis-v1
---

## Overview
[[AxiomDesignSystem]] is [[LossesDon]]'s Web Component design system combining selected early [[MaterialDesign]] and [[FluentDesign]] ideas through shared graphics and rendering infrastructure.

## Current Profile
Axiom began as individually optimized recreations of Reveal Highlight, elevation, acrylic, navigation, and pressure effects. Its rebuilt form replaces that component-by-component architecture with shared Shape geometry, Surface rendering control, and Typed OM design-token parsing so the same spatial and shape semantics can propagate through the system.

The source presents Axiom less as a style catalog than as a constrained implementation model. It restricts shadow color and direction to preserve the physical-occlusion metaphor, hides fragile animation timing behind a smaller API, and uses browser-specific perceptual fallbacks where literal rendering breaks.

## Key Characteristics
- Combines early Material elevation with early Fluent lighting, material, navigation, and pressure ideas.
- Uses Web Components and custom CSS properties as its public component and token surface.
- Shares Shape, Surface, and Typed OM infrastructure across components.
- Supports composable corner, border, shoulder, and vertex-offset geometry in equivalent Canvas and SVG paths.
- Schedules Canvas work with frame budgets and priorities.
- Treats accessibility, coherent metaphor, animation interruption, and browser behavior as system constraints rather than decorative polish.

## Evidence
- Architecture: [[ax-design]] says the rebuild unified rendering scheduling, shape geometry, and token parsing instead of leaving effects as isolated implementations.
- Geometry: [[ax-design]] and its animations show corner and edge decorations morphing across diverse cards, indicators, and acrylic surfaces.
- Motion: [[ax-design]] describes a Bezier mode for normal navigation and a Lerp mode for smooth mid-animation retargeting.
- Rendering: [[ax-design]] reports Canvas-based reveal lighting and elevation, including pixel-aligned shadows at fractional display scales.
- Composition: [[ax-design]] visually combines concave Shape geometry, acrylic blur, Reveal Highlight, and controls in a player card.

## Qualifications
The profile comes from the system's creator and project demos rather than an independent audit. The source gives no package-usage data, accessibility study, broad device matrix, comparative frame-time measurements, or long-term maintenance results. Its reported AI-driven speedups and browser workarounds should therefore be treated as project evidence, not universal design-system or model performance claims.

## What Changed
- Created the entity with its transition from isolated effects to a shared graphics architecture.

## Relationships
- [[LossesDon]] - creator and principal designer of Axiom.
- [[DesignSystemArchitecture]] - Axiom operationalizes design language through shared geometry, scheduling, and tokens.
- [[MaterialDesign]] - supplies the elevation and outward-layering reference.
- [[FluentDesign]] - supplies Reveal Highlight, acrylic, pressure, and navigation references.
- [[AICodingPractice]] - the rebuild used expert-directed models for optimization and implementation.
- [[Firefox]] - required a browser-specific pressure-effect fallback.
