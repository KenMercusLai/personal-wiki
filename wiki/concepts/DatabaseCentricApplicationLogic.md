---
title: "Database-Centric Application Logic"
type: concept
tags: [databases, software-architecture, postgresql, api-design]
sources:
  - simplify-move-code-into-database-functions
last_updated: 2026-10-02
knowledge_schema: synthesis-v1
---

## Definition
[[DatabaseCentricApplicationLogic]] is an architecture in which the database owns shared data validity, normalization, reusable operations, and response shaping, while external applications act mainly as thin adapters.

## Current Synthesis
[[DerekSivers]] proposes moving durable data rules from language-specific classes into [[PostgreSQL]]. Constraints protect invariants for every caller, triggers normalize writes, functions encapsulate multi-step operations, and views plus JSON functions define returned representations. A REST service or client library can then pass parameters to approved database functions and return their JSON, making application-language replacement less likely to require rewriting the same data behavior.

This arrangement simplifies one axis by giving rules a single enforcement point close to the data. It complicates another by concentrating application behavior in a particular database engine, procedural language, permission model, and schema-change workflow. The useful principle is therefore narrower than "all intelligence belongs in the database": place invariants and data-intensive operations where all writers can share them, but decide case by case where authorization, orchestration, external effects, presentation, and rapidly changing product policy belong.

## Key Claims
- Database constraints provide universal enforcement for invariants that must hold regardless of which application or script performs a write.
- Triggers and functions can centralize normalization and reusable multi-step data operations instead of duplicating them across language-specific models.
- Database views and JSON construction can expose stable representations to thin REST or client adapters.
- Centralizing durable data behavior can reduce rewrite cost when surrounding application languages or interfaces change.
- Moving logic inward trades application-database coupling for PostgreSQL, PL/pgSQL, schema, permission, and operational coupling rather than eliminating dependency.
- Logic placement should distinguish shared data invariants from authorization, external side effects, presentation, and product rules whose ownership may fit other boundaries.

## Evidence
- Universal validity: [[simplify-move-code-into-database-functions]] uses checks, uniqueness, foreign keys, and cascading deletion to make rules apply at the storage boundary.
- Normalization and operations: [[simplify-move-code-into-database-functions]] demonstrates a write trigger and a reusable get-or-create-style function as database-owned behavior.
- Representation boundary: [[simplify-move-code-into-database-functions]] combines a view, `json_agg`, and JSON-returning API functions with thin Sinatra routes and a small client library.
- Longevity argument: [[simplify-move-code-into-database-functions]] says one PostgreSQL database persisted while its surrounding Perl, PHP, Rails, Ruby, and JavaScript layers changed.
- Concentration tradeoff: [[simplify-move-code-into-database-functions]] accepts PL/pgSQL's usability cost and explicitly chooses PostgreSQL because the author expects the database to remain more stable than application languages.

## Counterevidence & Qualifications
The evidence is one author's 2015 experience and illustrative code, not a comparative study of maintainability, portability, reliability, or team productivity. The examples omit versioned deployment, rollback, testing strategy, observability, authorization, connection and transaction behavior, and interaction with external services. They also contain concrete hazards: the shown `BEFORE` trigger does not return `NEW`, the existence-check-then-insert helper can race, the email regular expression is only a rough validity proxy, and the API functions do not establish caller permissions. Database-resident logic can also make horizontal scaling, vendor migration, local development, review, and staffing harder. The pattern is strongest for invariants and data-intensive operations shared by all writers; it is not evidence that every business rule or side effect belongs in a stored procedure.

## What Changed
- Created the concept as a qualified database-owned logic pattern rather than a universal stored-procedure prescription.
- Separated reduced rule duplication from the PostgreSQL-specific coupling and operational burden it introduces.

## Related Concepts
- [[PostgreSQL]] - supplies the constraints, triggers, functions, views, procedural language, and JSON operations used by the pattern.
- [[SimpleMadeEasy]] - motivates separating one durable rule set from multiple changing application layers.
- [[APIDesign]] - database functions and JSON representations form the external contract in the source's design.
- [[DatabaseEngineeringTradeoffs]] - logic placement changes correctness, portability, scaling, testing, and operational tradeoffs.
- [[TechnologyStackComplexity]] - centralization can remove duplicated layers while concentrating expertise in the database stack.
- [[PasswordHashing]] - credential transformation is one narrowly bounded operation shown inside a database function.
