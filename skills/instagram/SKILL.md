---
name: instagram
description: The Instagram app guide for agents driving the user's real iPhone with Zeptap - screen map, tab bar, profile and Settings paths, gestures for feeds and Reels, how to read a post, a timed browse session, recovery from popups and stuck sheets, and the stop rules. Loaded by every Instagram job skill (instagram-story-poster, instagram-poster, instagram-dm-replies and others) before they touch the app. Use it directly for Instagram tasks no job skill covers, such as "browse Instagram for 20 minutes and like skincare posts" or "open my Instagram notifications". Instagram's API excludes personal accounts and most in-app features, so this works inside the app itself.
---

# Instagram

The app guide every Instagram job skill loads first. Builds on `iphone-use`: its loop, connection check and safety rules apply.

Positions are fractions of the screenshot (`x 0.5w, y 0.93h`). Layouts shift between app versions and between posts, so find each element on the current screenshot before tapping. Never reuse coordinates from an earlier post. App screens here were seen on 2026-11-18 [v18] unless tagged otherwise.

## Job skills (load the one that matches)

| The user wants to | Skill |
|---|---|
| Post a Story with a link, poll, question, mention or location sticker | `instagram-story-poster` |
| Post a photo, carousel or Reel | `instagram-poster` |
| Answer DMs and message requests | `instagram-dm-replies` |
| DM everyone who commented a keyword | `instagram-comment-to-dm` |
| Reply to comments on their posts | `comment-replies` |
| Edit bio, link in bio, name | `iphone-use` |
| Export Saved posts and collections | `competitor-content-check` |
| Read their own Instagram numbers | `weekly-creator-report` |
| Find trending Reels audio | `hook-and-format-scout` |
| Research top posts in a niche | `competitor-content-check` |
| Find brand deals in the inbox | `instagram-dm-replies` |

## Without Zeptap

Do the planning and writing the task needs (the caption, the reply, the session plan), then send the connect message from `iphone-use` with `utm_campaign=instagram`.

## Screen map

**Bottom tab bar** (y about 0.93h): five icons, no labels, tapped by position. Order on the 2026-11-18 build, left to right: **Home** (house), **Reels** (play in a frame), **Messages** (paper plane), **Search and Explore** (magnifier), **Profile** (your round photo) [v18]. Instagram reorders these between versions: confirm each icon's shape before tapping. The tab bar **hides while a profile or long grid is scrolled**; a tap at y 0.93h then lands on a grid tile. Scroll up a little, or go back, before tapping a tab.

**Home**: `+` (top left), the Instagram wordmark (a ⌄ next to it opens a feed menu), the heart (notifications, top right, often with a red dot or a bubble of counts). Then the Stories row ("Your story" with a `+` on your avatar first), then posts.

**A post**:

| Part | Holds |
|---|---|
| Header | Avatar, `username`, an audio line for Reels (`♫ name · Original audio`), sometimes `Suggested for you` or `Sponsored`, a **Follow** button on accounts you don't follow, a menu icon (`=` lines or `…`) on the right |
| Media | Photo, video or carousel ("1/5" or dots) |
| Action row | Heart + count, comment bubble + count, repost arrows + count, paper plane + count on the left; bookmark on the right (filled = saved) |
| Below | `username caption … more`, then the date |

**Reels viewer**: full screen. Right rail top to bottom: heart, comments, repost, share (each with a count), bookmark (saves count), menu `=`. Bottom left: avatar, `username`, **Follow**, caption, "Followed by …". Some viewers show an **Add comment…** field at the bottom: never type into it unless commenting was asked for.

**Search and Explore**: a **Search** field and a grid; Explore tiles show a view count (eye icon, `182K`). Tapping the field shows **Recent** searches with X to clear each and **Cancel**. Typed results show a keyword row first, then accounts. **Look-alike handles appear side by side** (`socialinfluencestudios` and `socialinfluencestudio`): match the exact handle.

**Another account's profile**: category, `posts / followers / following`, bio, link, "Followed by …", **Follow** (large blue) and **Message**, highlights, then tabs: grid, Reels (each tile shows views), reposts, tagged. Pinned posts carry a pin icon. Once the profile scrolls, **Follow moves into the top right of the header**, where you might expect a menu.

**Your profile**: username with ⌄ (account switcher) at the top, a Threads icon and **☰** at the top right; `posts / followers / following`, bio, link, **Edit profile**, **Share profile**, then grid / Reels / tagged tabs.

**☰ Settings and activity** [v18]: Search field; Meta Account; How you use Instagram: **Saved**, **Archive**, **Your activity**, **Notifications**, Time management; Subscriptions; Who can see your content: **Profile privacy**, Close Friends; further down, privacy and interaction settings.

**Messages**: see `instagram-dm-replies` for the full map.

## Gestures

