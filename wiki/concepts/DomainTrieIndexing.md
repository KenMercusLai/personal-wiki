---
title: "Domain Trie Indexing"
type: concept
tags: [trie, radix-tree, domains, matching]
sources:
  - store-domains-ips-text-only
last_updated: 2026-10-18
knowledge_schema: synthesis-v1
---

## Definition
[[DomainTrieIndexing]] stores domain rules in reverse suffix order so shared top-level domains, public suffixes, labels, or character tails become reusable trie paths, optionally compressed into a radix trie.

## Current Synthesis
Domain matching is structured rather than arbitrary string comparison. Reversing traversal makes the stable suffix appear first, allowing related names such as a parent domain and its subdomains to share nodes. Exact-domain and suffix rules can inhabit the same tree when terminal nodes record whether matching must end at that name or may accept descendants.

Node granularity controls the space-time tradeoff. Character nodes maximize suffix sharing, label nodes usually reduce comparisons at a memory cost, and treating a whole public suffix as the first node can align the index with actual registration boundaries. For a matcher built once and then read repeatedly, non-branching paths can be merged into radix edges, reducing nodes, pointers, and comparisons. Lookup cost then follows the input name's traversal length rather than a scan across every stored domain, although build cost and total storage still grow with the rules.

## Key Claims
- Reverse traversal exposes the suffix hierarchy shared by related domain names.
- Exact-domain and domain-suffix rules can share one tree with different terminal metadata.
- Character, label, and public-suffix nodes occupy different points on the memory-versus-comparison tradeoff.
- Read-mostly indexes can compress non-branching trie paths into radix edges after construction.
- Indexed lookup scales with the queried domain's traversed length rather than the number of entries in a linear list.

## Evidence
- Hierarchical sharing: [[store-domains-ips-text-only]] derives a suffix trie from TLD, domain, and subdomain structure and notes shared tails among otherwise unrelated names.
- Match semantics: [[store-domains-ips-text-only]] stores a terminal distinction between exact DOMAIN and descendant-accepting DOMAIN-SUFFIX rules.
- Granularity: [[store-domains-ips-text-only]] contrasts character nodes with label nodes and describes Surge using Public Suffix List boundaries.
- Compression: [[store-domains-ips-text-only]] merges isolated single-child chains after construction into a radix trie for a rebuildable read-only engine.

## Counterevidence & Qualifications
The archived article's interactive construction and lookup diagrams are missing, leaving only the prose explanation. It reports illustrative raw-list memory and comparison costs but no measured comparison among character, label, public-suffix, and radix implementations. Real systems must also specify normalization, internationalized names, case folding, malformed inputs, wildcard semantics, update strategy, allocator overhead, cache locality, and concurrent access. Public-suffix data changes over time, and sharing it as a node boundary adds a maintenance dependency.

## What Changed
- Created a unified model for reversed domain tries, exact-versus-suffix terminal state, and radix compression.
- Added node granularity and public-suffix boundaries as explicit space-time choices.

## Related Concepts
- [[ProxyRuleSetSemantics]] - explains why domain rules can be separated from a heterogeneous rule file and indexed independently.
- [[AhoCorasickMatching]] - handles arbitrary domain substrings that do not preserve suffix hierarchy.
- [[RebuildableDerivedIndex]] - captures why a read-mostly trie may be discarded and rebuilt when configuration changes.
- [[SuffixArrays]] - provides a different suffix-oriented indexing structure with distinct construction and query semantics.
