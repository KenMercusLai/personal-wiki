---
title: "Server-side game logic as client"
description: "把服务器端游戏逻辑作为消息服务中的特殊客户端接入，以复用游戏逻辑、支持同步模型迁移，并与消息转发服务解耦。"
type: "concept"
updated: "2026-09-02"
source_keys: ["jysperm-2018-technical-year-review"]
---

来源：[2018 年度小结（技术方面）]({{< relref "/wiki/sources/jysperm-2018-technical-year-review.md" >}})

Server-side game logic as client 是一种多人游戏后端架构选择：服务器端游戏逻辑不直接嵌入消息转发服务，而是作为一个特殊客户端加入同一个消息系统。王子亭在 LeanCloud 游戏后端方案中提出这个方式，用来满足反作弊所需的服务器端逻辑运行能力。

这种设计的好处是让客户端和服务器端可以复用大部分游戏逻辑。游戏可以从单机逻辑开始，逐步迁移到动作同步，再迁移到状态同步；服务器端逻辑仍围绕消息协议与其他客户端交互，不需要把消息转发服务改造成承载所有游戏规则的中心。

架构边界也因此更清楚。消息转发服务负责连接和状态同步通道，服务器端游戏逻辑负责规则校验和状态推进，两者通过同一套消息机制协作。来源中的验证 Demo 是一个简单回合制卡牌游戏，这个模式后来被 LeanCloud 发布为 Client Engine 产品。
