---
title: "Accessibility Tree"
type: concept
tags: [accessibility, ui, agents]
sources:
  - yi-kou-qi-ba-suo-you-rang-ni-mu-xuan-de-llm-ming-ci-quan-dou-guo-yi-bian
last_updated: 2026-09-12
knowledge_schema: synthesis-v1
---

## Definition
[[AccessibilityTree]] is a semantic representation of user-interface elements that records roles, names, states, and hierarchy for assistive technology and can also support agentic UI automation.

## Current Synthesis
The source introduces the accessibility tree as one route for Computer Use. Instead of making the model infer everything from pixels, the system can expose elements such as buttons, inputs, links, roles, names, states, and hierarchy. This gives an LLM a cleaner interface for choosing actions, especially in browser contexts where the DOM is a close relative.

## Key Claims
- Accessibility trees describe UI elements in semantic rather than purely visual terms.
- They are maintained by operating systems and browsers for assistive technologies.
- Their structure can make Computer Use cleaner because models can reason over buttons, inputs, links, and state.
- Browser DOM parsing is adjacent to accessibility-tree interaction.
- Natural-language browser agents can use this route to drive web operations.

## Evidence
- Semantic structure: [[yi-kou-qi-ba-suo-you-rang-ni-mu-xuan-de-llm-ming-ci-quan-dou-guo-yi-bian]] says accessibility trees contain role, name, state, and hierarchy.
- Assistive-technology origin: [[yi-kou-qi-ba-suo-you-rang-ni-mu-xuan-de-llm-ming-ci-quan-dou-guo-yi-bian]] frames the tree as infrastructure for screen readers and similar tools.
- Agent advantage: [[yi-kou-qi-ba-suo-you-rang-ni-mu-xuan-de-llm-ming-ci-quan-dou-guo-yi-bian]] says this route gives LLMs meaningful nodes instead of raw pixels.
- DOM relation: [[yi-kou-qi-ba-suo-you-rang-ni-mu-xuan-de-llm-ming-ci-quan-dou-guo-yi-bian]] compares the browser DOM to the accessibility tree and names page-agent.js as an example of DOM-based operation.

## Counterevidence & Qualifications
The source does not discuss accessibility-tree completeness, cross-application inconsistency, hidden controls, custom-rendered canvases, security boundaries, or cases where pixels still matter.

## What Changed
- Created the concept page for accessibility-tree-based Computer Use.

## Related Concepts
- [[ComputerUse]] - accessibility-tree parsing is one route for agentic computer operation.
- [[NaturalLanguageInterface]] - semantic UI trees help map natural-language requests to interface actions.
- [[ModelContextProtocol]] - tree inspection and event injection can be exposed as structured tool calls.
- [[PlayerGuidance]] - both concern UI semantics, but accessibility trees are machine-readable interface structure rather than game-design cues.
