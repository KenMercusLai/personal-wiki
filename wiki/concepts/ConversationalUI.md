---
title: "Conversational UI"
type: concept
tags: [interaction-design, ai, chatbots]
sources:
  - agent-experience-dao-lun-luo-li-li-de-shu-ju-zhong-xin
last_updated: 2026-09-13
knowledge_schema: synthesis-v1
---

## Definition
[[ConversationalUI]] is an interaction pattern where users communicate with software through chat-like natural-language exchanges, sometimes combined with richer cards, canvases, previews, or generated artifacts.

## Current Synthesis
RORIRI treats conversational UI as having two waves. The 2016 bot-platform wave misread WeChat's success as evidence that bots would replace apps, even though the real platform gains came from installation, login, payment, notification, and embedded web-view flows. LLMs created a second wave with a stronger language substrate, but mainstream products often route rich output into side canvases rather than deepening interaction inside the conversation stream.

## Key Claims
- The first bot-platform wave failed because rule engines and keyword matching could not sustain natural conversation.
- WeChat's success was not mainly proof that chatbots were the future of all applications.
- LLMs made conversational UI newly plausible by handling open-ended language better than earlier bot stacks.
- Many current LLM products use chat as command input while placing durable artifacts in side panels or canvases.
- Rich in-stream conversational components remain underdeveloped compared with canvas-based document, code, chart, and preview surfaces.

## Evidence
- First-wave history: [[agent-experience-dao-lun-luo-li-li-de-shu-ju-zhong-xin]] names Facebook Messenger Bot, Kik, Telegram, Slack, and WeChat-inspired "conversation as platform" claims.
- Misread platform cause: [[agent-experience-dao-lun-luo-li-li-de-shu-ju-zhong-xin]] cites Dan Grover's critique that WeChat won through installation, login, payment, and notification simplification rather than bot commerce alone.
- Technical failure: [[agent-experience-dao-lun-luo-li-li-de-shu-ju-zhong-xin]] says earlier bots broke on indirect phrasing and often became menu systems in chat clothing.
- Second wave: [[agent-experience-dao-lun-luo-li-li-de-shu-ju-zhong-xin]] says LLMs finally supplied a language substrate matching conversational ambition.
- Canvas drift: [[agent-experience-dao-lun-luo-li-li-de-shu-ju-zhong-xin]] observes that mainstream LLM products often use a left chat pane plus right artifact canvas.

## Counterevidence & Qualifications
The source does not reject canvases: it says documents, code, slides, charts, and tests often benefit from a visible artifact space. The critique is that chat risks becoming merely an instruction box if products stop designing richer conversational interaction.

## What Changed
- Created the concept page for conversational UI's failed bot wave, LLM-era revival, and canvas-centered qualification.

## Related Concepts
- [[NaturalLanguageInterface]] - conversational UI is one visible form of natural-language software interaction.
- [[AgentExperience]] - user-to-agent communication is one AX layer.
- [[AXFriendlyInterfaceDesign]] - rich or visible interaction elements affect whether agents and users can perceive state.
- [[MessagingAsPlatform]] - the 2016 bot wave was tied to messaging-platform expectations.
