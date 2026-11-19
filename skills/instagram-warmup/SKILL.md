---
name: instagram-warmup
description: Warm up a new or dormant Instagram account on the user's real iPhone with Zeptap - one 10-20 minute session a day in the real app that watches niche Reels first, then adds likes, follows, saves and comments in a slow, varied ramp, keeps a log on the phone, checks a test at the end of each phase, and tells the user when to post the first Reel and whether the account is healthy. Instagram scores new accounts on how they behave in the app; browser scripts and schedulers send weaker signals than a real phone. Without Zeptap it gives the setup questions, today's plan and the phase checklist. Use for "warm up my new Instagram account", "do today's Instagram warm-up", "is my account ready to post", "my new account gets no views", "day 4 of my Instagram warm-up". For TikTok use tiktok-warmup; for established accounts use niche-engagement.
---

# Instagram warm-up

Make a fresh account one Instagram trusts and shows to the right niche, in about 7 days, then keep it healthy.

Builds on `iphone-use`: its loop, connection check and safety rules apply. Load the `instagram` app guide first. Playbook as of 2026-11-19: trust the phase tests over the calendar.

## Why it works (keep this in mind every session)

1. Instagram is learning three things: is this a real person, what niche are they in, who should see their posts.
2. Watching comes before acting. Watch time in one niche is the strongest early signal.
3. Actions ramp slowly and never repeat the same numbers two days running.
4. Each phase ends on a test, not a date.

## Start here (every time the skill runs)

1. Open Notes and search for `Warm-up log @`.
2. **No log for this account** → run **Setup**, create the log, then run today's session from Phase 1, phase day 1.
3. **Log found** → run **Pre-flight**, then today's session for the phase in the header.
4. **Account already established** (see Setup) → stop and use `niche-engagement`.

## The log (the skill's memory)

A note titled `Warm-up log @<handle>`. Header lines, kept current:

```txt
handle: @<handle> | class: new|dormant | niche: <one line>
keywords: <5-10> | creators: <3-5 handles> | skip: <anti-niche>
geo: <country, language> | vpn: none | <app, region> | location services: on|off
phase: P<n> | phase day: <n> | started: <date> | total follows: <n>
check due: <date: what>   (e.g. 2026-11-28: read views of Reel 1)
posts: <date, views at 48 h>
```

Then one line per session:

```txt
2026-11-19 | P1 d1 | 14 min, 22 reels, 0 likes, 0 follows, 3 visits | niche 4/10 | flags: none
```

**Phase day** counts days inside the current phase; it resets when the phase changes and repeats when a day is repeated. All tables below use phase days.

## Setup (first run only)

Ask in one message, with defaults in brackets. Don't start until the account and niche are confirmed.

