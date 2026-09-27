---
title: "PERT Estimation"
type: concept
tags: [software-engineering, estimation, uncertainty, planning]
sources:
  - estimation-for-fun-and-profit-but-mostly-for-sanity-8th-light
last_updated: 2026-09-27
knowledge_schema: synthesis-v1
---

## Definition
[[PERTEstimation]] is a three-scenario estimation method that asks for optimistic, realistic, and pessimistic completion times so uncertainty, risks, and confidence become explicit rather than being hidden inside one duration guess.

## Current Synthesis
PERT acts as an antidote to idealized software schedules. The optimistic case assumes unusually favorable working conditions, the realistic case captures an ordinary-day judgment, and the pessimistic case explores adverse conditions such as interruptions and blockers. Considering all three can reveal risks that a single most-likely estimate leaves implicit.

The article pairs this scenario method with team elicitation. In “Flying Fingers,” people consider the work individually and reveal point estimates simultaneously; wide variation then becomes a reason to compare assumptions and concerns. This pairing separates two useful questions: what range of conditions could affect the work, and how differently do team members understand it?

## Key Claims
- One duration estimate conceals the range of plausible working conditions.
- Optimistic, realistic, and pessimistic inputs force favorable, ordinary, and adverse cases into the discussion.
- Pessimistic estimation can surface blockers and risks excluded by idealized planning.
- Standard deviation is presented as a way to express confidence around the combined estimate.
- Independent, simultaneous team estimates reduce the influence of an early dominant opinion.
- Large differences among team estimates are evidence of assumptions or concerns worth discussing.

## Evidence
- Scenario structure: [[estimation-for-fun-and-profit-but-mostly-for-sanity-8th-light]] defines optimistic, realistic, and pessimistic completion-time inputs.
- Risk discovery: [[estimation-for-fun-and-profit-but-mostly-for-sanity-8th-light]] says explicit permission to be pessimistic can expose risks and blockers.
- Confidence framing: [[estimation-for-fun-and-profit-but-mostly-for-sanity-8th-light]] says a PERT calculator combines the inputs and reports confidence using standard deviation.
- Team elicitation: [[estimation-for-fun-and-profit-but-mostly-for-sanity-8th-light]] describes individual reflection followed by simultaneous finger voting.
- Disagreement signal: [[estimation-for-fun-and-profit-but-mostly-for-sanity-8th-light]] treats widely varying estimates as a prompt to discuss concerns and confidence.

## Counterevidence & Qualifications
The evidence is one 2016 practitioner article with no forecast-versus-actual results, calibration data, controlled comparison, or worked calculation. It does not specify the PERT formula, distributional assumptions, units, or how standard deviation becomes a confidence statement. Its optimistic and pessimistic examples mix task uncertainty with meetings, blockage, fatigue, and interruption, which may be better modeled separately when they have different causes. Simultaneous reveal can reduce public anchoring, but prior discussion can still anchor the group, and averaging divergent votes can erase meaningful disagreement rather than resolve it.

## What Changed
- Created a three-scenario estimation concept that separates schedule range from team disagreement.
- Preserved the article's confidence claim while qualifying its missing formula and calibration evidence.

## Related Concepts
- [[SoftwareEstimation]] - broader practice in which PERT makes uncertainty and risk more explicit.
- [[UserStories]] - source applies the method to a vertically sliced, acceptance-tested story.
- [[CrossFunctionalProductTeams]] - diverse team input can expose different assumptions about the same work.
- [[AgileSoftwareDevelopment]] - iterative delivery context in which estimates guide coordination without becoming guarantees.
- [[BackOfEnvelopeEstimation]] - related decomposition practice for plausibility checks rather than schedule scenarios.
