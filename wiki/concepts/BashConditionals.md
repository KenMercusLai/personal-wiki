---
title: "Bash Conditionals"
type: concept
tags: [bash, shell, conditionals, exit-status]
sources:
  - when-are-square-brackets-required-in-a-bash-if-statement
last_updated: 2026-10-04
knowledge_schema: synthesis-v1
---

## Definition
[[BashConditionals]] are control-flow constructs in which `if` executes a command or command list and chooses a branch according to its exit status, rather than requiring a Boolean expression enclosed in square brackets.

## Current Synthesis
The central model is command success. In Bash, status zero is success and selects the `then` branch; a nonzero status selects `else` when present. A command such as `grep -q` can therefore be used directly as a condition because it already reports its result through an exit status.

Square brackets become useful when the desired condition starts as a string, numeric, or file expression rather than as a command. The `[` command evaluates that expression and returns a status for `if` to consume. It is nearly equivalent to `test`, except that `[` requires `]` as its final argument. The brackets are consequently command arguments with spacing requirements, not general grouping punctuation supplied by `if`.

## Key Claims
- Bash `if` branches on the success or failure status of a command or command list.
- Commands that already encode the desired result in their status can be used directly as conditions.
- Comparisons and file predicates need an evaluator such as `test` or `[` because a bare expression is not a command.
- `[` is a command, commonly implemented as a Bash builtin, rather than mandatory `if` syntax.
- `[` and `test` are nearly equivalent, but `[` requires `]` as its final argument.

## Evidence
- Command-status model: [[when-are-square-brackets-required-in-a-bash-if-statement]] explains that `if` runs a command, treats status zero as success, and uses nonzero status as failure.
- Direct command condition: [[when-are-square-brackets-required-in-a-bash-if-statement]] contrasts `grep -q` with a bare string comparison because `grep` already supplies a usable result status.
- Expression evaluation: [[when-are-square-brackets-required-in-a-bash-if-statement]] rewrites the name comparison first with `test` and then with `[ ... ]`.
- Command identity: [[when-are-square-brackets-required-in-a-bash-if-statement]] identifies `[` as a command that Bash normally provides as a builtin while an external executable may also exist.
- Closing argument: [[when-are-square-brackets-required-in-a-bash-if-statement]] distinguishes `[` from `test` by the former's required final `]` argument.

## Counterevidence & Qualifications
The source gives a compact mental model rather than a complete Bash conditional reference. It does not compare single brackets with Bash's `[[ ... ]]` compound command, arithmetic conditions, compound command lists, pipelines, negation, short-circuit operators, or the distinct non-match and error statuses that commands such as `grep` can return. Its sample leaves `$file` unquoted; production code generally must consider word splitting, globbing, option parsing, and command-specific status conventions. The external `/usr/bin/[` example establishes that `[` can be an executable, but Bash will normally resolve its builtin first.

## What Changed
- Created the concept around command exit status rather than bracket-shaped syntax.
- Clarified the difference between direct command conditions and evaluated expressions.
- Recorded the required closing `]` as an argument to the `[` command.

## Related Concepts
- [[BashAsMetaTool]] - status-driven branching lets shell programs coordinate tools according to success and failure.
- [[ShellRedirection]] - both concepts expose the operational meaning behind compact shell notation.
- [[AutomationFriendlyCLI]] - predictable exit statuses let other shell programs use a command reliably in conditional control flow.
- [[CommandLineUX]] - human-readable output and machine-consumable success status are separate parts of a command's interface.