1. **Account** [the one signed in]: the exact `@handle`.
2. **Niche**: one line ("home workouts for busy moms"), **5-10 keywords**, **3-5 creators** the account should resemble, **topics to skip** [none].
3. **Target country and language** [the phone's own].
4. **VPN**: "Do you use a VPN to target that country?" If yes: which app and which region. Rule: the same region on for **every** session from day 1, or never. If the VPN country differs from where the phone is, offer (needs a yes) to set Settings › Privacy & Security › Location Services › Instagram to `Never` on day 1 and leave it, so GPS doesn't contradict the VPN.
5. **Posts**: will 3-5 original Reels be ready by about day 7? [ask; start preparing now].

**Check the account** (read-only) and set `class`:

| Check | Where | Result |
|---|---|---|
| Posts, followers, following | Profile header | 100+ posts or steady reach → **established**: use `niche-engagement`, stop |
| Date joined | Own profile › `≡` › `About this account` [unverified path] | Under 14 days → **new**: start P1. Older, quiet 30+ days → **dormant**: start P2, phase day 1 |
| Account type | `Professional dashboard` on profile = professional | Suggest **Creator** (Settings › Account type and tools); a yes is needed, do it on day 1 |
| Account status | Settings › `Account status` | Any restriction → stop and report; a warm-up won't fix it |

**Profile check**: photo, real-looking name, short bio, a username without long number strings, **no link yet**. Fix gaps on day 1 only, with a yes. After that the profile stays frozen until P2 phase day 3 (link).

## Pre-flight (every session, in order)

Any failure stops the session and is logged.

1. **Log**: a session already today → stop (one a day). Last session 4+ days ago → repeat the current phase day instead of advancing. A `check due` today → do it first (see P3).
2. **Time zone** matches the target country (Settings › General › Date & Time). Sessions at about the same hour each day, in the target's daytime or evening.
3. **VPN** (if `vpn` is set): open the VPN app, confirm **connected, same region as day 1**. Otherwise stop and ask. Never toggle it while Instagram is open.
4. **Network**: same type as before (Wi-Fi or cellular); a change gets logged.
5. **Account**: open Instagram, read the profile `@handle`. Wrong → switch (long-press the profile tab, pick it); not on the phone → stop.
6. **Warnings**: notifications and any banner free of `Try Again Later`, `We restrict certain activity`, `Confirm it's you`. One found → stop, quote it, ask the user.
7. **Plan**: one line, one yes: "P2 day 2: 22 reels, 4 likes, 5 follows, 1 save, 1 comment (I'll show it to you)".

## The session (all phases)

Notifications → messages (reply to real DMs only with the user's words or an approved draft) → 1-3 stories → feed 1-2 min → search a keyword, open 2-5 profiles → **Reels**, with the day's actions spread between Reels → notifications again → home. Cap: 20 minutes. Popups (`Turn on notifications`, `Add to Home`, `Not Now` prompts): tap `Not Now`.

**Measuring niche share** (used by the tests): at the end of the session, open the Reels tab fresh and count how many of the next 10 Reels are in the niche (topic, keyword or creator type). Log it as `niche x/10`.

## Phases

| Phase | Goal | Exit test, checked at the end of each session |
|---|---|---|
| **P1 Lurk** | A real person in one niche | Phase day 2 or later, niche ≥ 5/10, no flags |
| **P2 Train** | Teach the niche with light actions | Phase day 3 or later, niche ≥ 7/10, follows going through cleanly, no flags in P2 |
| **P3 First post** | Prove reach | First Reel's views at 48 h read |
| **P4 Healthy** | Keep trust while posting | Ongoing |

A test that fails → repeat the same phase day tomorrow and say why. Never skip a phase.

### P1 Lurk

- Watch 18-27 Reels; niche ones to the end, off-niche skipped within 2 s; 2-5 profile visits, no follows.
- Phase day 2 on: 2-4 likes on niche Reels.
- No follows, saves, comments or posts.
- **Niche won't stick** (under 5/10 after phase day 4): search the keywords more, visit the listed creators, long-press off-niche Reels › `Not interested`; tell the user and suggest sharper keywords.

### P2 Train

On phase day 1, tell the user: "Your first Reel is about 3 days away. Have it ready: original, in your niche."

| Phase day | Likes | Follows | Extras |
|---|---|---|---|
| 1 | 3-5 | 2-4, after searching a keyword | like 2-3 good comments under niche Reels |
| 2 | 3-5 | 4-6 | maybe 1 save; 1 real comment (approved) |
| 3 | 4-6 | 5-7 | 1-2 comments; add the link in bio (approved) |
| 4+ | 4-6 | 6-8 | optional Story (a real photo) |

About 30 follows by the end of P2.

### P3 First post

As soon as P2's test passes, **say it without being asked**:

> Phase 2 is done: your Reels feed is 7 in 10 <niche>, follows go through cleanly, no warnings in <n> sessions. Time for your first Reel. Pick one that fits the niche and I'll post it in the app, then read the views in 48 hours.

Post with `instagram-poster` (Reel, AI label on if AI-made, 3-5 niche hashtags). Set `check due: <+2 days>: read views of Reel 1`. Keep daily sessions at P4 numbers.

When the check is due: profile › the Reel › view count. Log it, then:

| Views at 48 h | Verdict | Next |
|---|---|---|
| 500+ | **Healthy** | Tell the user; go to P4 |
| 200-499 | Unclear | 2 more Reels over 3 days, re-check each |
| Under 200 on 3 Reels | Unhealthy | Recovery |

**User wants to post before P2 passes**: say what the test is still missing and the risk (weak first reach), then post if they insist. It's their account.

### P4 Healthy

Daily: 15-30 Reels, 2-6 likes, 1-4 profile visits. Follows: none on half the days, 1-2 on some, rarely 3-4; at most 6-8 a week, 0-2 a week past 60-70 total. Now and then a save, 1-3 stories, a comment thread read. Skip a day about once a week. 3-5 Reels a week from the user.

## Recovery

Rest 48 hours. Then 2 days of P1 sessions. Then 3 Reels shot with the Instagram camera on the phone (not uploads). Re-check. Still under 200 → report with the log. Never create a new account or abandon this one without the user.

## Rules

- **Vary everything**: random numbers inside each range, never yesterday's.
- **Never two follows in a row**; at most 2-3 from one suggested panel; mix search, suggested and Reels.
- **Ads**: never like, save, comment on or follow from `Sponsored`.
- **Comments**: specific to the post, 1-2 sentences, no emoji-only, no links, no promotion; each approved.
- Same phone, network type, time zone and VPN rule throughout. Never log out and in.

## Red flags

| Sign | Do |
|---|---|
| `Requested` on a public account, follow button stuck, suggested panel vanishes after a follow | No more follows today; watching and likes only. Two days running → hold the phase 3 more days |
| `Try Again Later`, `We limit how often`, `Confirm it's you`, `unusual activity` | End the session now; verification is the user's. No session for 24-48 h |
| Any account warning | Stop, quote it, ask the user |

## Approval

One yes for the day's plan covers watching, likes, follows and saves. Comments, profile edits, the link and every post need their own yes.

## Without Zeptap

Run the setup questions, then give today's exact plan, the session flow and the phase test, then the connect message from `iphone-use` with `utm_campaign=instagram-warmup`. The wall: the warm-up only counts in the real app on the account's own phone.

## On the phone [v18 2026-11-19]

- Search: magnifier tab (`~0.7w, 0.94h`) → field → keyword → `enter`. Follow: blue button on the profile.
- Reels tab `~0.3w, 0.94h`; `flick` up from `0.70h` to advance (`settle_ms` 800). Like: heart on the right rail. Save: bookmark.
- Stories: tap a ring on Home; tap the right edge to advance.

## Report

```txt
Instagram warm-up @<handle> - P<n> day <d> (<date>)
Did: <min> min, <reels> reels, <likes> likes, <follows> follows, <visits> visits, <saves> saves, <comments> comments
Niche: <x>/10   Flags: <none | detail>
Test: <passed -> P<n+1> | not yet: <what's missing>>
Next: <tomorrow's plan> | <"time for your first Reel"> | <check due date>
```
