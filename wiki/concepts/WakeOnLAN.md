---
title: "Wake-on-LAN"
type: concept
tags: [networking, remote-access, power-management]
sources:
  - does-wake-on-lan-via-wan-needs-port-forwarding
last_updated: 2026-09-27
knowledge_schema: synthesis-v1
---

## Definition
[[WakeOnLAN]] is a network power-management mechanism in which a sleeping or powered-down computer's network interface detects a magic packet containing its repeated MAC address and signals the computer to wake.

## Current Synthesis
Wake-on-LAN is naturally a local-broadcast mechanism. A sender places the target MAC address in a recognizable payload and sends it across the target LAN, conventionally in a UDP datagram to port 7 or 9. Extending that path across a WAN is therefore not ordinary host-level port forwarding alone: the edge router must admit the packet and still deliver it on the LAN when the target host cannot participate normally in IP or ARP resolution. Depending on router capabilities, this can mean forwarding to a subnet broadcast address, maintaining a static IP-to-MAC ARP binding, or using a router or another always-on LAN device as the magic-packet relay.

The source supports the packet mechanics and one reported ARP-binding fix, but it does not establish a universal recipe. Directed broadcasts are frequently unsupported, internet access may sit behind another NAT layer, and exposed UDP relay rules need deliberate security scoping.

## Key Claims
- The wake target is selected by a MAC address repeated in the magic-packet payload.
- Wake-on-LAN usually relies on local broadcast delivery rather than a normal session with an awake IP host.
- UDP ports 7 and 9 are common conventions, not intrinsic requirements of the magic-packet format.
- Wake-on-WAN requires the edge network to admit and relay the packet into the target broadcast domain.
- Static ARP binding can preserve delivery to a sleeping host when dynamic ARP state would otherwise expire.
- Router broadcast policy, upstream NAT, hardware support, and security controls determine whether a WAN setup is viable.

## Evidence
- Packet structure: [[does-wake-on-lan-via-wan-needs-port-forwarding]] includes a capture whose payload starts with six `FF` bytes followed by repeated copies of MAC address `00 E0 4C 31 03 AC`.
- Broadcast delivery: [[does-wake-on-lan-via-wan-needs-port-forwarding]] shows UDP traffic addressed to `192.168.1.255` and states that LAN hosts receive the broadcast while the MAC identifies the wake target.
- WAN boundary: [[does-wake-on-lan-via-wan-needs-port-forwarding]] says firewalls must admit the packet and that routers differ in whether they forward broadcasts.
- ARP behavior: [[does-wake-on-lan-via-wan-needs-port-forwarding]] records the questioner's report that binding the computer's MAC and IP addresses solved the issue.

## Counterevidence & Qualifications
The source is one 2015 Super User answer plus a brief questioner follow-up, not a cross-router test or protocol specification. Its statement that the sleeping PC listens on UDP ports 7 and 9 compresses two layers: UDP is a common transport convention, while the network interface or firmware recognizes the magic payload. Static ARP binding and directed-broadcast forwarding are router-specific, and neither addresses carrier-grade NAT, public-address discovery, Wi-Fi wake support, firmware settings, source authentication, or denial-of-service exposure. A VPN or authenticated relay on an always-on LAN device may provide a safer path, but this source does not compare those alternatives.

## What Changed
- Created the concept with separate local-broadcast, WAN-relay, and ARP-resolution requirements.
- Qualified UDP/7 and UDP/9 as conventions rather than mandatory listening ports.

## Related Concepts
- [[NATTraversal]] - both cross private-network boundaries, but Wake-on-WAN may require broadcast or relay behavior rather than ordinary service tunneling.
- [[DefensivePortTriage]] - any internet-facing UDP forwarding rule creates an exposure that should be reviewed and constrained.
- [[RemoteAdministrationExposure]] - remote wake capability changes the externally reachable control surface of a private machine.
- [[NetworkSegmentation]] - broadcast-domain boundaries determine where a magic packet can naturally propagate.
