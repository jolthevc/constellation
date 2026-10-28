# Engagement Testing, Retention Diagnostics, and Learning Loop
Status: initial manual phase; no predictive algorithm model is claimed.
Last reviewed: 2026-10-28

## Why metrics matter
Aim to understand the full funnel: eligible exposure -> chose to watch -> held attention -> satisfied outcome -> authentic action -> repeat relationship. High raw views may be the wrong north star if audience is irrelevant, payoff is weak or follow/return intent is absent.

## Per-content required fields
Property ID, account/channel ID, content ID, platform/surface, format IDs, hook IDs, declared viewer benefit, creative hypothesis, publication time, duration, reach/impressions if available, views, measured retention, follows, shares/sends, saves, comments, return signals, production cost, and source/export timestamp. Preserve exact platform metric definitions; never calculate rates with mismatched denominators.

## Platform notes with primary sources
- **YouTube Shorts:** compare shown in feed; chose to view vs swiped away; engaged views where available; average view duration and average percentage viewed. Separate distribution problem (not shown) from weak hook (shown but swiped). https://support.google.com/youtube/answer/12942217?co=YOUTUBE._YTVideoType%3Dshorts&hl=en
- **YouTube long-form:** title/thumbnail CTR sets expectation, 30-second intro retention and later dips/spikes diagnose experience; compare videos of similar duration. Rewatch spikes can indicate confusion, not solely delight. https://support.google.com/youtube/answer/9314415?hl=en
- **Instagram Reels:** track average watch time, likes per reach and sends per reach; interpret separately for existing versus new viewers when data permits. Instagram surface rankings vary, and exact signal weights are not public. Source on Mosseri's Jan 2025 comments: https://www.socialmediatoday.com/news/instagram-shares-algorithm-insights-2025/738034/
- **TikTok:** viewer interactions, watch/full-watch/skip and video metadata affect personalized recommendations; avoid treating one universal “magic completion threshold” as official. https://newsroom.tiktok.com/how-tiktok-recommends-videos-for-you?lang=en

## Experimental design
1. Record a concrete hypothesis: “This audience will choose to view more often if the opening shows the outcome before the explanation.”
2. Choose a primary metric linked to the change. Hook test -> chose-to-view/first-seconds retention; progress test -> retention curve and completion; payoff test -> meaningful comments/saves/shares/follow behavior (not direct satisfaction proof).
3. Produce plausible variants without compromising brand identity or substance. When testing opening hooks, keep subsequent content comparable.
4. If same-video randomized distribution is unavailable, treat separately published posts as **observational comparisons**, not clean A/B tests. Control for topic, duration, upload time, audience and platform when possible.
5. Measure at consistent post-publication windows; note audience sizes, paid reach, trend externalities and missing data.
6. Read qualitative audience feedback. “This was clickbait” can override apparent short-term lift.
7. Keep a change log. Adopt patterns after repeated evidence across content, not one outlier. Retire ineffective or low-trust patterns.

## Diagnosing the funnel
| Observation | Candidate explanation | Next test |
| --- | --- | --- |
| High exposure, low chose-to-view | Weak or unclear opening, poor fit for surfaced audience | Test first frame, opening line, on-screen premise |
| Strong start, sharp 3-8s fall | Delay before substance, muddy setup, bait gap | Show proof earlier, reduce setup |
| Good middle, weak ending | Unsatisfying result or forced CTA | Strengthen payoff; test no-CTA ending |
| High retention, low shares | Content enjoyable but little social expression or utility | Test a more specific insight or relatable angle |
| High views, low follows | One-off curiosity, weak recurring property proposition | Strengthen series, identity and next-visit promise |
| High rewatches, mixed comments | Delight OR confusion | Inspect exact timestamp and comments |
| High saves, modest shares | Practical reference rather than social conversation | Preserve useful content; don't “fix” it by forcing shares |

## Reporting cadence
Manual pilot: per-post review at 48-72 hours and again at 7 days; weekly comparison across similar posts; monthly review of creative signatures, audience psychology hypotheses and production economics. These are workflow defaults, not platform-confirmed ranking windows.

## Guardrails
No bought engagement, bots, manufactured comments, coordinated inauthentic amplification, forced subscriptions, misleading CTA rewards, invented user anecdotes or deceptive synthetic footage. Respect platform changes and revise guidance quarterly. Link experiments back to property bibles and common hook / format libraries without overwriting historical evidence.
