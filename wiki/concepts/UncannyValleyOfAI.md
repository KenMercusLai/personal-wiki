---
title: "Uncanny Valley of AI"
type: concept
tags: [ai, product, ux, voice-assistants]
sources:
  - voice-and-the-uncanny-valley-of-ai-benedict-evans
last_updated: 2026-09-17
knowledge_schema: synthesis-v1
---

## Definition
[[UncannyValleyOfAI]] is the product-experience pattern in which improving an AI system's capability makes the product feel worse before it feels better, because added realism, fluency, or apparent generality raises user expectations faster than the system's real coverage grows.

## Current Synthesis
[[BenedictEvans]] borrows the computer-animation term and applies it to voice assistants in 2017: a rendering moving from cartoon toward a real person can look less real before it looks more real, just as a voice interface can feel more frustrating as it becomes more convincing. The mechanism is an expectation gap rather than a quality regression. Speech recognition and intent parsing had become good enough to invite arbitrary requests, while the set of things the assistant could actually execute stayed small and hand-built, so the assistant demoed well and then answered most real requests with a shrug. The essay's image for the failure is a system that pretends users are talking to HAL 9000 while it remains a better interactive voice response line, with no known path from one to the other.

The escape routes are scoping, expectation-setting, and honesty about the boundary rather than more raw capability. Narrow domains work because both sides know the edge of the system, such as timers, music, maps, or hotel rooms, and Amazon's Alexa is credited with communicating what could and could not be asked where Siri implied the opposite. Evans adds a second curve to the same argument: the useful number of voice functions is U-shaped, so one command is excellent, about ten is tolerable, and 50 or 100 is worse than either, because the user still cannot ask anything and can no longer remember the list. Platform scale only partly escapes the trap, since companies that already hold enormous volumes of typed queries can build structured answers for the most common request types, but that compensation depends on a screen and fails on an audio-only device. The essay's remaining contradictions, an interface that looks more general while being narrower, lower friction that appears only after a mental-model shift, a futuristic surface that resembles a feature phone or carrier deck, and a platform that may get worse as its ecosystem grows, are all versions of the same expectation-capability mismatch.

## Key Claims
- The valley is an expectation gap: capability improvements raise perceived generality faster than real coverage grows.
- For 2017 voice, recognition and intent parsing were solved well enough to invite requests the back end could not execute, and no data-driven method existed for building that back end.
- Narrow, predictable domains avoid the valley because the user learns the boundary, while open-ended framing triggers it.
- Function count follows a U-shaped usefulness curve, so adding more commands can lower the experience past roughly ten.
- Low-friction and general-assistant claims are conditional on a mental-model shift and a habit the user does not yet have.
- Platform-scale compensation is partial: query volume supports structured answers for the most common request types, and those answers fail without a screen.
- The valley is a way of judging AI products rather than evidence that the underlying technology regressed.

## Evidence
- Expectation gap: [[voice-and-the-uncanny-valley-of-ai-benedict-evans]] says the uncanny-valley concept captures that making the tech better produces a worse user experience at first.
- Demonstration gap: [[voice-and-the-uncanny-valley-of-ai-benedict-evans]] contrasts pretending users are talking to HAL 9000 with having built a better IVR and no idea how to get from the IVR to HAL.
- Coverage limit: [[voice-and-the-uncanny-valley-of-ai-benedict-evans]] says the dialogue box has to exist first, because machine learning builds the front end while the expert system stays hand-crafted and pre-data.
- General-AI boundary: [[voice-and-the-uncanny-valley-of-ai-benedict-evans]] says building answers to all possible questions by machine would be general AI, pretty much by definition, and is decades away.
- Discoverability curve: [[voice-and-the-uncanny-valley-of-ai-benedict-evans]] gives the U-shaped curve where one command is great, ten is probably OK, and 50 or 100 is terrible.
- Boundary communication: [[voice-and-the-uncanny-valley-of-ai-benedict-evans]] says Siri gave the impression you could ask anything while Alexa did a much better job of communicating what you can and cannot ask.
- Platform compensation: [[voice-and-the-uncanny-valley-of-ai-benedict-evans]] says platform companies can build structured responses to the top 100 or 500 request types from existing query volume, but that this works well on a screen and fails on an audio-only device.
- Contradiction set: [[voice-and-the-uncanny-valley-of-ai-benedict-evans]] lists the narrower-than-it-looks, less-friction-only-after-a-mental-shift, feature-phone-like, and worse-with-a-bigger-ecosystem contradictions as instances of the same pattern.
- Habit prerequisite: [[voice-and-the-uncanny-valley-of-ai-benedict-evans]] compares Alexa with the Apple Watch, arguing that both move a task to a new context with less friction only after the user changes their mental model and remembers the option exists.

## Counterevidence & Qualifications
This is a single-source concept built from a 2017 strategic essay, and the uncanny-valley term is borrowed from computer animation as a rhetorical analogy rather than a measured phenomenon. Its most period-specific claim, that the back end cannot be generated from data and must be hand-built, has weakened since large generative models could handle far more phrasing without per-intent construction, even though grounding, action coverage, permissions, latency, and reliability keep the same boundary in place. The essay also supplies its own counterweight: companies that hold natural-language query volume at scale can answer the head of the request distribution, which is why the valley bites hardest for small products with neither query data nor a narrow scope. Evans frames the moment as a stage rather than a verdict, closing with the expectation that voice is a big thing while the next platform shift is still to come.

## What Changed
- Created the concept from Evans's essay as the wiki's page for expectation-capability mismatch in AI products.
- Recorded the U-shaped command-count curve and the screen-dependence of platform-scale compensation as the source's two conditions for escaping the valley.

## Related Concepts
- [[VoiceAssistantUX]] - the source case where the valley is diagnosed, through scope, discoverability, and expectation setting.
- [[ConversationalUI]] - text bots show the same expectation gap and the same hand-built coverage limit.
- [[AIMarketingHype]] - the marketing-side version of the gap, where labels raise expectations beyond the delivered capability.
- [[ProductFlowFriction]] - promised lower friction only materializes after habit and mental-model change.
- [[NaturalLanguageInterface]] - the broader interface pattern whose apparent generality creates the gap.
- [[AmazonEcho]] - the product example credited with communicating its limits better than a rival assistant.
