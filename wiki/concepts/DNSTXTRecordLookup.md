---
title: "DNS TXT Record Lookup"
type: concept
tags: [dns, txt-record, linux, command-line]
sources:
  - linux-command-to-inspect-txt-records-of-a-domain
last_updated: 2026-10-04
knowledge_schema: synthesis-v1
---

## Definition
[[DNSTXTRecordLookup]] is the retrieval of TXT resource records for an exact DNS name, commonly from a Linux shell with a record-type-specific query such as `dig -t txt` or `host -t txt`.

## Current Synthesis
The source presents TXT inspection as an exact-name DNS query. `dig -t txt example.com` displays the TXT answer with broader response detail, while `dig -t txt example.com +short` favors a compact answer. `host -t txt example.com` is a second terse interface.

The requested name is as important as the record type. A query for a parent domain does not enumerate TXT records attached to its subdomains. For DKIM, the caller therefore needs the selector-qualified name, such as `google._domainkey.example.com`, before issuing the TXT query.

## Key Claims
- A TXT lookup must specify both the target DNS name and the TXT record type.
- `dig -t txt <name>` provides a detailed command-line query, while `+short` suppresses most surrounding response information.
- `host -t txt <name>` provides an alternative concise lookup.
- Querying a parent domain does not automatically discover TXT records attached to subdomains.
- DKIM lookup requires the exact selector-qualified `_domainkey` name.

## Evidence
- `dig` query form: [[linux-command-to-inspect-txt-records-of-a-domain]] gives `dig -t txt example.com` as the primary command.
- Compact output: [[linux-command-to-inspect-txt-records-of-a-domain]] recommends `+short` when only the quoted TXT answer is wanted.
- Alternative client: [[linux-command-to-inspect-txt-records-of-a-domain]] gives `host -t txt google.com` as a terse alternative.
- Exact-name boundary: [[linux-command-to-inspect-txt-records-of-a-domain]] says `dig` does not show subdomains automatically and demonstrates a selector-qualified DKIM query.

## Counterevidence & Qualifications
The source is a concise 2010 Q&A, not a complete DNS troubleshooting guide. It does not distinguish recursive from authoritative answers, show how to choose or identify the queried resolver, discuss caching, TTLs, truncation, DNSSEC, CNAME handling, exit statuses, or explain how long TXT data may be split into multiple character strings. `+short` is useful for inspection but removes metadata needed for deeper diagnosis. The DKIM example assumes the selector is already known; DNS does not provide a general selector-enumeration mechanism through the parent-domain TXT query. Command availability and exact output remain dependent on the installed DNS utilities and their versions.

## What Changed
- Created an exact-name model for command-line TXT record inspection.
- Distinguished full `dig` output from the compact `+short` form and the terse `host` alternative.
- Made selector knowledge and explicit DKIM subdomain queries part of the lookup boundary.

## Related Concepts
- [[EmailDeliverability]] - SPF policies and DKIM public keys use DNS-published data whose exact records may need inspection.
- [[AnycastDNS]] - describes routing queries among DNS servers, whereas TXT lookup describes the client-side record request.
- [[AutomationFriendlyCLI]] - compact output can be easier to consume, although removed metadata may matter for diagnosis.
- [[CommandLineUX]] - `dig` and `host` expose different levels of response detail for the same lookup task.
