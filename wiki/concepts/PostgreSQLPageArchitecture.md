---
title: "PostgreSQL Page Architecture"
type: concept
tags: [postgresql, storage, page-layout, mvcc]
sources:
  - inside-postgresqls-8kb-page
last_updated: 2026-10-10
knowledge_schema: synthesis-v1
---

## Definition
[[PostgreSQLPageArchitecture]] is the organization of a PostgreSQL storage page into header metadata, line pointers, free space, tuple or index data, and optional access-method-specific special space.

## Current Synthesis
The default 8KB page is PostgreSQL's basic storage and I/O unit, but its useful property is not the number alone. The page is a slotted structure: a 24-byte header describes safety, visibility, cleanup, and region boundaries; fixed four-byte line pointers grow from the header; variable-size tuples grow from the other end; and the remaining middle gap absorbs inserts and later compaction.

This indirection separates a tuple's logical physical address from its present byte offset. Indexes can retain a `(page, line pointer)` reference while PostgreSQL moves tuple bytes within the page or redirects a slot during a HOT update. The same page boundary also concentrates recovery and maintenance decisions: a page LSN coordinates WAL replay, an optional checksum detects corruption, visibility state can reduce heap visits, and the prune horizon can trigger local reclamation.

The architecture makes capacity measurable but not constant. Header, pointer, tuple-header, alignment, and payload costs all matter; variable-width values change the number of rows that fit. Heap and index pages also share the general shape while allocating their trailing special space differently.

## Key Claims
- PostgreSQL's default 8KB page is both an I/O boundary and a container for independently managed storage metadata.
- Opposing growth of line pointers and tuples preserves one contiguous free-space region and accommodates variable-width rows.
- Stable line-pointer indirection lets indexes address slots rather than mutable tuple byte offsets.
- Page metadata joins crash recovery, corruption detection, visibility, and opportunistic pruning to the physical layout.
- Page-size and row-density choices trade metadata overhead against wasted space, row width, access pattern, and I/O amplification.

## Evidence
- Page regions and direction: [[inside-postgresqls-8kb-page]] inspects a page with a 24-byte header, three four-byte line pointers ending at byte 36, tuples beginning at byte 7,976, and 7,940 bytes between them; its retained diagram shows the same layout and direction.
- Stable addressing: [[inside-postgresqls-8kb-page]] shows line pointers carrying tuple offset, length, and state, while `(page, slot)` forms the `ctid` used by index references and HOT redirection.
- Lifecycle metadata: [[inside-postgresqls-8kb-page]] maps `pd_lsn`, `pd_checksum`, flags, boundary offsets, special-space offset, layout version, and `pd_prune_xid` into the 24-byte header.
- Capacity: [[inside-postgresqls-8kb-page]] estimates roughly 107 rows from average row cost, then observes 119 variable-width rows on the first page and nearly full first and second pages after further inserts.
- Access-method variation: [[inside-postgresqls-8kb-page]] observes zero special space on its heap page and 16 bytes of B-tree-specific special space on an inspected leaf page.

## Counterevidence & Qualifications
The article is a practitioner tutorial built around one synthetic schema and one database instance, not a cross-version or cross-workload storage study. Its row-density measurements are value-dependent, its historical and hardware-alignment rationale does not establish present-day optimality, and compile-time block-size alternatives carry ecosystem and rebuild consequences that are not evaluated. The article also overstates the page LSN's sole responsibility for recovery and blurs the page-header all-visible flag with the separate visibility map used by index-only scans.

## What Changed
- Added a concrete synthesis of PostgreSQL's slotted heap-page regions and their opposing growth directions.
- Connected stable line-pointer addressing to tuple movement and HOT-update behavior.
- Distinguished shared page structure from heap-versus-index use of trailing special space.

## Related Concepts
- [[DatabaseEngineeringTradeoffs]] - page size couples metadata cost, row density, and I/O amplification.
- [[StoragePerformanceBenchmarking]] - raw-page inspection and measured tuple sizes reveal physical behavior that logical row counts hide.
- [[BackupAndRecovery]] - page LSNs and checksums contribute to replay coordination and corruption detection.
- [[DatabaseCentricApplicationLogic]] - PostgreSQL's physical page layer is the storage substrate beneath database-owned constraints, functions, and views.
