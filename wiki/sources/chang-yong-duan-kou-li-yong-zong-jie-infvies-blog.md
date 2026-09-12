---
title: "常用端口利用总结"
type: source
tags: [security, penetration-testing, ports, cheatsheet]
date: 2026-02-28
source_file: /mnt/ken_personal_wiki/Articles/常用端口利用总结 - Infvie's Blog.md
---

## Summary
This Infvie's Blog article is a port-oriented penetration-testing checklist that maps common exposed services to likely risk classes: weak credentials, cleartext sniffing, unauthenticated access, web flaws, deserialization, remote-administration weaknesses, database exposure, and legacy protocol bugs. Its main defensive value is not a novel exploit technique, but a compact triage map for [[DefensivePortTriage]] across network services, administration interfaces, middleware, and databases.

## Key Claims
- Exposed management services such as FTP, SSH, Telnet, RDP, VNC, pcAnywhere, Radmin, and SMB should be treated as high-priority [[RemoteAdministrationExposure]] because weak credentials, cleartext transport, or historical remote-code bugs can turn service access into host control.
- Cleartext or legacy protocols such as FTP, Telnet, POP3, and some database or remote-control services create [[CleartextProtocolExposure]] when credentials or sensitive data cross observable network paths.
- Many services in the table, including Rsync, NFS, ZooKeeper, Docker Remote API, Redis, InfluxDB, Memcached, MongoDB, and Elasticsearch, are dangerous when misconfigured for [[UnauthenticatedServiceExposure]].
- Database ports such as MSSQL, Oracle, MySQL, PostgreSQL, Sybase/DB2, and MongoDB combine [[DatabaseServiceExposure]] with credential guessing, injection paths, misconfiguration, and sometimes memory-corruption or command-execution risks.
- Web and middleware ports such as HTTP/HTTPS, Tomcat/JBoss/Resin, WebLogic, WebSphere, ActiveMQ, Zabbix, GlassFish, and FastCGI require application-layer review because risk often comes from consoles, upload paths, weak passwords, file-write behavior, or deserialization.

## Key Quotes
> "用户名：anonymous 密码：为空或者任意邮箱" - The FTP section uses anonymous login as a representative misconfiguration check.

> "网络上传输的用户和密码都是以明文方式传送的" - The Telnet section highlights why legacy cleartext administration remains risky.

> "未授权访问" - The source repeatedly uses unauthenticated access as the key risk label for exposed storage, coordination, cache, and database services.

## Connections
- [[Infvie]] - Source site credited in the imported article metadata.
- [[DefensivePortTriage]] - The article is organized as a port-to-risk triage table.
- [[RemoteAdministrationExposure]] - Many sections concern remote login, file sharing, and desktop administration services.
- [[CleartextProtocolExposure]] - FTP, Telnet, POP3, and some database or remote-control paths are framed around sniffing or unencrypted credential transfer.
- [[WeakCredentialExposure]] - Brute force and default credentials recur across SSH, Telnet, databases, middleware consoles, and remote-control tools.
- [[UnauthenticatedServiceExposure]] - Misconfigured services are repeatedly described as exploitable when exposed without authentication.
- [[DatabaseServiceExposure]] - MSSQL, Oracle, MySQL, PostgreSQL, Sybase/DB2, Redis, MongoDB, and related services are grouped as database-facing risk surfaces.

## Contradictions
- No direct contradictions with existing wiki pages were found.
