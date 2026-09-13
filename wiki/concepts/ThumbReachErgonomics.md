---
title: "Thumb Reach Ergonomics"
type: concept
tags: [mobile, ux, ergonomics, interaction-design]
sources:
  - all-thumbs-why-reach-navigation-should-replace-the-navbar-in-ios-design
last_updated: 2026-09-13
knowledge_schema: synthesis-v1
---

## Definition
[[ThumbReachErgonomics]] is the design constraint created by how far, comfortably and accurately, a user's thumb can reach while holding a phone in one hand.

## Current Synthesis
The source treats thumb reach as a practical interface boundary. As iPhone screens grew, the upper screen and especially top corners became less natural for one-handed taps. The inspected touch-zone diagram reinforces this by showing a lower green natural zone, a middle stretch zone, and red harder-to-reach areas that expand around the top and far side as the phone grows. The design implication is that frequent actions should track the hand's natural range, while less frequent or risky actions can tolerate distance.

## Key Claims
- Device size changes the physical cost of interface conventions.
- Top navigation bars become more awkward as screen height increases.
- One-handed use matters because phones are often used while the other hand is occupied.
- Touch-zone diagrams can make reach constraints visible enough to guide layout decisions.
- Ergonomic reach should influence both navigation placement and action risk.
- A control's frequency and consequence should affect whether it belongs in the natural, stretch, or hard-to-reach zone.

## Evidence
- Large-phone claim: [[all-thumbs-why-reach-navigation-should-replace-the-navbar-in-ios-design]] argues that bigger phones increased the distance between thumbs and navbar buttons.
- Reach diagram: [[all-thumbs-why-reach-navigation-should-replace-the-navbar-in-ios-design]] includes a Scott Hurff-style touch-zone visual showing natural, stretch, and hard-to-reach areas across device sizes.
- One-handed context: [[all-thumbs-why-reach-navigation-should-replace-the-navbar-in-ios-design]] says a phone that can be held in one hand should also be operable with one hand.
- Navigation implication: [[all-thumbs-why-reach-navigation-should-replace-the-navbar-in-ios-design]] uses thumb reach to motivate sheets, bottom placement, broad gestures, and moving top-right actions.
- Safety implication: [[all-thumbs-why-reach-navigation-should-replace-the-navbar-in-ios-design]] allows hard-to-reach placement for actions that could delete important documents or cost money.

## Counterevidence & Qualifications
The source focuses on right-handed thumb reach and does not deeply address left-handed use, two-handed use, accessibility settings, hand-size variation, landscape orientation, motor impairments, or later gesture-navigation systems. Reach is therefore a strong design input, not the only criterion for mobile layout.

## What Changed
- Created the initial concept page for thumb reach ergonomics as a mobile interaction-design constraint.

## Related Concepts
- [[ReachNavigation]] - design pattern that responds directly to thumb-reach constraints.
- [[IOS]] - the article's platform context for the ergonomic critique.
- [[ConstraintShapedInterfaceDesign]] - device size and hand posture are constraints that shape interface conventions.
- [[MobileEcosystem]] - mobile device evolution changes the ergonomic conditions for software.
- [[CognitiveLoadInUXResearch]] - physically awkward controls can add effort alongside cognitive interpretation cost.
