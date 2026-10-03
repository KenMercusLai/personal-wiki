---
title: "小贴士：Docker清理作弊手册"
type: source
tags: [docker, cleanup, devops]
date: 2019-11-01
source_file: /mnt/ken_personal_wiki/Articles/Docker清理作弊手册.md
---

## Summary
伊布整理了一份面向本地磁盘回收的 [[Docker]] 清理速查表，分别列出停止容器、悬空或未使用镜像、卷与网络的清理命令，并以 `docker system prune` 作为组合入口。文章也揭示了 [[DockerResourceCleanup]] 的顺序依赖：先删除全部容器，再执行 `docker image prune -a`，会让所有镜像都失去容器引用并进入可删除范围。

## Key Claims
- `docker system prune` 可组合清理停止的容器、悬空镜像和未使用网络，但文中没有把卷列入该命令的默认范围。
- 停止容器不会自动删除容器；若希望退出后自动清理，应在运行时使用 `--rm`，否则可另行执行 `docker container prune`。
- `docker container stop $(docker container ls -aq)` 与随后的 `docker container rm $(docker container ls -aq)` 会停止并删除列出的全部容器，破坏范围明显大于只清理已停止容器。
- `docker image prune` 针对构建后留下的悬空镜像；`docker image prune -a` 则扩展到所有未被容器使用的镜像。
- 清理动作具有顺序依赖：若先删除所有容器，`docker image prune -a` 的可删除集合可能扩大到全部本地镜像。
- 卷和网络有独立的 `docker volume prune` 与 `docker network prune` 命令，不能仅从容器或镜像已清理推断它们也已被回收。

## Key Quotes
> “慎用。如果前面已经清理了所有的容器，`-a` 参数会清理所有的镜像。” — 对清理顺序扩大镜像删除范围的警告。

## Connections
- [[Docker]] - 提供文中列出的容器、镜像、卷、网络与系统级清理命令。
- [[DockerResourceCleanup]] - 将对象引用关系、命令范围和执行顺序视为清理前的判断条件。
- [[ContainerNativePractice]] - 运行时资源生命周期是容器化应用操作纪律的一部分。

## Contradictions
- 未发现与现有 wiki 的直接矛盾；本文补充的是本地资源回收，而现有 Docker 材料主要讨论应用启动、镜像构建、渐进式升级和事件响应。
- 文章是 2019 年的简短速查表，没有固定 Docker 版本，也没有讨论确认提示、过滤器、BuildKit 缓存、命名卷中的持久数据或恢复方案；具体删除集合应以执行环境的命令帮助与预览为准。
