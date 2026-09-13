---
title: "Mobile Runtime"
type: concept
tags: [mobile, runtime, apps, web, platform]
sources:
  - 16-mobile-theses-benedict-evans
  - advertising-models-in-mobile-messaging-apps-mobile-dev-memo
last_updated: 2026-09-13
knowledge_schema: synthesis-v1
---

## Definition
[[MobileRuntime]] is the service-execution, interaction, and monetization surface that users treat as the place where digital services live, such as the browser, native apps, messaging, maps, assistants, or notifications.

## Current Synthesis
The Evans source argues that the desktop internet had a relatively stable runtime: browser plus mouse plus keyboard. Smartphones broke that unity into competing surfaces. Native apps, the mobile web, app stores, Siri, Google Now, messaging, maps, and notifications all represent possible ways to build, invoke, discover, and reuse services. The runtime question is therefore not only technical; it is a distribution, user-acquisition, and monetization question. The Mobile Dev Memo source makes this concrete for chat: messaging runtimes can host brand conversations, content channels, sponsored feed units, and sticker-store ads without requiring a separate app install.

## Key Claims
- The browser was the dominant consumer runtime of the desktop internet era.
- Smartphones split the internet into multiple competing interaction surfaces.
- Native apps and the web do different jobs, and neither had fully settled the mobile runtime question in the source.
- Assistants, messaging, maps, and notifications are candidate runtimes because they can host service interactions and discovery.
- Runtime strategy is inseparable from search, discovery, and user acquisition.
- A runtime can also become ad inventory when brands can interact with users inside the surface.

## Evidence
- Desktop baseline: [[16-mobile-theses-benedict-evans]] says the old internet was effectively browser plus mouse plus keyboard for ordinary consumers.
- Mobile fragmentation: [[16-mobile-theses-benedict-evans]] says the smartphone broke that model apart.
- Apps and web: [[16-mobile-theses-benedict-evans]] discusses the unresolved relationship between smartphone apps and the web.
- Candidate surfaces: [[16-mobile-theses-benedict-evans]] lists Siri, Google Now, messaging, maps, and notifications as possible new runtimes.
- Discovery tie: [[16-mobile-theses-benedict-evans]] says the aim is a new search and discovery model, not just a technical runtime.
- Messaging monetization: [[advertising-models-in-mobile-messaging-apps-mobile-dev-memo]] shows chat apps hosting promoted chats, Discover-like channels, sponsored content, and branded stickers.

## Counterevidence & Qualifications
The sources intentionally leave the winning runtime unresolved. They predate later progressive web app work, voice-assistant disappointments, super-app expansion, mobile OS policy changes, privacy changes, and LLM assistant interfaces.

## What Changed
- Created the mobile runtime concept for the post-browser/post-native-app strategic question.
- Added chat advertising as evidence that runtimes can monetize service interaction surfaces.

## Related Concepts
- [[MobilePlatformDiscovery]] - runtimes matter because they route discovery and acquisition.
- [[MessagingAsPlatform]] - messaging is one runtime candidate.
- [[MobileMessagingAdvertising]] - messaging ads show how runtime surfaces become monetizable brand-interaction spaces.
- [[MobileInternet]] - the internet's primary interface is no longer only the desktop browser.
- [[NaturalLanguageInterface]] - assistants and later AI interfaces are possible runtime surfaces.
