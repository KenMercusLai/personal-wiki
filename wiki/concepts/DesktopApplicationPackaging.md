---
title: "Desktop Application Packaging"
type: concept
tags: [desktop, electron, packaging, distribution]
sources:
  - blog-innei-lobehub-performance-and-dx-optimization
last_updated: 2026-09-25
knowledge_schema: synthesis-v1
---

## Definition
[[DesktopApplicationPackaging]] is the practice of assembling a desktop release with only the runtime resources, bundled dependencies, native modules, signing material, and platform artifacts the application actually requires.

## Current Synthesis
The LobeHub example treats distribution size as an inspectable dependency problem. Electron Framework localization directories can be reduced to the languages the application needs, provided at least one valid localization remains. JavaScript dependencies can be bundled into the main-process output and the general `node_modules` tree excluded, while native bindings receive explicit inclusion and ASAR-unpack patterns. Together, the source reports roughly 100 MB removed and a resulting application near 260 MB.

## Key Claims
- Runtime-supplied localization assets should be audited when the application maintains its own internationalization layer.
- Resource pruning must preserve runtime invariants; removing every Electron localization reportedly causes the application to crash.
- Bundled JavaScript can make shipping the complete dependency tree unnecessary when no native binding requires filesystem-level packaging.
- Native modules need an explicit exception path because they may not run directly from an ASAR archive.
- Package-size savings should be measured on produced artifacts rather than inferred only from source dependencies.

## Evidence
- Locale footprint: [[blog-innei-lobehub-performance-and-dx-optimization]] reports about 34 MB of Electron Framework language bundles and retains English variants.
- Dependency exclusion: [[blog-innei-lobehub-performance-and-dx-optimization]] shows Electron Builder `files` excluding `node_modules` after bundling application dependencies.
- Native compatibility: [[blog-innei-lobehub-performance-and-dx-optimization]] uses generated include and ASAR-unpack patterns for native bindings.
- Reported result: [[blog-innei-lobehub-performance-and-dx-optimization]] says the combined changes removed about 100 MB and left an application around 260 MB.

## Counterevidence & Qualifications
The size result is a single application report without before-and-after artifact listings or per-platform breakdown. Locale removal can harm users if the application relies on framework-provided strings, and native dependencies, code signing, auto-update channels, crash reporting, and operating-system packaging rules can require files that a simple bundle analysis misses. The exact technique is version- and platform-specific.

## What Changed
- Created the concept from LobeHub's Electron Builder packaging case.

## Related Concepts
- [[Electron]] - runtime whose resources and ASAR behavior shape the packaging strategy.
- [[DeveloperExperience]] - smaller, explicit dependency boundaries can simplify release reasoning.
- [[TechnologyStackComplexity]] - packaging exposes the distribution cost of runtime and dependency choices.
- [[LobeHub]] - application reporting the size reduction.
