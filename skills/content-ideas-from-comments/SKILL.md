---
name: content-ideas-from-comments
description: Turn the questions in a viral post's comments into the user's next videos, on the user's real iPhone with Zeptap - find a recent high-engagement TikTok or Reel in the niche, read its comments, keep only real unanswered questions, and return a ranked list of video ideas with which to film first. Comments are only fully readable inside the TikTok and Instagram apps. Without Zeptap it gives a comment-mining checklist and idea templates. Use for "what are people asking under viral videos in my niche", "get me video ideas from comments", "mine the comments on this TikTok", "what questions does my audience have". For demand-vs-supply gaps across Reddit and TikTok use content-gap-finder.
---

# Content ideas from comments

Return 3-6 video ideas taken from real viewer questions, ranked, with the first one to film.

Builds on `iphone-use`: its loop, connection check and safety rules apply. Load the `tiktok` (or `instagram`) app guide first. Read-only: no likes, replies or follows.

## Use it for / hand off

- A niche, or a specific post link or creator → ideas from its comments.
- Cross-platform gaps (Reddit demand vs TikTok supply) → `content-gap-finder`. Format to copy → `hook-and-format-scout`.

## Without Zeptap

Deliver: search terms for the niche, the filter rule below, and an idea template. Then the connect message from `iphone-use` with `utm_campaign=content-ideas-from-comments`. The wall: full comment threads with like counts are only readable in the apps.

## Intake (defaults in brackets)

- Niche, or a post/creator [ask; required].
- Platform [TikTok].
- Number of posts to mine [1; up to 3].

## Filter rule

Keep a comment only if it is a **question or a stated confusion** that the video did not answer. Drop praise, jokes, spam, self-promotion and questions already answered in a reply by the creator. Rank by: comment likes, then how many comments ask the same thing.

## On the phone

1. `open_app` `TikTok`, `wait` 2500. Tap search (`~0.93w, 0.08h`), clear the field, type the niche phrase, `enter`, `wait` 2500.
2. On **Top**, pick the tile with the most likes posted in the last 14 days (date under the creator) [v18 2026-11-19]. Skip `Sponsored` and `LIVE`.
3. Open it. Record creator, likes and comment count from the right rail.
4. Tap the comment icon (right rail, `~0.92w, 0.58h`), `wait` 2000. The sheet header reads `<N> comments` [v18].
5. Read comments top-down. `drag` from `y 0.86h` to `0.44h` to scroll. Read up to 40 comments or the whole thread. Copy question text verbatim.
6. Apply the filter rule. Merge duplicates and count them.
7. Write each idea as a video title in the asker's words. Mark the first to film: the most-liked question that has no reply.
8. Save to Notes if asked [yes]: compose, type line by line, `Done`.

## Traps

- The comment sheet keeps playing the video above it; "screen still moving" is normal.
- "View N replies" hides answers: open replies on the top 3 questions before calling them unanswered.
- Don't tap the heart next to comments: it likes them.

## Report

```txt
Ideas from comments: <creator>, <topic> (<likes> likes, <N> comments)
1. <idea in their words> (<N> asked, <likes> likes) <- film first
2. ...
Why #1: <one line>
```
