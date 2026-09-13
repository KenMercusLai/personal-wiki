---
title: "Technical Accessibility"
type: concept
tags: [technical-education, explanation, learning]
sources:
  - andrej-karpathy-on-x-on-technical-accessibility
last_updated: 2026-09-13
knowledge_schema: synthesis-v1
---

## Definition
[[TechnicalAccessibility]] is the work of making a technical artifact easier to approach, understand, and use by lowering its barrier to entry without changing the artifact's underlying substance.

## Current Synthesis
Karpathy's Micrograd reflection shows accessibility as a multiplier on existing technical work. The code was already short, commented, documented, and conceptually minimal, but it did not reach its full learning audience until Karpathy built a video ramp that walked through the system from scratch. The source is useful because it separates artifact quality from artifact approachability: people may ignore good work not because it lacks value, but because entering it requires too much unassisted effort.

## Key Claims
- Technical creators can mistake their own fluency for general clarity.
- Comments and README files may not be enough to make a compact codebase approachable.
- Accessibility work can increase the impact of an unchanged technical artifact.
- Beginners and experts both benefit from ramps that reduce initial engagement cost.
- From-scratch walkthroughs can turn a finished artifact into a teachable path.

## Evidence
- Creator fluency: [[andrej-karpathy-on-x-on-technical-accessibility]] says the Micrograd code made sense to Karpathy because he wrote it, but that did not mean it was self-explanatory to others.
- Documentation limits: [[andrej-karpathy-on-x-on-technical-accessibility]] says the repo was around 200 lines, extensively commented, and had a README, yet still stagnated.
- Impact multiplier: [[andrej-karpathy-on-x-on-technical-accessibility]] reports that the same code saw much larger engagement after the explanatory video.
- Expert benefit: [[andrej-karpathy-on-x-on-technical-accessibility]] notes that even technical friends could have understood the code with time but were deterred by the barrier to entry.
- Walkthrough ramp: [[andrej-karpathy-on-x-on-technical-accessibility]] frames the video as building the ramp after building the thing.

## Counterevidence & Qualifications
The source is a single creator reflection about one project, so its 10-100X framing should be treated as a practical heuristic rather than a general measured law. Better accessibility cannot rescue every weak artifact, and the source does not compare video against other ramps such as interactive notebooks, diagrams, examples, documentation, courses, or workshops.

## What Changed
- Created the concept to capture accessibility as a distinct layer around technical artifacts, not merely prose quality.

## Related Concepts
- [[ExplanatoryWriting]] - technical accessibility often depends on examples, sequencing, audience awareness, and revision.
- [[ActiveLearning]] - ramps can help learners move from passive reading into working through a system.
- [[FromScratchProtocolLearning]] - implementation-first walkthroughs are one way to make complex systems accessible.
- [[ComputerScienceZines]] - visual self-published formats are another accessibility strategy for technical ideas.
