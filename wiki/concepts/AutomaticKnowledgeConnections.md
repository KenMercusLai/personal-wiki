---
title: "Automatic Knowledge Connections"
type: concept
tags: [knowledge-management, nlp, knowledge-graph]
sources:
  - on-the-automatic-generation-of-knowledge-connections
last_updated: 2026-10-03
knowledge_schema: synthesis-v1
---

## Definition
[[AutomaticKnowledgeConnections]] are machine-proposed navigation edges among text passages, concepts, and authors, produced from shared concepts and semantic relatedness and exposed through a linked-note interface.

## Current Synthesis
The source describes an incremental graph whose nodes are user-selected highlights, recognized concepts, and authors. Concept recognition and entity linking identify candidate concepts; confidence, type, and occurrence filters narrow them; DBpedia and ConceptNet add concept-to-concept relationships. In parallel, the system averages knowledge-based relatedness from concept overlap, concept embeddings, and relationship indicators with corpus-based cosine similarity from Sentence Transformer embeddings. It then converts nodes and edges into [[Obsidian]] pages and bidirectional links.

This design usefully separates two discovery modes. Shared concepts can bridge highlights whose topics are not obviously adjacent and are intended to support divergent exploration, while direct passage similarity keeps navigation closer to the current material and is intended to support convergence. The workflow remains partly human because users choose highlights and interpret the proposed connections. Its validation is preliminary: correlation between two model-derived matrices shows that the signals are not independent, but does not establish human relevance, causal effects on recall or insight, precision at a safe publication threshold, or scalability to a large and heterogeneous vault.

## Key Claims
- A heterogeneous graph can unify passage, concept, and author navigation in one note environment.
- Shared-concept and semantic-relatedness edges offer complementary divergent and convergent discovery paths.
- Concept connections inherit errors and scope limits from recognition, entity linking, filtering, DBpedia, and ConceptNet.
- Combining knowledge-based and corpus-based scores can diversify evidence for a connection, but agreement is not ground truth.
- Automatic proposals should remain reviewable because useful discovery and safe canonical link materialization have different evidence thresholds.

## Evidence
- Graph construction: [[on-the-automatic-generation-of-knowledge-connections]] formalizes highlight, concept, and author nodes with six edge types and incrementally updates the graph as highlights arrive.
- Complementary discovery paths: [[on-the-automatic-generation-of-knowledge-connections]] separates shared-concept navigation from direct highlight relatedness and associates them with divergent and convergent thinking.
- NLP pipeline: [[on-the-automatic-generation-of-knowledge-connections]] combines entity recognition and linking, external concept relationships, Numberbatch-style concept vectors, Sentence Transformer embeddings, and cosine similarity.
- Interface realization: [[on-the-automatic-generation-of-knowledge-connections]] maps graph nodes to Obsidian pages and graph edges to bidirectional links.
- Preliminary coherence: [[on-the-automatic-generation-of-knowledge-connections]] reports Mantel correlations of 0.679 and 0.519 for 52- and 182-highlight datasets, both with P < 0.001.

## Counterevidence & Qualifications
The paper evaluates only two small collections spanning two and eight books. Correlation between knowledge-based and corpus-based matrices does not measure precision or recall against human relevance judgments, and the work does not isolate whether the averaged score outperforms either component. It also provides no controlled evidence for recall, elaboration, new insight, navigation success, user trust, maintenance burden, or long-term learning. External concept systems can import ambiguity, coverage gaps, outdated relationships, and relation types whose bidirectional treatment erases direction. Computational cost changed the chosen concept threshold, while large-vault latency and graph-density behavior remain untested. These limits support draft suggestions and review more strongly than automatic writes into canonical notes.

## What Changed
- Created the concept and separated concept-mediated navigation from direct passage similarity.
- Added a review boundary between graph-visible suggestions and canonical note links.
- Recorded matrix correlation as preliminary coherence evidence rather than human relevance validation.

## Related Concepts
- [[PersonalKnowledgeManagement]] - supplies the note corpus and human knowledge-work setting the method is intended to augment.
- [[SemanticSearch]] - provides meaning-based passage comparison beyond exact lexical overlap.
- [[Embeddings]] - encode passages and concepts for vector similarity calculations.
- [[OrphanNotes]] - automatic proposals may surface candidate context, but do not justify forced links.
- [[KnowledgeAsCode]] - provides deterministic validation and review gates around semantic automation.
- [[Obsidian]] - exposes the generated graph as pages and bidirectional hyperlinks.
