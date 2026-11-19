---
name: linkedin-poster
description: Write and post (or schedule) a LinkedIn post from the user's own profile on their real iPhone with Zeptap - a short post in their voice with a strong first line, line breaks and one to three hashtags, optional image, then stop at Post or Schedule for approval. LinkedIn's posting API is limited to approved partners, so personal-profile posting happens in the app. Without Zeptap it writes the post ready to paste. Use for "post this on my LinkedIn", "schedule a LinkedIn post for tomorrow 9am", "turn this into a LinkedIn post and publish it", "share my launch on LinkedIn from my phone". For short videos across Reels, TikTok and Shorts use short-video-cross-poster.
---

# LinkedIn poster

Turn the user's point into a LinkedIn post that reads like them, then post it or schedule it from their phone. Builds on `iphone-use`: its loop, connection check and safety rules apply.

Screens seen 2026-11-18 on iOS 18.7 [v18] unless tagged. Find each element on the current screenshot.

## Without Zeptap

Deliver the finished post (and an image suggestion), then send the connect message from `iphone-use` with `utm_campaign=linkedin-poster`. The wall: LinkedIn's posting API is open only to approved partners.

## Start here: the LinkedIn brief (first run, then reuse)

Look in Notes for `LinkedIn brief`. None → ask once, in one message, and save the answers there:

1. **Who you are on LinkedIn** in one line (role, company, who you help).
2. **Who should read your posts** (titles, industries, company size).
3. **3-4 content pillars** (e.g. "lessons from building X", "behind the numbers", "tools I use", "hiring").
4. **Voice**: 2-3 of your past posts, or "read my last 5 posts" [the agent reads them on your profile].
5. **Never post about** [none]. **Cadence** [2-3 posts a week]. **Links**: in the body or first comment [first comment].

Every run after that: read the brief, pick the pillar that hasn't been used most recently (log the pillar under `posts:` in the brief), and write to it.

## Intake (this post)

- The point: a link, a note, a result, or "about X" [ask for one concrete detail: a number, a moment, a lesson].
- Voice samples: a past post or two [read the user's recent posts on the profile if they say so].
- Post now or **schedule** (date, time, time zone) [now, after approval].
- Image from Photos? [no]. Audience [Anyone].

## Write it

- **45-120 words.** LinkedIn cuts the post after the first lines with "…more": line 1 must make someone tap.
- **Line 1: the claim or the moment**, not a greeting. "My agent booked a client call from my own iPhone." not "Excited to share…".
- Short paragraphs, one or two lines each, a blank line between. Plain words. No "game-changer", no emoji walls, no hashtag stacks.
- End on a concrete line or a question people can answer.
- **1-3 hashtags** at the end, specific (#iOSDev, #indiehackers), not #success.
- Links in the post body cut reach on many accounts; if the user wants a link, say so and let them choose body or first comment (first comment is a separate approval).
- ASCII typing; paste for emoji or accents (`iphone-use/references/text-entry.md`). **Show the post first and get the text approved.**

## On the phone

1. `open_app` `LinkedIn`, `wait` 3000 (splash). Close popups.
2. Home has **no Post tab**: the bottom bar is `Home`, `Jobs`, `My Network`, `Notifications`, `More` [v18]. Top bar: your avatar, search "I'm looking for…", the **compose icon (pencil in a square, ~0.81w, 0.08h)**, then messages [v18].
3. Tap compose, `wait` 2500 (skeleton screen first) [v18].
4. **Composer** [v18]: X top left, your avatar with **`Anyone ▾`** (audience) and `Add collaborators`, a **clock icon** (schedule), **`Post`** (grey until there's text). A "Collaborative Posts are here!" tip may show: its X closes it. The field **"Share your thoughts …"** is already focused. Bottom: `Proofread`, a character counter (`0/120`, meaning unverified), image icon, `+`.
5. `type_text` the post. Line breaks: `\n` (blank line = `\n\n`) [v26 typing rule; field behaviour unverified]. Read the whole post back from the screenshot; long posts scroll inside the field, so `find_text` and scroll to check every line. Fix autocorrect damage before going on.
6. Image (if asked): image icon → Photos picker → select → Done [unverified].
7. **Schedule** (if asked): clock icon → date and time pickers → Next [unverified: find the labels on screen; use `iphone-use/references/pickers.md`]. Check the time zone shown.
8. Stop at **Post** or the schedule confirm (below).

## Traps

- Settle fires early on launch and compose: `wait` before re-tapping.
- Back or X with text may ask to save a draft or discard [unverified]: read the options; choose "Save as draft" if unsure.
- `Proofread` may rewrite the text: don't tap it unless the user asks.

## Stop and show

Screenshot of the composer, plus the account name, audience, the exact text, the image, and the schedule time if any. Ask "Post this now?" or "Schedule this for <time>?" Post publishes at once.

## Proof

Post: the feed shows "Post successful" or the post at the top of the profile's activity [unverified]. Schedule: the composer's scheduled-posts view lists it [unverified].

## Report

```txt
LinkedIn: <Posted | Scheduled for <date time tz> | Stopped at composer> as <name>
Audience: <Anyone|…>   Image: <none|which>
Text: "<exact text>"
Proof: <what the screen showed>
```
