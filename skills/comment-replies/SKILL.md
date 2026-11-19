---
name: comment-replies
description: Reply to comments on the user's own posts on their real iPhone with Zeptap - open the post in Instagram or YouTube, read the unanswered comments, draft replies in the user's voice, show them as one batch for approval, then post each reply under the right comment. Replying from the user's own app keeps it native and works for personal accounts the APIs exclude. Without Zeptap it drafts replies from comments the user pastes. Use for "reply to comments on my last reel", "answer the questions under my YouTube video", "clear my unanswered comments", "reply to everyone asking about the price". To send DMs to commenters use instagram-comment-to-dm; for content ideas from comments use content-ideas-from-comments.
---

# Comment replies

Answer the comments that deserve a reply, in the user's voice, after one batch approval.

Builds on `iphone-use`: its loop, connection check and safety rules apply. Replies are public: the batch needs a yes before the first one posts.

## Use it for / hand off

- The user's own Instagram posts and YouTube videos (Shorts and long-form).
- DM the link to commenters → `instagram-comment-to-dm`. Video ideas → `content-ideas-from-comments`.

## Without Zeptap

Draft replies for comments the user pastes, following the rules below. Then the connect message from `iphone-use` with `utm_campaign=comment-replies`.

## Intake (defaults in brackets)

- Which post [the newest]. Platform [Instagram].
- Voice [match the user's existing replies]. Skip list [spam, hate, bots].

## Reply rules

- Reply to: questions, honest feedback, first-time commenters with a real sentence. Skip: emoji-only, spam, links, hate (report hate to the user, don't engage).
- One or two short sentences. Answer the question; add one useful detail. No links unless the user approved one. Never copy-paste the same reply twice in a row.
- Show the batch (comment → reply) before posting.

## On the phone: Instagram [v18]

1. `open_app` `Instagram`, `wait` 1500. Profile (bottom right) → tap the post.
2. Tap the **speech bubble** under the media → **Comments** sheet. Rows: avatar, username, age, text, **Reply**, heart. Drag inside the list (`0.8h → 0.4h`) to load more. Expand **View replies** to see if the account already answered.
3. For each approved reply: tap **Reply** under that comment, check the field targets the right person, `type_text`, verify on the screenshot, `press_key` `enter`.
4. Confirm the reply appears under the comment, then the next.
5. Close the sheet by tapping the dimmed post above it.

## On the phone: YouTube [unverified]

1. `open_app` `YouTube` → **You** → **Your videos** → the video → the comments panel under the player.
2. Each comment has a reply icon; tap it, type, check, send. YouTube Studio (if installed) lists unanswered comments across videos: prefer it for batches.

## Traps

- The emoji row above **Add a comment…** may post an emoji in one tap. Don't touch it.
- **Add a comment…** without **Reply** posts a top-level comment.
- `enter` posts immediately: only press it on checked text.
- Stop on "Try Again Later", "Action Blocked" or any warning: quote it and end the job.

## Report

```txt
Comment replies on <post> (<platform>)
Replied: <n>  Skipped: <n> (spam <n>, already answered <n>)
1. @<user>: "<comment>" -> "<reply>"
Flagged for you: <hate, legal, unusual>
```
