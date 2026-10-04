---
title: "On the Automatic Generation of Knowledge Connections"
type: source
tags: [pkm, nlp, knowledge-graph, semantic-similarity]
date: 2023-04-28
source_file: "/mnt/ken_personal_wiki/Articles/On the Automatic Generation of Knowledge Connections.md"
---

## Summary
[[FelipePoggiAFraga]], [[MarcusPoggi]], [[MarcoACasanova]], and [[LuizAndrePPaesLeme]] propose [[AutomaticKnowledgeConnections]], a method that turns selected text highlights into an incrementally updated graph of highlights, concepts, and authors. One path links highlights through recognized and externally related concepts; the other combines knowledge-based relatedness with Sentence Transformer cosine similarity to recommend related highlights, then renders the graph as pages and bidirectional links in [[Obsidian]]. Two small evaluations show that the two relatedness matrices correlate, but do not establish connection correctness, learning outcomes, or value relative to simpler baselines.

## Key Claims
- [[AutomaticKnowledgeConnections]] can transform isolated highlights into a navigable graph by connecting highlight, concept, and author nodes.
- Shared-concept navigation depends on entity recognition and linking, confidence and occurrence filters, and external DBpedia and ConceptNet relationships.
- Text relatedness averages a knowledge-based score from concepts and their relationships with a corpus-based cosine-similarity score from Sentence Transformer embeddings.
- The system maps graph nodes to Obsidian pages and graph edges to bidirectional hyperlinks, allowing incremental updates as users add highlights.
- Concepts connections are intended to encourage divergent exploration, while direct highlight similarity is intended to encourage convergent exploration.
- Mantel tests found correlation between the knowledge-based and corpus-based matrices in datasets of 52 highlights from two books and 182 highlights from eight books, but agreement between two automated signals is not ground-truth relevance.
- Human selection of highlights and interpretation of proposed links remain part of the workflow rather than being replaced by automation.

## Key Quotes
> "The navigation mechanisms are based on shared concepts and semantic relatedness between texts." — on the two connection paths

> "Users actively cocreate connections" — on retaining a human role in the generated graph

## Connections
- [[FelipePoggiAFraga]] — first author of the paper.
- [[MarcusPoggi]] — coauthor of the paper.
- [[MarcoACasanova]] — coauthor of the paper.
- [[LuizAndrePPaesLeme]] — coauthor of the paper.
- [[AutomaticKnowledgeConnections]] — central method for generating concept and related-highlight links.
- [[Obsidian]] — page-and-link interface used to expose the generated graph for navigation.
- [[PersonalKnowledgeManagement]] — target practice the authors seek to augment with NLP-generated connections.
- [[Embeddings]] — vector representations underpin the corpus-based and part of the knowledge-based relatedness score.
- [[SemanticSearch]] — nearest-by-meaning comparison is used to recommend related highlights rather than retrieve only exact lexical matches.

## Contradictions
- The paper's automatic materialization of bidirectional links qualifies [[OrphanNotes]] and the wiki's own promotion-gate rule: matrix agreement does not demonstrate that each proposed semantic link is accurate enough to write into canonical notes without review.
- The evaluation establishes correlation between two automated relatedness matrices, not relevance against human judgments, improvement in recall or insight, comparison with either component alone, or usefulness at vault scale.
