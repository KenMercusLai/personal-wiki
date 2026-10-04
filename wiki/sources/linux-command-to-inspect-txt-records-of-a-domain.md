---
title: "Linux command to inspect TXT records of a domain"
type: source
tags: [linux, dns, txt-record, command-line]
date: 2010-06-06
source_file: "/mnt/ken_personal_wiki/Articles/Linux command to inspect TXT records of a domain.md"
---

## Summary
This Server Fault Q&A gives two Linux command-line routes for [[DNSTXTRecordLookup]]: `dig -t txt` and `host -t txt`. It also explains that `dig +short` suppresses surrounding response detail and that a DKIM key must be requested at its exact selector subdomain because a TXT lookup does not enumerate subdomains.

## Key Claims
- `dig -t txt example.com` requests TXT records for a specified domain name.
- Adding `+short` returns a terse answer rather than the fuller DNS response display.
- DKIM public keys are queried at a specific selector name such as `google._domainkey.example.com`, not discovered automatically from a query for the parent domain.
- `host -t txt google.com` provides another concise command for retrieving TXT records.
- The queried name matters: TXT records attached to a subdomain must be requested explicitly.

## Key Quotes
> "Adding the `+short` option gives just the TXT record in quote marks with no other cruft." — Answer 1

> "The `host(1)` command has a nice, terse output" — Answer 2

## Connections
- [[DNSTXTRecordLookup]] - captures the exact-name lookup model and the `dig` and `host` command forms.
- [[EmailDeliverability]] - SPF policies and DKIM public keys are common email-authentication data published in TXT records.
- [[AnycastDNS]] - concerns how DNS service instances receive queries, while this source concerns issuing one record-type query from a client.
- [[AutomationFriendlyCLI]] - `dig +short` reduces presentation detail when a caller needs compact output.

## Contradictions
- No direct contradiction with the existing wiki was identified. The source instead qualifies any expectation that querying a parent domain will reveal TXT records on its subdomains.
