---
title: "David Postill"
type: entity
tags: [technical-author, networking, super-user]
sources:
  - does-wake-on-lan-via-wan-needs-port-forwarding
last_updated: 2026-09-27
knowledge_schema: synthesis-v1
---

## Overview
[[DavidPostill]] is represented in this wiki as the author of an accepted Super User answer explaining the packet path and router requirements for [[WakeOnLAN]] across a WAN.

## Current Profile
Postill's answer provides a compact operational model: a UDP-carried magic packet is broadcast on the LAN, its embedded MAC address selects the sleeping host, and WAN delivery depends on firewall and router forwarding behavior. The profile is intentionally limited to this single technical contribution and does not infer broader expertise, employment, or biography.

## Key Characteristics
- Technical answer author on Super User.
- Explains Wake-on-LAN through broadcast delivery and MAC-based target identification.
- Identifies firewall admission and router broadcast support as Wake-on-WAN constraints.
- Uses a packet-capture example to illustrate the magic-packet structure.

## Evidence
- Authorship: [[does-wake-on-lan-via-wan-needs-port-forwarding]] attributes the accepted answer to David Postill.
- Networking explanation: [[does-wake-on-lan-via-wan-needs-port-forwarding]] describes broadcast delivery, conventional UDP ports 7 and 9, and MAC-address target selection.
- Router qualification: [[does-wake-on-lan-via-wan-needs-port-forwarding]] distinguishes routers that permit LAN broadcast forwarding from those that refuse it.
- Visual evidence: [[does-wake-on-lan-via-wan-needs-port-forwarding]] includes a capture of a UDP/7 packet carrying the repeated target MAC address.

## Qualifications
This profile rests on one accepted answer from 2015. The answer's port-listening language is simplified, and the source provides no basis for claims about Postill beyond this contribution.

## What Changed
- Created the entity from the accepted Wake-on-LAN via WAN answer.

## Relationships
- [[WakeOnLAN]] - networking mechanism explained in the accepted answer.
- [[NATTraversal]] - adjacent remote-reachability problem implicated by WAN-to-LAN delivery.
- [[DefensivePortTriage]] - security perspective relevant to the proposed inbound UDP forwarding rule.
