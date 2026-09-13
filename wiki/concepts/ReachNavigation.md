---
title: "Reach Navigation"
type: concept
tags: [mobile, ux, ios, navigation]
sources:
  - all-thumbs-why-reach-navigation-should-replace-the-navbar-in-ios-design
last_updated: 2026-09-13
knowledge_schema: synthesis-v1
---

## Definition
[[ReachNavigation]] is a mobile interface pattern that places high-frequency navigation and actions within comfortable one-handed thumb reach, especially near the lower part of large phone screens.

## Current Synthesis
The source defines Reach Navigation as a response to the mismatch between older top-navbar conventions and newer large-phone ergonomics. The goal is not simply to move everything downward; it is to match action placement to use frequency and consequence. Common or navigational actions belong in reachable areas through bottom controls, sheets, drawers, tab bars, content-area buttons, and swipe gestures, while destructive or high-cost actions may remain less reachable to prevent accidental taps.

## Key Claims
- Large phones make top-navbar controls less reachable and therefore less suitable for frequent actions.
- Bottom sheets, exposed drawers, floating buttons, and content-area controls can replace some top-navbar duties.
- Swipe gestures can reduce dependence on hard-to-reach back buttons.
- Tab-bar apps should treat bottom real estate as precious and reserve it for mission-critical destinations.
- Destination actions such as search, cart, or new message should usually be tabs or in-content controls rather than navbar buttons.
- Legacy apps can adopt the pattern incrementally by moving the most-used items downward and preserving reliable swipe-back behavior.
- Destructive or financially consequential actions may be safer when they are not in the easiest thumb zone.

## Evidence
- Pattern definition: [[all-thumbs-why-reach-navigation-should-replace-the-navbar-in-ios-design]] names navigation within thumb reach as Reach Navigation.
- Apple examples: [[all-thumbs-why-reach-navigation-should-replace-the-navbar-in-ios-design]] presents swipe-back, Reachability, Maps sheets, and Apple Music sheets as signs of reduced navbar dependence.
- Tab-bar guidance: [[all-thumbs-why-reach-navigation-should-replace-the-navbar-in-ios-design]] recommends sheets, bottom-floating controls, careful tab selection, and avoiding important destination buttons in the navbar.
- No-tab guidance: [[all-thumbs-why-reach-navigation-should-replace-the-navbar-in-ios-design]] recommends exposed drawers, sheets, and bottom button placement.
- Legacy guidance: [[all-thumbs-why-reach-navigation-should-replace-the-navbar-in-ios-design]] recommends moving most-used items downward, ensuring edge-swipe back works, nesting lesser items, and removing important actions from the top right.
- Safety exception: [[all-thumbs-why-reach-navigation-should-replace-the-navbar-in-ios-design]] says serious consequences can justify putting actions farther from reach.

## Counterevidence & Qualifications
The source is a 2017 design essay, so its examples reflect iOS 10-era interface patterns and phone hardware. It argues from practitioner observation, Apple examples, and app screenshots rather than controlled measurement. Reach-first placement can also compete with visibility, hierarchy, platform convention, accessibility needs, and the safety value of making dangerous actions harder to hit.

## What Changed
- Created the initial concept page for reach navigation as a mobile UX pattern.

## Related Concepts
- [[ThumbReachErgonomics]] - the physical constraint that motivates reach navigation.
- [[IOS]] - the platform context where the source proposes the pattern.
- [[MobileEcosystem]] - larger smartphones are part of the mobile platform environment that changes design constraints.
- [[MobilePlatformDiscovery]] - tab and destination placement affects how users find and return to core app functions.
- [[InformationHierarchy]] - reach navigation changes where important controls and labels appear in the interface hierarchy.
- [[ProductRedesign]] - legacy apps may need structural redesign rather than cosmetic navbar changes.
