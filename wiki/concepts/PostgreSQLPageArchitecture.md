---
title: "PostgreSQL Page Architecture"
type: concept
tags: [postgresql, storage, page-layout, mvcc]
sources:
  - inside-postgresqls-8kb-page
  - introduction-to-buffers-in-postgresql
last_updated: 2026-10-10
knowledge_schema: synthesis-v1
---

## Definition
[[PostgreSQLPageArchitecture]] is the organization of a PostgreSQL storage page into header metadata, line pointers, free space, tuple or index data, and optional access-method-specific special space.

## Current Synthesis
The default 8KB page is PostgreSQL's basic storage and I/O unit, but its useful property is not the number alone. Reading or changing one row brings its containing page through the buffer system. The page itself is a slotted structure: a 24-byte header describes safety, visibility, cleanup, and region boundaries; fixed four-byte line pointers grow from the header; variable-size tuples grow from the other end; and the remaining middle gap absorbs inserts and later compaction.

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
- Buffer boundary: [[introduction-to-buffers-in-postgresql]] shows that a row access operates on its containing 8KB page and traces those pages through shared buffers, dirtying, eviction, and reload.

## Counterevidence & Qualifications
Both articles are practitioner tutorials built around synthetic examples, not cross-version or cross-workload storage studies. Row-density measurements are value-dependent, historical and hardware-alignment rationales do not establish present-day optimality, and compile-time block-size alternatives carry ecosystem and rebuild consequences that are not evaluated. The page-layout article overstates the page LSN's sole responsibility for recovery and blurs the page-header all-visible flag with the separate visibility map used by index-only scans. The buffer article's claim that a row may span multiple pages needs a TOAST-aware qualification: an ordinary heap tuple must fit on one heap page, while oversized attributes are compressed or moved out of line into separately paged storage.

## What Changed
- Connected the physical 8KB layout to shared-buffer residency, dirtying, eviction, and reload.
- Qualified the suggestion that one ordinary heap tuple directly spans multiple heap pages by preserving PostgreSQL's TOAST boundary.

## Related Concepts
- [[DatabaseEngineeringTradeoffs]] - page size couples metadata cost, row density, and I/O amplification.
- [[StoragePerformanceBenchmarking]] - raw-page inspection and measured tuple sizes reveal physical behavior that logical row counts hide.
- [[BackupAndRecovery]] - page LSNs and checksums contribute to replay coordination and corruption detection.
- [[DatabaseCentricApplicationLogic]] - PostgreSQL's physical page layer is the storage substrate beneath database-owned constraints, functions, and views.
- [[PostgreSQLBufferManagement]] - manages the in-memory residency, replacement, and persistence of these page-sized units.
