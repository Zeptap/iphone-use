---
name: multi-account-poster
description: Post or draft content across several Instagram or TikTok accounts the user runs - switching accounts inside the app or working across up to five iPhones connected to the same Mac with Zeptap - with a caption adapted to each account and an approval per account. For agencies, brands and creators managing client or niche accounts on real phones, where scheduling APIs need business accounts and app review. Without Zeptap it writes the per-account captions and the posting plan. Use for "post this to all five client accounts", "draft this reel on each of my brand accounts", "post on @brand_us and @brand_uk with different captions", "use each phone to post today's video". For one account use instagram-poster or tiktok-uploader.
---

# Multi-account poster

The agency job: one asset (or a set), many accounts the user manages, each post adapted and approved. Builds on `iphone-use`: its loop, connection check and safety rules apply. Uses `instagram-poster`, `tiktok-uploader` and the `instagram` / `tiktok` app guides for the screens.

## Use it for / hand off

- Accounts the user owns or manages with permission, each with a reason to carry the content.
- One account → `instagram-poster` / `tiktok-uploader`. Same video on three platforms for one brand → `short-video-cross-poster`.
- **Not for** pushing identical content through many accounts to game reach. Platforms treat that as spam and restrict accounts. Every account gets its own caption, and the user approves each post.

## Without Zeptap

Write the per-account plan (account, platform, caption, settings, timing) as a table, then send the connect message from `iphone-use` with `utm_campaign=multi-account-poster`. The wall: scheduling APIs need business accounts and app review per platform.

## Intake

- Accounts: platform + `@handle` each, and **where each lives**: which iPhone, and whether several share one app via the account switcher.
- The asset per account [same video], and each account's audience or angle in a few words.
- Mode: drafts or publish [drafts]. Timing gaps between accounts [none, but sequential].

## Plan before the phone

1. `list_phones`. Map each account to a phone `id`. A phone with `ready=no` can't be used now: say which accounts that affects.
2. Write the table and get it approved:

```txt
| # | Phone | Platform | @handle | Caption (first line) | Settings | Mode |
```

Captions: same facts, each account's angle and voice; never identical. Hashtags differ per audience.

## On the phone

**Several phones.** Pass `phone: <id>` on **every** call, and check the phone name at the start of each result. Calls to different phones run side by side, so you may work two phones in parallel; calls to one phone run in turn. Finish an account fully (to Drafts or its final screen) before starting the next on the same phone.

**Several accounts in one app.**
- Instagram: the account name with **⌄** at the top of the Profile tab (and of Messages) opens the account switcher [v18: `brand_us ⌄` seen; switcher list itself unverified]. Tap the target `@handle`, then confirm the header shows it before doing anything else.
- TikTok: Profile › the name with **▾** at the top left [v18: seen next to the display name; switcher list unverified].
- **Check the active account on every screen where it shows** (profile header, Instagram's "New reel" screen avatar, TikTok's post screen). Posting from the wrong account is the costly mistake here.

Then run the platform skill's steps for that account: caption from the approved table, settings, Drafts or stop at the final screen.

## Stop and show

Drafts mode: no stop per account; one report at the end. Publish mode: per account, the final screen screenshot + `@handle` + exact caption, and a yes before Share/Post. "Yes to all" covers only the table the user saw; any difference on screen means stop and show.

### Verified run: two Instagram accounts on one phone [v18 2026-11-19]

1. Post on the active account (instagram-poster steps). Success banner reads `Posted! Your reel just dropped.` and the feed shows the reel with `AI content` when the AI label is on.
2. **Switch account:** `long_press` the profile tab (bottom right `~0.9w, 0.94h`). A sheet lists the accounts with a blue check on the active one. Tap the other account's row by position (`tap_text` can hit the page behind the sheet). Toast: `Switched to <handle>`; the tab-bar avatar changes.
3. Post again with a **different caption** (identical captions across accounts look like spam). The second account may show `Video posts are now shared as reels` once: tap `OK`.
4. The `Add AI Label` toggle moves down after a caption is added; re-read its position before tapping (a stale tap opened `Audience`).

## Traps

- Wrong active account after a switch: verify the header every time.
- A login screen on switching: user-only; skip that account and report.
- Platform warnings ("Try Again Later", "You're tapping too fast"): stop that account and the rest on the same platform, report the exact text.
- `Your story` / `Your Story` one-tap publish buttons in both editors (see the platform skills).

## Report

```txt
Multi-account run: <asset> · <mode>
| Phone | Platform | @handle | Result | Proof |
Skipped: <account, reason>   Warnings: <exact text or none>
```