| Want | Do | Check |
|---|---|---|
| Next post on Home or a feed of results | `drag` from (0.5w, 0.78h) to (0.5w, 0.3h), default duration | A new post header near the top. Drag, not flick, so no post is skipped |
| Next Reel | `flick` `up` from (0.4w, 0.6h), `settle_ms` 800 | Username or caption changed. If not, `drag` (0.4w, 0.78h) → (0.4w, 0.22h), `duration_ms` 300 |
| Like | `double_tap` the middle of the media | Heart turns red. A double tap only ever likes |
| Next photo in a carousel | `flick` `left` from the middle of the media | Counter or dots advanced |
| Leave a Story you opened | `flick` `down` from the middle | Back where you were |
| Close a sheet | Tap the dimmed area above it, or drag its handle down | The sheet is gone |

Tapping a red heart **un-likes**. Avoid sideways swipes outside carousels: on Home and Reels they open the camera or Messages. Start gestures in the content, away from screen edges, the tab bar and the Reels rail. Reels and feed videos never stop moving: pass `settle_ms` 800 there and ignore "screen still moving".

## Reading a post

Judge by caption, hashtags, on-screen text and what the media shows. `find_text` with no query lists the caption lines; don't open `more` just to read. `find_text` reads emoji-only text poorly: judge it from the screenshot.

**On-topic** means the post's subject is the user's topic, not a passing hashtag. For "marketing": ads and creative, branding, social growth, content strategy, copywriting, SEO, email, e-commerce, agency life, case studies. Memes, food and lifestyle posts are off-topic even with a business hashtag. Unsure: don't like, move on.

Skip `Sponsored` posts without liking or tapping them, and never tap `Shop now`, `Learn more` or `Install`.

## Browse session

For "browse Instagram for 20 minutes and like the marketing posts":

1. **Time it.** If Zeptap's chat offers `set_goal`, call it with the task and minutes. Otherwise keep time with your own clock, or count posts (about 2 to 4 a minute).
2. `open_app` `Instagram`. If the screenshot still shows the splash logo, `wait` 2000 before acting. Close any popup.
3. **Split the time** unless told otherwise: a quarter on Home, half on Reels, a quarter on Search (a topic term or hashtag, then a result feed).
4. **One post at a time:** off-topic or ad → move on immediately. On-topic → `wait` 1000-3000 ms (photo) or 2000-6000 ms (video), `double_tap`, confirm the red heart, count it, move on. Never wait for a video to end.
5. **Limits:** about 2 or 3 likes a minute at most, or the user's own limits ("at most 10 likes"). Warmup stage limits: https://zeptap.com/docs/playbooks/instagram-warmup.md.
6. **Tally** as you go. "You're all caught up" on Home means carry on into suggested posts or move to Reels.
7. When time is up: finish the post on screen, `home`, report (and `end_goal` if you used `set_goal`).

```txt
Instagram session: <minutes> min on <topic>
Seen: <n> feed posts, <n> Reels, <n> from search (<n> on-topic, <n> ads skipped)
Liked: <n>
Searches: <terms, or none>
Feed fit: <share of Home and Reels on-topic>
Pushback: <none, or the exact message>
```

## Recovery

| You see | Do |
|---|---|
| The splash logo after `open_app` | `wait` 2000, look again. Don't tap yet |
| A popup: notifications, contacts, Find friends, new feature, Threads, Meta Verified, rating, Save login info, "Introducing …" | `Not now`, `Skip`, `Cancel`, `OK` or the X |
| The app opened on an old screen (a sheet, a Privacy page, an editor) | Instagram resumes where it was left. Close that screen with its own back chevron or X first |
| **Manage comments** sheet (Select multiple comments, Turn off commenting, …) | `dismiss` does **not** close it. Tap the dimmed area above the sheet. A blind tap at the bottom lands on "Change privacy settings" |
| A comments sheet you didn't mean to open | Tap the dimmed media above it, or drag the handle down |
| A profile, hashtag or audio page you didn't mean to open | `back` |
| Camera (swiped sideways by accident) | The X top left, or `back` |
| Tab bar missing | Scroll up slightly or go back; it hides while a grid scrolls |
| A tap that should open something left the screen unchanged | `wait` 1500 and look again before re-tapping |
| Blank, frozen or endless spinner | `wait` 2000, then `open_app` `Instagram` again |
| Lost | Home icon in the tab bar (tap again to jump to the top) |

Two misses with one approach: change approach (`tap_text` instead of coordinates, `drag` instead of `flick`, reopen the app). A miss is never a reason to end a session.

## Stop and hand over

Stop at once, leave the screen as it is, and quote it word for word when Instagram shows:

- "Try Again Later", "We restrict certain activity to protect our community", "Action Blocked"
- "We suspect automated behavior on your account" or any account warning
- a request to confirm it's you (code, selfie, CAPTCHA)
- a login, sign-up or password screen

Call `end_goal` with status `blocked` if a goal is running. The account owner deals with these.

## What needs the user's say-so

Browsing and liking on the user's topic are covered by a session request. Everything else needs the user to have asked: follow, comment, reply to a Story, share, repost, save, DM, accept or delete a message request, post, change settings or the profile.

- **Return sends** in comments, Story replies and DMs.
- **Final screens need a fresh yes:** show the screenshot, the exact text and the account (the username at the top of Profile or Messages), then wait.
- **Several accounts on one phone:** the ⌄ next to the username switches accounts. Confirm the active account before any final action.
