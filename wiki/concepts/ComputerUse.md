---
title: "Computer Use"
type: concept
tags: [ai, agents, ui-automation]
sources:
  - yi-kou-qi-ba-suo-you-rang-ni-mu-xuan-de-llm-ming-ci-quan-dou-guo-yi-bian
  - agent-experience-dao-lun-luo-li-li-de-shu-ju-zhong-xin
  - yan-li-how-llm-agents-became-what-they-look-like-in-2026
  - muse-qu-mei-cong-wo-zuo-qi-ni-ka-zai-na-er
  - zhuan-fang-deepchat-zuo-zhe-men-liao-liao-ben-di-you-xian-mcp-yu-agent-memory
  - apps-agents-and-aggregation
last_updated: 2026-10-13
knowledge_schema: synthesis-v1
---

## Definition
[[ComputerUse]] is an agentic software-control pattern where an LLM operates applications through computer interfaces such as windows, buttons, keyboard events, screenshots, DOM nodes, or accessibility-tree elements.

## Current Synthesis
The sources treat Computer Use as a label for letting LLMs sit in front of ordinary software rather than as a separate foundational technology. Underneath, the agent still needs Skills, MCP-style calls, event injection, or another action interface; the target simply becomes the operating system and its applications.

The full AX essay supplies the missing route taxonomy. One route reads [[AccessibilityTree]] or DOM-like semantic structure and injects system events. A second route uses screenshots enhanced with numbered boxes, such as Set-of-Mark prompting, so the model chooses symbols instead of raw coordinates. A third route asks a native multimodal model to inspect the screenshot and output coordinates directly. DOM and accessibility routes provide clean semantics but can miss spatial relationships in complex tables; screenshot and video routes are less dependent on application cooperation but depend on model spatial understanding and inference cost.

The staged-history source supplies the reason this category remains open rather than solved. It argues that bash is a near-universal meta tool for text-and-file work but cannot cover the browser, "the ultimate GUI program". Its explanation for the gap is that GUI exists precisely to bypass the TTY, because complex tasks overwhelm a human's context window, so graphical work is where shell and file tooling stop being sufficient. Browser-use, computer-use, and interaction with specific GUIs therefore appear in the same source's list of capabilities users still want beyond coding agents, and the browser is named as the next stage of agent architecture.

The two [[Muse]] accounts add a consumer-product boundary. Computer operation is presented as the feature that makes Muse more compelling than a chatbot, but onboarding itself can require app-store access, network and identity checks, card verification, account connections, and code redemption. Thompson's recipe experiment supplies a positive case: Muse used Instagram saves to generate a searchable personal app and continued analyzing videos while the user did something else. It also makes dependency visible—Instagram rate limiting constrained progress. Together the sources show that Computer Use expands task coverage by inheriting supplier controls and increasing permission, privacy, containment, observability, destination-policy, and infrastructure obligations.

[[DeepChat]] supplies a concrete modular implementation. It integrates the driver portion of Cua, exposes the adapted operations through an MCP server, and loads a Skill that tells the agent how to use those tools. The client offers ask-every-time, fully automatic, and model-reviewed “Approve for me” permission modes, but its developers still describe safety as unresolved: a strict sandbox can block legitimate globally installed tools, while a permissive client can expose files and credentials. A separate ACP case shows another boundary—cross-application code-signing mismatch can make an otherwise valid Computer Use call crash—so protocol interoperability does not remove operating-system trust and identity constraints.

## Key Claims
- Computer Use packages an LLM action channel into normal desktop or browser software rather than defining a standalone core technology, and it inherits the context-management problems of Skills, MCP, and tool-result loops.
- Accessibility-tree interaction can provide cleaner semantic structure than screenshot-only control.
- Screenshot routes - numbered-region markup or native multimodal coordinate prediction - trade dependence on application cooperation for spatial-precision and inference-cost demands.
- AX-friendly interfaces need persistent visible state because screenshot-based agents can miss transient animation, toast messages, or tooltip-only guidance.
- The browser is the frontier that shell and file tooling cannot cover, because GUI exists to bypass the TTY when complex tasks overwhelm a human's context window.
- Consumer Computer Use joins action capability to onboarding, account connection, permission, destination-policy, and virtual-computer cost constraints.
- Modular Computer Use can separate the device driver, protocol bridge, procedural Skill, and permission policy, but reliability still crosses application signatures, supplier access limits, and operating-system authority.

