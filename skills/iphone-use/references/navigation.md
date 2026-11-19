# iOS navigation

Seen on iOS 26.4.1 (iPhone 14 Pro, 2026-11-03) `[v26]` and iOS 18.7.12 (iPhone XR, 2026-11-18) `[v18]`.

## Open an app

`open_app` with the **name under the app's icon**, which can differ from the App Store name: Chrome (not "Google Chrome"), Support (not "Apple Support"). It goes home, searches Spotlight, and taps only an app result. When it fails, its message says which case you're in:

| Message | Do |
|---|---|
| `No app named "…" is installed on this iPhone` | If it lists similar names, retry with the one the user meant. Otherwise tell the user the app isn't installed; [app-store.md](app-store.md) covers installing it |
| `"…" is installed …, but Spotlight didn't show it as an app` | Open it from the Home Screen or the App Library |
| `Spotlight didn't open` | `home`, then `open_app` once more |

Apps reopen on the screen they last showed: Settings on its last page, Notes inside the last note (possibly a personal one), Instagram inside a half-closed sheet `[v18]`. Read the screenshot after `open_app`, and get to the screen you need before typing anything.

`open_app` can report "settled" while the app's **splash screen** (its logo on a plain background) is still up `[v18]`: Instagram, TikTok, YouTube and LinkedIn all did. `wait` 2000–3000 ms until the app's own screen shows before acting.

## Move within an app

| Need | Do |
|---|---|
| One screen back | The app's back chevron or X. `back` (a left-edge swipe) is the fallback |
| Switch sections | `tap_text` the tab bar label |
| Tab bar missing | Many apps hide it while scrolled (Instagram profiles `[v18]`): a tap where it used to be lands on the content instead. Scroll up a little, or go back, and confirm the bar is visible before tapping it |
| Top of a long list | Tap the status bar at the top center |
| Close a menu, sheet, Spotlight or the emoji keyboard | `dismiss` |
| Leave the app | `home` |

## Home Screen

- `home` from an app lands on the Home Screen page you last used, not page 1. On the Home Screen itself it stays put.
- **Change page:** `flick` `left`/`right` or `drag` across 75% of the width, starting on **empty wallpaper** (just above the Search pill). A swipe that starts on an icon can press it and leave the page half-turned; `home` or a tap on the page dots clears that.
- **Spotlight:** tap the Search pill above the dock by position (its glass label can't be read by `find_text`), or let `open_app` do it.
- **Spotlight results** need about 1.5 s after typing. `wait` before reading them.

## Recover when lost

1. `screenshot` and name the surface: an app, Home Screen, App Library, Spotlight, a folder, icon-editing mode (icons jiggle), the App Switcher (app cards), Control Center, Notification Center, or the lock screen.
2. Leave it deliberately:
   - Menu, sheet or Spotlight: `dismiss`
   - App Switcher or Control Center: `home` (it taps the strip below the dock, which closes both)
   - Icon-editing mode: tap Done
   - Lock screen, or `Nothing sent: … locked`: `unlock` once
3. Still unsure: `home` once and start again from the Home Screen.

## Hazards

- Swipes from screen edges trigger system gestures: left edge goes back, bottom edge goes home or opens the App Switcher, top edges open Notification Center or Control Center. Start in-app gestures inside the content.
- A long press on a Home Screen icon opens its menu, and holding longer enters icon-editing mode. Use a tap to open an app.
