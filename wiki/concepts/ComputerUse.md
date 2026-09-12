---
title: "Computer Use"
type: concept
tags: [ai, agents, ui-automation]
sources:
  - yi-kou-qi-ba-suo-you-rang-ni-mu-xuan-de-llm-ming-ci-quan-dou-guo-yi-bian
last_updated: 2026-09-12
knowledge_schema: synthesis-v1
---

## Definition
[[ComputerUse]] is an agentic software-control pattern where an LLM operates applications through computer interfaces such as windows, buttons, keyboard events, screenshots, DOM nodes, or accessibility-tree elements.

## Current Synthesis
The source treats Computer Use as a label for letting LLMs sit in front of ordinary software rather than as a separate foundational technology. Underneath, the agent still needs Skills, MCP-style calls, or another action interface; the target simply becomes the operating system and its applications. The article's available route discussion focuses on reading the [[AccessibilityTree]] and injecting system events, which gives the model semantic UI elements instead of only raw pixels.

## Key Claims
- Computer Use gives LLMs an action channel into normal desktop or browser software.
- The category is closer to product packaging than to a standalone core technology.
- Computer Use still inherits context-management problems from Skills, MCP, and tool-result loops.
- Accessibility-tree interaction can provide cleaner semantic structure than screenshot-only control.
- Browser DOM control is related to the accessibility-tree route for web tasks.

## Evidence
- Category framing: [[yi-kou-qi-ba-suo-you-rang-ni-mu-xuan-de-llm-ming-ci-quan-dou-guo-yi-bian]] says Computer Use is closer to a brand-like label than a distinct technology.
- Underlying mechanisms: [[yi-kou-qi-ba-suo-you-rang-ni-mu-xuan-de-llm-ming-ci-quan-dou-guo-yi-bian]] says Computer Use still runs on Skills or MCP-like mechanisms.
- Context inheritance: [[yi-kou-qi-ba-suo-you-rang-ni-mu-xuan-de-llm-ming-ci-quan-dou-guo-yi-bian]] notes that the same context problems apply when the operation target is windows, buttons, and keyboard input.
- Accessibility route: [[yi-kou-qi-ba-suo-you-rang-ni-mu-xuan-de-llm-ming-ci-quan-dou-guo-yi-bian]] describes reading accessibility-tree nodes and injecting events as one route.

## Counterevidence & Qualifications
The source says there are three technical routes but only includes the first before the document ends. This page therefore captures the source's general framing and the accessibility-tree route, not a complete taxonomy of Computer Use.

## What Changed
- Created the concept page for Computer Use as agentic UI operation built on lower-level action and context-management mechanisms.

## Related Concepts
- [[ModelContextProtocol]] - MCP can expose UI operations as structured tool calls.
- [[LLMToolingSkills]] - Skills can guide Computer Use workflows.
- [[AccessibilityTree]] - accessibility-tree parsing is one semantic route for Computer Use.
- [[DynamicContextCompression]] - Computer Use may need domain-specific compression of observations such as screenshots.
- [[NaturalLanguageInterface]] - Computer Use turns natural-language goals into software actions.
