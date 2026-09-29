---
title: "Amazon Mechanical Turk"
type: entity
tags: [amazon, labor-platform, crowdsourcing, data-labeling, ai]
sources:
  - inside-amazons-clickworker-platform-how-half-a-million-people-are-being-paid-pennies-to-train-ai-techrepublic
last_updated: 2026-09-30
knowledge_schema: synthesis-v1
---

## Overview
[[AmazonMechanicalTurk]] is Amazon's online marketplace for Human Intelligence Tasks: small units of work posted by requesters and completed by distributed contract workers, including data labeling, transcription, surveys, data cleaning, and content moderation.

## Current Profile
The 2016 TechRepublic account portrays AMT as a programmable labor layer. Requesters define tasks and prices, restrict eligibility, approve or reject submissions, and can use an API-like system to move results into larger workflows. Workers compete for intermittent tasks and supply judgment where software cannot yet perform reliably. That made AMT important to [[DataAnnotationLabor]], including the large-scale human checking and labeling behind [[ImageNet]].

The same design created pronounced asymmetry. Workers carried search time, availability risk, rejection risk, equipment costs, and exposure to disturbing material. Location and an opaque Masters designation controlled access; cash payment was then limited to the United States and India; requester identity and purpose could remain obscure; and the platform offered no native reciprocal requester rating. Worker forums and [[Turkopticon]] partially rebuilt information and support outside Amazon's formal system.

## Key Characteristics
- Converts larger workflows into posted Human Intelligence Tasks that workers claim and complete for piece-rate pay.
- Gives requesters substantial control over price, eligibility, acceptance, and worker reputation.
- Supplies human judgment for AI training, data cleaning, moderation, research, retail, and other digital operations.
- Had more than 500,000 registered workers but an estimated 15,000–20,000 active workers per month in the article's 2016 snapshot.
- Uses location and a nontransparent Masters status to segment worker access to tasks and pay.
- Externalizes unpaid search, intermittent availability, rejection, payment conversion, and some health risks to workers.
- Supports machine-human systems in which automation handles routine cases while workers label, correct, or resolve exceptions.

## Evidence
Marketplace and scale:
- [[inside-amazons-clickworker-platform-how-half-a-million-people-are-being-paid-pennies-to-train-ai-techrepublic]] reports more than 500,000 registrations, 15,000–20,000 estimated monthly active workers, and an average of 1,278 daily requesters in 2015.

AI and digital operations:
- [[inside-amazons-clickworker-platform-how-half-a-million-people-are-being-paid-pennies-to-train-ai-techrepublic]] lists labeling, categorization, transcription, deduplication, moderation, surveys, and retail-data work and connects AMT labor to [[ImageNet]].

Worker access and pay:
- [[inside-amazons-clickworker-platform-how-half-a-million-people-are-being-paid-pennies-to-train-ai-techrepublic]] reports below-minimum-wage earnings for more than half of workers, geographic restrictions, cash-payment limits, and one non-Master worker eligible for only 393 of 4,911 visible tasks.

Governance and risk:
- [[inside-amazons-clickworker-platform-how-half-a-million-people-are-being-paid-pennies-to-train-ai-techrepublic]] documents opaque Masters selection, unexplained rejection, weak support, requester pseudonyms, nonreciprocal ratings, and worker exposure to graphic content.

## Qualifications
This profile is bounded to a December 2016 journalistic account and should not be treated as a description of current AMT policy, payment methods, workforce size, task mix, or support. Its numerical claims combine Amazon statements, outside estimates, survey findings, and a small set of worker examples. The source does not provide platform transaction logs, representative longitudinal worker outcomes, requester-side economics, or a causal comparison with alternative work.

## What Changed
- Created a profile that treats AMT simultaneously as AI infrastructure and a governed labor marketplace.
- Distinguished registered workforce scale from estimated monthly participation.
- Made worker-side information, payment, rejection, and health risks part of the platform profile.

## Relationships
- [[Amazon]] - parent company that created and governed the marketplace.
- [[PlatformMicrowork]] - labor model implemented through granular tasks, piece rates, and software-mediated allocation.
- [[DataAnnotationLabor]] - major task category through which workers make data usable for machine learning.
- [[ImageNet]] - dataset whose construction reportedly relied heavily on workers recruited through AMT.
- [[Turkopticon]] - external worker-built requester reputation system responding to platform opacity.
- [[AugmentedIntelligence]] - human-machine arrangement in which worker judgment supplements or teaches automated systems.
- [[WorkplaceAutomation]] - changes the mix and organization of tasks while also depending on human exceptions and labels.
