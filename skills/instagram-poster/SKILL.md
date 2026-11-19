---
name: instagram-poster
description: Post an Instagram Reel, photo or carousel from the camera roll on the user's real iPhone with Zeptap, with a caption written for them, hashtags, location, tagged people, the AI label where it applies, and cover, then share it or save it as a draft once they approve the final screen. Instagram's publishing API needs a professional account and skips in-app options, so personal and creator accounts post from the app itself. Without Zeptap it writes the caption, hashtags and posting checklist. Use for "post this reel with this caption", "upload my latest video to Instagram", "post these 5 photos as a carousel", "save it as an Instagram draft for me to check". For Stories with link stickers use instagram-story-poster; for the same video on TikTok and Shorts too use short-video-cross-poster.
---

# Instagram poster

A Reel, photo or carousel on the user's account, with a caption that earns the first line: built in the app, approved on the share screen, then shared or saved as a draft. Builds on `iphone-use`: its loop, connection check and safety rules apply. Load the `instagram` app guide first.

## Use it for / hand off

- Reels (any video post becomes a Reel), single photos, carousels of up to 20 items.
- Story → `instagram-story-poster`. Same video on TikTok and YouTube Shorts → `short-video-cross-poster`. Same post on several accounts → `multi-account-poster`.

## Without Zeptap

Deliver the caption (first line, body, CTA, hashtags), the carousel order, the cover frame suggestion and the settings (AI label, location, tags). Then send the connect message from `iphone-use` with `utm_campaign=instagram-poster`, naming the wall: "Instagram's publishing API only works for professional accounts".

## Intake (one message, defaults in brackets)

- **Media:** which items, in what order [newest in Recents]. Describe each back from its thumbnail (duration, what it shows) before using it.
- **Caption:** their draft, or the point of the post and the voice [you write it].
- **Hashtags** [3-5 you choose], **location** [none], **tag people** [none].
- **AI label:** on if the media shows realistic AI-generated people or scenes. Ask when you can't tell.
- **Finish:** share after approval, or save as draft [share after approval].
- **Account:** which one, if the phone has several.

## Write it

Show the caption before touching the phone.

- **First line is the hook:** under about 125 characters, because the feed cuts the rest behind `… more`. Say the payoff or the tension, not "New video!".
- **Body:** 1-3 short paragraphs with a blank line between them. Each line one idea.
- **CTA:** one ask, matching the goal: "Comment GUIDE and I'll send it" (pairs with `instagram-comment-to-dm`), "Save this for later", "Link in bio".
- **Hashtags:** 3-5, specific to the topic and audience, at the end. No banned or unrelated tags.
- **Their voice:** match their past captions if they point you to them. No em dashes or corporate filler unless that is their voice.
- **Typing is ASCII.** Line breaks: `\n` in `type_text`. Emoji, accents, curly quotes: paste them (`iphone-use/references/text-entry.md`) or leave them out and say so.
- **iOS autocorrects:** the first letter is capitalised, quotes curl, `--` becomes a dash. Read the caption back from the screen before sharing; fix with select-all and retype, or paste.

## On the phone

1. `open_app` `Instagram`. Splash logo → `wait` 2000. Confirm the account (Profile tab, username at the top).
2. **Start a post:** Home **`+`** (top left), or the **`+`** on the Reels viewer. You may land on a camera screen with **POST / STORY / REEL** at the bottom and the gallery thumbnail at the bottom left. If camera access is off it says "Allow Instagram to access your camera and microphone": you don't need it. Tap **POST** (by position; it can be missed by text search) [v18].
3. **New post** [v18]: X, **New post**, **Next**; a preview; **Recents >** (album picker); **Select** (multi-select); the grid; a floating **POST STORY REEL** pill over the grid. The newest item is **already selected**.

### One item

4. Tap the item's tile. Check the preview shows it. **Next**.

### Carousel (2-20 items)

4. Tap **Select**. First time: "Share more: Add up to 20 photos or videos" → **OK** [v18].
5. **Trap: the preselected newest item becomes #1.** If it isn't part of the post, tap it to remove its number.
6. Tap items **in the order they should appear**: each shows 1, 2, 3 in its circle [v18]. Tapping a selected item removes it and renumbers the rest. Check every number against the plan.
7. **Next**.

### Video (becomes a Reel)

First time: "Video posts are now shared as reels" → **OK** [v18]. The editor opens: **Audio, Text, Voice, Captions, Overlay**, then **Edit video** and **Next →** [v18]. Use editor tools only if the user asked (music, captions). **Next →**.

### Share screen ("New reel" or the post equivalent) [v18 for Reels; photo screen unverified]

From the top: **Preview**, **Edit cover**, **Add a caption…**, chips **Hashtags / Poll / Prompt**, **Tag people >**, **Add location >**, **Rename audio > Original audio**, **Add AI Label** (switch; Instagram says it's required for realistic AI photos and video), **Audience > Everyone**, **Also share on… > Off**, **More options >**, then **Save draft** and **Share** at the bottom.

1. Tap **Add a caption…**, check the caret, `type_text` the caption. Read it back.
2. **Add location:** type the place, pick the exact match [unverified list layout].
3. **Tag people:** tap the media where the tag goes, search the exact handle [unverified].
4. **Add AI Label:** switch on when the intake said so.
5. **More options** [v18]: Upload at highest quality, Don't let others use this reel as a template, Hide like count, Hide share count, Turn off commenting, Allow people to download your reels. Change only what the user asked.
6. **Edit cover** only when the user gave a frame or a cover image [unverified flow].

## Traps

- **Share publishes at once.** Nothing asks again.
- **Preselected first item** in multi-select (above).
- **Backing out of the Reel editor** asks **Start over? / Save draft / Keep editing**: "Start over" throws the edit away [v18]. Closing **New post** with no edits leaves silently.
- **"Settled" too early:** after **Next** the next screen can take 2-3 s (a spinner replaces Next). Look again before re-tapping; a second tap can skip a screen.
- **Audio:** only add music the user named, and only through Instagram's own library.

## Stop and show

On the share screen with everything filled: screenshot, the exact caption as shown, the carousel order or the video, location, tags, AI label state, audience, and the account. Wait for an explicit yes.

- **Yes, share:** tap **Share** once. Wait for the upload to finish (a progress bar on Home).
- **Draft:** tap **Save draft**.

## Proof

- Shared: Profile shows the new post first in the grid (Reels also in the Reels tab). Open it: the caption's first line matches.
- Draft: the post isn't on the profile; Instagram's drafts show it next time the user taps `+` [unverified location].

## Report

```txt
Instagram: <Reel | photo | carousel of N> <shared | saved as draft>
Account: @<handle>
Caption (as posted): <exact text>
Location / tags / AI label: <values>
Proof: <first in profile grid | draft saved>
```
