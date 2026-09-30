---
title: "Live Listen"
type: entity
tags: [apple, ios, accessibility, audio, privacy]
sources:
  - juli-clover-airpods-live-listen-hearing-aid-or-spy-tool
last_updated: 2026-10-01
knowledge_schema: synthesis-v1
---

## Overview
[[LiveListen]] is an Apple audio feature that uses an iPhone as a remote microphone and relays nearby sound to [[AirPods]], MFi hearing aids, or other compatible Bluetooth headphones.

## Current Profile
The source presents Live Listen as an accessibility capability with a consequential privacy boundary. It had long supported MFi-compatible hearing aids before iOS 12 made it available to general AirPods users. Once enabled through the Hearing control in Control Center, it lets a person place an iPhone nearer a sound source and listen through a paired device.

That separation between microphone and listener is the feature's value and its misuse path. It can bring speech closer to someone with hearing difficulty, but it can also relay a conversation from another room without the speakers realizing that the unattended phone is acting as a microphone. Live Listen is therefore a concrete case of [[AssistiveTechnologyDualUse]] rather than evidence that accessibility and privacy are inherently opposed.

## Key Characteristics
- Uses an iPhone microphone as a remotely positioned audio input.
- Relays captured sound to AirPods, MFi hearing aids, or compatible Bluetooth headphones.
- Extends an earlier hearing-aid capability to general AirPods users in iOS 12.
- Is activated through the Hearing control in Control Center.
- Remains limited by the Bluetooth connection range between the iPhone and listening device.
- Can support hearing access or enable covert room-to-room listening through the same technical path.

## Evidence
- Remote-audio path: [[juli-clover-airpods-live-listen-hearing-aid-or-spy-tool]] says the iPhone acts as the microphone and relays what it captures to the paired listening device.
- Accessibility history: [[juli-clover-airpods-live-listen-hearing-aid-or-spy-tool]] says Live Listen existed for MFi-compatible hearing aids before AirPods support arrived with iOS 12.
- User control: [[juli-clover-airpods-live-listen-hearing-aid-or-spy-tool]] provides the Control Center setup and activation sequence.
- Dual-use behavior: [[juli-clover-airpods-live-listen-hearing-aid-or-spy-tool]] describes leaving an iPhone near a conversation and listening through AirPods from another room within Bluetooth range.

## Qualifications
The source is a short 2019 technology-news article, not a usability, accessibility-outcome, range, security, or abuse-prevalence study. It does not test specific AirPods models, other Bluetooth headphones, microphone indicators, consent safeguards, later iOS behavior, or whether people actually used the feature for covert listening. Its “spy tool” framing describes a technically possible misuse rather than measured incidence or intended product design.

## What Changed
- Established Live Listen as a distinct feature whose remote-microphone architecture connects hearing assistance with a covert-listening risk.

## Relationships
- [[AirPods]] - supported listening endpoint that made Live Listen available beyond MFi hearing aids in iOS 12.
- [[IOS]] - operating system through which the source says AirPods support and Control Center access were provided.
- [[AssistiveTechnologyDualUse]] - Live Listen is a concrete example of one capability supporting access and creating a misuse path.
- [[PersonalAudioComputing]] - Live Listen extends ear-worn audio interaction by separating the microphone from the listener.