## Evidence
- Category framing: [[yi-kou-qi-ba-suo-you-rang-ni-mu-xuan-de-llm-ming-ci-quan-dou-guo-yi-bian]] says Computer Use is closer to a brand-like label than a distinct technology.
- Underlying mechanisms: [[yi-kou-qi-ba-suo-you-rang-ni-mu-xuan-de-llm-ming-ci-quan-dou-guo-yi-bian]] says Computer Use still runs on Skills or MCP-like mechanisms.
- Context inheritance: [[yi-kou-qi-ba-suo-you-rang-ni-mu-xuan-de-llm-ming-ci-quan-dou-guo-yi-bian]] notes that the same context problems apply when the operation target is windows, buttons, and keyboard input.
- Accessibility route: [[yi-kou-qi-ba-suo-you-rang-ni-mu-xuan-de-llm-ming-ci-quan-dou-guo-yi-bian]] describes reading accessibility-tree nodes and injecting events as one route.
- Three routes: [[agent-experience-dao-lun-luo-li-li-de-shu-ju-zhong-xin]] compares accessibility-tree or DOM control, screenshot markup with numbered regions, and native multimodal coordinate output.
- DOM limit: [[agent-experience-dao-lun-luo-li-li-de-shu-ju-zhong-xin]] says semantic nodes alone may not expose spatial relationships in Excel-like interfaces.
- Vision route: [[agent-experience-dao-lun-luo-li-li-de-shu-ju-zhong-xin]] argues that screenshot and video routes can work without application cooperation, while spatial precision and cost remain constraints.
- Interface reliability: [[agent-experience-dao-lun-luo-li-li-de-shu-ju-zhong-xin]] warns that animation, toasts, and tooltip-only information can be invisible to screenshot-driven agents.
- Browser frontier: [[yan-li-how-llm-agents-became-what-they-look-like-in-2026]] says many tasks cannot be covered by bash alone and names the browser as the ultimate GUI program.
- GUI rationale: [[yan-li-how-llm-agents-became-what-they-look-like-in-2026]] says GUI was designed to bypass the TTY because complex tasks can overwhelm a human's context window.
- User demand: [[yan-li-how-llm-agents-became-what-they-look-like-in-2026]] lists browser-use, computer-use, and specific-GUI interaction among the capabilities users want beyond coding agents.
- Consumer-agent boundary: [[muse-qu-mei-cong-wo-zuo-qi-ni-ka-zai-na-er]] presents Muse's computer operation as its core appeal while relaying onboarding, connector, security, privacy, destination-access, and infrastructure concerns.
- Delegated-work example: [[apps-agents-and-aggregation]] retains a Muse recipe app and progress message showing background video analysis plus Instagram rate limiting.
- Deterministic complement: [[apps-agents-and-aggregation]] frames the agent's computer as the deterministic execution layer used by a probabilistic language model.
- Modular implementation: [[zhuan-fang-deepchat-zuo-zhe-men-liao-liao-ben-di-you-xian-mcp-yu-agent-memory]] describes DeepChat adapting Cua's driver, exposing it through MCP, and guiding use with a dedicated Skill.
- Permission modes: [[zhuan-fang-deepchat-zuo-zhe-men-liao-liao-ben-di-you-xian-mcp-yu-agent-memory]] reports ask-every-time, fully automatic, and model-reviewed approval modes while acknowledging the capability-versus-containment tradeoff.
- Signature boundary: [[zhuan-fang-deepchat-zuo-zhe-men-liao-liao-ben-di-you-xian-mcp-yu-agent-memory]] reports a macOS signing mismatch when Computer Use is triggered through an ACP adapter between differently signed applications.

## Counterevidence & Qualifications
The sources do not benchmark the route taxonomy or DeepChat implementation. Claims about model parameter scale, current spatial precision, or relative ceilings should be treated as source-scoped observations rather than stable product guidance. The staged-history source states the browser gap as an architectural observation and does not compare browser agents against shell or API routes on cost, reliability, or coverage. One Muse article is secondary launch commentary and the newer one is a first-person strategy account with a single useful but incomplete workflow; neither supplies task-success, intervention, escape, or security rates. The DeepChat interview is likewise a first-party account without comparative evaluation. Their failures and tradeoffs identify diligence questions rather than category-wide rates.

## What Changed
- Added a concrete delegated workflow that produced a useful app and continued work asynchronously.
- Added supplier rate limiting as a boundary that broad UI access does not remove.
- Added the probabilistic-agent/deterministic-computer complement as a product-level framing.

## Related Concepts
- [[ModelContextProtocol]] - MCP can expose UI operations as structured tool calls.
- [[LLMToolingSkills]] - Skills can guide Computer Use workflows.
- [[AccessibilityTree]] - accessibility-tree parsing is one semantic route for Computer Use.
- [[DynamicContextCompression]] - Computer Use may need domain-specific compression of observations such as screenshots.
- [[NaturalLanguageInterface]] - Computer Use turns natural-language goals into software actions.
- [[AXFriendlyInterfaceDesign]] - UI visibility and persistence affect how well Computer Use agents perceive state.
- [[AgentInterfaceAsContext]] - software surfaces can deliver constraints and diagnostics into the agent's observation loop.
- [[LLMAgentStages]] - the browser is named as the next stage after the OS layer.
- [[AgentDeploymentTradeoffs]] - multimodal and browser-use demand is one of the deployment constraints.
- [[Muse]] - consumer-agent case connecting computer operation with access, permission, trust, and scaling constraints.
- [[AgentPermissionModel]] - broad UI reach must be bounded by explicit authority and reviewable effects.
- [[UserTrustCapital]] - privacy or security failures can outweigh the convenience of delegated computer action.
- [[DeepChat]] - implements Computer Use through an adapted Cua driver, MCP bridge, usage Skill, and permission modes.
- [[GenerativeUI]] - shows one downstream output of computer-mediated agent work.
