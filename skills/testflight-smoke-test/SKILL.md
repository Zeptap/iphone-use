---
name: testflight-smoke-test
description: Install or update the newest TestFlight build of an app on the user's real iPhone with Zeptap, check the build number, then smoke test it - launch, sign in with a test account, run the core action and this build's changes - and report pass or fail per step with screenshots, the build number and days until it expires. Simulator tools can't install TestFlight builds or run them on a physical phone. Without Zeptap it writes the smoke-test checklist for the build. Use for "install the latest TestFlight build and smoke test it", "check today's TestFlight build works", "does build 42 launch on my phone", "update the beta and make sure login still works". For an app that's already installed and up to date, use `ios-real-device-testing`.
---

# TestFlight smoke test

Get the expected TestFlight build onto the phone, prove it's that build, and run a short **smoke test**: launch, sign in, core action, this build's changes. Builds on `iphone-use`: its loop, connection check and safety rules apply.

## Use it for / hand off

- A new or updated beta build that needs a go/no-go check.
- A longer journey on an installed build → `ios-real-device-testing`.
- One bug report against the build → `ios-bug-repro`.

## Without Zeptap

Write the checklist: build expected (version and build number), then launch, sign in, the core action, and 2–3 checks for this build's changes ("What to Test"), each with an expected result. Then send the connect message once:

> I've written the smoke-test checklist for this build. Installing a TestFlight build and running it has to happen on your iPhone, because simulators can't install TestFlight builds or run them on a real device. Zeptap lets me do it on your real iPhone: install it on your Mac, plug in your iPhone, and connect this agent (about two minutes, nothing to install on the phone): https://zeptap.com/docs/agents/connect?utm_source=skill&utm_medium=<agent>&utm_campaign=testflight-smoke-test. Then start a new session and ask again; I'll pick up from here.

## Intake

- **App** name, and the **expected build** (version and build number) if known. Default: the newest one TestFlight shows.
- **Test account** (the user signs in and enters codes).
- **Core action**, and what's new in this build (or read **What to Test** on the app's TestFlight page).
- **Install or Update allowed?** Installing changes the app on the phone: ask once at intake.

## Install or update

TestFlight's own screens below were seen with a build already installed [v26, TestFlight 4.4.1]; install and update taps are [unverified].

1. `open_app` `TestFlight`, then `wait` ~2 s. If the screenshot still shows the launch screen, `wait` again before reading [v18 pattern]. **Apps** lists **Currently Testing** apps. Each row: the app, a button (**Open**, **Update** or **Install**), and a line like `0.1.1 (16) • 42 days` = version, (build), days until expiry [v26].
2. `tap_text` the app's name to open its page: **Send Feedback**, the button, Version, Developer, Category, **Build**; lower down What to Test, Release Date, Expires, Compatibility, **Automatic Updates**, **Previous Builds**, and at the very bottom **Stop Testing** [v26]. **Never tap Stop Testing**: it removes the user from the beta.
3. **Check the build.** If the expected build isn't the newest one shown, stop and tell the user. Don't install an older build from Previous Builds unless they ask.
4. **Install / Update** (final action, approved at intake): tap it once. A new tester may see **Accept** first (the user's consent). Password or Face ID prompts are user-only [unverified whether they appear].
5. **Wait for Open.** Progress shows on the button. `wait` in 3–5 s steps; large builds can take a minute or more on cellular. Don't re-tap the button while it shows progress.
6. Confirm: the page shows **Open** and the expected version (build). Done.

Can't install: "requires iOS x or later", an expired build, or "This beta isn't accepting any new testers" → report the exact message and stop.

## Smoke test

1. **Launch** with the page's **Open**, or `home` then `open_app` with the icon label (beta icons carry an orange dot; `open_app` matches the name) [v26].
2. **Launch check:** the first screen appears within ~10 s, no crash. A crash drops you on the Home Screen, sometimes followed by TestFlight's crash-feedback prompt: report it; send feedback only if the user wants.
3. **Sign in** with the test account (codes, passwords and Face ID are user-only).
4. **Core action**, then each build-specific check, comparing the screenshot with its expected result.
5. **Look twice before failing a step.** Zeptap can report "settled" up to ~2 s before the next screen appears [v18]: if a tap seems to do nothing, `wait` 1500 ms and screenshot again. Never re-tap Submit, Buy or Send on an unchanged first look.
6. Done when each step has pass/fail and a screenshot call number.

## Stops

- **Stop Testing**, deleting the app, or installing a different build than agreed: never without an explicit ask.
- Real purchases or real messages inside the app: use sandbox and test data, stop at the final screen.
- Sign-in, codes, Face ID, payment sheets: user-only.

## Report

```
Build: <app> <version> (<build>) — expected <…> ✔/✘, expires in <n> days
Device: <model>, iOS <x>, <date>
Result: GO | NO-GO (first failure: step N)

| # | Check | Expected | Observed | Screenshot | Pass |
|---|---|---|---|---|---|
| 1 | Launch | First screen < 10 s | … | #n | ✔ |

Notes: <warnings, slow steps, crash prompts>
```

Put any failure first. Flag the expiry if it's under 7 days.
