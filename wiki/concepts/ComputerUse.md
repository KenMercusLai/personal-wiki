---
title: "Computer Use"
type: concept
tags: [ai, agents, ui-automation]
sources:
  - yi-kou-qi-ba-suo-you-rang-ni-mu-xuan-de-llm-ming-ci-quan-dou-guo-yi-bian
  - agent-experience-dao-lun-luo-li-li-de-shu-ju-zhong-xin
last_updated: 2026-09-13
knowledge_schema: synthesis-v1
---

## Definition
[[ComputerUse]] is an agentic software-control pattern where an LLM operates applications through computer interfaces such as windows, buttons, keyboard events, screenshots, DOM nodes, or accessibility-tree elements.

## Current Synthesis
The sources treat Computer Use as a label for letting LLMs sit in front of ordinary software rather than as a separate foundational technology. Underneath, the agent still needs Skills, MCP-style calls, event injection, or another action interface; the target simply becomes the operating system and its applications.

The full AX essay supplies the missing route taxonomy. One route reads [[AccessibilityTree]] or DOM-like semantic structure and injects system events. A second route uses screenshots enhanced with numbered boxes, such as Set-of-Mark prompting, so the model chooses symbols instead of raw coordinates. A third route asks a native multimodal model to inspect the screenshot and output coordinates directly. DOM and accessibility routes provide clean semantics but can miss spatial relationships in complex tables; screenshot and video routes are less dependent on application cooperation but depend on model spatial understanding and inference cost.

## Key Claims
- Computer Use gives LLMs an action channel into normal desktop or browser software.
- The category is closer to product packaging than to a standalone core technology.
- Computer Use still inherits context-management problems from Skills, MCP, and tool-result loops.
- Accessibility-tree interaction can provide cleaner semantic structure than screenshot-only control.
- Screenshot markup can convert visual target selection into a more constrained symbolic choice.
- Native multimodal coordinate prediction is simpler architecturally but demands strong spatial ability.
- AX-friendly interfaces need persistent visible state because screenshot-based agents can miss transient animation, toast messages, or tooltip-only guidance.

## Evidence
- Category framing: [[yi-kou-qi-ba-suo-you-rang-ni-mu-xuan-de-llm-ming-ci-quan-dou-guo-yi-bian]] says Computer Use is closer to a brand-like label than a distinct technology.
- Underlying mechanisms: [[yi-kou-qi-ba-suo-you-rang-ni-mu-xuan-de-llm-ming-ci-quan-dou-guo-yi-bian]] says Computer Use still runs on Skills or MCP-like mechanisms.
- Context inheritance: [[yi-kou-qi-ba-suo-you-rang-ni-mu-xuan-de-llm-ming-ci-quan-dou-guo-yi-bian]] notes that the same context problems apply when the operation target is windows, buttons, and keyboard input.
- Accessibility route: [[yi-kou-qi-ba-suo-you-rang-ni-mu-xuan-de-llm-ming-ci-quan-dou-guo-yi-bian]] describes reading accessibility-tree nodes and injecting events as one route.
- Three routes: [[agent-experience-dao-lun-luo-li-li-de-shu-ju-zhong-xin]] compares accessibility-tree or DOM control, screenshot markup with numbered regions, and native multimodal coordinate output.
- DOM limit: [[agent-experience-dao-lun-luo-li-li-de-shu-ju-zhong-xin]] says semantic nodes alone may not expose spatial relationships in Excel-like interfaces.
- Vision route: [[agent-experience-dao-lun-luo-li-li-de-shu-ju-zhong-xin]] argues that screenshot and video routes can work without application cooperation, while spatial precision and cost remain constraints.
- Interface reliability: [[agent-experience-dao-lun-luo-li-li-de-shu-ju-zhong-xin]] warns that animation, toasts, and tooltip-only information can be invisible to screenshot-driven agents.

## Counterevidence & Qualifications
The sources are conceptual and do not benchmark these routes. Claims about model parameter scale, current spatial precision, or relative ceilings should be treated as source-scoped observations rather than stable product guidance.

## What Changed
- Created the concept page for Computer Use as agentic UI operation built on lower-level action and context-management mechanisms.
- Added the full AX taxonomy of accessibility/DOM, screenshot markup, and native multimodal routes plus interface-design implications.

## Related Concepts
- [[ModelContextProtocol]] - MCP can expose UI operations as structured tool calls.
- [[LLMToolingSkills]] - Skills can guide Computer Use workflows.
- [[AccessibilityTree]] - accessibility-tree parsing is one semantic route for Computer Use.
- [[DynamicContextCompression]] - Computer Use may need domain-specific compression of observations such as screenshots.
- [[NaturalLanguageInterface]] - Computer Use turns natural-language goals into software actions.
- [[AXFriendlyInterfaceDesign]] - UI visibility and persistence affect how well Computer Use agents perceive state.
- [[AgentInterfaceAsContext]] - software surfaces can deliver constraints and diagnostics into the agent's observation loop.
