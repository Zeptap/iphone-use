---
name: niche-engagement
description: Engage in the user's niche on Instagram and TikTok from their real iPhone with Zeptap - search niche terms, find fresh posts from the right creators, like and save the good ones, and leave real comments (approved by the user) so the right people notice the account, within daily caps. Engagement from the signed-in app is normal behavior; automation through APIs or scripts gets accounts restricted. Without Zeptap it builds the target list, caps and comment drafts. Use for "engage in my niche on Instagram", "comment on fitness creators' posts today", "do my TikTok engagement", "find creators in my niche and interact", "grow my account by engaging". For a brand-new account use instagram-warmup or tiktok-warmup; for Reddit use reddit-karma-builder.
---

# Niche engagement

One session of real engagement in the user's niche: likes, saves, a few real comments, within caps.

Builds on `iphone-use`: its loop, connection check and safety rules apply. Load the `instagram` / `tiktok` app guide first. Comments are public: approve each (or the batch) first.

## Rules

- **Targets:** posts under 48 hours old from accounts in the niche with 1K-200K followers (big enough to be seen, small enough to notice replies).
- **Comment bar:** add something specific to the post (a question, a detail, a short experience). No "great post", no emojis-only, no links, no self-promotion.
- **Caps per session:** likes 20, saves 5, comments 5, follows 3 (only accounts the user would genuinely follow). New accounts → the caps in `instagram-warmup` or `tiktok-warmup` instead.
- **Stop** on any warning ("Try Again Later", "Action Blocked", a verification prompt): quote it and end.

## Use it for / hand off

- Established accounts in a known niche.
- New account → `instagram-warmup` or `tiktok-warmup`. Reddit → `reddit-karma-builder`.

## Without Zeptap

Deliver: 5 niche search terms, 10 target accounts with why, today's caps, and 5 comment drafts. Then the connect message from `iphone-use` with `utm_campaign=niche-engagement`.

## Intake (defaults in brackets)

- Niche and the account's angle [ask; required]. Platform [Instagram, then TikTok].
- Approval mode [batch of comments shown before posting].

## On the phone: Instagram [v18]

1. `open_app` `Instagram`. Search (4th tab) → type a niche term → results grid; open recent Reels.
2. For each target post: double-tap is a like (prefer the heart icon on the right rail to be exact). Save via the bookmark.
3. Comment: speech bubble → read the top comments first (don't repeat them) → draft → after approval tap **Add a comment…**, `type_text`, verify, `enter`.
4. Follow only from the profile header after opening the account, within the cap.

## On the phone: TikTok [v18]

1. `open_app` `TikTok`, search (top right) → niche term → **Videos** tab sorted by recent if offered.
2. Right rail: heart (like), bookmark (save), speech bubble (comments). Comment the same way: read, draft, approve, type, verify, send.
3. Don't tap the red **+** on the avatar unless following is intended.

## Report

```txt
Niche session (<platform>, <date>): likes <n>, saves <n>, comments <n>, follows <n>
Comments:
1. @<creator> "<post first words>" -> "<comment>"
Warnings: <none | quote>
```
