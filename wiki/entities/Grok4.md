---
title: "Grok4"
type: entity
tags: [ai, model, voice-input]
sources:
  - ai-yu-yin-shu-ru-gong-ju-ti-shi-ci
last_updated: 2026-09-13
knowledge_schema: synthesis-v1
---

## Overview
[[Grok4]] is presented as the AI model used for post-processing in the author's [[Spokenly]] voice-input setup.

## Current Profile
The source pairs Grok4 with [[Soniox]]: Soniox transcribes speech, and Grok4 cleans the resulting text according to a detailed Chinese editing prompt. The author describes the output as stable and comfortable.

## Key Characteristics
- Serves as the AI cleanup model in a custom voice-input workflow.
- Is evaluated by the author through output feel rather than formal benchmarks.
- Operates under a prompt that forbids adding unsupported information.

## Evidence
- Setup role: [[ai-yu-yin-shu-ru-gong-ju-ti-shi-ci]] says the author uses Grok4 as the AI model in [[Spokenly]].
- Output impression: [[ai-yu-yin-shu-ru-gong-ju-ti-shi-ci]] describes the combined output as stable and comfortable.
- Prompt constraints: [[ai-yu-yin-shu-ru-gong-ju-ti-shi-ci]] gives the model detailed rules for punctuation, cleanup, structure, and information fidelity.

## Qualifications
The source does not compare Grok4 against other post-processing models beyond the author's practical setup.

## What Changed
- Created the initial entity profile for Grok4 as a voice-input post-processing model.

## Relationships
- [[AIVoiceInput]] - Grok4 performs the AI cleanup layer.
- [[Spokenly]] - Grok4 is used inside the author's Spokenly configuration.
- [[Soniox]] - paired with Soniox transcription in the workflow.
