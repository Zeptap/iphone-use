# The Settings app

Seen on iOS 26.4.1 (iPhone 14 Pro, 2026-11-03) `[v26]` and iOS 18.7.12 (iPhone XR, 2026-11-18) `[v18]`.

## Find a setting

1. `open_app` `Settings`. It reopens on the last page shown (seen `[v18]`: it came back on Larger Text). Use the page's back button (`Back`, or the parent's name at top left) until you reach the top level.
2. **Search.** Where the field sits depends on the iOS version:

   | iOS | Search field |
   |---|---|
   | iOS 18 and older `[v18]` | **Top** of the top level, under the "Settings" title. Tapping it opens Suggestions (Accessibility, Text Size, Bluetooth, Date & Time) and Recents, with **Cancel** at top right |
   | iOS 26 and newer `[v26]` | **Bottom** of the top level |

   Tap it, select all (`a` with `command`) in case it holds an old query, type the name, then `wait` **2000 ms** before reading. On iOS 18 the list first shows "No Results" and fills in about 1.5 s later `[v18]`.
3. Each result shows its **path** under its name (`Bold Text` › `Accessibility → Display & Text Size` `[v26]`; `YouTube` › `Apps` `[v18]`). Tap the one whose path matches.
4. **Search doesn't find everything.** On iOS 18, "Larger Text" returned No Results even after 2.5 s `[v18]`. When search fails, browse.
5. **Browse:** `tap_text` the row label. Off screen: `drag` from about 75% to 30% of the height at the centre, then `find_text` again. Tap the status bar to return to the top.

A row's value ("Off", "On", "Everyone") is a separate text line at the same height as its label: pair them by `y`.

## Paths seen

| Setting | Path |
|---|---|
| Text size | Accessibility › Display & Text Size › Larger Text `[v18]` `[v26]` |
| Bold Text | Accessibility › Display & Text Size › Bold Text (a switch on that page) `[v18]` |
| An app's permissions (camera, microphone, photos, notifications) | Search the app's name › the result under **Apps** `[v18]`. The page lists only the permissions that app has asked for: YouTube showed Local Network, Microphone, Camera, Siri, Search, Notifications, Live Activities, Background App Refresh, Cellular Data, Allow Tracking, and **no Photos row** because it had never asked |
| Notifications for an app | Settings › Notifications › the app `[v26]` |
| Focus | Settings › Focus `[v26]` |
| About (model, iOS version) | General › About `[v26]`, or `list_phones` |

## Switches

- Tap the **centre of the switch track**.
- Read the state from the result: green (or the accent colour) with the thumb on the right is **on**; grey with the thumb on the left is **off**.
- A page with one switch often shows its other options only when it's on.
- If the state didn't change, re-find the switch and tap once more. After two failures, stop and report.

## Sliders with steps

Tap the **tick** you want: the thumb snaps to it exactly `[v18]`. Dragging the thumb lands short, because content moves about 0.85× the drag distance. Count ticks from the screenshot; their spacing differs by model (about 75 px on an XR), so never use a fixed pixel step.

## Changes need approval

Settings changes affect the whole phone. Before changing a setting the user didn't name, say what you'll change and why. Take extra care with:

- Privacy, location, tracking and app permissions
- Accounts, passwords, Apple Account and iCloud
- Screen Time, Face ID and passcode
- Bluetooth, Airplane Mode, Wi-Fi and the Accessibility › Touch settings: Zeptap needs them, and turning them off disconnects you mid-task
- Resetting or erasing anything

## Leave it as you found it

Screenshot the page before changing a setting for a task, restore it at the end, and verify the restore with a screenshot that matches the first one.
