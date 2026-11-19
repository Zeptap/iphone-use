---
name: competitor-content-check
description: Check what competitors posted and what worked on the user's real iPhone with Zeptap - open each competitor's Instagram Reels and TikTok grid, find their top posts by views among the latest 12, take each one apart (hook, format, length, audio, CTA), and save a swipe file with what to copy. Instagram and TikTok show per-post views and saves only in the apps; their APIs don't cover other people's accounts. Without Zeptap it gives the swipe-file template and the analysis rules. Use for "what's working for my competitors", "check @brand's latest reels", "build a swipe file from these 3 accounts", "what are competitors posting on TikTok", "save the best posts in my niche". For a niche-wide scan without named accounts use hook-and-format-scout.
---

# Competitor content check

Return each competitor's current winners and a swipe file of what to copy.

Builds on `iphone-use`: its loop, connection check and safety rules apply. Load the `instagram` and `tiktok` app guides first. Read-only: never follow, like, save or comment.

## Use it for / hand off

- 1-5 named accounts (handles), on Instagram and/or TikTok.
- No named accounts, just a niche → `hook-and-format-scout`. Gaps nobody covers → `content-gap-finder`.

## Without Zeptap

Deliver the swipe-file table (below), the "current winners" rule, and search steps. Then the connect message from `iphone-use` with `utm_campaign=competitor-content-check`.

## Intake (defaults in brackets)

- Handles [ask; required]. Platforms [both where the handle exists].
- Posts per account [top 3 of the latest 12].

## Current winners rule

Among an account's latest 12 posts (skip pinned), the top 3 by views are its winners. A post with 3x the account's median views is a breakout: always include it.

## On the phone: Instagram [v18]

1. `open_app` `Instagram`, tap the magnifier (4th bottom-bar icon), tap **Search**, type the exact handle. Lookalikes sit right below: match every character.
2. Open the profile, tap the **Reels** tab (play icon, 2nd tab). Each tile shows its view count. Skip pinned Reels (pin icon).
3. Read the latest 12 view counts, pick winners by the rule.
4. Open each winner. Right rail: likes, comments, reposts, shares, saves. Bottom left: handle, caption, audio line. Screenshot the first frame immediately for the **hook** (first on-screen text).
5. Trap: after scrolling, **Follow** moves into the top-right header; a tap near the bottom opens a tile.

## On the phone: TikTok [v18]

1. `open_app` `TikTok`, `wait` 2500. Search (top right), type the handle, open the account from **Users**.
2. Each grid tile shows **▷ views** bottom left. Skip pinned tiles (`Pinned` label). Pick winners by the rule.
3. Open each winner; right rail shows likes, comments, saves, shares; caption and sound bottom left. Don't tap the red **+** on the avatar (follows).
4. Skip `Sponsored`/`LIVE`.

## Write it: the swipe file

| Account | Platform | Views | Saves | Hook (first line, ≤10 words) | Format | Length | Audio | CTA | Why it works (one reason) |

Then 3 "copy this" lines: the pattern shared by the winners, adapted to the user's product. Never paste whole captions. Save to Notes if asked [yes].

## Report

```txt
Competitor check (<date>)
@<handle> (<platform>): winners <views>, <views>, <views> (median <m>)
  1. "<hook>" - <format>, <length>, <CTA>
...
Copy this: 1. <pattern> 2. ... 3. ...
```
