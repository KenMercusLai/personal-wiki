---
title: "Steam Deck"
type: entity
tags: [gaming-hardware, linux, bluetooth, audio]
sources:
  - life-pro-tip-a-steam-deck-can-be-a-bluetooth-speaker
last_updated: 2026-10-07
knowledge_schema: synthesis-v1
---

## Overview
[[SteamDeck]] is presented as a Linux gaming device that can also act as a Bluetooth speaker for paired computers, consolidating their sound with its own output.

## Current Profile
In the source's coworking-space setup, the Deck sits alongside two laptops and supplies a common audio endpoint when the user's headphones would otherwise receive only one device at a time. Pairing a laptop to the Deck and selecting the Deck as the laptop's speaker routes that laptop's audio through the Deck; the source recommends maximizing sender volume and controlling final volume on the Deck.

## Key Characteristics
- Acts as a Bluetooth audio receiver for a paired computer in the reported setup.
- Can combine received computer audio with locally generated game notifications before headphone playback.
- May require Bluetooth discovery settings that expose computer-to-computer pairings.
- Provides the final volume-control point when sender volumes are maximized.

## Evidence
- Multi-device role: [[life-pro-tip-a-steam-deck-can-be-a-bluetooth-speaker]] describes routing laptop audio to the Deck while retaining Deck game notifications in the same listening setup.
- Physical context: [[life-pro-tip-a-steam-deck-can-be-a-bluetooth-speaker]] includes a photograph of the Deck beside two laptops at a coworking-space desk.
- Setup sequence: [[life-pro-tip-a-steam-deck-can-be-a-bluetooth-speaker]] instructs users to expose all Bluetooth devices, confirm pairing on both endpoints, choose the Deck as speaker, and centralize volume control there.

## Qualifications
The profile is limited to one author's successful setup. The source does not name the Bluetooth profile, SteamOS version, headphones, number of simultaneous senders actually tested, latency, mixing behavior, battery impact, or reconnect reliability. Its statement that there is "no real limit" to inputs is practical rhetoric rather than a demonstrated capacity bound.

## What Changed
- Created the entity from the source's reported Bluetooth audio-receiver setup.

## Relationships
- [[BluetoothAudioRouting]] - the Steam Deck is the receiving and mixing endpoint in the described multi-device workaround.
- [[life-pro-tip-a-steam-deck-can-be-a-bluetooth-speaker]] - provides the setup procedure and the sole evidence currently informing this profile.
