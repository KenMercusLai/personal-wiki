---
title: "A/A Testing: How I increased conversions 300% by doing absolutely nothing"
type: source
tags: [experimentation, statistics, conversion, email-marketing]
date: 2015-02-12
source_file: "/mnt/ken_personal_wiki/Articles/David Kadavy - A-A Testing How I increased conversions 300 percent by doing absolutely nothing.md"
---

## Summary
[[DavidKadavy]] reports running identical-variant email tests through [[Mailchimp]] across 56 campaigns and more than 750,000 sent emails over eight months. The resulting apparent lifts—including a 300% increase in clicks—illustrate how sampling variation, low baseline rates, inadequate sample sizes, false positives, and relative percentages can create persuasive but unactionable results. He presents [[AATesting]] as a calibration exercise and argues that small organizations should test only consequential questions they can power adequately, while weighing experimentation against product vision and other uses of attention.

## Key Claims
- An [[AATesting|A/A test]] sends identical variants through the normal experiment system so any observed difference exposes random variation or flaws in the testing process.
- Across 56 email campaigns and more than 750,000 total sends, identical variants produced apparent changes including 9% more opens, 20% more clicks, 51% fewer unsubscribes, and 300% more clicks.
- A nominally significant result can still be misleading when the baseline rate, sample size, statistical power, false-positive rate, and repeated opportunities to find a result are not considered together.
- With a 2.2% click baseline and 14,517 recipients per branch, the cited calculator could only begin detecting a change of about 0.49 percentage points, or 22% relative, at 80% power and a 5% significance level.
- Click-through rate is an intermediate outcome: fewer but better-qualified clicks can create more business value than a higher raw click count.
- Testing is worthwhile when the question is important, the likely decision value exceeds the effort, the sample is large enough, and the operator understands the method.
- For a resource-constrained business, experiment design and analysis compete with product creation, iteration, and strategic judgment rather than replacing them.

## Key Quotes
> “Try running A/A tests to get a feel for how misleading ‘results’ can be.” — on calibrating trust in experiment output

## Connections
- [[DavidKadavy]] - author and bootstrapped solopreneur who ran the eight-month email experiment.
- [[AATesting]] - identical-variant control used to reveal sampling noise and calibrate an experiment pipeline.
- [[ConversionRateOptimization]] - practice qualified by the article's warnings about power, false positives, intermediate metrics, and opportunity cost.
- [[StatisticalModelThinking]] - framework for treating measured differences as observations containing uncertainty rather than self-explanatory facts.
- [[UserBehaviorDebugging]] - complementary method-selection approach that conditions A/B testing on adequate traffic and a clear measurable outcome.
- [[ProductMetricLadder]] - distinguishes clicks from warmer prospects, conversions, and business value farther down the funnel.
- [[Mailchimp]] - email platform through which the identical variants were sent.

## Contradictions
- Qualifies [[a-first-peek-behind-the-scenes-of-hillary-clintons-technology-operation]], which reports large conversion lifts from campaign A/B tests: a large relative lift and a conventional confidence threshold are not sufficient without sample, baseline, power, and post-rollout evidence.
- Qualifies [[whyd-you-do-that-an-engineers-guide-to-debugging-user-behavior]], which recommends A/B tests for clear measurable outcomes: metric clarity must be paired with adequate power, calibration, and a decision important enough to justify the work.
