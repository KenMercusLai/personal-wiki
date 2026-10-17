---
title: "Proxy Rule-Set Semantics"
type: concept
tags: [proxy, rules, matching, indexing]
sources:
  - store-domains-ips-text-only
last_updated: 2026-10-18
knowledge_schema: synthesis-v1
---

## Definition
[[ProxyRuleSetSemantics]] distinguishes the OR relationship among rules inside one proxy rule set from the ordered evaluation of separate rule sets in a larger configuration.

## Current Synthesis
A rule engine only needs to know whether any rule in a selected RULE-SET or DOMAIN-SET matches the request. Because this within-set result is an OR reduction, input order can be discarded and rules can be streamed into indexes specialized for exact domains, suffixes, keywords, CIDR prefixes, and other predicates. The containing configuration still assigns policies and evaluates different sets in order, so order independence does not extend across rule-set boundaries.

This semantic separation is what permits representation to follow the query rather than the source file: domain hierarchy, substring search, and binary IP prefixes need different structures even when they arrived in one heterogeneous list.

## Key Claims
- Rules inside one set contribute to a single Boolean OR result.
- Reordering rules within that set therefore does not change the set-level match result.
- Separate rule sets retain an ordering relationship in the containing configuration.
- A parser can stream and classify rules without retaining the file as one linear matching sequence.
- Each rule category can use an index aligned with its own matching semantics.

## Evidence
- Set-level logic: [[store-domains-ips-text-only]] states that any matching member makes the whole RULE-SET select its assigned policy.
- Ordering boundary: [[store-domains-ips-text-only]] explicitly preserves precedence among multiple rule sets while rejecting precedence among members of one set.
- Typed indexing: [[store-domains-ips-text-only]] groups exact and suffix domains, keyword rules, IP prefixes, and remaining predicates before building specialized matchers.

## Counterevidence & Qualifications
The claim applies to formats and engines with the described set-level Boolean semantics; rule systems with actions, negation, priority, first-match behavior inside a set, or stateful predicates may not be safely reordered. Classification removes sequence only after those semantics are established. The source explains the architecture conceptually and supplies no parser benchmark, compatibility matrix, or formal semantics for every named proxy product.

## What Changed
- Created the distinction between order-independent members and ordered rule-set boundaries.
- Connected that distinction to streaming classification and specialized indexes.

## Related Concepts
- [[DomainTrieIndexing]] - implements exact-domain and suffix-rule lookup after domain rules are classified.
- [[AhoCorasickMatching]] - implements keyword-rule lookup after substring predicates are classified.
- [[TreeBitmapIPPrefixLookup]] - implements CIDR lookup after IP-prefix rules are classified.
- [[RebuildableDerivedIndex]] - describes the broader pattern of rebuilding query-optimized state from canonical inputs.
