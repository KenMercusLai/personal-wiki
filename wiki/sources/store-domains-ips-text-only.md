---
title: "生活在字典树上 —— 存储和匹配海量的域名和 IP 地址"
type: source
tags: [data-structures, networking, domain-matching, ip-routing]
date: 2026-08-19
source_file: "/mnt/ken_personal_wiki/Articles/store-domains-ips-text-only.md"
---

## Summary
[[Sukka]] explains how a proxy rule engine can classify unordered rules by type and replace linear scans with structures matched to each rule's semantics. Reversed [[DomainTrieIndexing]] and radix compression exploit domain suffix structure, [[AhoCorasickMatching]] handles arbitrary domain keywords in one pass, and [[TreeBitmapIPPrefixLookup]] packs stride-based CIDR traversal with internal and external bitmaps. The archived source preserves prose and code but lacks its cover and nine interactive demonstrations, so its qualitative mechanisms remain available while the visual walkthroughs and any behavior embodied only in them cannot be checked.

## Key Claims
- Rules within one RULE-SET or DOMAIN-SET have OR semantics, so reordering them does not change whether that set matches; ordering remains significant between different rule sets.
- Streaming rules into type-specific indexes avoids preserving one heterogeneous input file as a linear search structure.
- Exact domains and domain suffixes can share a reversed trie, with terminal metadata distinguishing an exact match from a suffix match.
- Grouping domain labels trades some memory for fewer comparisons, while radix compression merges non-branching paths after construction for a read-mostly matcher.
- Aho–Corasick adds failure links to a forward keyword trie so a domain string is traversed without restarting from its beginning after each mismatch.
- CIDR membership is binary prefix matching; taking four bits per stride reduces IPv4 traversal to at most eight levels but creates sparse 16-way branches.
- Tree Bitmap stores branch existence and in-node prefix termination in separate bitmaps, allowing sparse child data to remain compact and accommodating prefix lengths that do not align with the stride.

## Key Quotes
> "在一个 RULE-SET 文件内部的多条规则之间的逻辑关系是『或』。" — why individual rule order can be discarded during indexing.

> "输入的域名只需要被遍历一次，而不需要 lookback（回溯）。" — the intended effect of Aho–Corasick failure links.

## Connections
- [[Sukka]] — author presenting the data-structure tutorial.
- [[ProxyRuleSetSemantics]] — separates within-set OR semantics from ordering between sets.
- [[DomainTrieIndexing]] — stores exact-domain and suffix rules through reversed and compressed tries.
- [[AhoCorasickMatching]] — indexes substring-style domain keywords with failure links.
- [[TreeBitmapIPPrefixLookup]] — represents sparse stride-based CIDR prefixes compactly.

## Contradictions
- No direct contradiction with existing wiki claims was identified. The source's statements that matching time is independent of the number of stored entries describe traversal of an already-built index; they do not remove construction cost, memory growth, output-reporting cost, or implementation-dependent constants.
- The archived conversion is explicitly partial: the cover and nine client-rendered demonstrations are unavailable, so details shown only in those demonstrations cannot be verified from this source note.
