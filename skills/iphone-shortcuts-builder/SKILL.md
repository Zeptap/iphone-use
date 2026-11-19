---
name: iphone-shortcuts-builder
description: Build any Apple Shortcut from a plain request on the user's real iPhone with Zeptap - plan the actions, add them in the Shortcuts app in an order that links each output to the next, set Share Sheet input, name it, and test it from the app where it will be used. Shortcuts can only be created inside the Shortcuts app on the device; nothing outside can install a custom one. Without Zeptap it writes the exact action list to build by hand. Use for "make a shortcut that saves links to my ideas note", "build an iOS shortcut for...", "add a share-sheet shortcut", "automate this with Shortcuts", "make a Siri shortcut that...". For Focus or notification settings, use iphone-use.
---

# iPhone Shortcuts builder

Turn a one-sentence request into a working shortcut, tested where the user will use it.

Builds on `iphone-use`: its loop, connection check and safety rules apply. Screens verified on iOS 18.7 [v18 2026-11-19].

## Use it for / hand off

- Any linear shortcut: share-sheet savers, one-tap routines, Siri phrases, Home Screen buttons.
- Focus or notification settings → `iphone-use`. Automations that run by themselves (Automation tab) only on explicit request, and say they run without asking.

## Without Zeptap

Write the action list: exact action names as Shortcuts shows them, every parameter value, input source (Share Sheet or none), the name, how to run it. Then the connect message from `iphone-use` with `utm_campaign=iphone-shortcuts-builder`. The wall: shortcuts are built only on the device.

## Intake (defaults in brackets)

- What it does, in one sentence [ask; required].
- Where it's triggered [Share Sheet if it acts on a link, photo or text; otherwise a tile tap].
- Names it uses: note, album, contact, playlist [ask if missing].
- May the test have real effects [only on the user's own items; never message others].

## Design rules (decide before touching the phone)

1. **Linear only.** No If, Repeat, Menu or Wait. If the job needs them, give the user the written action list for those parts.
2. **Each action must take the previous action's output automatically.** The Shortcuts editor links a new action's first input to the previous output when the types match (verified: Get URLs from Input → Shortcut Input; Append to Note → URLs). The variable picker and the variable suggestion bar above the keyboard **cannot be tapped through Zeptap** (taps fall through to the toolbar under it) [v18 2026-11-19]. So design the chain so every input is the previous output, and pick fixed values (a note, a contact) from lists.
3. If an action doesn't auto-link (its first token stays grey after adding), delete it and choose a different action that takes the previous type, or hand that link to the user as a one-tap instruction.
4. Prefer the shortest chain. Each extra action is a failure point.

## Recipes (tested)

- **Save idea (share sheet → note).** Receive input from Share Sheet → `Get URLs from Input` → `Append to Note` (note: the user's ideas note). Safari, Reddit, YouTube shares save the link. **TikTok shares save the page's full preview** (creator photo, caption, hashtags) instead of a bare link [v18 2026-11-19]; say so in the report.
- **Battery saver (tile).** `Set Low Power Mode` (On) → `Set Brightness` (50%).

## On the phone

1. Create the target first if the shortcut writes to one (e.g. a note named `Ideas inbox`): Notes → compose → type the title → `Done`.
2. `open_app` `Shortcuts`, `wait` 1500 (open_app may report Spotlight still open; look again). **All Shortcuts** shows tiles; `+` is top right (`~0.92w, 0.08h`). **Tapping a tile runs it.** Edit via the tile's `•••`.
3. Tap `+`, `wait` 1500. The editor shows `New Shortcut N` and a **Search Actions** sheet.
4. **Add an action:** tap **Search Actions** once (`~0.5w, 0.55h` when the sheet is low, `~0.5w, 0.87h` when it is collapsed), `wait` 1200, then `type_text` the exact action name. **Don't tap again before typing:** the field already has focus and a second tap lands on the app list (it selected "Amazon" as a filter twice). If a filter chip appears in the field, tap the field's X and retype. Tap the single result (`~0.32w, 0.24h`).
5. After each add, `wait` 1500 and check: the new action is last, and its first token is blue (linked) not grey.
6. **Share Sheet input:** tap the `ⓘ` in the bottom toolbar (`~0.5w, 0.94h`) → toggle **Show in Share Sheet** → `Done`. A `Receive … input from Share Sheet` block appears at the top and the next action links to `Shortcut Input` [v18].
7. **Fixed values** (note, contact): tap the grey token, `wait` 2000 (the chooser opens late), `tap_text` the item.
8. **Delete an action:** its `ⓧ` at the right (`~0.9w`). `wait` 1500 and confirm it's gone before the next tap; the settle fires early and the next tap can land on a different row.
9. **Name:** tap the title (`~0.69w, 0.08h`) → `Rename` → `command`+`a` → type the name → `enter` → `Done` (top right). The tile appears in All Shortcuts.
10. **Test where it's used.** Share-sheet shortcut: open the source app, tap Share → `More` (or the iOS share sheet) → drag it up → `tap_text` the shortcut's name. Tile shortcut: tap the tile once.
11. First runs show **privacy prompts** ("Allow … to access 1 TikTok item…", "…to append to a note?"). These are the user's choice: show them, wait for the user's answer, tap it. Expect 2-3 prompts on the first share-sheet run [v18].
12. Verify the result (the note gained the item; the setting changed). Reopen a note from the list to refresh it.

## Traps

- `▶` (bottom right of the editor) runs the shortcut immediately; it asks for input with a text box when there is none. `Cancel` it.
- Never tap a tile to "open" it: that runs it.
- Clean up test output that contains other people's content (e.g. a saved TikTok preview) if the user wants the note clean.

## Stop and show

Before a test that sends, posts or deletes; before creating an automation; before deleting any shortcut the agent didn't create.

## Report

```txt
Shortcut: <name> (<Share Sheet | tile | Siri>)
Actions: 1. <action - value> 2. ...
Test: <where, result>  Prompts answered: <list>
Limits: <e.g. TikTok saves page preview, not the bare link>
```
