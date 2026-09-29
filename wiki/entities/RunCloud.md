---
title: "RunCloud"
type: entity
tags: [linux, server-management, firewall]
sources:
  - how-to-check-if-tcp-port-is-open-closed-or-in-use-on-linux
last_updated: 2026-09-29
knowledge_schema: synthesis-v1
---

## Overview
[[RunCloud]] is presented in the source as a Linux server-management product with a dashboard for firewall configuration and other hosting operations.

## Current Profile
The wiki currently knows RunCloud through its own educational and promotional article about Linux ports. The article teaches command-line inspection with `ss`, `netstat`, and `nc`, then positions RunCloud's Security interface as a graphical way to define and deploy firewall rules. This supports a narrow product profile rather than an independent assessment of the company's capabilities or security.

## Key Characteristics
- Publishes practical Linux server-administration guidance.
- Provides a dashboard that represents firewall rules by scope, protocol, port, address, and action.
- Separates editing firewall rules from deploying them to the managed server.
- Uses educational content to lead into a commercial server-management offering.

## Evidence
- Educational scope: [[how-to-check-if-tcp-port-is-open-closed-or-in-use-on-linux]] explains port numbering, TCP and UDP, common services, socket inventory, and active connectivity checks.
- Firewall interface: [[how-to-check-if-tcp-port-is-open-closed-or-in-use-on-linux]] includes a Security page with global TCP rules for ports 22, 443, and 80 plus an Add New Rule control.
- Deployment state: [[how-to-check-if-tcp-port-is-open-closed-or-in-use-on-linux]] shows a warning that the firewall setup is incomplete until the Deploy action pushes it to the server.
- Commercial context: [[how-to-check-if-tcp-port-is-open-closed-or-in-use-on-linux]] ends by recommending RunCloud and linking to account onboarding.

## Qualifications
All current evidence comes from RunCloud's own marketing content and one captured interface state. It does not independently verify enforcement behavior, supported distributions, product completeness, or security outcomes, and the screenshot explicitly shows rules that have not yet been deployed.

## What Changed
- Created the RunCloud profile from its Linux-port tutorial and firewall screenshot.

## Relationships
- [[DefensivePortTriage]] - RunCloud's article supplies basic listener and reachability checks used before exposure risks are prioritized.
- [[RemoteAdministrationExposure]] - the shown firewall allows TCP port 22, conventionally associated with SSH administration.
- [[DatabaseServiceExposure]] - the article identifies MySQL port 3306 as a service endpoint that administrators may need to inspect.
- [[NATTraversal]] - remote reachability of a managed server depends on more than its local listener inventory.
