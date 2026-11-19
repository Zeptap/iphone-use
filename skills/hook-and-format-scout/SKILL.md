---
name: hook-and-format-scout
description: Find the hooks and formats winning in a niche right now on the user's real iPhone with Zeptap - search the niche on TikTok and Instagram, read the top posts' opening line, format, sound and numbers, and return the pattern to copy with a hook written for the user's product. Search results with view and like counts are only shown inside the signed-in apps, and they differ from what web scrapers see. Without Zeptap it gives the scouting sheet and hook formulas. Use for "what hooks are working for budgeting apps", "what format should my next reel be", "scout TikTok for my niche", "what's trending for AI tools content", "find a viral format I can copy". For topics people ask about but nobody answers well use content-gap-finder.
---

# Hook and format scout

Return the 4-6 top posts in a niche with hook, format and numbers, the pattern they share, and one hook adapted for the user.

Builds on `iphone-use`: its loop, connection check and safety rules apply. Load the `tiktok` and `instagram` app guides first. Read-only.

## Use it for / hand off

- A niche or keyword → the format and hook to copy this week.
- Underserved questions → `content-gap-finder`. Ideas from comments → `content-ideas-from-comments`. Posting the result → `tiktok-uploader`, `instagram-poster`.

## Without Zeptap

Deliver the scouting sheet (hook, format, length, sound, numbers, date), 6 hook formulas (news, list, contrarian, before/after, "I tried", demo), and the search terms. Then the connect message from `iphone-use` with `utm_campaign=hook-and-format-scout`. The wall: in-app search ranking and live counts.

## Intake (defaults in brackets)

- Niche or keyword [ask; required]. The user's product or angle [none].
- Platforms [TikTok and Instagram]. Posts per platform [4].

## Field definitions (record exactly)

- **Hook** = the first on-screen text or first spoken line, verbatim. If only the thumbnail is visible, the thumbnail text.
- **Format** = one of: talking head, talking head + screen/green screen, phone-in-hand demo, screen recording, text slides/carousel, list with title bar, skit, faceless b-roll.
- **Numbers** = TikTok likes on the tile; Instagram views (eye icon) on the tile. Report as shown (6.6K).
- **Date** if shown. Skip anything older than 90 days unless it's the only data.

## On the phone

1. `open_app` `TikTok`, `wait` 2500 (feed keeps moving; carry on). Tap search (`~0.93w, 0.08h`), clear the field, type the keyword, `enter`, `wait` 2500.
2. **Top** tab: read the first 4 tiles (2 rows). Each tile shows thumbnail text, caption, creator, date, likes [v18 2026-11-19]. Skip `Sponsored`/`LIVE`. Open a tile only if the hook isn't readable on the thumbnail; read the first on-screen line, then `back`.
3. `open_app` `Instagram`, `wait` 2000. Tap the **Search** tab (`~0.7w, 0.94h`), tap the search field (`~0.5w, 0.08h`), type the keyword, `enter`, `wait` 2500.
4. **For you** results: `Accounts` first, then `Posts` grid with view counts on each tile [v18 2026-11-19]. `drag` from `y 0.86h` to `0.45h` to reach the grid. Read the first 4.
5. Find the pattern: which hook type and format appear in the top results on both platforms; which got the most views.
6. Write one hook for the user's product in that pattern (under 10 words), plus the format to shoot.
7. Save to Notes if asked [yes]: compose, type line by line, `Done`.

## Traps

- Instagram's search page opens on an Explore grid before you tap the field; that grid is not search results.
- TikTok likes and Instagram views aren't comparable; compare within a platform only.
- Don't tap the heart or Follow buttons next to accounts.

## Report

```txt
Hooks and formats: <keyword> (<date>)
1. "<hook>" - <format>, <platform> <numbers>
2. ...
Pattern: <hook type> + <format>
Your hook: "<hook>" (shoot as <format>)
```
