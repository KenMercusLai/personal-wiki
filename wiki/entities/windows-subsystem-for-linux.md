---
title: "Windows Subsystem for Linux"
description: "软件平台；该来源记录了在 Windows 10 上清理并重装 WSL 2，然后启用原生 systemd 支持的流程。"
type: "entity"
updated: "2026-09-02"
source_keys: ["clean-wsl-reinstall-windows-10-systemd-support"]
entity_kind: "software"
---

来源：[Clean WSL Reinstall for Native systemd on Windows 10]({{< relref "/wiki/sources/clean-wsl-reinstall-windows-10-systemd-support.md" >}})

Windows Subsystem for Linux 是这篇来源的主要操作对象。作者原本在 WSL 2 中配合 Genie 使用 systemd 类体验，后来因为 Windows 10 获得原生 systemd 支持，决定清理旧环境并重新安装 WSL。

来源把 WSL 的生命周期拆成几个边界清楚的步骤：发行版数据由 `wsl --unregister` 删除，发行版应用从 Windows Apps & Features 中卸载，平台能力由 Virtual Machine Platform 和 Windows Subsystem for Linux 两个 Windows Features 控制。重新开启后，`wsl --install` 负责安装 WSL 和默认发行版。

在发行版选择上，来源使用 `wsl --list --online` 查看可安装发行版，用 `wsl --install -d Debian` 安装 Debian，再用 `wsl --set-default Debian` 改默认发行版。它还指出，现代 WSL 安装路径通常不需要再执行 `wsl --set-default-version 2`。
