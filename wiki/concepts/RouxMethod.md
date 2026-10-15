---
title: "Roux Method"
type: concept
tags: [rubiks-cube, puzzle-solving, spatial-reasoning]
sources:
  - ru-he-bu-bei-gong-shi-jie-kai-mo-fang-xiao-xue-sheng-ye-neng-kan-dong
last_updated: 2026-10-15
knowledge_schema: synthesis-v1
---

## Definition
[[RouxMethod]] is a block-building approach to 3×3 [[RubiksCubeSolving]] that forms left and right 1×2×3 blocks before solving the remaining corners and last six edges.

## Current Synthesis
The source adapts Roux as a low-memorization teaching scaffold rather than a speed-solving specification. The learner keeps a fixed orientation, builds a red-centered left bridge and an orange-centered right bridge by observation, uses corner cycles to orient and position the four remaining corners, and finishes the six remaining edges mostly with middle-slice `M` and top-layer `U` turns. The staged structure protects completed blocks and narrows the visible problem, but the worked example still gives concrete sequences for difficult cases.

## Key Claims
- Fixed viewing orientation reduces the need to mentally remap face colors throughout the solve.
- Building two 1×2×3 bridges decomposes the cube into preserved side blocks and a smaller unsolved slice.
- The remaining four corners can be oriented and positioned with directional three-cycles and an adjacent-corner swap sequence.
- The last six edges can be separated into orientation and placement problems handled mainly with `M` and `U` turns.

## Evidence
- Orientation and blocks: [[ru-he-bu-bei-gong-shi-jie-kai-mo-fang-xiao-xue-sheng-ye-neng-kan-dong]] fixes green front, red left, orange right, yellow top, white bottom, and blue back before constructing the two bridges.
- Corner stage: [[ru-he-bu-bei-gong-shi-jie-kai-mo-fang-xiao-xue-sheng-ye-neng-kan-dong]] diagrams an `A→B→C→A` corner cycle and supplies mirrored sequences for opposite directions.
- Edge orientation: [[ru-he-bu-bei-gong-shi-jie-kai-mo-fang-xiao-xue-sheng-ye-neng-kan-dong]] classifies edges by whether white or yellow faces up or down and uses `M`/`U` sequences to change the bad-edge pattern.
- Edge placement: [[ru-he-bu-bei-gong-shi-jie-kai-mo-fang-xiao-xue-sheng-ye-neng-kan-dong]] places the red and orange edges before resolving the final blue and green edges.

## Counterevidence & Qualifications
The source demonstrates one scramble and presents a beginner adaptation; it does not establish completeness case by case, compare move counts or learning outcomes with CFOP or other methods, or measure novice solve times. Its claim that Roux requires fewer moves and less memorization than many alternatives is plausible but unsupported here. A fixed orientation and supplied sequences may reduce cognitive load without making the method formula-free.

## What Changed
- Created a source-scoped account of Roux as a block-building and last-six-edges teaching scaffold.

## Related Concepts
- [[RubiksCubeSolving]] - Roux is one strategy for completing the 3×3 cube.
- [[Commutators]] - corner and edge cycles help preserve completed bridges during later stages.
- [[GroupTheory]] - reversible, order-sensitive moves underlie every stage of the method.
