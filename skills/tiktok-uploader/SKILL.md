---
name: tiktok-uploader
description: Upload a video from the camera roll to TikTok on the user's real iPhone with Zeptap - write the caption and hashtags, set comments, reuse, the AI-generated label and branded-content disclosure, then save it to Drafts or stop at Post for approval. Apps that haven't passed TikTok's audit can only post privately through the API, so public posts and Drafts happen in the app. Without Zeptap it writes the caption, hashtags and settings checklist. Use for "upload this video to TikTok", "save my latest video to TikTok drafts", "post my render to TikTok with this caption", "put this clip on TikTok and label it AI". For the same video on Reels and Shorts too, use short-video-cross-poster.
---

# TikTok uploader

Take a video from Photos to TikTok's post screen with a caption that works, the right settings, and the user's choice of **Drafts** or **Post**. Builds on `iphone-use`: its loop, connection check and safety rules apply. Load the `tiktok` app guide first.

Screens seen 2026-11-18 on iOS 18.7 [v18] unless tagged. Find each element on the current screenshot.

## Use it for / hand off

- One video (or a photo carousel) from the camera roll to the user's own TikTok account.
- Same video to Reels and Shorts → `short-video-cross-poster`. Several accounts or phones → `multi-account-poster`. Editing the video itself (cuts, effects) is outside this skill: upload the finished file.

## Without Zeptap

Deliver the caption, 3-5 hashtags, the settings list (comments, reuse, AI label, disclosure) and Drafts-or-Post, then send the connect message from `iphone-use` with `utm_campaign=tiktok-uploader`. The wall: TikTok's API posts only privately for apps that haven't passed its audit.

## Intake (one message, defaults in brackets)

- Which video: "the newest" [newest video in Recents], or a description (length, first frame, date).
- Caption: the user's text, or the topic and tone [you write it].
- **Drafts or Post** [Drafts].
- Made or edited with AI? [ask if the video looks generated; TikTok's label exists for this].
- A paid brand deal? [no] → yes means Content disclosure and ads.
- Comments and reuse (Duet/Stitch) [both on]. Account, if the phone has several [the signed-in one].

## Write it

TikTok captions are searched like titles. Write:
- **Line 1 = the search phrase plus the hook**, as viewers type it: "how to get your first 100 customers (no ads)". Plain words beat clever ones.
- One or two short lines of context or a question that invites comments. No link (TikTok doesn't make caption links clickable).
- **3-5 hashtags**: 1-2 broad (#smallbusiness), 2-3 specific (#coldemailtips). No #fyp padding.
- ASCII only through typing. Emoji or accents: paste (see `iphone-use/references/text-entry.md`) or leave them out and say so.
- Show the caption to the user before touching the phone.

## On the phone

1. `open_app` `TikTok`, `wait` 2500 (splash). Close popups.
2. Tap **`+`** (centre of the tab bar). The camera opens with modes (`10m`, `60s`, `15s`, `PHOTO`, `TEXT`) and `CAMERA / CREATE / LIVE` at the bottom [v18].
3. Without camera access the screen reads "Create on TikTok … Access camera / Access microphone". **Uploads don't need either.** Tap the **gallery thumbnail at the bottom left** (~0.08w, 0.93h). The first tap may raise the iOS camera and microphone prompts instead: tap `Don't Allow` on each, then tap the thumbnail again [v18].
4. After the tap, `wait` 2000: the gallery can take ~2 s while Zeptap already reports settled [v18].
5. **Gallery**: `Recents ⌄` (album picker) top centre, `Text` top right, tabs `All / Videos / Photos / Live Photos / AI gallery`. **Select multiple is on by default** (red check bottom left). Tap the **circle** at a tile's top right: it shows `1`. Check the tray at the bottom shows the right clip and duration [v18].
6. `tap_text` `Next` (beside `AutoCut`), then `wait` 2500 [v18].
7. **Editor**: `Add sound` top, tools on the right rail (settings, share, crop, text `Aa`, stickers, effects, voice, captions), `AutoCut` centre bottom. Bottom: **`Your Story`** and **`Next`**. Leave the edits alone unless asked. `tap_text` `Next` [v18].
8. **Post screen** [v18]:
   - `Add description…`: tap it, `type_text` the caption, then read it back from the screenshot (iOS capitalised "test" to "Test").
   - `# Hashtags`, `@ Mention` chips (optional; typing `#tag` in the description works).
   - `Location` with suggested places (only if asked).
   - `Everyone can view this post` › visibility.
   - **`More options`**: `tap_text` may miss this row; tap it by position (~0.2w, 0.57h) [v18]. Inside: `Allow comments`, `Allow reuse of content` (Duet, Stitch, stickers, add to Story), `Add link` (greyed out on small accounts), **`Content disclosure and ads`** (branded content for paid deals), **`AI-generated content`** label, `Auto-check sound copyright`. Set what the intake says, then close with the X.
   - `Share to` (other apps; leave off unless asked).
   - Bottom: **`Drafts`** and **`Post`**.
9. **Drafts** (default): tap `Drafts`. Proof: Profile › the first grid tile reads `Drafts: N` with N one higher [v18].
10. **Post**: stop, show the final screen (below), and tap `Post` only on a fresh yes.

## Traps

- **`Your Story` on the editor publishes a TikTok Story in one tap** [v18]. Never tap it unless the user asked for a Story.
- **Backing out discards silently.** Back from the post screen or the editor lost the caption with no "save draft?" prompt [v18]. Keep work by tapping `Drafts`.
- **Settle fires early.** After `+`, the gallery, `Next`: if the screenshot didn't change, `wait` 1500 and look again; never re-tap `Next` or `Post` on an unchanged screen.
- Permission prompts: `Don't Allow`. Contacts sheet: `Don't allow`.
- Full-screen interactive ads on For You can swallow the first tab-bar tap: look before tapping again.

## Stop and show (before Post)

Screenshot of the post screen, plus: the account (`@handle`), the caption exactly as on screen, visibility, comments/reuse, AI label on/off, disclosure on/off. Ask: "Post this now?" `Post` publishes at once.

## Proof

- Drafts: `Drafts: N` tile on the profile.
- Post: TikTok shows upload progress, then the video appears first in the profile grid with `▷ 0`. Open it and check the caption.

## Report

```txt
TikTok upload: <Draft saved | Posted> on @<handle>
Video: <which clip, duration>
Caption: "<exact text>"
Settings: visibility <…>, comments <on/off>, reuse <on/off>, AI label <on/off>, disclosure <on/off>
Proof: <Drafts tile count | first grid tile, views shown>
```
