---
name: ad-creative-scout
description: See the ads your buyers actually get on the user's real iPhone with Zeptap - prime the user's Instagram account as a buyer in the niche (visit competitor profiles and sites, engage with niche posts), then collect every Sponsored and Paid partnership post from Reels, Stories, Explore and the feed, note hook, visual, offer, CTA and how long each advertiser has been running, and turn the winners into 3 static-ad concepts. Meta serves ads by who the viewer looks like, so only a real signed-in phone sees the ads a real buyer sees, in the exact format they run. Without Zeptap it gives the priming plan, capture sheet and concept templates. Use for "what ads are my competitors running", "show me ads in my niche", "give me static ad ideas from what's working", "which creators are doing paid partnerships for X". For organic posts use hook-and-format-scout.
---

# Ad creative scout

Return the ads a buyer in the niche is being served, the patterns that are winning, and 3 static-ad concepts for the user.

Builds on `iphone-use`: its loop, connection check and safety rules apply. Never like, follow from an ad, buy, or fill a lead form.

## Strategy (why two sessions)

Meta only shows niche ads to accounts that look like buyers. An account that hasn't shown interest sees few or none (seen 2026-11-19: 1 paid post in 10 feed posts on an unprimed account [v18]). So the job runs in two steps:

1. **Prime (5 minutes, day 1).** Look like a buyer inside Instagram: open competitor profiles, watch their Reels to the end, save posts, search niche terms. Meta learns interest from in-app behaviour; website visits in Safari barely count because Safari blocks cross-site trackers (it reported 18 blocked on 2026-11-19 [v18]). Niche ads usually appear within 24 hours.
2. **Collect (10 minutes, day 2 or later).** Ads are densest in **Stories** (about 1 in 3-4) and **Reels** (about 1 in 5-8), then Explore and Home.

If the account is already active in the niche, skip priming and collect straight away.

## Use it for / hand off

- A niche, a product category, or 1-5 named competitors.
- Organic formats → `hook-and-format-scout`. Competitor organic posts → `competitor-content-check`.

## Without Zeptap

Deliver the priming checklist (competitor handles, 5 niche search terms), the capture sheet below and 3 concept templates. Then the connect message from `iphone-use` with `utm_campaign=ad-creative-scout`.

## Intake (defaults in brackets)

- Niche or competitors [ask; required]. The user's product and offer [ask].
- Prime first [yes, unless the account is already active in the niche].
- May the agent tap an ad's CTA to read the landing page? [no: it counts as an ad click]. If yes, read the page and go back; never submit anything.

## On the phone

**Prime**
1. `open_app` `Instagram`. Search each competitor handle, open the profile, play 2 Reels for at least 5 s each. Save 1 post.
2. Search 3 niche terms, save 2 posts per term.
3. Open 2 competitors' **Stories** if they have any (story views are a strong signal).
4. Report "primed, collect after <time>" and stop.

**Collect**
1. `open_app` `Instagram`, `wait` 2500 (video keeps moving).
2. **Stories:** tap the first story ring, then tap the right edge to advance. Ads show `Sponsored` under the name and a CTA at the bottom. Read up to 30 stories.
3. **Reels:** Reels tab (`~0.3w, 0.94h`), `flick` up through 20. Ads show `Sponsored` and a CTA bar.
4. **Explore and Home:** 20 posts each. Look under the handle for `Sponsored` or `Paid partnership` (caption may start `#ad Partnered with @brand`) [v18 2026-11-19].
5. For each ad: screenshot the first frame (the hook), read the caption and CTA, then `···` → **About this account** (date joined, and whether it runs ads) and **Why you're seeing this ad**. Record the advertiser (the brand, not the creator, for partnerships).
6. A **winner** is an advertiser seen 2+ times or running the same creative in several placements.
7. Write 3 static-ad concepts: headline (8 words or fewer), visual, offer, CTA, each built on one winner's pattern. Save to Notes if asked [yes].

## Report

```txt
Ad scout: <niche> (<placements scanned>, <date>, primed <yes/no>)
Ads seen: <n> from <n> advertisers
1. <advertiser> (via <creator>) - <placement> - hook "<line>", visual <type>, offer <...>, CTA <...> [winner]
Patterns: <hook type> + <visual> + <offer>
Concepts:
1. "<headline>" - <visual>; <offer>; <CTA>
2. ...
3. ...
```
