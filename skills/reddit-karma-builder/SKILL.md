---
name: reddit-karma-builder
description: Build karma and trust on a Reddit account (or several) from the user's real iPhone with Zeptap - a phased karma ladder from a fresh account to one that can post and mention the product, with the subreddits picked from the user's niche, each subreddit's rules read first, daily sessions of helpful comments and votes in the user's voice, caps per phase, shadowban checks, and a log on the phone so every run knows where each account stands. Reddit trusts accounts by history and behavior in the signed-in app; bought accounts, scripts and vote rings get banned. Without Zeptap it gives the subreddit plan, the ladder and comment drafts. Use for "build karma on my Reddit account", "warm up my new Reddit account", "do my Reddit session today", "get my account ready to post in r/SaaS", "grow my 3 Reddit accounts". To find buyers use reddit-lead-finder; to post a thread use reddit-poster.
---

# Reddit karma builder

Take an account from new to trusted: enough karma and history to post and mention the product without being removed or banned.

Builds on `iphone-use` and the `reddit` app guide (load it first: brief, voice, safety, multi-account rules). Screens and taps are in the guide [v18 2026-11-19].

## Start here (every run)

1. Read the `Reddit brief`. None → run the brief questions from the `reddit` guide.
2. Pick the account for today (several accounts: the one with the oldest last session). Read its `Reddit log u/<name>`.
3. No log → **Account setup** (below). Log found → **Pre-flight**, then today's session.

## Account setup (first run per account)

1. Open the profile: comment karma, post karma, account age. Set the phase from the ladder.
2. **Subreddits.** If the brief lists them, use those. Otherwise find them: search the product's problem words (`Communities` tab) and the buyer phrasings (`Posts` tab, past month); keep subreddits with recent buyer questions and posts in the last 24 h. Build three tiers:
   - **Karma** (2-3): big, friendly, fast-moving, where anyone can comment (e.g. r/AskReddit-style or the user's hobby subs). Phase 1 only.
   - **Niche** (3-5): where the user's buyers talk (e.g. r/SaaS, r/startups, r/indiehackers for a founder tool).
   - **Promo-allowed** (1-3): niche subs whose rules allow disclosed mentions or showcase posts.
3. Read every chosen subreddit's rules (`reddit` guide) and record minimum karma/age, self-promo rule and format.
4. Profile: avatar set, a short bio in the persona's voice (no link, no product until Phase 3). A yes is needed for edits.
5. Join the karma tier now; join niche subs over the first week (2 a day).

## Pre-flight (every session)

1. Already done today on this account → pick another account or stop.
2. Shadowban check if 7+ days since the last one, or after any warning (`reddit` guide). Banned → stop this account.
3. Read the profile: karma now vs the log. Note any comment with negative score: what went wrong, one line.
4. Plan in one line: "u/<name>, Phase 2: 6 comments in r/SaaS and r/startups, 15 upvotes, 0 posts". Ask only if posting mode is `review` (see brief).

## The karma ladder

| Phase | Gate to enter | Where | Daily caps | What to do |
|---|---|---|---|---|
| **P1 New** | 0-50 comment karma or under 7 days | Karma tier | 3-5 comments, 10-20 upvotes, 2 joins | Crisp replies in the karma register (dry, sarcastic or funny, emoji where the sub uses them) on posts **under 3 hours old** that are still getting comments; reply to a top comment rather than the post. No niche selling, no links, no posts |
| **P2 Regular** | 50+ comment karma and 7+ days | Niche tier, plus some karma tier | 5-8 comments, 15-25 upvotes | Pointed value answers in the niche (help register): a specific step, a number from the user's experience, a short story. Ask genuine questions. Still no product |
| **P3 Trusted** | 250+ karma, 14+ days, no removals in 7 days, each sub's own minimums met | Niche + promo tier | 5-8 comments, 1 post a week (reddit-poster) | Keep helping; the product may appear in at most 1 of 10 comments, disclosed, only where relevant and allowed (reddit-lead-finder) |
| **P4 Authority** | 1,000+ karma, 30+ days | All tiers | as P3, posts up to 2 a week | Guides, story posts, AMAs in the niche; answer every reply to your posts within a few hours |

Move up only when the gate passes; tell the user when it does ("u/<name> hit 54 karma at 9 days: Phase 2 starts tomorrow, niche subs only."). Drop a phase after a removal or a negative streak (3 comments under 0 in a week).

## The session (10-20 minutes)

1. Home feed for 1-2 minutes; upvote a few genuinely good posts (part of the cap).
2. For each target subreddit: sort `New` (P1) or `Hot` and `New` (P2+). Pick posts with recent activity (newest comment under 3-4 hours) where the user has something real to add.
3. Read the post and top comments, write the comment in the brief's voice (`reddit` guide voice rules), check the sub's rules, post it. In `review` mode, show the batch first.
4. Reply to any replies on the account's earlier comments (they count as karma too).
5. Space comments 2-6 minutes apart; rotate subreddits. Stop at the caps.
6. Log: subreddits, threads (URL or title), comments, upvotes given, karma before and after.

## What earns karma fast without risk

- Being early: first useful comment on a post that's 10-60 minutes old and climbing.
- Replying to the top comment with a sharp addition (replies ride the parent's visibility).
- Concrete experience ("i tried x for 3 months, the y feature saved me") beats advice.
- A genuine question that invites the poster to explain.

## Stop rules

- Shadowban, suspension, or "you're doing that too much": stop the account, log, tell the user.
- A moderator message or removal: re-read that sub's rules; two removals in a week → drop the sub for 2 weeks.
- Never: vote or reply between the user's accounts, the same comment twice, links in P1-P2, the product before P3.

## Without Zeptap

Run the brief questions, then deliver the subreddit tiers with their rules to check, the ladder with today's caps, and 5 comment drafts for posts the user pastes. Then the connect message from `iphone-use` with `utm_campaign=reddit-karma-builder`.

## Report

```txt
u/<name> - P<n> (<karma> karma, <age> days) - <date>
Did: <n> comments in r/<a>, r/<b>; <n> upvotes; replies answered <n>
Karma: <before> -> <after>   Removals: <0|detail>   Shadowban check: <ok|date>
1. r/<sub> "<post title>" -> "<comment>"
Next gate: <what's left to reach P<n+1>>
```
