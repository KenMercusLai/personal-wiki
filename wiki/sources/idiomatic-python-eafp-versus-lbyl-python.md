---
title: "Idiomatic Python: EAFP versus LBYL"
type: source
tags: [python, code-style, exceptions, idioms]
date: 2016-06-29
source_file: /mnt/ken_personal_wiki/Articles/Idiomatic Python- EAFP versus LBYL - Python.md
---

## Summary
[[BrettCannon]] contrasts two [[Python]] control-flow idioms: EAFP performs the expected operation and handles a specific failure, while LBYL checks a precondition before acting. He argues that either can be legitimate, but EAFP often communicates the expected case more clearly when success is normal; its `try` block should remain narrow so unrelated exceptions are not accidentally suppressed.

## Key Claims
- [[EAFPAndLBYL]] differ in control-flow order: EAFP attempts an operation and catches an anticipated exception, while LBYL checks whether the operation should succeed first.
- The choice communicates expectations: an EAFP dictionary lookup suggests that the key is normally present, whereas a membership check emphasizes the possibility of absence.
- Python's preference for explicit code supports spelling out the specific failure path even when the EAFP form is longer.
- EAFP should catch only the intended exception and keep the `try` block as small as possible; otherwise an exception raised by later work can be mistaken for the anticipated lookup failure.
- LBYL remains reasonable when it is clearer or when the EAFP form would add disproportionate ceremony.
- The article says Python implementations make exception-based control flow cheap enough that developers should not reject EAFP on assumed performance grounds alone.

## Key Quotes
> "it’s easier to ask for forgiveness than permission" - definition of EAFP.

> "look before you leap" - definition of LBYL.

## Connections
- [[BrettCannon]] - author presenting EAFP as a legitimate Python style rather than a universal mandate.
- [[Python]] - language whose exception model and readability norms provide the article's context.
- [[EAFPAndLBYL]] - paired control-flow idioms compared through dictionary lookup examples.
- [[FunctionDesign]] - narrow exception boundaries keep a function call from being confused with the lookup it depends on.
- [[InternalSoftwareQuality]] - explicit intent and localized exception handling support readability and defect isolation.

## Contradictions
- No direct contradiction was found. The performance statement is an unbenchmarked 2016 generalization and should not replace measurement when exception frequency, interpreter, or workload makes cost material.
