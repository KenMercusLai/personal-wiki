---
title: "Production-like test data"
description: "Production-like test data preserves real data shape and edge cases while removing sensitive values, so tests can reveal search, performance, and migration failures that empty fixtures miss."
type: "concept"
updated: "2026-09-02"
source_keys: ["loadmill-seven-reasons-staging-environment-sucks"]
---

来源：[7 Reasons Why Your Staging Environment Sucks]({{< relref "/wiki/sources/loadmill-seven-reasons-staging-environment-sucks.md" >}})

Production-like test data 指在测试环境中保留接近生产的数据分布、规模和边界值，同时对敏感信息做脱敏处理。来源指出，空 staging 数据库或自动化测试失败后留下的零散数据，无法说明真实用户使用搜索、列表、筛选或复杂查询时会遇到什么。

这种数据对数据库迁移尤其重要。生产数据库里的怪异字符、空值、超长字段和历史遗留边界值，常常正是迁移脚本和应用代码最容易忽略的输入。只有 staging 中存在同类边界，团队才有机会在发布前发现 schema 变更会破坏哪些路径。

来源同时强调，接近生产不等于直接暴露生产秘密。密码哈希、信用卡号等敏感值不应出现在不该出现的环境里；更合适的做法是把生产数据提取后清洗和脱敏，让测试保留真实形态而不是真实秘密。
