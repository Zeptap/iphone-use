---
name: reddit
description: App guide for Reddit on the user's real iPhone with Zeptap - the shared rules every Reddit skill follows - the account brief (accounts, product, voice, posting mode), how to read a subreddit's rules, the comment voice that survives on Reddit, account safety and the shadowban check, multi-account rules, and the Reddit app's screens. Load it before reddit-research, reddit-karma-builder, reddit-lead-finder or reddit-poster.
---

# Reddit (app guide and shared rules)

Every Reddit skill loads this file first. Rules live here once; job skills don't repeat them.

## The Reddit brief (first run of any Reddit skill, then reuse)

Look in Notes for `Reddit brief`. None → ask once, in one message, save it, and never ask again unless the user changes something.

1. **Accounts on this phone**: each `u/name`, and its role [one account]. Roles: `founder` (can name the product, always disclosed), `helper` (value only, never names the product publicly).
2. **Product** in one line, who it's for, 3-5 competitors, and the problems it solves in the buyer's words.
3. **Voice**: how the user talks; 2 example comments they like [the default voice below].
4. **Posting mode** [review first 3, then auto]:
   - `review`: show every comment and post before it goes.
   - `auto`: post within these rules and daily caps without asking; send the report after.
   - In every mode, the first 3 comments of a new account are shown for a yes.
5. **DMs** [off]: may the agent DM people who publicly asked for a recommendation? (rules below)
6. **Never**: subreddits, topics or people to avoid.

Per account, keep a log note `Reddit log u/<name>`: karma (post / comment), account age, phase, subreddits with their rules, threads already used, daily counts, flags.

## Read a subreddit before acting in it

Open the subreddit › `About` (or the `i` / info tab) › `Rules`, and the pinned posts. Record in the log, per subreddit:

| Field | Look for |
|---|---|
| Self-promotion | Banned / allowed with disclosure / only in a weekly thread / only "launched products" |
| Minimum karma or account age | Often in the rules or a pinned post ("accounts under 10 days are removed") |
| Post format | Required flair, title format, text-only, no links |
| AI content | Some subs ban AI-written posts: then every line must be the user's or rewritten to sound like them, never generic |
| Activity | Posts in the last 24 h; members |

Unknown minimums: assume **14+ days and 100+ comment karma** before posting, and keep to comments until then.

## The voice that survives on Reddit (tested on our own accounts)

- **Value first, every time.** Every comment and post gives the reader something: a step, a number, a mistake to avoid, a sharper way to see the problem. Pointed and crisp; one idea, said well.
- **Short.** One to three lines, like a text message. Lowercase and loose grammar are fine.
- **Two registers, picked by the thread:**
  - *Help threads* (questions, niche subs, lead finding, posts): straight value, no jokes at the asker's expense.
  - *Karma threads* (big casual subs, memes, absurd posts, P1 of the karma builder): dry, sarcastic or funny the way Redditors are; emoticons and emoji are fine when the sub uses them (`:)`, `lol`, 💀). Still specific to the post, never mean, never a punchline formula.
- **No colons, no lists, no "X: Y" setups, no headings** in comments. They read as AI.
- **Read the whole post and the top comments first.** Every comment shows you got it: a specific detail, a real question, a precise observation, or what you actually did.
- **Tone follows the thread.** Warm post, warm line. Absurd post, dry funny line. Plainly wrong, say so.
- **No generic praise** ("great post", "this is so helpful"), no backhanded jokes, no setup-punchline formulas.
- **Nothing sharp to say → skip.** Skipping is better than a filler comment.
- **No links** in comments unless someone asked for one and the sub allows it.
- **Brand**: never named by a `helper` account; named by a `founder` account only in the moments reddit-lead-finder allows, always disclosed ("i built x", "we make x").

## Account safety (what gets accounts banned, and the rule against it)

| Risk | Rule |
|---|---|
| New account acting fast | Follow the karma ladder in reddit-karma-builder; respect its daily caps |
| Promotion before trust | 90% value, 10% product at most, and none before the ladder allows it |
| Same text twice | Never paste the same comment or post in two places |
| Bursts | Space actions 2-6 minutes apart; one subreddit at a time |
| Links | Few, and only where allowed |
| Vote manipulation | **Never** upvote, downvote or reply to another of the user's own accounts, never ask anyone to vote. Two of the user's accounts never comment in the same thread. This is Reddit's rule and the fastest way to lose every account on the phone |
| Posing as a customer | A `helper` account never recommends the user's product as if unaffiliated |
| Ignored rules | Read the sub's rules first (above) |

## Shadowban and removal check (weekly, and after any warning)

1. In Safari, open a **private tab** › `reddit.com/user/<name>`. "page not found" or "suspended" while the app shows the profile = **shadowbanned**: stop all activity on that account and tell the user (appeal at reddit.com/appeals is theirs).
2. Open the account's 3 newest comments in the private tab. Missing or `[removed]` = removed by moderators or filters: note the subreddit, stop commenting there, and re-read its rules.
3. Two removals in one subreddit in a week → drop that subreddit for 2 weeks.

## Multi-account (several personas, never a ring)

- Each account has its own log, persona, subreddits and voice. Overlap in subreddits is fine; overlap in threads is not.
- Switch accounts in the app (avatar › account switcher) between sessions, not mid-thread.
- No account ever interacts with another of the user's accounts: no votes, replies, mentions or DMs.

## DMs (only if turned on in the brief)

- Only to someone who **publicly asked for a recommendation or help** in the last 7 days.
- First message never mentions the product: name their exact problem, say truthfully if you're in the same boat, ask one real question, offer something back. One or two lines.
- The product comes up only after they reply, disclosed.
- At most 5 new DMs per account per day; never the same person twice; stop on any "unwanted message" warning.

## On the phone [v18 2026-11-19]

- Search: magnifier at the top (`~0.5w, 0.08h`) → type → `enter`. Result tabs: All / Posts / Communities / Comments / Media / People.
- Sort and time: the `Relevance ⌄` and `All time ⌄` chips under the tabs. Set `New` or `Top` and `Past week` / `Past month` as the job needs.
- Post rows: `r/<sub> · <age>`, title, `<N> upvotes · <N> comments`. Promoted rows say `Promoted`: skip them.
- Comment: `Join the conversation` bar at the bottom of a post (tap by position); reply to a comment with its `Reply`. The send arrow posts. Back without sending shows `Save draft?`.
- Vote: arrows under the post or comment. Join a sub: `Join` on its page.
- Own karma and age: avatar › profile (`<N> karma`, `<age>` / cake day).
