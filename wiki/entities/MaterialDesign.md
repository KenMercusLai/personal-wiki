---
title: "Material Design"
type: entity
tags: [design-system, google, product-design]
sources:
  - advocating-for-a-complete-product-redesign-google-design-medium
  - design-principles-behind-great-products-muzli-design-inspiration
last_updated: 2026-09-27
knowledge_schema: synthesis-v1
---

## Overview
[[MaterialDesign]] is Google's cross-product design system, represented in the sources both by its principles of tactile spatial metaphor, intentional graphic hierarchy, and meaningful motion and by its role as the visual system used by [[Firebase]] during the [[Crashlytics]] migration from [[Fabric]].

## Current Profile
The Muzli compilation presents Material Design as a system whose metaphor creates a rationalized space with surfaces, edges, light, and movement; print-derived typography, grids, scale, color, imagery, and whitespace establish hierarchy; and motion communicates causality, focus, feedback, and continuity. These are system principles meant to make related products feel coherent rather than a complete statement of any one product's differentiation.

The Crashlytics source shows the system acting as a practical constraint and opportunity. Because Firebase used Material Design and differed visually from Fabric, Crashlytics needed at least a visual update. The designer used that requirement to argue for repairing user flows and information hierarchy rather than performing a surface-level port.

## Key Characteristics
- Uses a tactile material metaphor to make spatial relationships and affordances legible.
- Uses typography, grids, space, scale, color, and imagery to create hierarchy, meaning, and focus.
- Treats motion as communication that preserves continuity and shows action results.
- Functions as Firebase's visual design system and created a mismatch with the existing Fabric Crashlytics interface.
- Forced a visual update that became the catalyst for a deeper [[ProductRedesign]] argument.

## Evidence
- System principles: [[design-principles-behind-great-products-muzli-design-inspiration]] summarizes Material Design around material metaphor, bold intentional graphic hierarchy, and meaningful motion.
- Metaphor and motion: [[design-principles-behind-great-products-muzli-design-inspiration]] says familiar tactile cues aid affordance recognition while motion focuses attention, preserves continuity, and provides feedback.
- Design-system role: [[advocating-for-a-complete-product-redesign-google-design-medium]] says Firebase uses Material Design and has a very different visual design system.
- Visual-update trigger: [[advocating-for-a-complete-product-redesign-google-design-medium]] says the need for a visual design update created the opportunity to rethink the entire user experience.
- Screenshot evidence: [[advocating-for-a-complete-product-redesign-google-design-medium]] shows the redesigned Firebase Crashlytics UI with lighter Material-style surfaces, cards, filters, tables, and action controls.

## Qualifications
The Muzli source is a 2017 secondary compilation of public guidance, while the Crashlytics account covers one migration. Neither describes the full component system, accessibility implementation, governance, later evolution, or measured outcomes. A coherent design language also does not by itself supply a product's distinctive [[ProductDesignPrinciples]] or repair underlying user journeys.

## What Changed
- Added Material Design's spatial, graphic, and motion principles while preserving the distinction between system coherence and product-specific direction.

## Relationships
- [[Firebase]] - Firebase used Material Design.
- [[Crashlytics]] - Crashlytics had to be redesigned into a Material Design context.
- [[Fabric]] - Fabric's older visual system is contrasted with the Firebase redesign.
- [[ProductRedesign]] - Material Design migration catalyzed a broader redesign case.
- [[InformationHierarchy]] - the visual refresh was used to repair hierarchy, not just style.
- [[ProductDesignPrinciples]] - product-specific commitments complement Material Design's cross-product system rules.
- [[DesignOperations]] - governance and implementation are required to carry a design language across products and platforms.
