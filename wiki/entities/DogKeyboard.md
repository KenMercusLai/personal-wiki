---
title: "DogKeyboard"
type: entity
tags: [software, automation, hardware, ai]
sources:
  - i-taught-my-dog-to-vibe-code-games-caleb-leak
last_updated: 2026-10-11
knowledge_schema: synthesis-v1
---

## Overview
[[DogKeyboard]] is Caleb Leak's Rust application for safely routing dog-generated keystrokes into Claude Code while coordinating submission, cues, recording overlays, and food rewards.

## Current Profile
The application sits between a Raspberry Pi keyboard proxy and [[ClaudeCode]]. It filters dangerous keys, targets the intended window, observes agent state through hooks, submits buffered input only when the agent is idle and a character threshold is met, removes eager input while the agent works, dismisses blocking Plan Mode prompts, and asks the Pi to dispense treats over Zigbee. It also supports delayed keystroke overlays for synchronized video recording.

## Key Characteristics
- Separates an uncontrolled physical keyboard from the target Windows application through network mediation and key filtering.
- Uses Claude Code hooks and idle state to time chimes and automatic submission.
- Couples a minimum character threshold to a pet-feeder reward command.
- Handles workflow stalls by clearing premature input and dismissing Plan Mode prompts.
- Exposes timing controls for recorded keystroke overlays.

## Evidence
- Input path: [[i-taught-my-dog-to-vibe-code-games-caleb-leak]] describes Raspberry Pi UDP broadcasts, key filtering, and injection into the selected application.
- Agent coordination: [[i-taught-my-dog-to-vibe-code-games-caleb-leak]] says hooks expose idle state, a chime cues Momo, and 16 characters trigger auto-submit.
- Reward integration: [[i-taught-my-dog-to-vibe-code-games-caleb-leak]] says DogKeyboard uses SSH to run two Zigbee feeder commands on the Pi.
- Blocking-state handling: [[i-taught-my-dog-to-vibe-code-games-caleb-leak]] says the app backspaces input received while Claude works and periodically dismisses Plan Mode prompts.
- Recording support: [[i-taught-my-dog-to-vibe-code-games-caleb-leak]] describes a web server and configurable delay for synchronizing a keystroke overlay with video.

## Qualifications
The source describes one personal setup and does not supply security analysis, packet-loss behavior, authentication details, reliability measurements, or a general safety review. Automatically dismissing review prompts is suitable only within the project's bounded environment and would weaken a meaningful approval gate elsewhere.

## What Changed
- Created DogKeyboard as the orchestration application joining keyboard input, agent state, and rewards.

## Relationships
- [[MomoDog]] - physical input source and reward recipient.
- [[CalebLeak]] - creator of the application and integrated workflow.
- [[ClaudeCode]] - target coding-agent process whose state controls submission and cue timing.
- [[HarnessEngineering]] - DogKeyboard supplies input constraints, state-aware orchestration, and an external reward loop.
