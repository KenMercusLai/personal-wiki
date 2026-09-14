---
title: "LLM Tooling Skills"
type: concept
tags: [ai, llm, prompting]
sources:
  - yi-kou-qi-ba-suo-you-rang-ni-mu-xuan-de-llm-ming-ci-quan-dou-guo-yi-bian
  - wei-shen-me-ai-xie-dai-ma-geng-kuai-dan-jiao-fu-mei-bian-yi-ji-wo-zen-me-ba-ta-ban-hui-lai-de
last_updated: 2026-09-15
knowledge_schema: synthesis-v1
---

## Definition
[[LLMToolingSkills]] are prompt-level instruction bundles that add domain knowledge, procedures, and reasoning guidance to an LLM's context without directly giving the model a new external action channel.

## Current Synthesis
The sources present Skills as prompt-level workflow guidance. A Skill imports expert structure into the prompt so the model can approach a task with better assumptions and workflow, but it does not enforce execution like a runtime API. Its value is highest when a task needs richer thinking, domain framing, or loose coordination that cannot easily be reduced to RPC-style functions.

The loading model is the practical distinction. Rules are short always-on constraints, specs are business-state inputs, and skills are on-demand workflows that can include SOP steps, few-shot references, and CLI/script hooks. Skill-following is still probabilistic, but it can improve when relevant instructions are loaded near generation time with a much higher signal-to-noise ratio than a long global rule file.

## Key Claims
- Skills add instructions and expert cognitive structure to the model context.
- Skill-following depends on the model's respect for context and remains probabilistic.
- Over-constraining model behavior can make reasoning less flexible.
- Skills do not directly modify the outside world; they need other tools or execution channels for action.
- Skills remain useful when a task is too open-ended, low-interaction, or expensive to encode as a dedicated server API.
- Skills can encode more than linear SOPs; exploration and brainstorming skills may be valuable precisely because they prompt multi-dimensional analysis.
- Skills work best when separated from rules and specs instead of becoming a large undifferentiated prompt file.

## Evidence
- Prompt nature: [[yi-kou-qi-ba-suo-you-rang-ni-mu-xuan-de-llm-ming-ci-quan-dou-guo-yi-bian]] describes Skills as instructions shown to the LLM rather than external action channels.
- Compliance limit: [[yi-kou-qi-ba-suo-you-rang-ni-mu-xuan-de-llm-ming-ci-quan-dou-guo-yi-bian]] says the model may or may not use the Skill, follow steps, or choose the expected order.
- Flexibility qualification: [[yi-kou-qi-ba-suo-you-rang-ni-mu-xuan-de-llm-ming-ci-quan-dou-guo-yi-bian]] warns that hard constraints can narrow the model's thinking.
- Use case: [[yi-kou-qi-ba-suo-you-rang-ni-mu-xuan-de-llm-ming-ci-quan-dou-guo-yi-bian]] says Skills are valuable when the work needs fuller reasoning and cannot reasonably be packaged as RPC.
- Loading distinction: [[wei-shen-me-ai-xie-dai-ma-geng-kuai-dan-jiao-fu-mei-bian-yi-ji-wo-zen-me-ba-ta-ban-hui-lai-de]] distinguishes specs as business knowledge, rules as always-loaded engineering constraints, and skills as on-demand workflows.
- Signal-to-noise: [[wei-shen-me-ai-xie-dai-ma-geng-kuai-dan-jiao-fu-mei-bian-yi-ji-wo-zen-me-ba-ta-ban-hui-lai-de]] argues that a focused skill can outperform a long rule file because only task-relevant instructions, examples, and scripts enter the immediate context.
- Skill dimensions: [[wei-shen-me-ai-xie-dai-ma-geng-kuai-dan-jiao-fu-mei-bian-yi-ji-wo-zen-me-ba-ta-ban-hui-lai-de]] describes SOP steps, reference examples, and CLI/script integration as complementary skill ingredients.

## Counterevidence & Qualifications
The sources evaluate Skills conceptually and through practitioner workflow rather than isolating skill effects in controlled benchmarks. They also use "Skills" broadly; implementations may vary in how they are selected, injected, validated, positioned in context, or combined with tools.

## What Changed
- Added the rule/spec/skill loading distinction and the claim that focused on-demand skills improve instruction signal-to-noise.

## Related Concepts
- [[LLMContextManagement]] - Skills manage context by adding structured instructions.
- [[ModelContextProtocol]] - MCP differs by exposing typed external tool calls.
- [[AIApplicationFramework]] - frameworks may combine prompt templates, tools, memory, and retrieval into application workflows.
- [[AIAgentCollaboration]] - coding-agent collaboration can use Skills to shape how agents reason with users.
- [[SpecDrivenAgentDevelopment]] - specs are durable inputs that skills can consume during execution.
- [[BottleneckAwareAICoding]] - focused skills help address SDLC bottlenecks rather than only code typing.
