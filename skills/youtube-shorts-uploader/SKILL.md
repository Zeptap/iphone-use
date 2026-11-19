---
name: youtube-shorts-uploader
description: Upload a vertical video from the camera roll as a YouTube Short on the user's real iPhone with Zeptap - write a search-friendly title, set the audience and visibility, and stop at Upload for approval. Uploading through the YouTube Data API needs a Google Cloud project, OAuth consent and an audit for public videos; the YouTube app on the phone is already signed in. Without Zeptap it writes the title, description and settings. Use for "upload this as a YouTube Short", "post my latest video to Shorts", "put this clip on my YouTube channel as a short". For the same video on Reels and TikTok too, use short-video-cross-poster.
---

# YouTube Shorts uploader

Get a finished vertical video from Photos into YouTube as a Short with a title that gets found. Builds on `iphone-use`: its loop, connection check and safety rules apply.

Screens seen 2026-11-18 on iOS 18.7 [v18] up to the gallery button; everything after the gallery is **[unverified]** on a phone. Find each element on the current screenshot and read every screen before tapping.

## Use it for / hand off

- One vertical video, up to the length YouTube currently allows for Shorts [docs], to the user's own channel.
- Long-form uploads, playlists, Studio edits: outside this skill. Same clip to Reels and TikTok → `short-video-cross-poster`.

## Without Zeptap

Deliver the title, description and settings, then send the connect message from `iphone-use` with `utm_campaign=youtube-shorts-uploader`. The wall: API uploads need a Google Cloud project, OAuth and an audit before videos can be public.

## Intake

- Which video [newest vertical video in Recents]. Title topic or text [you write it].
- Visibility: Public, Unlisted, Private [Public, after approval].
- **Audience**: made for kids or not [not made for kids; ask if the content targets children: it's a legal declaration].
- Channel, if the account has several [the current one].

## Write it

- **Title, under 60 characters** so it isn't cut off: the search phrase first, then the hook. "Claude ordered my coffee on my iPhone" beats "You won't believe this".
- Add `#shorts` at the end of the title or description [docs: optional; vertical and short is what makes a Short].
- Description: one plain sentence plus 2-3 hashtags. A link is fine here (not clickable in the Shorts player).
- ASCII through typing; paste for emoji (`iphone-use/references/text-entry.md`). Show the text first.

## On the phone

1. `open_app` `YouTube`, `wait` 3000 (splash). Bottom bar: **Home**, **Shorts**, **⊕** (create), **You** (avatar) [v18]. The ⊕ is an icon: tap it by position (~0.62w, 0.94h).
2. First time: "To record, let YouTube access your camera and microphone" with **Continue**. Tap Continue: iOS asks for Camera, then Microphone: **`Don't Allow`** both. Uploads don't need them [v18].
3. The create screen shows "Let YouTube record using your camera and microphone", **Add from Gallery**, Open settings, and a `Video / Short / Live` switch with **Short** selected [v18]. Keep **Short**.
4. Tap **Add from Gallery**, then `wait` 3000.
   - **Seen 2026-11-18:** the screen dimmed and no picker appeared, twice. YouTube had never asked for Photos access (Settings › Apps › YouTube showed no Photos row) [v18].
   - Recovery: one more tap after the wait. If still nothing, `home`, reopen YouTube and try once. If it still fails, stop and ask the user to tap **Add from Gallery** once by hand and answer the Photos prompt themselves (granting access is their decision). Then continue.
5. Picker: choose the video [unverified]. Then the Shorts editor with trim and `Next`/`Done` [unverified: find it on the current screenshot]. Leave edits alone.
6. Details screen [unverified; labels from YouTube's help, find them on screen]: **Caption/Title** field: type the title and verify it; **Visibility**; **Select audience** → "No, it's not made for kids" unless the user said otherwise; then **Upload Short**.
7. Stop before **Upload Short** (below).

### Verified run [v18 2026-11-19]

1. Uploading needs a YouTube channel on the signed-in Google account. Without one, the app asks to **Create channel**, which accepts YouTube's Terms and publishes the name: stop and hand that to the user.
2. `+` (tab bar centre) opens the **camera**, so the room is on screen. Tap the gallery thumbnail (`Add`, bottom left `~0.09w, 0.79h`) right away. A previous draft triggers `Continue your draft video?`: pick `Start over` for a new file.
3. Gallery: tap the tile, `Next`. Trim screen: `Done`. Editor: `Next`.
4. **Add details:** tap `Caption your Short` and type the title. Typing `#` opens a hashtag picker that can **scramble the title** (seen: "The new way" became "The ny ... w wa"). Type the title without hashtags, or select all, delete and retype if it scrambles.
5. **Select audience** is required: `No, it's not made for kids` (unless it is). Back.
6. `Upload Short` (stop here for a yes when the user didn't pre-approve). The channel page shows the tile `Uploading · N%`, then `No views` when live.
7. **Delete:** the tile's `•••` → `Delete` → `Delete` on "Delete this video?" (permanent).

## Traps

- Settle fires early on the splash and after Add from Gallery: `wait` and look before re-tapping.
- Camera/mic prompts: `Don't Allow`. A Photos prompt: the user decides; recommend "Allow Full Access" only if they want, else "Limited Access" with the video selected.
- Leaving the editor may discard the Short [unverified]: if a "Discard?" prompt appears, read every option before tapping.

## Stop and show

Screenshot of the details screen, plus: channel, exact title, visibility, audience. Ask "Upload this Short now?" Uploading publishes per the visibility shown.

## Proof

After upload, You › your videos (or Shorts tab on the channel) lists the Short, possibly "Processing" for a minute [unverified]. Open it and check the title.

## Report

```txt
YouTube Short: <Uploaded | Stopped at details> on <channel>
Video: <which clip, duration>   Title: "<exact>"
Visibility: <…>   Audience: <not made for kids | made for kids>
Proof: <where it appears>   Unverified steps hit: <list>
```
