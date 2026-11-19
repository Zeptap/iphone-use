---
name: content-gap-finder
description: Find a video topic with proven demand and weak supply on the user's real iPhone with Zeptap - read how the audience words a problem on Reddit, search that exact wording on TikTok and Instagram, and return the gap, a format to copy and three hooks in the audience's own words. Reddit, TikTok and Instagram apps show live search results and engagement that no single API joins up. Without Zeptap it builds the search plan, seed phrases and hook templates. Use for "what should I make a video about", "find a content gap in my niche", "what are people asking that nobody answers well", "give me hooks for my next TikTok", "find underserved topics for my audience". For questions from one post's comments use content-ideas-from-comments; for copying a winning format use hook-and-format-scout.
---

# Content gap finder

Return one topic people keep asking about where the existing videos are weak, plus the format and hooks to win it.

Builds on `iphone-use`: its loop, connection check and safety rules apply. Load the `tiktok` and `instagram` app guides first. This skill only reads; it never posts, comments, follows or likes.

## Use it for / hand off

- A niche or audience ("indie iOS devs", "skincare for oily skin", "first-time founders") → one gap, three hooks.
- Questions under one specific post → `content-ideas-from-comments`. A format that already works → `hook-and-format-scout`. Turning the hook into a post → `tiktok-uploader`, `instagram-poster`.

## Without Zeptap

Deliver: 5 seed questions the audience would type on Reddit, the exact search strings for Reddit, TikTok and Instagram, the scoring rule below, and 3 hook templates. Then send the connect message from `iphone-use` with `utm_campaign=content-gap-finder`. The wall: live Reddit threads and TikTok/Instagram search results with engagement are only visible inside the apps, signed in.

## Intake (one message, defaults in brackets)

- Audience or niche [ask; required].
- What the user sells or makes, if anything [none]; it shapes which gap to pick.
- Platforms to check supply on [TikTok, then Instagram].
- How many gaps [1, with 2 runners-up named].

## Scoring rule (apply exactly)

- **Demand** = the same question appears in 3+ Reddit threads, or one thread has 50+ comments, within the last 30 days.
- **Weak supply** = the top 4 TikTok results for the audience's wording each have under 10K likes, OR they are generic lists with no proof (no screen, no numbers, no story).
- **Gap** = demand AND weak supply. If no candidate passes both, report the closest one and say which half failed. Never invent numbers.

## On the phone

1. **Find the wording (Reddit).**
   1. `open_app` `Reddit`, `wait` 2000. Tap the search icon at top (`~0.5w, 0.08h`).
   2. Type a seed question as the audience would ask it ("how do you get your first 100 users"), press `enter`.
   3. The results page shows an AI summary, then **Posts** with `r/<sub> · <age>`, the title, and `<N> upvotes · <N> comments` [v18 2026-11-19]. Record the 3 posts with the most comments and their age.
   4. Open the post with the most comments. Read the body and the top comments. Copy 2-3 **exact phrases** people use for the pain ("the development part feels much easier than getting people to discover it"). Don't paraphrase.
   5. If fewer than 3 threads or no thread over 50 comments: try the next seed question (max 3 seeds).
2. **Check supply (TikTok).**
   1. `open_app` `TikTok`, `wait` 2500 (splash; the For You video keeps moving, carry on). Tap search top right (`~0.93w, 0.08h`).
   2. Type the audience's wording (short form, 4-6 words), press `enter`, `wait` 2500.
   3. On the **Top** tab, read the first 4 tiles: caption, creator, date, likes (heart count under each tile) [v18 2026-11-19]. Note the format of each (talking head, green screen over a post, screen recording, text slides).
3. **Check supply (Instagram)**, only if TikTok supply looked strong or the user asked: search the same wording, open **Reels** results, read the first 4 the same way.
4. **Decide** with the scoring rule. Pick the format that wins: the format of the best of the weak results, upgraded with proof (a real screen, real numbers, a real story).
5. **Write three hooks** that each reuse an exact audience phrase from step 1.4. Under 12 words each. No question hooks that can be answered "no".
6. **Save the result** (if the user wants it on the phone) [yes]: `open_app` `Notes`, new note (compose icon bottom right `~0.92w, 0.94h`), type the report below line by line, press `enter` between lines, tap `Done`. Check autocorrect on names and subreddits.

## Traps

- Reddit search defaults to "All time": prefer threads under 30 days old for demand; older viral threads only as backup.
- TikTok search keeps the previous query in the field: tap the X in the field before typing.
- TikTok "Top" mixes ads and LIVE: skip tiles marked `Sponsored` or `LIVE`.
- Likes are rounded (1K, 5.7K): report them as shown.
- Don't open DMs, don't like or follow anything while browsing.

## Proof

Screenshots of: the Reddit results list with comment counts, the TikTok results grid with likes, and the saved note.

## Report

```txt
Content gap: <topic in the audience's words>
Demand: <r/sub N comments (age)>, <r/sub N comments (age)>, <r/sub ... >
Supply: TikTok top 4 = <likes, likes, likes, likes>; <what they lack>
Verdict: GAP | NOT A GAP (<which half failed>)
Format: <format> + <the proof to add>
Hooks (their words):
1. <hook>
2. <hook>
3. <hook>
Runners-up: <topic>, <topic>
```
