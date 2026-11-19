---
name: reddit-poster
description: Write and stage a Reddit post that fits the subreddit, on the user's real iPhone with Zeptap - read the sub's rules and top posts, write a title and body in the sub's style, pick the right flair, and stop at the Post button (or save a draft) for the user's yes. Reddit's API is closed to most new apps, and posting from the user's own signed-in app keeps their account history and karma intact. Without Zeptap it writes the title, body, flair choice and a rules check. Use for "post this to r/SaaS", "write a Reddit post about my launch", "share my shortcut on r/shortcuts", "draft a Reddit post for me to check". For daily engagement to build karma use reddit-karma-builder; for finding threads to answer use reddit-research.
---

# Reddit poster

Stage one post that the sub's moderators and readers will accept, then stop for a yes.

Builds on `iphone-use` and the `reddit` app guide (load it first: brief, voice, safety). Posting follows the brief's posting mode: `review` shows the final screen for a yes, `auto` posts and reports. Only accounts at Phase 3+ (reddit-karma-builder) post.

## Use it for / hand off

- One post to one subreddit (text, link or image) from the user's account.
- Karma and daily engagement → `reddit-karma-builder`. Finding threads to reply to → `reddit-research`.

## Without Zeptap

Deliver: the title (2 options), the body, the flair, and a rules checklist with each rule marked pass/fail. Then the connect message from `iphone-use` with `utm_campaign=reddit-poster`.

## Intake (defaults in brackets)

- Subreddit [ask; required]. What to share [ask].
- Is it the user's own product? [ask] → yes means disclose it in the body ("I built this").
- Link, text or image post [text].
- Post or draft [draft for review].

## Pick the post type (these get upvoted)

| Type | Shape | Works for |
|---|---|---|
| Story | What happened, what you learned, one detail people can steal | Founders building in public |
| Guide | "How I did X" with the exact steps and numbers | Solution-aware readers |
| Problem / ask | "Struggling with X, here's what I tried, what am I missing?" | Starting conversations, research |
| Comparison / list | "I tried 5 tools for X, here's what each is good at" (fair, yours disclosed) | Buyers comparing |
| AMA | "I did X, ask me anything" | Authority in a niche, Phase 4 |

The product, if anywhere, is one disclosed line near the end of a post that's useful without it. 90% value, 10% product.

## Write it (rules, in order)

1. **Read the rules first** (step 2 on the phone). If self-promotion is banned or limited to a weekly thread, say so and stop; offer to write a value post without the link.
2. **Match the sub's top posts this month**: their title length, tone, and whether they lead with a question, a result or a build story.
3. **Title** = the specific outcome or question in plain words, under 100 characters. No clickbait, no emoji unless the sub uses them.
4. **Body**: what it is, what you learned or why it matters, one concrete detail (a number, a step, a screenshot), and a question that invites replies. Disclose ownership in the first two lines when it's the user's product. Links at the end, once.
5. In `review` mode show title + body + flair before typing; in `auto` mode post and report.

## On the phone

1. `open_app` `Reddit`, `wait` 3000. Tap search (`~0.5w, 0.08h`), type `r/<sub>`, `enter`, tap the community.
2. Open the sub's **About/Rules** (community header `…` or `See community info`). Read every rule. Then sort the feed **Top › This month** and read 5 titles.
3. Start a post: from the sub, tap `+`/`Create post` (top right `~0.72w, 0.08h` on the community screen [v18 2026-11-19]). The composer opens with the community preselected.
4. Tap **Title** and `type_text` the title. Check it on screen.
5. **Body**: tapping the body area may not focus it. Double-tap the body placeholder (`~0.1w, 0.33h`), `wait` 800, then type. If nothing changes, tap the title and press `tab` once, then type [v18 2026-11-19]. Read the body back from the screenshot; fix autocorrect.
6. **Flair**: tap `Add tags & flair` / `Flair`, pick the flair that matches the post type, confirm. Required-flair subs block `Post` until set.
7. `review` mode: screenshot with community, title, body and flair, ask "Post this to r/<sub>?". `auto` mode: go on.
8. Post: tap `Post`, `wait` 3000, open the new post and confirm it's live. On "draft": tap back (top left), choose **Yes, Save** on the "Save draft?" sheet [v18 2026-11-19].

## Traps

- Back without choosing loses the text on some versions; always answer the Save draft sheet.
- New accounts and low karma: many subs auto-remove posts silently. If the post isn't visible in the sub's New feed after 2 minutes, report "likely auto-removed" and suggest `reddit-karma-builder` first.
- Never post the same text to several subs in a row (spam filter); one sub per run unless the user approves each.

## Report

```txt
r/<sub>: <Posted | Draft saved | Stopped: rule X>
Title: "<title>"
Flair: <flair>  Disclosure: <yes/no/not needed>
Rules checked: <n> (<any warnings>)
Link: <post URL if posted>
```
