# Metrics Dictionary
Version 1 | 2026-10-28

| Metric | Definition | Key caveat |
| --- | --- | --- |
| Followers | Accounts following a specific channel at snapshot time | Cannot add across channels to yield unique people |
| Net followers | End followers - begin followers over comparable window | Acquisition and churn both matter |
| Reach | Unique accounts exposed where native platform explicitly reports it | Not cross-platform deduplicated |
| Impressions | Total exposures, including repeat ones if platform defines so | Different from unique reach |
| Views | Platform-specific qualified view count | Threshold/definition can change |
| Shown in feed | YouTube Shorts exposures in Shorts feed where reported | Not identical to impressions/views |
| Chose to view | YouTube Shorts viewers choosing to watch vs swipe, per native reporting | Use native denominator |
| Average view duration | Watch time per native view/engaged view as defined | Recording differences can invalidate comparison |
| Average percentage viewed | Watch fraction per native denominator | May exceed 100% for loops; not automatically desirable |
| Completion rate | Share reaching end if the platform explicitly exposes it or defensible derivation exists | May be unavailable |
| Shares/sends | Native measured repost/send events | Separate private sends when reported; don't invent reach |
| Saves | Native measured bookmarks/saves | Best interpreted relative to reach and content type |
| Comments | Native comment actions | Quality and sentiment matter; avoid empty bait |
| Likes | Native likes | Does not necessarily reflect lasting trust |
| Follows per view | Net new follows attributed to same post/period if available, divided by compatible native views | If attribution impossible label approximate |
| Returning viewers | Native reported returning audience | Platform-specific and often window-dependent |
| Revenue | Earned/recognized cash or contractual amount, labeled clearly | Separate gross/net, accrued/paid |
| Variable content cost | Tools, editing, VO, contractor and incremental production resources | Record human hours too |
| Property contribution | Net attributable revenue minus attributable operating costs | Account for allocation caveats |

## Required metadata
Observation ID, property/channel/content ID, platform, metric name, value, unit, numerator/denominator if rate, reporting window, pulled_at, source/export, attribution limits, whether estimated, whether organic or paid.

## Review logic
Choose ONE primary metric for an experiment, with secondary satisfaction/quality guardrails. Match topic, duration, platform and audience as well as possible. Do not claim externally available platform data proves exact algorithmic preferences.
