---
title: "EAFP and LBYL"
type: concept
tags: [python, control-flow, exceptions, code-style]
sources:
  - idiomatic-python-eafp-versus-lbyl-python
last_updated: 2026-09-29
knowledge_schema: synthesis-v1
---

## Definition
[[EAFPAndLBYL]] are contrasting control-flow styles: “easier to ask forgiveness than permission” attempts the expected operation and handles a specific failure, while “look before you leap” checks a precondition before acting.

## Current Synthesis
In the article's [[Python]] dictionary example, LBYL tests whether a key exists before retrieving it, while EAFP retrieves it directly and catches `KeyError`. The choice is not only mechanical. EAFP communicates that success is normal and absence is a bounded alternative; LBYL foregrounds the precondition and may be clearer when the check itself is meaningful.

Safe EAFP depends on exception precision. Only the operation expected to fail should be inside the `try` block, and only its anticipated exception should be caught. Dependent work belongs in `else` or after successful retrieval so its own failures remain visible. This makes EAFP a qualified idiom, not permission to use broad exception handlers.

## Key Claims
- EAFP attempts the normal path first and handles a specific anticipated exception.
- LBYL checks a condition before performing the operation that depends on it.
- Control-flow shape communicates which case the author expects to be common.
- EAFP is safest when the `try` block contains only the operation whose failure is intentionally handled.
- Catching the precise exception prevents unrelated defects from being silently reclassified as an expected absence.
- Neither style is universally required; clarity, race exposure, side effects, and workload behavior can affect the choice.

## Evidence
- Control-flow distinction: [[idiomatic-python-eafp-versus-lbyl-python]] contrasts a dictionary membership test with direct lookup under `try`/`except KeyError`.
- Expected-case communication: [[idiomatic-python-eafp-versus-lbyl-python]] argues that direct lookup makes ordinary key presence the main path.
- Exception locality: [[idiomatic-python-eafp-versus-lbyl-python]] moves the dependent function call into `else` so a `KeyError` raised there is not swallowed.
- Style flexibility: [[idiomatic-python-eafp-versus-lbyl-python]] explicitly permits LBYL when EAFP feels overly explicit.
- Performance scope: [[idiomatic-python-eafp-versus-lbyl-python]] argues that Python's use of exceptions for control flow makes assumed exception cost a poor blanket objection.

## Counterevidence & Qualifications
The source is a short 2016 practitioner explanation, not comparative empirical evidence. Its performance claim is not benchmarked and can vary with interpreter, exception frequency, and workload. The dictionary example also does not cover cases where checking and acting are separated by concurrent state changes, where the attempted operation has irreversible side effects, or where a cheap validation produces a better user-facing error. EAFP should never be read as justification for `except Exception` around a large block.

## What Changed
- Created a joint concept that distinguishes EAFP from LBYL without treating either as a universal rule.
- Made narrow `try` scope and exception specificity part of the concept's safety boundary.

## Related Concepts
- [[Python]] - language context in which the source presents the two idioms.
- [[FunctionDesign]] - exception boundaries affect how clearly a function exposes intent and failure.
- [[InternalSoftwareQuality]] - precise handling improves readability and prevents accidental error suppression.
- [[ConcurrencyFailureModes]] - state can change between an LBYL check and the later action in concurrent settings.
