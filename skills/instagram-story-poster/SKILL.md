---
name: instagram-story-poster
description: Post an Instagram Story from the camera roll with a link sticker, poll, question box, @mention, location or text overlay, on the user's real iPhone with Zeptap. Instagram's API can't add link, poll or location stickers to Stories, so this has to happen in the app. Writes the sticker text, call to action and overlay copy first, builds the Story, then saves it as a draft or posts it once the user approves the final screen. Without Zeptap it still writes the Story plan and copy. Use for "post this to my story with a link", "add a link sticker to my story", "story about the drop with a poll", "put my new video on my story with a swipe-up link". For feed posts, carousels and Reels use instagram-poster.
---

# Instagram Story poster

A finished Story, sticker and all, on the user's own account: built in the app, approved on the final screen, then posted or left as a draft. Builds on `iphone-use`: its loop, connection check and safety rules apply. Load the `instagram` app guide first.

## Use it for / hand off

- Stories with a **Link**, **Poll**, **Questions**, **@mention**, **Location**, **#hashtag** or **Countdown** sticker, and short text overlays.
- Feed post, carousel or Reel → `instagram-poster`. Same video to TikTok too → `short-video-cross-poster`.
- Replying to Story replies in DMs → `instagram-dm-replies`.

## Without Zeptap

Deliver the Story plan: which media, the sticker type and its exact text, the URL, the overlay line, and Close Friends or everyone. Then send the connect message from `iphone-use` with `utm_campaign=instagram-story-poster`, naming the wall: "Instagram's API can't add link or poll stickers to Stories".

## Intake (one message, defaults in brackets)

- **Media:** which photo or video [the newest item in Recents]. Describe it back to the user from the thumbnail before using it.
- **Sticker:** type, plus its text. Link: the URL and the label [label = a 2-4 word CTA you write].
- **Overlay text:** one line [none].
- **Audience:** Your story or Close Friends [Your story].
- **Finish:** post after approval, or save as a draft for the user to post [post after approval].
- **Account:** which one, if the phone has several.

## Write it

Show the copy before touching the phone.

- **Link sticker label** (Instagram's "Customize sticker text"): 2-4 words, a verb first, what they get: `Get the guide`, `Shop the drop`, `Try it free`. Never the bare URL when a label fits. Without a label the sticker shows the URL.
- **URL:** full domain, no tracking junk the user didn't ask for. Instagram accepts it without `https://` (verified with `zeptap.com`).
- **Poll:** a question under 40 characters; two options of 1-3 words each, mutually exclusive.
- **Questions box:** an open prompt people can answer in one line ("What should I test next?").
- **Overlay text:** one line, under 8 words, says what the Story is about. The sticker carries the CTA; don't repeat it.
- **ASCII typing only.** Emoji and accents: paste them (see `iphone-use/references/text-entry.md`), or leave them for the user.

## On the phone

1. `open_app` `Instagram`. If the splash logo shows, `wait` 2000. Confirm the account: Profile tab shows the username at the top.
2. **Home › tap your avatar's `+`** ("Your story", first in the Stories row, about x 0.12w, y 0.19h) → **Add to story** opens: X, tiles (Add Yours, Music, Collage), **Recents ⌄**, **Select**, then the grid with a camera tile first [v18].
3. **Tap the media tile.** The editor can take about 2 s to appear even when the tool reports "settled": `wait` 1500 and look again before re-tapping.
4. **First-run popups** (e.g. "Introducing story-to-story sharing" → **OK**) [v18].
5. **Video:** a **trim screen** comes first (Back, Done, a filmstrip). Tap **Done** [v18].
6. **Editor** [v18]: right rail top to bottom: **Aa** (text), **sticker** (smiley in a square), music, effects (sparkles), sound, ⌄ (more tools). Bottom: **Add a caption…**, then the pills **Your story** and **Close Friends**, and a blue **→** arrow.
7. **Sticker tray:** tap the sticker icon (about x 0.92w, y 0.15h). The tray shows a **Search** field and pills: Location, @mention, Music, Add Yours, Frames, Photostrip, Photo, Cutouts, Captions, Questions, Avatar, emoji slider, Poll, **Link**, #hashtag, Countdown, then GIFs and Stickers [v18]. The text reader merges each icon into its word ("OLink", "& mention"): use `tap_text` with `exact: false`, or type the sticker's name into the tray's **Search**.

### Link sticker [v18]

1. `tap_text` `Link`, `exact: false` → **Add link** sheet: Cancel, Done, a **URL** field already focused (caret visible, no on-screen keyboard: that's normal), "See preview", **+ Customize sticker text**.
2. `type_text` the URL. Check the field shows it exactly.
3. `tap_text` `Customize sticker text` → a **Sticker text** field opens, focused. `type_text` the label. iOS capitalises the first letter: check it.
4. `tap_text` `Done`. A spinner replaces Done for 1-2 s while Instagram checks the link; `wait` 2000. The sticker lands in the centre of the Story.

### Poll, Questions, @mention, Location, Countdown [unverified]

Tap the pill (`exact: false`), type into the field the sticker opens, tap Done or tap outside it. Each sticker's own fields differ by version: read the screenshot and fill only what the intake gave. @mention and Location show a search list: pick the exact handle or place, not the first fuzzy match.

### Text overlay [unverified]

**Aa** › type the line › tap outside the text (or Done) to place it.

### Placement

Stickers land in the centre. **Don't drag stickers or text** to move them: a `drag` on a Story sticker left the touch held on 2026-11-18 (the editor stuck in "Drag to delete", and the sticker followed every later tap). If that happens: `home`, then `open_app` `Instagram`; the editor comes back released with the Story intact. If the user needs a sticker moved, finish as a draft and let them nudge it.

## Traps

- **`Your story` and `Close Friends` publish in one tap.** They are the bottom pills of the editor. Never tap either before the user approved the composed screen. The **→** arrow opens the share sheet instead.
- **The X (top left)** asks **Discard media?** with **Discard / Save draft / Keep editing** [v18]. Discard throws the work away.
- A video Story first shows the trim screen; its **Back** leaves without the media.
- Tapping inside the image can open the text tool. Tap controls, not the canvas.

## Stop and show

On the composed editor screen, before any publish tap: send the screenshot, the URL, the sticker label, the overlay text, the audience (Your story or Close Friends) and the account. Wait for an explicit yes.

- **Yes, post:** tap **Your story** (or **Close Friends** if that was chosen). Once only.
- **Draft instead:** X › **Save draft**. The user posts it later from the Story camera's drafts [unverified location].

## Proof

- Posted: back on Home, your avatar in the Stories row has a coloured ring. Open it (tap the avatar) and check the sticker is there, then `flick` `down` to leave.
- Draft: the Discard sheet closed after **Save draft** and the gallery shows again.

## Report

```txt
Story: posted to <Your story | Close Friends> | saved as draft
Account: @<handle>
Media: <description, date if known>
Sticker: Link -> <url>, label "<text>" | Poll "<q>" (<a>/<b>) | …
Overlay: "<text>" or none
Proof: <ring seen on avatar | draft saved>
Left for you: <anything, e.g. move the sticker>
```
