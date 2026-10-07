---
title: "Procedural Road Geometry"
type: concept
tags: [game-development, computational-geometry, roads, splines]
sources:
  - art-of-roads-in-games
last_updated: 2026-10-08
knowledge_schema: synthesis-v1
---

## Definition
[[ProceduralRoadGeometry]] is the generation of road surfaces, lane boundaries, markings, junctions, and connectors from editable path geometry while preserving plausible widths, curvature, and vehicle movement.

## Current Synthesis
The source frames procedural road geometry as a representation problem rather than a cosmetic mesh problem. A visually smooth centerline is insufficient if offsetting it to form lane or road edges changes curvature unevenly, pinches the inner edge, or creates self-intersection. Roads need constraints derived from their physical use: vehicles occupy a stable width, high-speed paths cannot turn arbitrarily sharply, and intersections need coherent boundaries and connectors.

The proposed practical hierarchy is context-sensitive. Bézier splines are intuitive and flexible authoring tools, but their offsets are not generally Bézier curves and can fail under tight curvature. Circular arcs preserve concentric spacing and admit simpler analytic intersection calculations, making them attractive for urban streets where speeds are lower. At higher speeds, the constant curvature of an arc creates an abrupt force transition from a straight; a clothoid or other transition curve instead ramps curvature gradually. The article's custom-system video demonstrates dynamic regeneration as roads move, but stops before explaining data structures, algorithms, topology handling, or measured runtime.

## Key Claims
- A road representation must preserve usable parallel boundaries, not only produce a smooth centerline.
- Unconstrained Bézier editing can create implausible curvature, pinched offsets, and self-intersecting road geometry in tight layouts.
- Circular arcs provide stable concentric offsets and simpler intersection construction for many low-speed urban cases.
- Curve choice should reflect speed and comfort: constant-curvature arcs are often adequate in cities, while high-speed transitions benefit from gradually changing curvature.
- Procedural intersections must recompute connectors, boundaries, and markings as attached road segments move.
- Tool freedom and geometric validity are separate qualities; more placement freedom can expose more invalid or unrealistic configurations.

## Evidence
- Offset failure: [[art-of-roads-in-games]] states that a Bézier offset is not generally another Bézier and shows tight game roads with pinched lanes, crossed markings, and distorted inner edges.
- Circular alternative: [[art-of-roads-in-games]] visually compares uneven Bézier offsets with evenly spaced circular-arc offsets and argues that circle intersections avoid iterative spline-intersection work.
- Speed-sensitive transition: [[art-of-roads-in-games]] explains that joining a straight directly to a circular arc jumps from zero to constant curvature, while a clothoid increases curvature gradually.
- Dynamic construction: [[art-of-roads-in-games]] includes a short demo in which dragging road endpoints causes intersection connectors and road boundaries to regenerate.
- Tooling motivation: [[art-of-roads-in-games]] contrasts sophisticated city-builder results with examples of rigid, pinched, or sharply joined road-generation tutorials and assets.

## Counterevidence & Qualifications
The source is a design essay and teaser for a forthcoming custom asset, not a derivation or implementation report. It does not benchmark spline and arc intersection methods, define continuity requirements, explain compound-arc fitting, handle elevation or superelevation, or show how its system manages topology, lane connectivity, collision, terrain, traffic rules, or degenerate cases. Circular arcs do not by themselves solve every road-design problem, and the statement that stitched arcs can create any shape is best read as approximation rather than exact equivalence. The screenshots show correlation between extreme layouts and artifacts, not proof that the spline family alone caused every failure.

## What Changed
- Created the concept with a context-sensitive hierarchy among Bézier splines, circular arcs, and clothoid transition curves.
- Added visual evidence for offset pinching and dynamic intersection regeneration.

## Related Concepts
- [[IndieGameDevelopment]] - road tooling is a specialized technical capability that small game teams may need to build or buy.
- [[RamerDouglasPeuckerAlgorithm]] - both use computational geometry on paths, but road generation constructs offset surfaces while RDP removes redundant sampled points.
- [[CognitiveOverheadInProductDesign]] - freeform controls can feel expressive while shifting hidden validity and correction work onto the user.
- [[AutomatedGameTesting]] - procedural road systems need repeatable checks for geometric degeneracy, connectivity, and runtime behavior.
