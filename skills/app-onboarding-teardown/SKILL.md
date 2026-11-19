---
name: app-onboarding-teardown
description: Tear down any iPhone app's onboarding and paywall on the user's real iPhone with Zeptap - walk from first launch through sign-up, permission asks and the paywall, screenshot every screen, and write up the copy, step count, what's asked for and when, the price, trial and plan layout, and the persuasion and dark patterns used. Simulators can't install App Store apps and web teardowns miss the native flow and real prices. It never subscribes, pays or starts a trial. Without Zeptap it gives the teardown template and what to capture on each screen. Use for "tear down Duolingo's onboarding", "how does Calm's paywall work", "screenshot this app's onboarding for my swipe file", "compare the paywalls of these three apps". To test your own app's journey for bugs use ios-real-device-testing.
---

# App onboarding teardown

Experience a competitor's first five minutes as a new user would, and turn it into a teardown a marketer or indie dev can act on. Builds on `iphone-use`: its loop, connection check and safety rules apply.

## Use it for / hand off

- Someone else's app (or your own, as a marketer) → here.
- Your own app, checking for bugs against expected results → `ios-real-device-testing`.

## Without Zeptap

Deliver the teardown template (below) and a capture checklist per screen (headline, body, buttons, what's asked, skip option, progress indicator). Then send the connect message from `iphone-use` with `utm_campaign=app-onboarding-teardown`.

## Start here: is the app on the phone?

1. Ask which app (name and developer). Then check: Spotlight-search its name (`open_app` reports if it's not installed).
2. **Not installed** → install it (below). That's a true first run.
3. **Installed and already used** → the onboarding won't show again. Offer a fresh run: "To see the onboarding as a new user, I'd delete <app> and reinstall it from the App Store. That erases its data on this phone (accounts stay on their servers). OK?" Only on a yes:
   1. Long-press the app icon › `Remove App` › `Delete App` › `Delete` [v18].
   2. Install it again (below), then open it.
   No yes → tear down what shows from the current state and say the onboarding wasn't seen fresh.
4. Free apps can still ask for an Apple ID password or Face ID on `Get`: that step is the user's.

## Intake

- **App** (exact App Store name and developer) and whether it's installed.
- **Fresh run?** A true first-run needs the app deleted and reinstalled, which erases its data on the phone. Default: no; tear down what shows from the current state, or install if it isn't on the phone. Deleting is the user's decision.
- **Persona** to answer quiz questions as (default: a plausible new user for the app's core audience).
- **Sign-up:** stop at sign-up (default), or continue with a throwaway account the user creates. Sign-in, codes and Apple ID sheets are user-only.

## Install (if needed)

Follow `iphone-use/references/app-store.md`: check the developer matches, ignore **Ad** results and lookalikes, show name, developer, price and size, and get a yes before **Get**. Paid apps: hand over. While on the listing, note for the teardown: subtitle, the first three screenshots' captions, rating and count, the **In-App Purchases** line.

## On the phone

1. `open_app` with the icon label. Take a screenshot of **every** screen, numbered, before acting on it. Splash screens report "settled" early: `wait` 1500 ms and look again before judging the first screen.
2. On each screen record:
   - **Headline and body**, word for word (they're the product being studied).
   - **Buttons**: primary label, secondary label, and whether a **Skip** / **Not now** / X exists and how visible it is.
   - **What's asked:** name, goal quiz, email, permission, rating, payment.
   - **Progress cue:** bar, dots, "Step 3 of 7".
3. **Quiz questions:** answer as the persona; note how many there are and whether answers seem to change later screens ("personalised plan").
4. **System permission prompts** (notifications, tracking, location, camera): record the app's pre-prompt and the moment it asks. Choose the least access (**Don't Allow**, **Ask App Not to Track**) unless the user said otherwise; the choice changes the phone, and denial is the reversible default.
5. **Account wall:** at "Sign in with Apple", email or phone sign-up, stop unless the user chose to continue. Record which methods are offered and whether there's a guest path.
6. **Paywall:** record position (step number), headline, plan cards with prices and periods exactly as shown, the default-selected plan, trial length and what happens after it ("then $59.99/year"), the close button (where, how small, delay before it appears: `wait` 3000 ms and re-check), and any "special offer" shown on close.
7. **Never** tap Start trial, Subscribe, Continue on a plan card, or anything that opens Apple's purchase sheet. If the purchase sheet appears by accident, it's user-only: dismiss it with its Cancel or X, never confirm.
8. Close the paywall by its X if one exists and note what follows (a downsell, a "limited" free mode, or a hard wall).

## Look for (dark patterns and persuasion)

Name each with the screen number:
- Hidden or delayed close button; tiny "Restore" or "Not now".
- Trial toggle on by default; yearly plan pre-selected with a crossed-out "monthly equivalent".
- "Free" in the headline when a trial auto-converts.
- Fake progress ("Building your plan…") used to raise commitment before the paywall.
- Confirmshaming ("No, I don't want to get better").
- Notification pre-prompt that wraps the system prompt in benefits.
- Social proof claims (ratings, user counts): record them as the app's claims, not facts.

## Report

```txt
Onboarding teardown: <App> (<developer>), iOS <version>, app version <if shown>, <date>

Summary: <n> screens to the paywall, <n> questions, sign-up at step <n>, paywall at step <n>, hard / soft wall.

| # | Screen | Headline (exact) | Asks for | Primary / secondary button | Skip? | Notes |

Paywall: plans and prices as shown, default plan, trial and terms, close-button behaviour.
Patterns: <pattern — screen #>.
What to steal: 3 specific moves that work.
What to avoid: 2-3 moves that cost trust.
Screenshots: <list, numbered to match the table>.
```

Prices are in the phone's App Store currency and region: say which.

## Leave the phone tidy

List what changed: app installed, permissions denied, account created. Offer to delete the app (the user's decision; follow `iphone-use/references/app-store.md`).

Evidence: this is a method for any app; no teardown run is recorded yet [unverified]. App Store steps come from `iphone-use/references/app-store.md` [v26].
