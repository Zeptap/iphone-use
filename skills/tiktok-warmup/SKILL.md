---
name: tiktok-warmup
description: Warm up a new or dormant TikTok account on the user's real iPhone with Zeptap - short daily sessions in the real app that watch niche videos to the end first, then add search, likes, comment likes, follows and a few real comments, keep a log on the phone, check a test at the end of each phase, and tell the user when to post the first video and whether it passed the 700-view health test. TikTok decides who a new account is from how it behaves in the app, and posts made in the app outperform schedulers. Without Zeptap it gives the setup questions, today's plan and the phase checklist. Use for "warm up my new TikTok", "do today's TikTok warm-up", "is my TikTok ready to post", "my TikTok gets 0 views", "train my For You page for my niche". For Instagram use instagram-warmup; for established accounts use niche-engagement.
---

# TikTok warm-up

Teach TikTok who this account is and which niche it belongs to in about 5 days, prove it with the first posts, then keep it healthy.

Builds on `iphone-use`: its loop, connection check and safety rules apply. Load the `tiktok` app guide first. Playbook as of 2026-11-19: trust the phase tests over the calendar.

## Why it works (keep this in mind every session)

1. TikTok learns who the account is, what it should see, and which audience its posts go to. Without a warm-up it guesses, and guessing is bad.
2. Watch time is the signal: niche videos to the end, everything else skipped fast.
3. Posting before the For You page is trained wastes the first posts.
4. Each phase ends on a test, not a date.

## Start here (every time the skill runs)

1. Open Notes and search for `TikTok warm-up @`.
2. **No log for this account** → run **Setup**, create the log, then run today's session from Phase 1, phase day 1.
3. **Log found** → run **Pre-flight**, then today's session for the phase in the header.
4. **Account already established** (see Setup) → stop and use `niche-engagement`.

## The log (the skill's memory)

A note titled `TikTok warm-up @<handle>`. Header lines, kept current:

```txt
handle: @<handle> | class: new|weak|dormant | niche: <one line>
keywords: <5-10> | creators: <3-5 handles> | skip: <anti-niche>
geo: <country, language> | vpn: none | <app, region> | location services: on|off | sim: <country or none>
phase: P<n> | phase day: <n> | started: <date> | total follows: <n>
check due: <date: what>
posts: <date, views at 48 h>
```

One line per session:

```txt
2026-11-19 am | P1 d1 | 8 min, 31 videos, 4 likes, 0 follows | FYP niche 3/10 | flags: none
```

**Phase day** counts days inside the current phase; it resets on a phase change and repeats when a day is repeated.

## Setup (first run only)

Ask in one message, with defaults in brackets. Don't start until the account and niche are confirmed.

1. **Account** [the one signed in]: the exact `@handle`.
2. **Niche**: one line, **5-10 keywords**, **3-5 creators** the account should resemble, **topics to skip** [none].
3. **Target country and language** [the phone's own].
4. **VPN**: "Do you use a VPN to target that country?" If yes: which app and which region. Rule: the same region on for **every** session from day 1, or never. If the VPN country differs from where the phone is, offer (needs a yes) to set Settings › Privacy & Security › Location Services › TikTok to `Never` on day 1. TikTok also reads the SIM's country: a SIM from a different country than the target is a mismatch to report before day 1 (the agent can't fix it).
5. **Posts**: will 6 original videos be ready by about day 5? [ask; start preparing now].

**Check the account** (read-only) and set `class`:

| Check | Where | Result |
|---|---|---|
| Posts, following, followers, likes | Profile header | Steady views over 1K → **established**: use `niche-engagement`, stop |
| Old posts all under 100 views | Profile grid ▷ counts | **weak**: full warm-up, then Recovery-style first posts |
| No activity 30+ days, older posts | Profile grid dates | **dormant**: start P2, phase day 1 |
| Otherwise (0-5 posts, under 50 following) | | **new**: start P1 |
| Account type | Settings and privacy › Account | Stay **personal/creator**; business accounts lose most trending sounds |
| Account status | Settings and privacy › Account › `Account status` | Violations → stop and report |
| App language | Settings and privacy › Language | Should match the target language |

**Profile check**: photo, real-looking name, short bio, username without long number strings, **no link** during the warm-up. Fix gaps on day 1 only, with a yes. After that the profile stays frozen.

## Pre-flight (every session, in order)

Any failure stops the session and is logged.

1. **Log**: P1-P2 allow 2 sessions a day (4+ hours apart), later phases 1; over the limit → stop. Last session 4+ days ago → repeat the current phase day. A `check due` today → do it first (see P3).
2. **Time zone** matches the target country (Settings › General › Date & Time). Sessions at about the same hours each day.
3. **VPN** (if `vpn` is set): open the VPN app, confirm **connected, same region as day 1**. Otherwise stop and ask. Never toggle it while TikTok is open.
4. **Network**: same type as before; a change gets logged.
5. **Account**: open TikTok › Profile › read the `@handle`. Wrong → tap the name at the top, switch; not on the phone → stop.
6. **Warnings**: Inbox › activity and any banner free of `Too many attempts`, `You're following too fast`, violation notices. One found → stop, quote it, ask the user.
7. **Plan**: one line, one yes: "P2 day 1, morning: 10 min, 8 likes, 4 follows, like 3 comments, no posting".

## The session (all phases)

