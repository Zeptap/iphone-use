---
name: linkedin-engagement
description: Engage on LinkedIn from the user's real iPhone with Zeptap - after a one-time brief on who the user wants to be seen by (titles, companies, people, topics), find fresh posts from those people, react, and leave 2-5 thoughtful comments a day that the user approves, so the right people notice and visit their profile. LinkedIn's API doesn't let apps comment or react as a member; the signed-in app does. Without Zeptap it drafts comments for posts the user pastes. Use for "comment on LinkedIn posts in my industry", "do my LinkedIn engagement today", "engage with founders I follow on LinkedIn", "leave smart comments on AI posts", "get on the radar of VPs of marketing". To write and publish a post use linkedin-poster.
---

# LinkedIn engagement

A short daily session that puts the user in front of the people they want to reach: read, react, and leave a few comments worth replying to.

Builds on `iphone-use`: its loop, connection check and safety rules apply. Comments are public: each one needs the user's yes (or a yes on the batch).

## Start here: the engagement brief (first run, then reuse)

Look in Notes for `LinkedIn brief`. If it has no `engage:` section, ask once in one message and save it:

1. **Who to be seen by**: titles (e.g. "Head of Growth"), industries, company size, and any **named people or companies** [none].
2. **Topics** the user can comment on with real experience (3-5).
3. **Voice**: how they talk (short and direct, warm, technical) and 1-2 examples of comments they liked.
4. **Never engage with** [competitors' staff, politics].
5. **Daily cap** [3 comments, 15 reactions].

## The session

1. `open_app` `LinkedIn`, `wait` 3000. Read the brief.
2. **Find posts** (in order, until there are 5-8 candidates):
   - Named people first: search each name → their profile → `Activity` → posts from the last 48 hours.
   - Then search a topic → `Posts` filter → sort `Latest` [unverified labels].
   - Then the Home feed, keeping only posts from people who match the brief.
3. **Pick** posts under 24 hours old with active discussion but under 100 comments; skip anything on the never list.
4. **React** to all picks (long-press `Like` for `Insightful` or `Support` when it fits).
5. **Draft comments** for the best 2-5 (rules below) and show them as one batch: post author, first line of the post, the draft.
6. On the yes: open the post → `Comment` → `type_text` → check the text on screen → `Post`. Confirm it shows under the post. One every few minutes, not in a burst.
7. Log the session under `engage log:` in the brief (date, people, comments).

## Comment rules

- 2-4 sentences. Add **one** thing the post didn't have: a number from the user's experience, a short story, a counterpoint, or a sharp question.
- Name the specific point you're answering. Never "Great post!", never a pitch, never a link.
- Match the user's voice from the brief.

## Stops

- Any restriction notice, `You've reached the weekly invitation limit`, or a verification screen: stop and tell the user.
- Connection requests only when the user asks, each with a short note they approve.

## Without Zeptap

Run the brief questions, then draft comments for posts the user pastes, following the comment rules. Then the connect message from `iphone-use` with `utm_campaign=linkedin-engagement`.

## On the phone [v18 2026-11-16]

- Bottom bar: `Home`, `Jobs`, `My Network`, `Notifications`, `More`; search at the top.
- Under a post: `Like`, `Comment`, `Repost`, `Send`. The comment field opens at the bottom; `Post` sends it.
- Tested on 2026-11-16: browsing the feed and leaving 2 warm, specific comments.

## Report

```txt
LinkedIn engagement <date>: reactions <n>, comments <n> (cap <n>)
1. <author, title> "<post first line>" -> "<comment>"
People reached from the brief: <names>
Next: <who to look for tomorrow>
```
