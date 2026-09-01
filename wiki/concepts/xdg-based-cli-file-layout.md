---
title: "XDG-based CLI file layout"
description: "命令行工具按 XDG Base Directory 和平台惯例分别放置配置、数据和缓存文件。"
type: "concept"
updated: "2026-09-01"
source_keys: ["jeff-dickey-twelve-factor-cli-apps"]
---

来源：[12 Factor CLI Apps]({{< relref "/wiki/sources/jeff-dickey-twelve-factor-cli-apps.md" >}})

XDG-based CLI file layout 指 CLI 遵循 XDG Base Directory 以及平台惯例放置本地文件。Jeff Dickey 认为，工具不应随意把配置、数据和缓存混在用户主目录下，而应尊重标准位置和环境变量。

在这篇来源中，配置文件默认放在 `~/.config/myapp`，数据文件默认放在 `~/.local/share/myapp`，并允许 `XDG_CONFIG_HOME` 等环境变量覆盖。缓存文件在 Unix 上使用 `~/.cache/myapp`，在 macOS 上更适合使用 `~/Library/Caches/myapp`，在 Windows 上使用 `%LOCALAPPDATA%\myapp`。

这个概念服务于可维护性和用户控制。标准文件布局让用户更容易备份配置、清理缓存、迁移数据、调试问题，也让 CLI 的行为符合其他 Unix 风格工具和跨平台应用的预期。
