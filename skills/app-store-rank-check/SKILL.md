---
name: app-store-rank-check
description: Check where apps rank for App Store keywords on the user's real iPhone with Zeptap - search each keyword in the App Store app, skip the ads, record the top organic results with rating counts, find the user's own app's position, and say which keywords are winnable. App Store search results are personalised by device and region and only shown in the App Store app; there is no public ranking API. Without Zeptap it builds the keyword list and the scoring sheet. Use for "where does my app rank for habit tracker", "check my App Store keywords", "who ranks top for budget app", "is this keyword winnable", "ASO check on my iPhone". For reading reviews use app-review-digest; for a competitor's onboarding use app-onboarding-teardown.
---

# App Store rank check

Return a rank table per keyword and a verdict on which keywords are worth targeting.

Builds on `iphone-use`: its loop, connection check and safety rules apply. Read-only: never tap `Get`, `Open`, a price button or `In-App Purchases`.

## Use it for / hand off

- 1-10 keywords, optionally the user's own app name → ranks, competitors, winnability.
- Review themes → `app-review-digest`. Competitor onboarding and paywall → `app-onboarding-teardown`.

## Without Zeptap

Deliver the keyword list (the user's plus 5 long-tail variants), the table template from Report, and the winnability rule. Then the connect message from `iphone-use` with `utm_campaign=app-store-rank-check`. The wall: live, region-specific App Store results are only in the App Store app.

## Intake (defaults in brackets)

- Keywords [ask; required, max 10].
- The user's app name [none = competitors only].
- How deep to read [top 10 per keyword; user's app searched up to 30].
- Region is the phone's App Store region; say which in the report.

## Winnability rule

- **Winnable** = at least one of the top 3 organic results has under 5K ratings.
- **Hard** = all of the top 3 have over 100K ratings or carry Editors' Choice.
- Otherwise **Possible**. One developer holding #1 on several keywords = note it as the pattern to study.

## On the phone

1. `open_app` `App Store`, `wait` 2500. Tap the **Search** tab (bottom right `~0.9w, 0.94h`).
2. Tap the search field (`~0.47w, 0.14h`), type the keyword, press `enter`, `wait` 2500.
3. The first result may be an **Ad** (blue `Ad` badge, often a big card) [v18 2026-11-19]. Record the advertiser, then skip it: ranks count organic results only.
4. For each organic result read: name, developer if shown, star rating and **rating count** (e.g. `149K`), and badges (`Editors' Choice`). One result fills about half the screen; `drag` from `y 0.86h` to `0.23h` to advance about one result.
5. Continue to the depth from intake. If the user's app appears, record its position. Not found by 30 = "not in top 30".
6. Next keyword: tap the search field, clear it with the field's X, repeat from 2.
7. Apply the winnability rule per keyword.
8. Save to Notes if asked [yes]: `open_app` `Notes`, compose (`~0.92w, 0.94h`), type the report line by line, tap `Done`. Fix autocorrect on app names (iOS changed "Fleur" to "Flyer" [v18]): double-tap the word, retype.

## Traps

- Ad cards look like results; the `Ad` badge is small and sits under the icon.
- Search suggestions appear while typing; press `enter` rather than tapping a suggestion, or you search a different phrase.
- Ranks shift by region, device and day. Report the date and region; never claim a global rank.
- Never tap `Get`: it downloads.

## Report

```txt
App Store rank check (<region>, <date>)
<keyword> (ad: <advertiser or none>)
  1. <app> - <ratings> ratings <badges>
  2. ...
  Your app: #<n> | not in top 30
  Verdict: Winnable | Possible | Hard
...
Takeaway: <one line: which keyword to target and why>
```
