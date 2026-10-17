---
title: "Aho–Corasick Matching"
type: concept
tags: [algorithms, string-matching, trie, automata]
sources:
  - store-domains-ips-text-only
last_updated: 2026-10-18
knowledge_schema: synthesis-v1
---

## Definition
[[AhoCorasickMatching]] is multi-pattern string matching built from a forward prefix trie plus failure links that redirect traversal after a mismatch without restarting at the beginning of the input.

## Current Synthesis
Domain keyword rules can match anywhere within a hostname, so they cannot rely on the label and suffix boundaries used by [[DomainTrieIndexing]]. A forward trie still shares common keyword prefixes, while precomputed failure links encode the best alternate state when the current path cannot continue. The matcher can therefore consume the hostname in one forward pass and detect stored keywords without separately rescanning it for every pattern.

The article's independence claim is about input traversal after the automaton exists: adding patterns changes construction time, automaton size, cache behavior, and potentially the number of matches emitted, even when the scan remains linear in the hostname length under the usual model.

## Key Claims
- Keyword rules require substring matching rather than exact-name or suffix matching.
- A forward trie shares common prefixes among stored keywords.
- Failure links precompute where matching should resume when a trie edge is absent.
- The input string need not be rewound and restarted for each failed path.
- Search traversal is governed primarily by input length once the automaton has been built.

## Evidence
- Problem shape: [[store-domains-ips-text-only]] shows that one keyword may match a bare domain and longer hostnames containing it in different positions.
- Shared prefixes: [[store-domains-ips-text-only]] groups examples such as `github`, `gitlab`, and `gitbook` in a forward keyword trie.
- Failure behavior: [[store-domains-ips-text-only]] explains failure links as construction-time answers to where traversal should continue when the current path fails.

## Counterevidence & Qualifications
The source's two interactive automaton demonstrations are unavailable in the archived text conversion, and it gives no implementation, memory accounting, build complexity, output-link treatment, Unicode or normalization policy, or benchmark. Matching time can also include reporting occurrences; it is not literally independent of the stored pattern set when many patterns match at one position. Product-specific keyword semantics may impose additional normalization or boundary rules.

## What Changed
- Created a source-bounded explanation of prefix sharing and failure-link traversal.
- Qualified the distinction between linear input scanning and pattern-dependent construction, storage, and output cost.

## Related Concepts
- [[DomainTrieIndexing]] - uses suffix structure for exact and suffix rules rather than arbitrary substrings.
- [[ProxyRuleSetSemantics]] - permits keyword predicates to be classified into their own matcher.
- [[NaturalLanguageProcessing]] - uses related multi-pattern and automaton techniques in text processing, though domain keywords are a narrower byte-or-character matching problem.
- [[RebuildableDerivedIndex]] - describes automata that can be regenerated from canonical keyword rules.
