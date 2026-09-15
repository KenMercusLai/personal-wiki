---
title: "Conversational UI"
type: concept
tags: [interaction-design, ai, chatbots]
sources:
  - agent-experience-dao-lun-luo-li-li-de-shu-ju-zhong-xin
  - chat-is-the-new-browser-ted-livingston-medium
  - chatbots-deliver-the-worst-customer-service-late-night-coding
  - chatbots-were-the-next-big-thing-what-happened
last_updated: 2026-09-15
knowledge_schema: synthesis-v1
---

## Definition
[[ConversationalUI]] is an interaction pattern where users communicate with software through chat-like natural-language exchanges, sometimes combined with richer cards, canvases, previews, or generated artifacts.

## Current Synthesis
RORIRI treats conversational UI as having two waves. Livingston's 2016 chatbot essay captures the first wave's optimistic self-understanding: chat would become the new browser because bots reduced access friction and would improve as suggested replies, sharing mechanics, developer tooling, and payments matured. The GrowthBot and Late Night Coding sources supply near-period rebuttals: first-wave chatbots often acted like phone trees in text form, hid available options, depended on brittle decision trees or keyword matching, demanded unnatural precision, and failed when users needed human adaptation. GrowthBot adds the constructive middle ground: bots should extend apps, narrow themselves to one useful job, and combine conversation with dashboards, lists, maps, cards, or other visible UI when the task is too rich for pure chat. RORIRI's later analysis generalizes that failure: the bot-platform wave misread WeChat's success as evidence that bots would replace apps, even though many gains came from installation, login, payment, notification, and embedded web-view flows. LLMs created a second wave with a stronger language substrate, but mainstream products often route rich output into side canvases rather than deepening interaction inside the conversation stream.

## Key Claims
- The first bot-platform wave failed because rule engines and keyword matching could not sustain natural conversation.
- The first bot-platform wave's strongest thesis was that low-friction chat access could compensate for crude early bot quality, much as early websites improved after gaining distribution.
- WeChat's success was not mainly proof that chatbots were the future of all applications.
- Hidden conversational interfaces can create friction that visible menus, forms, and pages avoid.
- Hybrid or multimodal interfaces are often stronger than pure chat because conversation can sit beside durable visual state.
- LLMs made conversational UI newly plausible by handling open-ended language better than earlier bot stacks.
- Many current LLM products use chat as command input while placing durable artifacts in side panels or canvases.

## Evidence
- First-wave history: [[agent-experience-dao-lun-luo-li-li-de-shu-ju-zhong-xin]] names Facebook Messenger Bot, Kik, Telegram, Slack, and WeChat-inspired "conversation as platform" claims.
- First-wave optimism: [[chat-is-the-new-browser-ted-livingston-medium]] argues that chatbots were like early websites: basic at first, but advantaged by easier access than native apps.
- Misread platform cause: [[agent-experience-dao-lun-luo-li-li-de-shu-ju-zhong-xin]] cites Dan Grover's critique that WeChat won through installation, login, payment, and notification simplification rather than bot commerce alone.
- Interaction aids: [[chat-is-the-new-browser-ted-livingston-medium]] treats suggested responses as better than a blank text field for taking commands, showing that first-wave bots already needed structured UI inside chat.
- Customer-support failure: [[chatbots-deliver-the-worst-customer-service-late-night-coding]] compares support bots to phone-tree robots and argues that they cannot improvise around unusual problems.
- Hidden UI cost: [[chatbots-deliver-the-worst-customer-service-late-night-coding]] says restaurant menus, website navigation, and forms make available options and required information visible, while chatbots make users guess what the system can do.
- Quick-reply concession: [[chatbots-deliver-the-worst-customer-service-late-night-coding]] interprets Facebook Messenger quick replies as evidence that pure chat needed visible hints.
- First-wave postmortem: [[chatbots-were-the-next-big-thing-what-happened]] says the predicted bot ecosystem failed to emerge after the hype peak.
- Brittle logic: [[chatbots-were-the-next-big-thing-what-happened]] says most bots used decision-tree or keyword logic whose coverage depended on what builders anticipated.
- Hybrid direction: [[chatbots-were-the-next-big-thing-what-happened]] uses Penny, HubSpot Conversations, and Layer as examples of chat extending dashboards, inboxes, web, and native app surfaces rather than replacing them.
- Technical failure: [[agent-experience-dao-lun-luo-li-li-de-shu-ju-zhong-xin]] says earlier bots broke on indirect phrasing and often became menu systems in chat clothing.
- Second wave: [[agent-experience-dao-lun-luo-li-li-de-shu-ju-zhong-xin]] says LLMs finally supplied a language substrate matching conversational ambition.
- Canvas drift: [[agent-experience-dao-lun-luo-li-li-de-shu-ju-zhong-xin]] observes that mainstream LLM products often use a left chat pane plus right artifact canvas.

## Counterevidence & Qualifications
Livingston's source is a period argument from a company leader with a direct stake in bot-platform success, so it is evidence of the thesis, not proof that the thesis worked. The Late Night Coding and GrowthBot sources are experiential product critiques rather than controlled support benchmarks, but they clearly name failure modes that later interface critiques preserve. GrowthBot still leaves room for long-run bot growth as NLP and AI improve, especially for bounded automation and hybrid interfaces. RORIRI's source does not reject canvases: it says documents, code, slides, charts, and tests often benefit from a visible artifact space. The critique is that chat risks becoming merely an instruction box if products stop designing richer conversational interaction.

## What Changed
- Created the concept page for conversational UI's failed bot wave, LLM-era revival, and canvas-centered qualification.
- Added the optimistic 2016 "chat is the new browser" view and preserved it as the position later conversational-UI critiques qualify.
- Added a 2017 customer-support critique focused on hidden UI, poor adaptation, and bot-to-human escalation.
- Added GrowthBot's post-hype synthesis: first-wave bots failed as app replacements, but remain useful when narrowly scoped or paired with visual interfaces.

## Related Concepts
- [[NaturalLanguageInterface]] - conversational UI is one visible form of natural-language software interaction.
- [[AgentExperience]] - user-to-agent communication is one AX layer.
- [[AXFriendlyInterfaceDesign]] - rich or visible interaction elements affect whether agents and users can perceive state.
- [[MessagingAsPlatform]] - the 2016 bot wave was tied to messaging-platform expectations.
- [[ProductFlowFriction]] - first-wave chatbots promised lower first-use effort than app installs or mobile web flows.
