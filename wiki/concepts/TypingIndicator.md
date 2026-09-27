---
title: "Typing Indicator"
type: concept
tags: [instant-messaging, presence, interaction-design, privacy]
sources:
  - danny-glasser-is-typing-danny-glasser
last_updated: 2026-09-26
knowledge_schema: synthesis-v1
---

## Definition
[[TypingIndicator]] is a transient messaging state that tells participants someone is actively composing input without transmitting the unfinished text itself.

## Current Synthesis
The original MSN Messenger design is a deliberately lossy presence signal. The sender periodically communicates activity while entering data; the receiver displays an indicator and removes it after activity updates stop. That protocol gives a conversation enough information to coordinate turn-taking without the bandwidth and privacy cost of streaming every character. The visible words or animation are only one layer: the source distinguishes the underlying detection, update, and timeout behavior from the final interface created around it.

## Key Claims
- A typing indicator mediates between no response feedback and full exposure of an unfinished draft.
- Periodic activity updates reduce communication to a state signal rather than keystroke content.
- Receiver-side expiry is part of correctness because abandoned or interrupted input must not leave a permanent typing state.
- The design trades precision for network efficiency and limited compositional privacy.
- Patent authorship for the mechanism does not capture all design and implementation work in the shipping experience.
- The interaction became a durable convention across consumer messaging and customer-support chat.

## Evidence
- Design trade-off: [[danny-glasser-is-typing-danny-glasser]] contrasts IRC and AIM's absent signal with Unix talk and ICQ's character-by-character display.
- Protocol behavior: [[danny-glasser-is-typing-danny-glasser]] retains the patent page describing periodic activity messages and timer-based removal.
- Privacy boundary: [[danny-glasser-is-typing-danny-glasser]] retains paired classroom mock-ups where the sender sees a draft but the recipient sees only “is writing a message.”
- Product adoption: [[danny-glasser-is-typing-danny-glasser]] names Facebook Messenger, iMessage, WhatsApp, Skype, and support-chat plugins as later examples.
- Collaborative implementation: [[danny-glasser-is-typing-danny-glasser]] credits Glasser with the mechanism and rough UI while crediting Auerbach and others with the polished shipping interface.

## Counterevidence & Qualifications
The source is a first-person historical account and does not independently establish priority across every earlier messaging system. A typing signal protects draft content relative to character streaming, but it still reveals presence, timing, responsiveness, and interruption patterns. The patent image explains one implementation family, not every modern product's protocol, and the article explicitly avoids a definitive claim about later infringement.

## What Changed
- Created the concept as a protocol-and-interaction trade-off rather than only a familiar UI animation.

## Related Concepts
- [[PrototypeFirstProductDiscovery]] - the original mechanism was made tangible with a rough interface and validated through self-hosting.
- [[MessagingAsPlatform]] - typing state is one interaction primitive inside broader messaging runtimes.
- [[CommunicationMultitasking]] - persistent activity signals can coordinate conversation while also increasing perceived response pressure.
- [[LocationDataPrivacy]] - related by the broader principle that useful presence signals can reveal behavioral metadata without exposing primary content.
