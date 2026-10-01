---
title: "Notifications: A Tragedy Of the Digital Commons"
type: source
tags: [notifications, mobile, product-design, attention, artificial-intelligence]
date: 2017-05-29
source_file: "/mnt/ken_personal_wiki/Articles/Notifications- A Tragedy Of the Digital Commons - Positive Slope - Medium.md"
---

## Summary
[[ScottBelsky]] frames mobile notifications as a tragedy of the commons: each app can improve its own engagement by sending more attention-catching alerts, while the aggregate volume degrades the shared out-of-app interface for users and other developers. He proposes moving prioritization into a mandatory operating-system notification layer that ranks messages using urgency, relevance, context, relationships, and response history, while recommending better app-level logic as an incomplete near-term defense. The essay is a 2017 practitioner proposal, not evidence that centralized algorithmic filtering improves user welfare or can safely infer importance.

## Key Claims
- Notification badges and alerts became an operating-system response to apps that could act continuously beyond their isolated interfaces, but developers then used that shared channel to reclaim attention.
- Finance, fear, and fear of missing out can make notifications effective for an individual sender while encouraging collectively noisy and manipulative competition.
- Notifications constitute a shared digital commons because every app's sending behavior affects the usefulness of the home screen, notification tray, and other out-of-app surfaces.
- App-by-app optimization cannot fully solve the aggregate problem: even a thoughtful message competes within a stream containing every sender's alerts.
- A centralized notification layer could rank or suppress alerts using location, schedule, past response, similar users' behavior, urgency, relevance, and relationships.
- Platform-level filtering could reverse developer incentives by making frequent ignored alerts less visible and rewarding actionable, well-timed messages with access to scarce attention.
- Until platforms supply such governance, richer application-level decision logic may help preserve users' willingness to receive alerts but cannot remove the commons-level incentive conflict.

## Key Quotes
> "The surplus of notifications - and a few bad actors - spoiled the channel for everyone." - Belsky's diagnosis of aggregate degradation.

> "A tragedy of the commons is not solved until self-interests are flipped or rules are put in place." - argument for platform governance rather than voluntary restraint alone.

## Connections
- [[ScottBelsky]] - author proposing centralized notification governance and contextual ranking.
- [[NotificationDesign]] - the essay adds a shared-resource and platform-incentive model to the timing, relevance, and interruption problem.
- [[AttentionManagement]] - application senders compete for a finite supply of user attention.
- [[AttentionEconomy]] - engagement gains for individual apps can impose aggregate interruption costs on users and other senders.
- [[EngagementIncentiveConflict]] - local optimization for opens and re-engagement can degrade the shared notification channel.
- [[Apple]] - iOS owner positioned to govern notification delivery with cross-application context.
- [[Google]] - Android owner positioned to govern notification delivery with cross-application context.
- [[Slack]] - cited as an example of unusually sophisticated app-level notification decision logic.

## Contradictions
- The proposal complements existing [[NotificationDesign]] sources that favor platform context, targeted delivery, batching, and cadence controls, but it shifts discretion from users and individual apps toward a centralized algorithm whose objectives and accountability are unspecified.
- Collaborative filtering from “people like you” can reproduce majority preferences, suppress minority needs, expose sensitive behavioral patterns, and mistake non-response for low value. Location, schedules, relationships, and response history also create privacy, consent, security, transparency, and contestability requirements absent from the essay.
- The article supplies no experiment, outcome measure, ranking policy, urgency definition, exception path, or evidence that operating-system filtering would improve welfare. Its examples and platform capabilities are historical 2017 observations.
- All six local images were opened. Five are decorative or duplicate bell and app-badge illustrations. The remaining image is a materially relevant Slack notification-logic diagram, but the saved file is only a 60-by-57-pixel thumbnail; its labels and flows cannot be interpreted reliably, and the publisher original was inaccessible. No image was retained or used as independent evidence.
