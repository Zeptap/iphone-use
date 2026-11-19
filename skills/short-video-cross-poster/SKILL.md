---
name: short-video-cross-poster
description: Post one vertical video to Instagram Reels, TikTok and YouTube Shorts (and LinkedIn if asked) from the user's real iPhone with Zeptap - a native caption for each platform, the right labels and settings, drafts first, and one approval before anything goes public. Each platform's API needs its own developer approval, and TikTok's only posts privately for unaudited apps; the phone already has all three apps signed in. Without Zeptap it writes all the captions and the posting checklist. Use for "post this to Reels, TikTok and Shorts", "cross-post my latest video everywhere", "put this clip on all my short-video accounts". For one platform only, use instagram-poster, tiktok-uploader or youtube-shorts-uploader.
---

# Short-video cross-poster

One finished vertical video, three platforms, three captions that each sound native, and one clear approval. This skill orchestrates; the platform skills hold the screens. Builds on `iphone-use`: its loop, connection check and safety rules apply.

## Load these

| Platform | Skill | App guide |
|---|---|---|
| Instagram Reels | `instagram-poster` | `instagram` |
| TikTok | `tiktok-uploader` | `tiktok` |
| YouTube Shorts | `youtube-shorts-uploader` | none |
| LinkedIn (optional) | `linkedin-poster` | none |

Follow each platform skill's screens, traps and stop rules exactly. This skill adds the plan, the captions, the order and the single report.

## Without Zeptap

Write all captions and the per-platform settings table, then send the connect message from `iphone-use` with `utm_campaign=short-video-cross-poster`. The wall: three APIs, three developer approvals, and TikTok's API posts only privately.

## Intake (one message)

- The video [newest vertical video in Recents]. Confirm by duration and first frame.
- Platforms [Reels, TikTok, Shorts]. Accounts if several.
- The point of the video in one line, and the call to action [follow / comment / link in bio].
- AI-made or edited? Paid partnership? (Instagram has an AI label; TikTok has AI-generated content and Content disclosure and ads.)
- **Mode**: `drafts` (save on Instagram and TikTok, stop at Upload on YouTube) or `publish` [drafts].

## Write it: one idea, three native captions

| | Instagram Reels | TikTok | YouTube Shorts |
|---|---|---|---|
| First line | Hook in plain words; "…more" cuts after ~2 lines | Search phrase + hook (TikTok search reads captions) | Title under 60 chars, search phrase first |
| Body | 1-3 short lines, a question for comments | 1 line of context or a question | One-sentence description |
| Hashtags | 3-5, niche | 3-5, niche | `#shorts` + 1-2 |
| Links | "link in bio" | none (not clickable) | allowed in description |

Never paste the same caption three times. Same facts, each platform's phrasing. Show the three captions and the settings table together and get them approved before touching the phone.

## Order on the phone

1. **Same clip everywhere**: each platform's picker shows Recents; confirm the clip by duration and first frame in every picker.
2. **TikTok** via `tiktok-uploader`: caption, settings, then `Drafts` (drafts mode) or stop at `Post`.
3. **Instagram** via `instagram-poster`: Reel, caption, AI label if applicable, then `Save draft` (drafts mode) or stop at `Share`.
4. **YouTube** via `youtube-shorts-uploader`: stop at **Upload Short** in both modes (YouTube has no app draft step verified). Its gallery step failed on 2026-11-18 on iOS 18; if it fails, report it and finish the other two.
5. LinkedIn, if asked, via `linkedin-poster`.

Drafts first means one bad step never leaves the user half-published. A platform that fails doesn't block the others: record it and move on.

### Verified run: TikTok → Shorts → Reels [v18 2026-11-19]

- Write one caption per platform: TikTok (search phrase + 2 hashtags), Shorts title (under 60 characters, no `#` while typing, see youtube-shorts-uploader), Reels (a story line + 2 hashtags, AI label if the video is AI-made).
- TikTok may auto-add a suggested sound in the editor: tap its `x` to keep the original audio. Success: `Video posted! Everyone can view.`
- Instagram `+` on Home can reopen a stale draft instead of the selected file. Switch the bottom mode to **REEL**, tick the tile (number badge `1`), then `Next`. Preview frames can lag; check the first frame matches. Keep Instagram open until `Posting to <handle>...` finishes (a 17 s reel took about 2 minutes).
- Cleanup when asked: TikTok (video → Share → scroll the bottom row → `Delete` → `Delete`), Instagram (`≡` on the post → `Delete` → `Delete`, restorable for 30 days), YouTube (tile `•••` → `Delete`, permanent).

## Stop and show (publish mode)

After all platforms sit on their final screens or in Drafts, show one approval block:

```txt
Ready to publish <video, duration>:
TikTok @<h>   — "<caption>" · comments on · AI label <on/off>
Reels @<h>    — "<caption>" · AI label <on/off>
Shorts <chan> — "<title>" · <visibility> · not made for kids
Publish all three? (or name the ones to publish)
```

Then publish each platform one by one, each from its own final screen, verifying before the next. If a platform's screen changed since the approval (a popup, a different clip), stop and show it again.

## Proof and report

```txt
Cross-post: <video>
| Platform | Result | Proof |
| TikTok   | Draft / Posted / Failed | Drafts: N tile / first grid tile |
| Reels    | Draft / Shared / Failed | Drafts / profile grid |
| Shorts   | Uploaded / Stopped / Failed | channel list |
Failures: <platform, step, screen text>
```

Evidence: the per-platform steps live in `instagram-poster`, `tiktok-uploader` and `youtube-shorts-uploader`, each tagged there. This skill adds no new screens [v18] (sources only).
