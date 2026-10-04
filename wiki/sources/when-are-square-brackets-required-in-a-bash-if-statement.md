---
title: "When are square brackets required in a Bash if statement?"
type: source
tags: [bash, shell, conditionals, exit-status]
date: 2012-01-19
source_file: "/mnt/ken_personal_wiki/Articles/When are square brackets required in a Bash if statement.md"
---

## Summary
This [[StackOverflow]] discussion explains [[BashConditionals]] through command status: Bash `if` executes a command and selects `then` when that command returns zero. Square brackets are not required `if` syntax; `[` is a command, usually a shell builtin, that evaluates expressions much like `test` and requires `]` as its final argument.

## Key Claims
- Bash `if` decides which branch to run from the exit status of a command, with zero meaning success and nonzero meaning failure.
- `grep -q "$text" "$file"` can serve directly as an `if` condition because `grep` already communicates match success or failure through its exit status.
- A bare comparison such as `"$name" = 'Bob'` is not a command, so it needs an evaluator such as `test` or `[`.
- `if test "$name" = 'Bob'` and `if [ "$name" = 'Bob' ]` express nearly the same test.
- `[` is a command rather than punctuation owned by `if`; unlike `test`, it requires a closing `]` argument.
- Bash commonly provides `[` as a builtin even when an external executable such as `/usr/bin/[` also exists.

## Key Quotes
> "An `if` statement checks the exit status of a command in order to decide which branch to take." — Answer 1

> "`[` is actually a command, equivalent (almost, see below) to the `test` command." — Answer 2

## Connections
- [[BashConditionals]] - captures the command-status model and the role of `[` and `test` as expression evaluators.
- [[StackOverflow]] - hosts the question and community answers summarized here.
- [[BashAsMetaTool]] - conditional execution lets shell programs compose commands according to their success or failure.
- [[ShellRedirection]] - another case where punctuation-looking shell notation has concrete operational semantics that matter for command composition.

## Contradictions
- No direct contradiction with the existing wiki was identified. The source corrects the common misconception that square brackets are mandatory syntax for every Bash `if` statement.
