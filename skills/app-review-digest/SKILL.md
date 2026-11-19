---
name: app-review-digest
description: Turn an app's App Store reviews into a ranked fix list on the user's real iPhone with Zeptap - open the app's page in the App Store app, sort reviews by Most Critical and Most Recent, read them, group complaints into themes with counts and quotes, and say what to fix first. Works for the user's own app or a competitor's. The App Store app shows the review sort and Apple's review summary for the phone's region; reading competitors needs no developer account. Without Zeptap it gives the theme template and the triage rule. Use for "what are people complaining about in my app", "summarise my App Store reviews", "read Fleur's 1-star reviews", "what do users hate about this competitor", "turn reviews into a roadmap". For keyword ranks use app-store-rank-check.
---

# App review digest

Return complaint themes with counts and verbatim quotes, and one thing to fix first.

Builds on `iphone-use`: its loop, connection check and safety rules apply. Read-only: never tap `Get`, `Write a Review`, `Report a Problem` or a star rating.

## Use it for / hand off

- One app (own or competitor) → themes, quotes, fix-first. Two apps → run twice, then compare.
- Keyword ranks → `app-store-rank-check`. Walking the app's onboarding → `app-onboarding-teardown`.

## Without Zeptap

Deliver the theme list template, the triage rule, and the exact App Store steps. Then the connect message from `iphone-use` with `utm_campaign=app-review-digest`. The wall: the App Store app's review sorts and region-specific reviews; App Store Connect only covers apps the user owns.

## Intake (defaults in brackets)

- App name [ask; required]. Own app or competitor [competitor].
- Sorts [Most Critical, then Most Recent]. Reviews to read [up to 20 per sort].

## Triage rule (fix first)

Score each theme: **reach** (how many reviews) × **severity** (3 = paying users blocked or charged wrongly, 2 = core feature broken, 1 = annoyance or taste). The highest score is fix-first. Tie → the one in Most Recent wins.

## On the phone

1. `open_app` `App Store`, `wait` 2500. Tap **Search** (`~0.9w, 0.94h`), tap the field (`~0.47w, 0.14h`), type the app name, `enter`, `wait` 2500.
2. Apps often bid on their own name: the top card may carry `Ad` [v18 2026-11-19]. Tap the first result **without** `Ad` whose developer matches.
3. On the app page, read `<N> RATINGS`, the average, the category and developer.
4. Tap the ratings number (`~0.16w, 0.31h`): the page jumps to **Ratings & Reviews**. Tap the `Ratings & Reviews ›` header to open the full list [v18].
5. The full list shows Apple's `Review Summary` and a sort button `Most Helpful ⌄` (right, `~0.8w, 0.47h`; `tap_text` may miss it, tap by position). Choose **Most Critical** in the `Sort by` sheet. `wait` 1500 (settle fires early).
6. Read each card: title, stars, date, reviewer, text. `drag` from `y 0.86h` to `0.31h` to scroll. Copy short quotes verbatim.
7. Re-sort to **Most Recent** and read again; note whether the critical themes are still current (dates in the last 90 days).
8. Group into themes, count, apply the triage rule.
9. Save to Notes if asked [yes]: compose, type line by line, `Done`.

## Traps

- Long reviews are truncated with `…` in the list; tap the card to read the whole text, then `Back`.
- Developer replies appear under some reviews: note "dev replied" so the user doesn't treat it as ignored.
- Apple's Review Summary skews positive; never use it in place of reading.

## Report

```txt
<App> review digest (<rating>, <N> ratings, <region>, <date>)
1. <theme> - <count> reviews, latest <date>. "<quote>"
2. ...
Fix first: <theme> (<reach> x <severity>): <one line why>
Praised (keep): <1-2 themes>
```
