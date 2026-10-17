---
title: "Multicolor Dithering"
type: concept
tags: [dithering, color-printing, color-separation, special-inks]
sources:
  - spie2000-techart
last_updated: 2026-10-17
knowledge_schema: synthesis-v1
---

## Definition
[[MulticolorDithering]] converts local proportions of several basic colors into mutually exclusive pixel coverage by comparing one dither threshold against cumulative color proportions.

## Current Synthesis
For an in-gamut tristimulus value, tetrahedral color separation identifies four neighboring printable colors and expresses the target as their barycentric combination. Multicolor dithering accumulates those four proportions into ordered intervals and assigns each output location to exactly one color according to the local threshold. Unlike independently halftoned plates, the construction enforces side-by-side coverage and therefore supports opaque, semitransparent, fluorescent, metallic, and other nonstandard inks whose overlap is undesirable or unpredictable.

The dither matrix can also encode artistic motives. Combining a continuous motive surface with randomized background thresholds prevents the main shape from simply swelling at high coverage, while model-based local equilibration attempts to compensate for dot gain and human spatial sensitivity. These controls broaden the useful tonal range but do not replace device calibration, registration control, or gamut mapping.

## Key Claims
- Cumulative threshold intervals turn four barycentric color weights into exactly one selected basic color per output pixel.
- Tetrahedral decomposition connects a three-dimensional target color to the four printable colors used by the ditherer.
- Side-by-side coverage is valuable when opaque or special inks must not overlap.
- Partially random backgrounds can preserve an artistic motive over a wider coverage range than ordinary clustered growth.
- Local equilibration must model both printer dot gain and human visual filtering when large structured matrices create uneven apparent tone.

## Evidence
- Allocation mechanism: [[spie2000-techart]] diagrams black-white thresholding and its extension to four cumulative color proportions.
- Color separation: [[spie2000-techart]] decomposes an RGB cube into six tetrahedra and renders a wedge whose basic-color dots remain side by side.
- Motive preservation: [[spie2000-techart]] compares continuous and mixed continuous-random SIGGRAPH99 screens across a grayscale wedge.
- Physical and perceptual correction: [[spie2000-techart]] describes iterative local threshold changes after simulated dot gain and low-pass visual filtering.

## Counterevidence & Qualifications
The source assumes target colors lie inside the printable gamut and explicitly does not solve full printer calibration. Linear tetrahedral interpolation can miss measured output because registration, dot gain, ink density, substrate, and ink interaction remain device-specific. The visual examples do not quantify color error, motive recognition, robustness across presses, or comparison with calibrated alternatives. The claimed advantage of partial randomization shrinks when dot gain reduces high-coverage contrast.

## What Changed
- Established cumulative barycentric thresholding as the core side-by-side allocation rule.
- Connected artistic-motive preservation to mixed continuous and random thresholds.
- Made calibration, gamut, registration, and dot-gain boundaries explicit.

## Related Concepts
- [[ArtisticHalftoning]] - supplies recognizable screen motives that multicolor allocation can render with several inks.
- [[DigitalEngraving]] - shares threshold construction and local equilibration while targeting line-based portrait rendering.
