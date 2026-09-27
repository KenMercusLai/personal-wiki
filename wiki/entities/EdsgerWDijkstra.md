---
title: "Edsger W. Dijkstra"
type: entity
tags: [person, computer-science, algorithms]
sources:
  - freecodecamp-dijkstras-shortest-path-algorithm-a-detailed-and-visual-introduction
  - e-w-dijkstra-archive-why-numbering-should-start-at-zero-ewd-831
last_updated: 2026-09-27
knowledge_schema: synthesis-v1
---

## Overview
[[EdsgerWDijkstra]] was a Dutch computer scientist and software engineer represented here through both his design of [[DijkstrasAlgorithm]] and his argument connecting [[HalfOpenIntervals]] to [[ZeroBasedIndexing]].

## Current Profile
The sources present a consistent design style across algorithm and notation. Dijkstra's shortest-path method arose from a deliberately simple formulation of route finding and was published in 1959. In EWD 831, he evaluates four integer-range conventions by their arithmetic, composition, and edge-case behavior, selects lower-inclusive and upper-exclusive bounds, and then derives zero-based ordinals because a length-N sequence becomes `0 ≤ i < N`. Both cases emphasize removing avoidable complexity by choosing a representation whose structure matches the problem.

## Key Characteristics
- Dutch computer scientist and software engineer.
- Designer of the greedy shortest-path method now bearing his name.
- Published the algorithm in a three-page paper in 1959.
- Associated the design with deliberate avoidance of unnecessary complexity.
- Argued for half-open integer ranges and zero-based sequence indexing through boundary-case analysis.

## Evidence
- Identity and role: [[freecodecamp-dijkstras-shortest-path-algorithm-a-detailed-and-visual-introduction]] identifies Dijkstra as a Dutch computer scientist and software engineer.
- Algorithm design: [[freecodecamp-dijkstras-shortest-path-algorithm-a-detailed-and-visual-introduction]] attributes [[DijkstrasAlgorithm]] to him.
- Publication: [[freecodecamp-dijkstras-shortest-path-algorithm-a-detailed-and-visual-introduction]] names the 1959 paper “A note on two problems in connexion with graphs.”
- Design account: [[freecodecamp-dijkstras-shortest-path-algorithm-a-detailed-and-visual-introduction]] reproduces his retrospective description of devising the method without pencil and paper and avoiding unnecessary complexity.
- Range convention: [[e-w-dijkstra-archive-why-numbering-should-start-at-zero-ewd-831]] compares four endpoint conventions and argues for inclusive lower and exclusive upper bounds.
- Indexing argument: [[e-w-dijkstra-archive-why-numbering-should-start-at-zero-ewd-831]] derives a zero-based range for length-N sequences and defines an ordinal as the number of preceding elements.
- Practitioner evidence: [[e-w-dijkstra-archive-why-numbering-should-start-at-zero-ewd-831]] reports that Mesa's alternative interval forms caused recurring clumsiness and mistakes, without providing quantitative results.

## Qualifications
This remains a narrow technical profile rather than a comprehensive biography. The shortest-path history comes through an introductory secondary article and a retrospective interview excerpt rather than direct study of the 1959 paper. EWD 831 is a primary design note, but its Mesa evidence is anecdotal and unquantified, and its preferred convention does not establish that every mathematical or user-facing numbering domain should start at zero.

## What Changed
- Added Dijkstra's argument for half-open ranges and zero-based ordinals.
- Generalized the profile's design theme from one algorithm to representation choices that reduce boundary complexity.

## Relationships
- [[DijkstrasAlgorithm]] - algorithm he designed and published.
- [[GraphModeling]] - problem representation underlying the shortest-path work discussed in the source.
- [[HalfOpenIntervals]] - endpoint convention he defended through arithmetic and boundary behavior.
- [[ZeroBasedIndexing]] - sequence-numbering convention he derived from half-open ranges.
