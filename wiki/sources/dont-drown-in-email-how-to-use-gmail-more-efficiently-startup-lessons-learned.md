---
title: "Don’t Drown in Email! How to Use Gmail More Efficiently"
type: source
tags: [email, productivity, gmail, inbox-zero]
date: 2013-12-30
source_file: "/mnt/ken_personal_wiki/Articles/Don’t drown in email! How to use Gmail more efficiently. - Startup Lessons Learned.md"
---

## Summary
[[AndreasKlinger]] describes a personal [[Gmail]] workflow that turns special stars into explicit email states—action needed, awaiting reply, delegated, and scheduled—and exposes those states in search-backed side panels while the ordinary inbox is archived to zero. The method combines rapid triage, follow-up visibility, bulk archiving, filters, keyboard shortcuts, auto-advance, undo send, and account consolidation, but its screenshots document an older Gmail interface and some named settings or extensions may no longer exist in the same form.

![Gmail with an empty primary inbox and right-side action, awaiting-reply, and scheduled panels](../../wiki-assets/dont-drown-in-email-how-to-use-gmail-more-efficiently-startup-lessons-learned/gmail-multiple-inbox-overview.png)

## Key Claims
- [[EmailTaskManagement]] can move actionable messages out of the inbox without losing them by assigning each thread a visible state and surfacing that state through saved searches or multiple inbox panels.
- The daily loop is: handle short messages immediately, mark deferred work, mark sent messages that require follow-up, archive processed threads, and let new replies return to the inbox.

![Replied Gmail thread marked with a purple question icon to indicate an awaited reply](../../wiki-assets/dont-drown-in-email-how-to-use-gmail-more-efficiently-startup-lessons-learned/awaiting-reply-thread.png)

- The configuration uses Gmail's historical Multiple Inboxes lab, special stars, search queries, and right-side panels; the author's example combines `has:yellow-bang OR has:red-bang` for action, `has:purple-question` for awaited replies, `has:purple-star` for scheduled items, and `has:orange-guillemet` for delegated work.

![Historical Gmail Labs control with Multiple Inboxes enabled](../../wiki-assets/dont-drown-in-email-how-to-use-gmail-more-efficiently-startup-lessons-learned/multiple-inboxes-lab-setting.png)

![Gmail special-star configuration with action, reply, delegation, and schedule symbols in use](../../wiki-assets/dont-drown-in-email-how-to-use-gmail-more-efficiently-startup-lessons-learned/special-stars-selection.png)

![Multiple Inboxes queries and panel titles for action, awaiting reply, scheduled, and delegated email](../../wiki-assets/dont-drown-in-email-how-to-use-gmail-more-efficiently-startup-lessons-learned/multiple-inbox-search-panels.png)

- The historical setup requires the default inbox, disabled importance overrides, minimal category tabs, and a compact layout so the side panels remain visible.

![Historical Gmail inbox settings using the default type, no importance markers, and no filter overrides](../../wiki-assets/dont-drown-in-email-how-to-use-gmail-more-efficiently-startup-lessons-learned/default-inbox-settings.png)

![Gmail settings menu with Compact display density and Configure inbox controls](../../wiki-assets/dont-drown-in-email-how-to-use-gmail-more-efficiently-startup-lessons-learned/compact-density-menu.png)

![Gmail tab configuration with only the Primary category selected](../../wiki-assets/dont-drown-in-email-how-to-use-gmail-more-efficiently-startup-lessons-learned/inbox-tabs-configuration.png)

- A first-time reset can classify the recent pages of messages, apply action or follow-up states, then bulk-archive the remaining backlog; this clears the inbox without claiming that every old message was individually completed.

![Yellow action marker applied to a Gmail message before archiving](../../wiki-assets/dont-drown-in-email-how-to-use-gmail-more-efficiently-startup-lessons-learned/todo-star-on-message.png)

- Repetitive mail should be reduced or automated through unsubscribing and filters, including skip-inbox rules, labels, and forwarding where appropriate.

![Gmail filter that labels and archives a recurring Akismet account statement](../../wiki-assets/dont-drown-in-email-how-to-use-gmail-more-efficiently-startup-lessons-learned/automatic-invoice-filter.png)

- Keyboard shortcuts and auto-advance reduce per-message handling overhead, while undo send adds a short recovery path after sending.

![Gmail setting with keyboard shortcuts enabled](../../wiki-assets/dont-drown-in-email-how-to-use-gmail-more-efficiently-startup-lessons-learned/keyboard-shortcuts-setting.png)

![Historical Gmail Labs setting with auto-advance enabled and configured to open the next conversation](../../wiki-assets/dont-drown-in-email-how-to-use-gmail-more-efficiently-startup-lessons-learned/auto-advance-setting.png)

![Historical Gmail Labs setting with Undo Send enabled](../../wiki-assets/dont-drown-in-email-how-to-use-gmail-more-efficiently-startup-lessons-learned/undo-send-setting.png)

- Multiple accounts can be consolidated into one inbox if outbound mail uses the appropriate SMTP identity and replies default to the address that received the message.

![Gmail send-mail-as account configured through an SMTP server with TLS](../../wiki-assets/dont-drown-in-email-how-to-use-gmail-more-efficiently-startup-lessons-learned/smtp-account-configuration.png)

![Gmail preference to reply from the same address to which a message was sent](../../wiki-assets/dont-drown-in-email-how-to-use-gmail-more-efficiently-startup-lessons-learned/reply-from-received-address.png)

## Key Quotes
> "All done with 0 plugins, using only standard gmail features" - on implementing the core triage system with built-in Gmail controls.

> "You archive all emails" - on separating inbox arrival from the state of actionable work.

> "Now your inbox should at zero and your right areas full." - on moving visible work from the inbox into explicit state panels rather than erasing obligations.

## Connections
- [[AndreasKlinger]] - author and long-term user of the workflow.
- [[Gmail]] - product whose stars, search, filters, multiple inboxes, and account settings implement the method.
- [[EmailTaskManagement]] - broader practice of representing email as action and follow-up states rather than leaving every message in one queue.
- [[PersonalProductivity]] - the workflow externalizes tasks, delegation, waiting, and scheduled commitments.
- [[AttentionManagement]] - archiving and filtering reduce the number of messages competing in the default inbox.
- [[CommunicationMultitasking]] - the method organizes processing but does not by itself determine how often email should interrupt focused work.
- [[WorkHabits]] - rapid handling, state assignment, archiving, and follow-up review form a repeated operating loop.

## Contradictions
- [[blog-jeff-huang-my-productivity-app-is-a-never-ending-txt-file]] also uses a small email-flag system but explicitly does not make inbox zero the main goal; together the sources support explicit action states more strongly than any universal requirement to empty the inbox.
- The screenshots show an older Gmail product state, including Labs and historical Multiple Inboxes controls. They support the described workflow but should not be treated as current setup instructions without checking today's interface.
