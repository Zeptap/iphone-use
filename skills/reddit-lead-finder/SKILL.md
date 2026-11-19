---
name: reddit-lead-finder
description: Find people on Reddit who are asking for a product like the user's right now, and answer them, from the user's real iPhone with Zeptap - search buyer phrasings sorted by new, score each thread for buying intent, check which threads also rank on Google, then post a reply that answers the question first and mentions the product second (disclosed, only where the subreddit allows it), and optionally send a curiosity-first DM to people who asked publicly. Uses the user's own trusted accounts in the signed-in app, never rented accounts or vote boosting. Without Zeptap it gives the keyword plan, intent scoring and reply drafts. Use for "find leads on Reddit", "get customers from Reddit", "who on Reddit wants a tool like mine", "reply to people asking for alternatives to a competitor", "find Reddit threads that rank on Google for my keywords". For market research use reddit-research; for building karma first use reddit-karma-builder.
---

# Reddit lead finder

Be the most useful answer in the threads where buyers are asking, minutes or hours after they ask, and on the threads Google and AI already show.

Builds on `iphone-use` and the `reddit` app guide (load it first: brief, voice, safety, DM rules). Screens and taps are in the guide [v18 2026-11-19].

## Start here

1. Read the `Reddit brief` (none → ask its questions). Lead finding needs a `founder` account (can name the product, disclosed).
2. That account must be **Phase 3 or higher** in its `Reddit log` (reddit-karma-builder). Lower → say so and run a karma session instead. Helper accounts may still answer without naming the product.
3. First run only, add to the brief: **buyer keywords** (below), the **one-line disclosure** the user is happy with ("i built x", "i'm the founder of x", "we make x"), and the 2-3 things the product does better than the competitors, in plain words.

## Buyer keywords (build once, refine every run)

| Intent | Patterns |
|---|---|
| Asking for a tool (highest) | "best <category> for <job>", "recommend a <category>", "any tool that <job>", "looking for an app to <job>" |
| Switching | "alternative to <competitor>", "<competitor> too expensive", "leaving <competitor>" |
| Comparing | "<a> vs <b>", "is <competitor> worth it" |
| Problem | "how do you <job>", "struggling with <job>" |

## Find (each run)

1. Search each keyword in the app: `Posts`, sort `New`, time `Past week`. Then the same for the promo and niche subreddits from the log, sorted `New`.
2. Google check (weekly): in Safari, `<keyword> reddit`; note Reddit threads in the top 5. Open ones (under 6 months) go on the list; archived ones are skipped.
3. **Score** each thread:
   - Intent: tool ask 3, switching 3, comparing 2, problem 1.
   - Freshness: under 2 h +2, under 24 h +1.
   - Visibility: ranks on Google +2; 20+ comments +1.
   - Fit: the product really solves what they asked (no → drop it).
4. Skip: the sub bans promotion (answer value-only or skip), the user's other account already commented there, a thread already in the log.
5. Work the top 3-5 by score.

## Write the reply (the order is the rule)

1. **Answer the question** in 2-4 short lines with something they can use now: the criteria that matter, a step, what to avoid. This must stand alone without the product.
2. **Bridge, only if fit is real and the sub allows it**: one line with the disclosure, e.g. "i built x for exactly this, it does <the one thing they asked>". No link unless they asked or the sub allows it; offer "happy to share the link" instead.
3. Name competitors fairly when they fit better; credibility is the asset.
4. Voice rules from the `reddit` guide: short, no colons, no lists, no praise filler, no copy-paste between threads.
5. At most **1 in 10** of the account's comments may name the product (count in the log). Over the ratio → value-only reply.

## Post

Posting mode from the brief: `review` shows the batch (thread, score, reply); `auto` posts and reports. Space replies 3-6 minutes apart, different subreddits. After posting, open the thread in a Safari private tab to confirm the reply is visible; `[removed]` → log it, no more mentions in that sub, re-read its rules.

## DMs (only if turned on in the brief)

To the poster of a score-5+ thread who asked publicly, after the public reply: the curiosity-first opener from the `reddit` guide (their problem, one real question, no product). Product only after they reply, disclosed. Max 5 a day per account.

## Follow-up

Next run, before finding new threads: open the account's recent replies, answer every reply to them, and note any "thanks, trying it" or questions (a warm lead: log it for the user).

## Without Zeptap

Run the brief and keyword setup, then give the search plan, the scoring sheet and reply drafts for threads the user pastes, then the connect message from `iphone-use` with `utm_campaign=reddit-lead-finder`. The wall: posting from the user's own trusted account happens in the signed-in app.

## Report

```txt
Reddit leads - u/<name> - <date>
Found <n> threads, answered <n> (<n> with product mention, ratio <x>/10)
1. r/<sub> "<title>" (<age>, score <n>, Google #<n>|-) -> "<reply first line>"
Removed: <none|detail>   DMs: <n sent | off>
Warm leads: u/<name> "<what they said>" (<thread>)
Keywords to add: <phrasings seen in threads>
```
