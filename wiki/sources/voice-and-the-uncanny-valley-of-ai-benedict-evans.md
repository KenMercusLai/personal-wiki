---
title: "Voice and the uncanny valley of AI"
type: source
tags: [ai, voice-assistants, platform-strategy, ux, machine-learning]
date: 2017-03-09
source_file: '/mnt/ken_personal_wiki/Articles/Voice and the uncanny valley of AI — Benedict Evans.md'
---

## Summary
[[BenedictEvans]] asks why voice looked like the next platform in 2017 and finds real enablers - machine learning that finally made speech recognition and intent parsing work, a smartphone supply chain that makes microphones, CPUs, and wireless chips cheap, GAFA-scale revenue and talent, and platform anxiety at internet companies that do not control iOS or Android. His correction is that only the input half is solved: sound can be turned into text and routed as a query, but the "dialogue boxes" that answer it - flight booking, restaurant booking, scheduling - still have to be hand-built, so today's assistant is a machine-learned front end bolted onto a pre-data expert system. The essay's title image is the resulting [[UncannyValleyOfAI]]: better voice technology produced a worse experience at first, because the assistant invited requests it could not fulfil.

## Key Claims
- Voice *input* works in a way it did not before 2012: machine learning cut voice-recognition and natural-language error rates from roughly a third to under 5%, though a 5% error rate is still encountered daily.
- Voice is booming for non-model reasons too: the smartphone supply chain, Shenzhen contract manufacturing, enormous GAFA revenue, and platform anxiety about Apple and Google controlling mobile distribution.
- Recognising a request and being able to execute it are different problems, and the back-end dialogue box stays hand-built, so voice assistants scale only as far as someone has built and maintained the services behind them.
- The gap does not close with more machine learning: using data to build every possible query would amount to general AI, which the source puts decades away, so a machine-learned front end on a hand-crafted expert system remains the ceiling.
- Discoverability is the second scaling limit. Users must know what they can ask, and the ideal number of voice functions follows a U-shaped curve: one command is great, around ten is acceptable, and 50 or 100 is worst.
- Big platforms can partly escape the coverage limit because they already hold huge volumes of typed natural-language queries, so they can build structured responses for the top few hundred request types - [[Google]]'s knowledge graph - but that works on a screen and fails on an audio-only device.
- For most companies voice therefore needs a narrow and predictable domain where both the system's coverage and the user's expectations are bounded; Siri's structural problem was implying that anything could be asked, while Alexa communicated its limits better.
- Voice is not the right interface for some tasks even with a perfect assistant, because even human voice is too limited - you want to see options when rebooking a flight or buying clothes - so the honest fix is to add a screen and make voice optional.
- Adoption depends on habit, not capability. Alexa and the [[AppleWatch]] do nothing a phone cannot, but they move a task to a better context with less friction, and that only pays off once the user has changed their mental model and remembers the new option exists.

## Key Quotes
> "You can use voice to fill in a dialogue box, but the dialogue box has to exist - you need to have built it first." - on the back-end services that voice cannot generate.

> "The trap that some voice UIs fall into is that you pretend the users are talking to HAL 9000 when actually, you've just built a better IVR, and have no idea how to get from the IVR to HAL." - on the gap between the demo and the deployable system.

> "As a rendering of a person goes from 'cartoon' to 'real person' there's a point where increased realism makes it look less rather then more real - making the tech better produces a worse user experience at first." - the uncanny-valley framing.

> "For most companies, for voice to work really well you need a narrow and predictable domain." - the essay's practical conclusion.

## Connections
- [[BenedictEvans]] - author applying his platform-transition lens to voice rather than mobile hardware.
- [[UncannyValleyOfAI]] - the essay's central framing concept, created from this source.
- [[VoiceAssistantUX]] - the essay's scope, coverage, discoverability, and expectation-setting critique of spoken control.
- [[ConversationalUI]] - the same hand-built-dialogue-box limit appeared in the earlier chatbot wave, which the source calls "last year's Next Big Thing".
- [[NaturalLanguageInterface]] - voice is the spoken case of software that takes ordinary language as its input surface.
- [[MobileEcosystem]] - the smartphone supply chain and mobile platform control supply the essay's motive and opportunity.
- [[AmazonEcho]] - the source's main product example: roughly 10m Echos sold, ubiquitous Alexa partnerships at CES, and an assistant that communicates its limits better than Siri.
- [[AppleWatch]] - used as the friction-and-habit comparison case for a device that moves a task to a new context.
- [[Google]] - knowledge-graph-style structured answers for the head of the query distribution.
- [[ProductFlowFriction]] - voice is claimed to be lower friction, but only after a mental-model shift.
- [[AIKnowledgeAssistant]] - the broader promise of answering arbitrary questions that the source treats as general AI.

## Contradictions
- Qualifies [[chat-is-the-new-browser-ted-livingston-medium]]'s low-friction platform optimism by showing that the chatbot and voice waves shared an unsolved back-end coverage problem, not only an interface problem.
- Tensions with the source's own optimistic enablers: the essay argues the enabling conditions were real while denying that they implied a general assistant.
- The source contains no effective image references; the only non-prose element is a link to the original 2017 post.
