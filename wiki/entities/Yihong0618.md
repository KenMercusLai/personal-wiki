---
title: "Yihong0618"
type: entity
tags: [software-engineering, reverse-engineering, blogging]
sources:
  - gitblog-205-leetcode-runtime
last_updated: 2026-10-25
knowledge_schema: synthesis-v1
---

## Overview
[[Yihong0618]] is the author of a runtime-introspection investigation into LeetCode's historical Python execution environment.

## Current Profile
The available source shows Yihong0618 using submitted Python code as an observational probe: printing globals and loaded modules, enumerating directories, and reading the generated runner. The investigation connects a surprising name-resolution bug to `from re import *`, then reconstructs how [[LeetCode]] joined platform code, a user `Solution`, typed input conversion, method invocation, and output serialization inside an apparently containerized runtime.

The author also models appropriate temporal caution. When a reader asked in 2026 whether LeetCode still sent code into Docker, he answered that this had been true five years earlier but that he was no longer certain.

## Key Characteristics
- Uses small runtime probes to reveal hidden execution context.
- Connects observed namespace behavior to the underlying imported module symbol.
- Reads generated glue code to explain platform behavior end to end.
- Distinguishes historical observation from current knowledge in a later follow-up.

## Evidence
- Namespace probe: [[gitblog-205-leetcode-runtime]] prints `L`, globals, and loaded modules from a submitted solution.
- Filesystem probe: [[gitblog-205-leetcode-runtime]] enumerates the working directory, root filesystem, and `/mnt`.
- Harness reconstruction: [[gitblog-205-leetcode-runtime]] reads and reproduces the generated Python runner.
- Temporal qualification: [[gitblog-205-leetcode-runtime]] includes the author's 2026 statement that the current Docker arrangement is unknown.

## Qualifications
This profile is derived from one technical post and one short author follow-up. It does not establish the author's broader biography, current work, or expertise beyond the demonstrated investigation, and the reproduced motivating code contains an unrelated syntax error that narrows what the example proves.

## What Changed
- Created the entity profile from the runtime investigation and later qualification.

## Relationships
- [[LeetCode]] - platform whose historical Python runner the author inspected.
- [[OnlineJudgeExecutionHarness]] - architecture reconstructed through generated-code and filesystem inspection.
- [[Python]] - language used both as submission code and as the introspection mechanism.
- [[Docker]] - historical runtime inference the author later declined to generalize to the current system.
