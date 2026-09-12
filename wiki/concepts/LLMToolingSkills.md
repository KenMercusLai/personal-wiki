---
title: "LLM Tooling Skills"
type: concept
tags: [ai, llm, prompting]
sources:
  - yi-kou-qi-ba-suo-you-rang-ni-mu-xuan-de-llm-ming-ci-quan-dou-guo-yi-bian
last_updated: 2026-09-12
knowledge_schema: synthesis-v1
---

## Definition
[[LLMToolingSkills]] are prompt-level instruction bundles that add domain knowledge, procedures, and reasoning guidance to an LLM's context without directly giving the model a new external action channel.

## Current Synthesis
The source presents Skills as pure prompt engineering. A Skill imports expert structure into the prompt so the model can approach a task with better assumptions and workflow, but it does not enforce execution like a runtime API. Its value is highest when a task needs richer thinking, domain framing, or loose coordination that cannot easily be reduced to RPC-style functions.

## Key Claims
- Skills add instructions and expert cognitive structure to the model context.
- Skill-following depends on the model's respect for context and remains probabilistic.
- Over-constraining model behavior can make reasoning less flexible.
- Skills do not directly modify the outside world; they need other tools or execution channels for action.
- Skills remain useful when a task is too open-ended, low-interaction, or expensive to encode as a dedicated server API.

## Evidence
- Prompt nature: [[yi-kou-qi-ba-suo-you-rang-ni-mu-xuan-de-llm-ming-ci-quan-dou-guo-yi-bian]] describes Skills as instructions shown to the LLM rather than external action channels.
- Compliance limit: [[yi-kou-qi-ba-suo-you-rang-ni-mu-xuan-de-llm-ming-ci-quan-dou-guo-yi-bian]] says the model may or may not use the Skill, follow steps, or choose the expected order.
- Flexibility qualification: [[yi-kou-qi-ba-suo-you-rang-ni-mu-xuan-de-llm-ming-ci-quan-dou-guo-yi-bian]] warns that hard constraints can narrow the model's thinking.
- Use case: [[yi-kou-qi-ba-suo-you-rang-ni-mu-xuan-de-llm-ming-ci-quan-dou-guo-yi-bian]] says Skills are valuable when the work needs fuller reasoning and cannot reasonably be packaged as RPC.

## Counterevidence & Qualifications
The source evaluates Skills conceptually rather than measuring task outcomes. It also uses "Skills" broadly; implementations may vary in how they are selected, injected, validated, or combined with tools.

## What Changed
- Created the concept page for Skills as prompt-level guidance rather than external execution infrastructure.

## Related Concepts
- [[LLMContextManagement]] - Skills manage context by adding structured instructions.
- [[ModelContextProtocol]] - MCP differs by exposing typed external tool calls.
- [[AIApplicationFramework]] - frameworks may combine prompt templates, tools, memory, and retrieval into application workflows.
- [[AIAgentCollaboration]] - coding-agent collaboration can use Skills to shape how agents reason with users.
