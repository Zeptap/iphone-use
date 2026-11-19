---
name: reddit-research
description: Research what real people said on Reddit in the last 30 days, on the user's real iPhone with Zeptap - search the question several ways in the signed-in Reddit app, sort by top and new for the window, read the busiest threads and their top comments, rank by engagement, and return the signal with numbers, dates and verbatim quotes - what people want, their exact words, tools praised and hated, open questions, and live threads worth answering. Reddit's API is closed to most apps and web search misses fresh threads and comments; the app shows them live and sorted. Without Zeptap it gives the search plan and report template. Use for "what is Reddit saying about cold email tools", "research my market on Reddit", "what do founders recommend for X", "last 30 days on Reddit about Y", "find threads where people want an app like mine". To reply to buyers use reddit-lead-finder; to build karma use reddit-karma-builder.
---

# Reddit research

The last 30 days of Reddit on a topic, ranked by what people actually engaged with, ending in a verdict the user can act on.

Builds on `iphone-use` and the `reddit` app guide (load it first). Read-only: no votes, comments or joins. Screens and taps are in the guide [v18 2026-11-19].

## Setup (ask once per topic, defaults in brackets)

1. **Topic or question** [ask; required]. One line.
2. **Why**: market research / buying decision / content ideas / find buyers [market research]. It changes the verdict.
3. **Window** [last 30 days]. Options: 7 days, 30 days, 12 months.
4. **The user's product and competitors**, if any [read the `Reddit brief`].
5. **Depth** [standard: 8-12 threads, top 10 comments each].

## Method (in order)

1. **Write 4-6 search phrasings** the way people actually ask: the problem ("how do you get first users"), the category ("best cold email tool"), comparison ("x vs y"), alternative ("alternative to <competitor>"), complaint ("<competitor> is so expensive").
2. **Search each in the app**: `Posts` tab, sort `Top`, time = the window. Then once more sorted `New` for anything from the last 3 days.
3. **Note the subreddits** that keep appearing (3+ hits). For the top 2-3, open the subreddit and browse `Top › This month` too.
4. **Shortlist threads** inside the window. Score each: `upvotes + 3 × comments`, halved if older than 3 weeks. Keep the top 8-12; skip `Promoted` and duplicates.
5. **Read each thread**: the post, then the top 10 comments (sort `Top`). Expand replies under any comment with 20+ upvotes.
6. **Extract**, keeping the source on every item (subreddit, date, upvotes):
   - **Wants**: what people are trying to do.
   - **Their words**: short verbatim phrases (under 15 words each).
   - **Tools**: each named tool with + and − counts and the reason in their words.
   - **Open questions**: asked, with no good answer in the thread.
   - **Live threads**: under 7 days old, still getting comments, matching what the user offers.
7. **Google check** (when the goal is buyers or content): in Safari, search `<main phrasing> reddit` and note which Reddit threads rank in the top 5. Threads older than 6 months are archived (no new comments): note them, don't plan replies.
8. **Verdict**: three bullets that answer the "why" from setup.

## Rules

- Inside the window only; older threads only to show the pattern is long-running, labelled as such.
- Numbers as shown (`1.2K`). Never estimate a count you didn't see.
- Quotes word for word and short; paraphrase anything longer.
- No conclusions from one thread. A claim needs 2+ threads or one thread with 50+ upvotes behind it.
- The AI summary at the top of search results is not evidence; use it only to find subreddits.

## Without Zeptap

Deliver the search phrasings, the subreddit guesses, the scoring rule and the report template, then the connect message from `iphone-use` with `utm_campaign=reddit-research`. The wall: Reddit's API is closed to most apps; the app shows live threads and comments sorted by time.

## Report

```txt
Reddit research: <topic> (last <window>, <date>, <n> threads, <n> comments read)

The signal
1. <finding> (<n> threads, top: r/<sub> <upvotes>)
2. ...
3. ...

Their words: "<phrase>" (r/<sub>, <date>), ...
Tools: <tool> +<n> / -<n> "<why>", ...
Open questions: "<question>" (r/<sub>, <age>, <n> comments, no good answer)
Live threads to answer: r/<sub> "<title>" (<age>, <n> comments) -> reddit-lead-finder
Ranks on Google: "<thread title>" (#<n> for "<query>", open|archived)
Subreddits that matter: r/<a> (<members>, <posts/day>), ...

Verdict: <three bullets for the user's goal>
```
