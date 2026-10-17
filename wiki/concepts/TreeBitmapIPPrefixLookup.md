---
title: "Tree Bitmap IP Prefix Lookup"
type: concept
tags: [networking, cidr, trie, bitmap]
sources:
  - store-domains-ips-text-only
last_updated: 2026-10-18
knowledge_schema: synthesis-v1
---

## Definition
[[TreeBitmapIPPrefixLookup]] is a compact stride-based trie representation for IP prefixes that uses an external bitmap for existing child branches and an internal bitmap for prefixes terminating within a stride.

## Current Synthesis
CIDR membership becomes prefix matching when an address is viewed as 32 IPv4 bits or 128 IPv6 bits. A binary trie expresses that directly but may require one branch decision per bit. Consuming four bits at a time reduces IPv4 depth to at most eight stride levels, at the cost of 16 possible child branches per node.

Tree Bitmap avoids reserving 16 pointers at every sparse node. Its external bitmap marks which child branches exist so their records can be packed contiguously; its internal bitmap records prefixes that terminate at or within the current stride, including lengths such as `/10` that leave a partial group after complete four-bit strides. Lookup checks internal matches and then uses external branch state while consuming successive address groups.

## Key Claims
- CIDR lookup is binary prefix matching over fixed-width IPv4 or IPv6 addresses.
- Multi-bit strides reduce tree depth while increasing each node's potential fanout.
- Sparse wide nodes make a full pointer array wasteful.
- An external bitmap records populated child branches and supports compact child storage.
- An internal bitmap records matching prefixes that terminate within the current stride.
- Partial-stride prefix lengths can be represented without forcing every prefix length to be a multiple of the stride.

## Evidence
- Prefix reduction: [[store-domains-ips-text-only]] derives `/24` and `/16` as fixed leading-bit sequences followed by unconstrained bits.
- Stride tradeoff: [[store-domains-ips-text-only]] replaces 32 one-bit IPv4 levels with at most eight four-bit levels and notes the resulting 16-way sparse fanout.
- Dual bitmaps: [[store-domains-ips-text-only]] assigns branch existence to the external bitmap and prefixes terminating at the node to the internal bitmap.
- Unaligned prefix: [[store-domains-ips-text-only]] uses `100.64.0.0/10` to show two full four-bit strides plus a two-bit remainder recorded internally.

## Counterevidence & Qualifications
The source attributes the structure to an APNIC article and points to Rust examples but does not reproduce a full implementation, rank calculation, child-address formula, short-circuit optimization, IPv6 walkthrough, or benchmark. Its two interactive demonstrations are absent from the archive. Actual performance depends on stride choice, bitmap operations, memory layout, allocator and cache behavior, update frequency, longest-prefix versus Boolean-match semantics, and hardware; the tutorial only establishes the qualitative representation.

## What Changed
- Created a CIDR-focused synthesis of stride depth, sparse fanout, and dual-bitmap roles.
- Added partial-stride prefixes and missing implementation evidence as explicit boundaries.

## Related Concepts
- [[ProxyRuleSetSemantics]] - permits CIDR rules to be classified into a dedicated prefix matcher.
- [[DomainTrieIndexing]] - shares the trie principle but operates on reversed domain structure rather than address bits.
- [[RebuildableDerivedIndex]] - applies when the packed prefix structure is regenerated after rule updates.
- [[DDoSTrafficMonitoring]] - represents a networking workload that may also depend on compact address classification, though this source does not connect the implementations directly.
