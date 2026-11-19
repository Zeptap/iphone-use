---
name: tiktok
description: The TikTok app guide for agents working on the user's real iPhone with Zeptap - screen map, gestures, the For You browse session, profile, Drafts, TikTok Studio and Inbox, recovery and the stop rules. Job skills (tiktok-uploader, tiktok-analytics-report, short-video-cross-poster) load it first. TikTok's API only lets unaudited apps post privately and exposes no feed or inbox, so this work happens in the app. Without Zeptap it plans the session or the post and explains how to connect. Use for "scroll TikTok for 20 minutes on fitness", "check my TikTok inbox", "open my TikTok drafts". To upload a video use tiktok-uploader.
---

# TikTok

How TikTok looks and behaves on the iPhone, and how to move through it without wrong taps. Builds on `iphone-use`: its loop, connection check and safety rules apply. Job skills load this guide first and add their own flow.

Positions are fractions of the screenshot (`x 0.4w` = 40% of the width). TikTok moves elements between videos and app versions: find each one on the current screenshot, never reuse coordinates from an earlier video. Screens below were seen 2026-11-18 on iOS 18.7 [v18] unless tagged.

## Job skills

| The user wants to | Load |
|---|---|
| Upload a video, to Drafts or as a post | `tiktok-uploader` |
| Weekly numbers from TikTok Studio | `weekly-creator-report` |
| Same video to TikTok, Reels and Shorts | `short-video-cross-poster` |
| Post across several accounts or phones | `multi-account-poster` |
| Research hooks or trending sounds | `competitor-content-check`, `hook-and-format-scout` |
| Browse or like on a topic | this guide, **For You session** below |

## Without Zeptap

Plan the job (the search terms and topic rules for a session, the caption for a post, the metrics for a report), then send the connect message from `iphone-use` with `utm_campaign=tiktok`. The wall: TikTok's API exposes no feed, inbox or Studio, and only lets unaudited apps post privately.

## Screen map

**Launch.** `open_app` `TikTok` reports "settled" on the splash logo. `wait` 2000-3000 ms before reading the screen [v18].

**Bottom tab bar** (labelled, `tap_text` works): `Home`, `Friends` (some accounts show `Shop`), `+` (centre, create), `Inbox` (red badge = unread count), `Profile` [v18].

**Top of Home**: `LIVE` icon top left, then scrolling feed tabs such as a location tab (`Los Angeles`), `Following`, `Shop`, `For You`; the magnifier top right opens Search [v18]. `tap_text` `For You` to reach the main feed.

**Right rail** (x ~0.88-0.95w, y ~0.45-0.88h), top to bottom: creator avatar with a red `+` (**follows**: never tap unless asked), heart with count (tapping a red heart un-likes), speech bubble with count (comments sheet), bookmark with count (Favorites), arrow with count (share sheet), spinning disc (sound page). Find the heart with `find_text` on its count (e.g. `8,488`): the heart sits just above it [v18].

**Bottom left** (y ~0.75-0.9h): `@username` or display name, caption with `#hashtags` and `more`, sound line `♫ …`, sometimes a location chip (`Café Tondo · Los Angeles`) [v18].

**Ads.** Marked `Sponsored` or `Ad`, with a big red button (`Shop now`, `Learn more`, `Download`). Some ads take over the full screen with an interactive layout: a search bar, product cards and a `Shop now` button, with the rail on the right (seen: an Amazon ad) [v18]. Never tap anything inside an ad. `flick` `up` from the centre-left to leave it. A tab-bar tap during such an ad may be swallowed: if the screen didn't change, `wait` 2000 and look again before re-tapping.

## Profile

`tap_text` `Profile` [v18]:
- Header: pencil (edit profile) and a gift icon top left; add-friends and **☰** (menu, may carry a red badge) top right.
- Name, `@handle`, then **Following / Followers / Likes** counts, bio.
- Tabs under the bio: videos (grid icon), a second creator tab, **lock** (private videos), **bookmark** (Favorites), **heart** (Liked).
- Grid: **`Drafts: N` is the first tile** when drafts exist; each video tile shows its views as `▷ 37`. Story-type tiles carry a stacked icon top right.

**☰ menu** (slides in from the right): Balance, Activity center, Offline videos, Your QR code, **TikTok Studio**, Settings and privacy [v18]. `tap_text` missed "TikTok Studio" once: tap the row by position (~0.4w, 0.43h) if `tap_text` fails.

