---
title: "Code review as team learning"
description: "把代码评审从单纯找 bug 或风格把关，转成团队共享代码理解、最近变更和同事思维方式的学习机制。"
type: "concept"
updated: "2026-09-02"
source_keys: ["asana-uplevel-code-review-skills"]
---

来源：[7 Ways to Uplevel Your Code Review Skills]({{< relref "/wiki/sources/asana-uplevel-code-review-skills.md" >}})

Code review as team learning 指把代码评审视为团队学习和知识扩散机制，而不是只把它当作缺陷筛查或风格检查。Asana engineering 的文章强调，团队需要先约定评审的主要目标；如果作者期待找 bug，评审者却主要讨论样式，双方都会误判彼此的工作价值。

这个概念最重视两类学习。第一，评审者通过阅读同事的实现方式，学习他们如何理解代码库、拆解问题和组织变更。第二，团队通过评审让最近改动不只留在作者脑中；当问题之后出现时，至少有两个人知道相关文件和功能发生过什么。

它也重新划分了人工评审和自动化工具的边界。文章认为，运行时 bug 更适合通过自动测试和实际使用应用发现，基础风格规则更适合交给 linter。人工评审的稀缺价值在于建立共享上下文、发现人需要讨论的设计问题，并维护团队信任。

因此，好的评审不是把所有评论都压到作者身上，而是帮助团队形成共同语言。评审者可以写下问题、说明自己还不确定的地方，或把某次评审当成学习同类功能实现方式的机会；这些行为都让代码评审成为团队能力建设的一部分。
