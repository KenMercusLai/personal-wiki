---
title: "Brett Cannon"
type: entity
tags: [python, software-development, writing]
sources:
  - idiomatic-python-eafp-versus-lbyl-python
last_updated: 2026-09-29
knowledge_schema: synthesis-v1
---

## Overview
[[BrettCannon]] is represented in the wiki as a Python practitioner and author explaining how control-flow style communicates a programmer's expectations.

## Current Profile
Cannon presents [[EAFPAndLBYL]] as two legitimate Python idioms rather than a rigid good-versus-bad rule. His main concern is semantic clarity: code should reveal whether success is the expected path and should isolate the exact operation whose failure is being handled.

## Key Characteristics
- Explains Python idioms through small dictionary-access examples.
- Treats code structure as communication about normal and exceptional cases.
- Prefers specific exception handling and narrow `try` blocks.
- Allows LBYL when it is clearer than an explicit EAFP form.

## Evidence
- Idiom comparison: [[idiomatic-python-eafp-versus-lbyl-python]] contrasts membership checking with `try`/`except KeyError`.
- Communication emphasis: [[idiomatic-python-eafp-versus-lbyl-python]] interprets control-flow order as a signal about the expected case.
- Safety boundary: [[idiomatic-python-eafp-versus-lbyl-python]] separates dictionary access from the dependent function call so the latter's own `KeyError` is not suppressed.

## Qualifications
The wiki currently has one Cannon source, so this is a source-scoped technical profile rather than a full biography or summary of his broader work on Python.

## What Changed
- Created Brett Cannon as the author entity for the EAFP and LBYL article.

## Relationships
- [[Python]] - language and implementation culture discussed in the article.
- [[EAFPAndLBYL]] - paired idioms Cannon explains and qualifies.
- [[FunctionDesign]] - narrow exception boundaries clarify which operation is allowed to fail.
- [[InternalSoftwareQuality]] - readability and precise failure handling are the article's quality outcomes.