5-12 minutes. For You first, then search (from P2), then Profile › Inbox › home. Popups (`Sync contacts`, `Turn on notifications`): decline. Never open LIVE.

**Measuring niche share** (used by the tests): at the end of the session, swipe the next 10 For You videos and count those in the niche. Log `FYP niche x/10`.

## Phases

| Phase | Goal | Exit test, checked at the end of each session |
|---|---|---|
| **P1 Lurk** | A real person in one niche | Phase day 2 or later, 4+ sessions, FYP niche ≥ 5/10, no flags |
| **P2 Train** | Sharpen the niche, light social signals | Phase day 3 or later, FYP niche ≥ 7/10, follows going through cleanly, no flags in P2 |
| **P3 First post** | Health test | First video's views at 48 h read |
| **P4 Grow** | Build a posting history | 6 posts done, views checked |

A failed test → repeat the same phase day and say why. Never skip a phase.

### P1 Lurk (2 sessions a day)

- For You: niche videos watched **to the end** (rewatch one now and then); off-niche swiped within 2 s; long-press › `Not interested` on 1-2 clearly off-niche ones per session.
- Phase day 1: 2-5 likes on niche videos. Phase day 2: 3-8 likes, 2-4 follows of niche creators.
- No posts, no comments.
- **Niche won't stick** (under 5/10 after phase day 4): search the keywords, open the listed creators and watch 3 of their videos each; tell the user and suggest sharper keywords.

### P2 Train (2 sessions a day)

On phase day 1, tell the user: "Your first post is about 2 days away. Have it ready: original, in your niche, made for TikTok."

- Search 2-3 keywords per session, rotate them; filter (sliders icon) › date posted › last 3 months; watch the results like a feed.
- Likes 5-10, follows 3-6 a day (never two in a row).
- Open comments on 2-3 niche videos, read, **like 2-4 comments**.
- From phase day 2: 1-2 real comments a day (each approved).

### P3 First post

As soon as P2's test passes, **say it without being asked**:

> Phase 2 is done: your For You page is 8 in 10 <niche>, follows go through cleanly, no warnings. Time for your first post. Easiest strong start: a picture-and-text slideshow or a short clip in a format that's working in your niche (I can find one with hook-and-format-scout). I'll post it in the app and read the views in 48 hours.

Post with `tiktok-uploader` (original content, AI label on if AI-made). Set `check due: <+2 days>: read views of post 1`. Keep one session a day.

When the check is due: Profile › the video's ▷ count. Log it, then:

| Views at 48 h | Verdict | Next |
|---|---|---|
| 700+ | **Healthy** | Tell the user; go to P4 |
| 300-699 | Unclear | 2 more posts within 2 days, re-check each |
| Under 300 | Weak | Recovery |

**User wants to post before P2 passes**: say what the test is still missing and the risk, then post if they insist.

### P4 Grow

- 6 posts at about 2 a day, made or finished in the app; read each one's views at 48 h.
- One 10-20 minute session a day: For You in the niche, 5-10 likes, 0-3 follows, a comment now and then. Skip a day about once a week.
- After 6 posts: all under 300-500 → Recovery. Otherwise tell the user it's healthy and hand over to `hook-and-format-scout` for what to make next.

## Recovery

Rest 48 hours. Then 2 days of P2 sessions. Then 3 videos shot with the TikTok camera on the phone (not uploads). Still weak → report with the log. Never create a new account or abandon this one without the user.

## Rules

- **Vary everything**: random numbers inside each range, never yesterday's.
- **Never two follows in a row**; mix search, For You and a creator's followers.
- **Ads and LIVE**: never like, follow or comment from `Sponsored` or LIVE.
- **Comments**: specific to the video, 1-2 sentences, no emoji-only, no links, no promotion; each approved.
- **Original content only**; never repost someone else's video.
- Same phone, network type, time zone and VPN rule throughout. Never log out and in.

## Red flags

| Sign | Do |
|---|---|
| A follow fails or reverts, `You're following too fast` | No more follows today. Two days running → hold the phase 3 more days |
| `Too many attempts`, `Try again later`, a verification puzzle, a suspension notice | End now; verification is the user's. Rest 24-48 h |
| A post `Under review`, or 0 views after 2 h | Log it; no new post until the user decides |

## Approval

One yes for the day's plan covers watching, likes, comment likes and follows. Comments, profile edits and every post need their own yes.

## Without Zeptap

Run the setup questions, then give today's exact plan, the session flow and the phase test, then the connect message from `iphone-use` with `utm_campaign=tiktok-warmup`. The wall: the warm-up only counts in the real app on the account's own phone.

## On the phone [v18 2026-11-19]

- For You: Home tab; `flick` up to advance (`settle_ms` 800; the feed never stops moving). Like: heart on the right rail. Comments: speech bubble; comment likes are the small hearts beside each comment.
- Search: magnifier top right (`~0.93w, 0.08h`); the sliders icon on results opens filters.
- Follow from the creator's profile, not the red `+` on the rail.
- `Not interested`: long-press the video.

## Report

```txt
TikTok warm-up @<handle> - P<n> day <d>, <am|pm> (<date>)
Did: <min> min, <videos> videos, <likes> likes, <comment likes> comment likes, <follows> follows, <comments> comments
FYP niche: <x>/10   Flags: <none | detail>
Test: <passed -> P<n+1> | not yet: <what's missing>>
Next: <next session> | <"time for your first post"> | <check due date>
```
