# Alerts, sheets and overlays

Read the whole overlay before touching it. The buttons decide something, and the highlighted one is rarely the safe one.

## What to do

| Overlay | Do |
|---|---|
| iOS permission prompt ("<App>" Would Like to Access the Camera / Microphone / Photos / Contacts / Location) | The user's decision. If the job doesn't need it, choose **Don't Allow** (or **Allow Once**, **Limited Access**, **Ask App Not to Track**) and say so in the report. Uploading from the gallery doesn't need the camera or microphone `[v18]` |
| An app's own pre-prompt before the iOS one ("To record, let YouTube access your camera…" › **Continue**; "Find contacts" › **Don't allow** / **Open settings**) | Continue only leads to the iOS prompt above. Prefer the dismissive option when the job doesn't need the access `[v18]` |
| Two prompts in a row (camera, then microphone) | Answer each. The tap that triggered them usually did nothing else: tap the control again afterwards `[v18]` |
| First-run feature sheet ("Introducing story-to-story sharing", "Video posts are now shared as reels", "Share more: add up to 20 photos") | Read it, then **OK**. Avoid "View settings" / "Go to settings" `[v18]` |
| Upsell, premium or subscription offer | The dismissive option: "Not now", "No thanks", "Maybe later", or X |
| Notification opt-in inside an app, Rate this app | "Not now" |
| Full-screen interactive ad in a feed (TikTok "Shop now" takeovers) | Don't tap it. Flick past it; if the tab bar ignores a tap, `wait` 1500 ms and look again `[v18]` |
| "Allow Paste" | Allow only when you started the paste yourself |
| Sign-in, one-time code, Face ID, password, CAPTCHA, identity check | Stop. Tell the user exactly what appeared. They complete it |
| Rate limit or warning ("Try again later", "Action blocked") | Stop the task. Report the exact wording |
| Countdown that confirms on its own (rides, orders) | Reaching it counts as submitting. Only get there with the user's go-ahead |
| Discard prompt when leaving an editor ("Discard media?" / "Start over?" with **Save draft** and **Keep editing**) | Choose what the user asked for. Default for unapproved work: **Save draft** if the user wants to keep it, otherwise **Discard** / **Start over** `[v18]` |
| Notification banner at the top | Ignore it, or wait for it to leave. Don't tap it by accident |
| An on-screen control menu opened | Tap outside it |
| Control Center, the App Switcher or Notification Center | `home` |
| An app's first-launch welcome or data-use consent | Show the user; consent is theirs |

## Closing sheets

- Prefer the overlay's own button (X, Cancel, Done, a back chevron).
- `dismiss` closes most menus, Spotlight and the keyboard, but **not every in-app sheet**: Instagram's "Manage comments" sheet stayed open after two `dismiss` calls `[v18]`. Then tap the **dimmed area above the sheet**, or drag the sheet's grab handle down.
- Beware the screen under a sheet that didn't close: the next tap can land on a row inside it. On 2026-11-18 a tap meant for the tab bar opened "Change privacy settings" from a sheet that was still up.
- Tapping outside an iOS alert does nothing. Tapping outside an in-app sheet usually closes it.
- After closing, confirm with the screenshot that the screen underneath is the one you expected.
