---
title: "37signals"
type: entity
tags: [company, software, customer-support, ai]
sources:
  - dhh-its-easier-to-forgive-a-human-than-a-robot
  - guide-37signals-how-we-communicate
last_updated: 2026-09-29
knowledge_schema: synthesis-v1
---

## Overview
[[37signals]] is represented in this wiki as a software company whose operating practices connect [[AsynchronousWorkplaceCommunication]], [[Basecamp]], and cautious experimentation with AI customer support.

## Current Profile
37signals is presented as a writing-led, remote organization that centralizes almost all internal communication in Basecamp. It favors asynchronous exchange, durable decisions, delayed response, contextual discussion attached to work objects, and predictable daily, weekly, and six-week reporting rhythms. Meetings and video calls remain available but are treated as exceptions whose combined time and interruption cost must be justified.

The same operating profile includes cautious AI-support experimentation inside [[AutomationErrorTolerance]]. AI support could answer hard questions well, but occasional severe errors raised an unresolved product threshold: customers may punish authoritative machine nonsense more strongly than a comparable human mistake. The evidence does not identify the systems, test design, deployment status, volume, or measured error rate.

## Key Characteristics
- Uses Basecamp as the centralized record for nearly all reported internal communication.
- Defaults to asynchronous, long-form, context-attached writing while reserving real-time communication for selective use.
- Uses automatic prompts, Heartbeats, and Kickoffs to share reflection, plans, and social context at predictable intervals.
- Experimented with AI systems for customer-support interactions.
- Observed a mix of strong difficult-case performance and materially wrong answers.
- Treated customer trust and negative word of mouth as constraints on acceptable automation error.

## Evidence
- Communication system: [[guide-37signals-how-we-communicate]] describes writing-led norms, a reported 98% Basecamp share, and task- or document-local discussions.
- Awareness cadence: [[guide-37signals-how-we-communicate]] describes daily reflection, weekly planning, optional social questions, and six-week Heartbeats and Kickoffs.
- Synchronous boundary: [[guide-37signals-how-we-communicate]] treats meetings as a last resort while preserving occasional small video conversations.
- Experiment context: [[dhh-its-easier-to-forgive-a-human-than-a-robot]] says 37signals tried several AI customer-support systems.
- Mixed performance: [[dhh-its-easier-to-forgive-a-human-than-a-robot]] reports that the systems handled some hard cases well and got other answers seriously wrong.
- Adoption concern: [[dhh-its-easier-to-forgive-a-human-than-a-robot]] asks whether even a one-percent machine error rate could be psychologically unacceptable despite worse human performance.

## Qualifications
Both sources are first-party practitioner accounts. The communication guide reports intended norms without comparative output, decision-quality, inclusion, or employee-experience evidence. The AI source gives no sample size, task mix, model names, comparison group, severity rubric, customer outcomes, or production status; its proposed error rates are speculative rather than performance measurements.

## What Changed
- Created the company profile from its role in the source's customer-support AI experiment.
- Added the company's writing-led, asynchronous communication system and its use of Basecamp as a shared record.

## Relationships
- [[DavidHeinemeierHansson]] - author reporting the company's AI support experiments.
- [[JasonFried]] - co-founder and author documenting the company's internal communication norms.
- [[Basecamp]] - product and central workspace used for the company's internal communication.
- [[AsynchronousWorkplaceCommunication]] - dominant communication model described in the guide.
- [[AutomationErrorTolerance]] - the experiments motivate the question of how much less error users tolerate from machines.
