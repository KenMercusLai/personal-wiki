---
title: "Bluetooth Audio Routing"
type: concept
tags: [bluetooth, audio, linux, device-integration]
sources:
  - life-pro-tip-a-steam-deck-can-be-a-bluetooth-speaker
last_updated: 2026-10-07
knowledge_schema: synthesis-v1
---

## Definition
[[BluetoothAudioRouting]] is the use of Bluetooth audio roles and system sound controls to send audio from one computing device into another device that acts as the shared playback endpoint.

## Current Synthesis
The source demonstrates a practical topology in which a laptop treats a [[SteamDeck]] as its speaker, while the Deck also supplies its own game audio to the listener's headphones. This turns the Deck into an aggregation point for otherwise separate personal and work sound sources. The setup is valuable where speakers would disturb others, but the source establishes only one successful configuration rather than universal Linux support or an unlimited input count.

## Key Claims
- A general-purpose Linux device can, in at least the reported configuration, expose a Bluetooth audio-receiver role to another computer.
- Routing multiple source devices through one endpoint can work around a headphone's single-source constraint.
- Computer-to-computer Bluetooth pairing may be hidden behind expanded device-discovery controls.
- Centralizing final volume at the receiving device simplifies control when sender volumes are maximized.

## Evidence
- Receiving role: [[life-pro-tip-a-steam-deck-can-be-a-bluetooth-speaker]] reports pairing a laptop with a Steam Deck and selecting the Deck as the laptop's speaker.
- Aggregation use case: [[life-pro-tip-a-steam-deck-can-be-a-bluetooth-speaker]] combines Deck notifications, work-laptop notifications, personal-laptop music, and potentially phone audio for private listening.
- Physical setup: [[life-pro-tip-a-steam-deck-can-be-a-bluetooth-speaker]] shows a Deck and two laptops sharing one coworking desk.

## Counterevidence & Qualifications
The source does not identify the Bluetooth profile or audio server, document per-distribution configuration, or test latency, codecs, synchronization, reconnect behavior, battery cost, and simultaneous-input capacity. Its claims that any Linux device can work and that inputs have no real limit therefore remain source-scoped. Multipoint headphones may also address part of the motivating problem, but the article does not compare them.

## What Changed
- Created the concept from the reported Steam Deck audio-routing procedure.

## Related Concepts
- [[SteamDeck]] - acts as the shared receiving and playback endpoint in the reported setup.
- [[life-pro-tip-a-steam-deck-can-be-a-bluetooth-speaker]] - supplies the procedure and current evidence boundary.
