---
title: "Capability Accessibility"
type: concept
tags: [usability, accessibility, user-interface, computing]
sources:
  - creation-and-consumption-benedict-evans
  - hover-is-dead-long-live-hover
last_updated: 2026-09-29
knowledge_schema: synthesis-v1
---

## Definition
[[CapabilityAccessibility]] is the practical availability of a computing function to a person, determined not only by whether the feature exists but also by whether the person can discover, understand, and operate it with the inputs available in context.

## Current Synthesis
Evans separates two meanings of "can't": technical absence and unusability. Experts often compare devices by asking which specialized operations the hardware and software permit, but ordinary users experience undiscoverable or incomprehensible features as if those features did not exist. This changes the platform comparison: a simpler interface can remove or postpone some expert functions while expanding effective capability for a much larger population.

Staniscia adds a device-input case. A commenting feature existed on a desktop web page, but a Surface Pro user navigating by touch could not reveal its hover-only controls. Practical availability therefore depends not just on user knowledge and interface abstraction, but on whether the interface exposes an operable path for the input modality actually in use. A hybrid device can cross categories, making assumptions based on laptop form or viewport width unreliable.

The mobile creation examples show the same broader principle. PC workflows such as downloading, installing, moving files, or importing camera photographs imposed abstractions that many users never mastered, whereas phones combine capture, editing, communication, and sharing in a more direct flow. Capability accessibility concerns the match among interface model, user knowledge, input capability, and task, not a claim that one device is universally simpler or more powerful.

## Key Claims
- Feature presence is insufficient when users cannot discover, understand, or operate the feature.
- Device comparisons should distinguish expert capability ceilings from mainstream effective capability.
- Simpler interface abstractions can expand participation even when they initially constrain specialized users.
- Integrated capture, editing, and sharing workflows can turn previously expert operations into ordinary creation.
- Input assumptions can make an existing feature unavailable when the active modality cannot trigger its controls.
- Capability remains task-, user-, and context-dependent; broad accessibility does not erase precision-heavy professional requirements.

## Evidence
Technical versus practical absence:
- [[creation-and-consumption-benedict-evans]] distinguishes a missing feature from a feature that a person does not know how to use.
- [[hover-is-dead-long-live-hover]] shows the parallel case of a present feature whose hover trigger could not be operated by a touch user.

Interface abstraction and participation:
- [[creation-and-consumption-benedict-evans]] uses software installation and digital-camera transfer to show how available PC functions could remain practically inaccessible.
- [[creation-and-consumption-benedict-evans]] argues that iOS and Android made writing, photography, video, sharing, and app use understandable to many more people.

Input-path availability:
- [[hover-is-dead-long-live-hover]] describes a Surface Pro user who could read and scroll a desktop page by touch but could not reveal paragraph-level commenting controls.
- [[hover-is-dead-long-live-hover]] recommends preserving hover feedback while providing a finger-operable primary route to the same essential action.

Expert qualification:
- [[creation-and-consumption-benedict-evans]] preserves a class of precise professional tasks that phones and tablets could not perform in the source's 2017 context.

## Counterevidence & Qualifications
Both sources are historical practitioner essays supported by illustrative examples rather than controlled comparisons. Simplicity for mainstream users can hide state, reduce interoperability, limit repair or automation, and create new accessibility barriers. The sources do not comprehensively analyze disability access, assistive technology, keyboard-only use, mobile-only disadvantage, later platform changes, or the effects of affordability, connectivity, charging, language, training, peripherals, and institutional workflow. The hover case is one observed participant, so it strongly demonstrates possibility rather than failure prevalence.

## What Changed
- Added input modality as a determinant of whether a technically present capability is practically available.
- Replaced device-form assumptions with a context model that includes the input actually being used.

## Related Concepts
- [[InputModalityIndependence]] - operationalizes capability accessibility by preserving essential actions across touch and pointer input.
- [[MobileProductivity]] - mobile-centered workflows can make creation and routine work accessible without reproducing every PC convention.
- [[MobileInternet]] - the smartphone becomes meaningful as a primary computer when people can use its capabilities directly.
- [[MobileEcosystem]] - platform scale grows through both distribution and usable capability.
- [[TechnicalAccessibility]] - applies the same barrier-lowering logic to approaching and understanding technical artifacts.
- [[ConstraintShapedInterfaceDesign]] - interface constraints can simplify interaction while changing which tasks remain practical.
