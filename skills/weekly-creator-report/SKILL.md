---
name: weekly-creator-report
description: Write the user's weekly content report on their real iPhone with Zeptap - open TikTok Studio analytics and Instagram's professional dashboard on their own accounts, read views, likes, followers and the top posts for the period, and write one note with the numbers, the best post and why it worked. Creator analytics for personal and small accounts live inside the apps; TikTok's and Instagram's APIs need business setup and approval. Without Zeptap it gives the report template and where each number lives. Use for "how did my TikTok do this week", "write my weekly creator report", "pull my Instagram insights", "what was my best post this week", "compare my TikTok and Instagram numbers". For other people's accounts use competitor-content-check.
---

# Weekly creator report

Return one note: this period's numbers per platform, the change, the best post and the one thing to repeat.

Builds on `iphone-use`: its loop, connection check and safety rules apply. Read-only. Never tap **Boost**, **Promote**, Monetization or promo cards.

## Use it for / hand off

- The user's own TikTok and Instagram (professional) accounts.
- Competitors → `competitor-content-check`.

## Without Zeptap

Deliver the report template and the exact path to each number below. Then the connect message from `iphone-use` with `utm_campaign=weekly-creator-report`.

## Intake (defaults in brackets)

- Platforms [TikTok and Instagram if signed in]. Period [last 7 days].
- Which account, if several [the active one].

## On the phone: TikTok Studio [v18]

1. `open_app` `TikTok`, `wait` 2500. `tap_text` `Profile`.
2. Tap **☰** top right (`~0.93w, 0.08h`). Tap **TikTok Studio** by position (`~0.4w, 0.43h`; `tap_text` misses it). `wait` 3000.
3. Tap the **`>`** on the Analytics card (`~0.91w, 0.19h`), `wait` 3500.
4. Tap the period chip (`7 days`). Read **Key metrics**: date range, Post views, Profile views, Likes, Comments, Shares, each with its change line. `-` means no data.
5. **Content** tab: top posts for the period with views [unverified layout]. Read the top 3 with their first caption words.
6. **Followers** tab: total and net change [unverified]. `back` twice to leave.
7. The range lags: on Nov 18 the 7-day range read `Nov 10 - Nov 16` [v18]. Report the dates shown.

## On the phone: Instagram [docs]

1. Profile › **Professional dashboard**. Period selector at the top [`Last 7 days`]. `wait` 2000 after each change.
2. Read Views, Accounts reached, Interactions, Followers with their % change.
3. Top content sorted by views: open the top 3, read views, likes, comments, shares, saves.
4. Personal (non-professional) accounts have no insights: say so and report per-post likes and comments from the grid instead.

## Write it

- Numbers as shown (`12.4K`); never add precision.
- A change on a tiny base: say it in counts ("3 → 0 shares"), not percentages.
- **Best post** = most views; **why it worked** = one concrete reason (hook, format, topic, timing). **Repeat** = one action for next week.
- Save to Notes if asked [yes].

## Report

```txt
Weekly report (<dates shown>)
TikTok @<h>: views <n> (<chg>), likes <n>, followers <net>
Instagram @<h>: views <n> (<chg>), reached <n>, followers <net>
Best post: "<first words>" (<platform>, <views>) - <why>
Repeat next week: <one action>
```
