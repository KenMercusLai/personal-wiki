---
title: "Simplify: move code into database functions"
type: source
tags: [postgresql, databases, software-architecture, simplicity]
date: 2015-05-04
source_file: /mnt/ken_personal_wiki/Articles/Simplify move code into database functions.md
---

## Summary
[[DerekSivers]] proposes [[DatabaseCentricApplicationLogic]]: place data validation, normalization, reusable operations, and JSON projection inside [[PostgreSQL]], leaving REST endpoints or client libraries as thin argument-and-result adapters. He connects the design to [[SimpleMadeEasy]], arguing that one database-owned rule set reduces coupling to replaceable application-language layers. The essay is a first-person architecture proposal, however, and its compact SQL omits important correctness, authorization, migration, testing, observability, and portability concerns.

## Key Claims
- Databases often outlive the applications and programming languages that access them, so repeatedly reimplementing durable data rules in each application layer creates migration work and inconsistent access paths.
- Constraints can make validity rules such as nonempty names, unique email addresses, referential integrity, cascading deletion, and tag formats apply to every database client.
- Triggers can normalize input before storage, while reusable functions can encapsulate multi-step reads and writes behind a stable database interface.
- Views and PostgreSQL JSON functions can shape nested API representations inside the database rather than requiring every client to reconstruct them.
- A deliberately narrow set of JSON-returning database functions can let REST routes and client libraries become thin adapters whose implementation language is easier to replace.
- The proposed simplicity is contextual: centralizing logic removes duplicated application rules but increases dependence on PostgreSQL, PL/pgSQL, database permissions, and database-centered deployment practice.

## Key Quotes
> "Databases outlive the applications that access them." - the essay's durability premise.

> "Complex means many things tied together." - the Rich Hickey distinction used to motivate the design.

## Connections
- [[DerekSivers]] - author describing his move toward database-owned application logic.
- [[PostgreSQL]] - database, procedural runtime, constraint system, trigger system, and JSON interface used by the examples.
- [[DatabaseCentricApplicationLogic]] - architectural pattern synthesized from the article.
- [[SimpleMadeEasy]] - conceptual distinction used to argue that language-specific models and database rules should not be interwoven.
- [[TechnologyStackComplexity]] - thin language adapters can reduce duplicated data logic while database-specific implementation creates a different form of concentration.
- [[APIDesign]] - JSON-returning functions become the contract used by REST endpoints and client libraries.
- [[PasswordHashing]] - the password-update example uses PostgreSQL `crypt()` and `gen_salt()` inside a database function.

## Contradictions
- [[appcanary-simple-aint-easy-but-hard-aint-simple-leaving-clojure-for-ruby]] accepts the simple-versus-easy distinction but warns that conceptual simplicity can become an excuse for poor developer experience; Sivers acknowledges PL/pgSQL's awkwardness but treats centralization as worth the cost.
- The claim that putting intelligence in the database makes it self-contained and "not tied to anything" is too strong: the design becomes tied to PostgreSQL semantics, procedural languages, schema migrations, permissions, and operational capacity.
- The snippets are illustrative rather than production-ready. The `BEFORE` trigger function shows no `RETURN NEW`, `get_person` uses a race-prone check-then-insert sequence, and the API sketch does not demonstrate authentication, authorization, error semantics, or safe evolution.