## Inbox

`tap_text` `Inbox` [v18]. First open may show a "Find contacts" sheet: tap `Don't allow`. Layout: add-friends top left, `Inbox` with a status dot, search top right, a Stories row (`Create`, …), then rows:
- **New followers** ("… and 9 others started following you")
- **Activity & new followers** (likes, comments, mentions, invitations)
- DM threads (a camera icon on the right = reply with a photo)
- **System notifications**, TikTok's own assistant thread.
A red count on a row = unread. Opening a DM marks it read for the sender.

## Gestures

| Want | Do | Check |
|---|---|---|
| Next video | `flick` `up` from (0.4w, 0.65h), `settle_ms` 800 | Username or caption changed. If not: `drag` (0.4w, 0.78h)→(0.4w, 0.22h), `duration_ms` 300 |
| Previous video | `flick` `down` from (0.4w, 0.35h) | |
| Like | `double_tap` (0.45w, 0.45h) | Rail heart is red. A double tap only ever likes |
| Pause / resume | `tap` the centre once | Play triangle = paused |
| Creator profile | tap `@username` | `back` to return |

Start feed gestures in the video's middle: never on the rail, the caption block, or within 5% of an edge (iOS back/home gestures). Feeds never stop moving: pass `settle_ms` 800 on every feed gesture and ignore "screen still moving".

## Reading a video

Judge by caption, hashtags, on-screen text and what it shows; `find_text` with no query lists the lines (left of the rail, above 0.9h). A video is **on-topic** when its subject is the topic, not a passing hashtag. Unsure: don't like, move on. Skip ads and LIVE (a `LIVE` badge, comments streaming over the picture) without tapping them.

## For You session

For "scroll TikTok for 20 minutes and like the marketing videos":
1. If a `set_goal` tool is available, call it with the task and minutes; otherwise keep time yourself (2-4 videos a minute).
2. `open_app`, close popups, `tap_text` `For You`.
3. Loop, one video at a time: off-topic, ad or LIVE → next at once. On-topic → `wait` 2000-6000 ms, `double_tap`, confirm the red heart, count it, next. Never wait for a video to end, and don't stop to report progress.
4. If fewer than 1 in 5 of the last 15 videos were on-topic: Search (magnifier) › type a topic term › `press_key` `enter` › first video › same loop, then back to `For You`.
5. At most 2-3 likes a minute, or the user's limits. Warmup stage limits: https://zeptap.com/docs/playbooks/tiktok-warmup.md.
6. When time is up: finish the current video, `home`, report:

```txt
TikTok session: <minutes> min on <topic>
Videos watched: <n> (<n> on-topic, <n> ads/LIVE skipped)
Liked: <n>   Searches: <terms or none>
Feed fit: <share on-topic, and whether it improved>
Pushback: <none, or the exact message>
```

## Recovery

| You see | Do |
|---|---|
| Popup (notifications, contacts, "Find contacts", rating, new feature, save login) | `Not now`, `Don't allow`, `Skip` or X |
| iOS camera / microphone prompt | `Don't Allow` unless the user is recording live; uploads don't need them |
| Comments sheet | `dismiss`, or tap the video above the sheet |
| Profile, sound or hashtag page by mistake | `back` |
| LIVE stream | `flick` `up`; else the X top right, or `back` |
| Full-screen ad | `flick` `up` from the centre-left |
| Blank or frozen | `wait` 2000, then `open_app` `TikTok` again |
| Lost | `tap_text` `Home`, then `For You` |

Two misses with one approach: change approach (`tap_text` ↔ coordinates, `drag` ↔ `flick`, reopen). A miss is never a reason to end a session.

## Stop and hand over

Stop at once, leave the screen as it is (call `end_goal` with `blocked` if available) and quote the screen word for word on: rate limits ("You're tapping too fast", "You're visiting too frequently"), any restriction, ban or community-guidelines notice, a CAPTCHA or "Verify to continue", a login or password screen. Never solve a CAPTCHA.

## Needs the user's say-so

Watching and liking on the topic are covered by a session request. Everything else needs an explicit ask: follow (the `+` on the avatar), comment, reply, share, repost, Favorites, DM, duet, stitch, shop links, LIVE, gifts, posting, settings. Comments: draft them (specific, plain ASCII, no links), show them, post only the approved text; `enter` in the comment field posts.
