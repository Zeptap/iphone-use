# iPad layout: columns, Home Screen, multitasking

Observed on an iPad Air (4th generation), iPadOS 16.3.1, in landscape, 2026-11-04. Steps marked *(unverified)* haven't
been run on an iPad yet.

## Sidebars and columns

Settings, Notes, Mail, Files, Music and most iPad apps show a sidebar or list on the left and the selected item on the right.

- **Settings:** the sidebar takes the left third in landscape; the right two thirds show the selected page. Settings
  reopens on the page it last showed, and the sidebar can be scrolled so that page's own row is out of view. Tapping a
  sidebar row (`tap_text` its label) replaces the right side and highlights the row in blue.
- The right column's page title often repeats the sidebar label: when `find_text` returns two matches, the sidebar one
  is in the left third.
- Going deeper inside the right column adds a back button (the previous page's name) at the top left of **that
  column**. `back` works for it: it went from About to General.
- Tapping the status bar above a column scrolls that column to the top; the other column stays put.
- **About** (Settings › General › About) lists the iPadOS version, the capacity and the space **Available**.
- In portrait the sidebar may be hidden behind a button at the top left *(unverified)*.

## Scrolling

- `drag` scrolls lists by about its full length (a 400 px drag scrolled 385 to 389 px in the Settings sidebar).
- `flick` scrolls a list well (a flick up went from the top of General to its bottom) and doesn't get stuck.
- Drags and flicks that start on a row scroll without opening it.

## Home Screen and Dock

- `home` (it sends ⌘H) returns to the Home Screen from anywhere and closes Spotlight and menus. From a menu, it only
  closes the menu: call it again to get to page 1.
- The Home Screen mixes widgets with app icons. The **Dock** stays visible; apps after its divider are recent ones (they
  change), and the **App Library** (four small icons) is last. Tapping it opens the App Library: a search field at the
  top and category folders. `home` closes it.
- **Page** with a slow `drag` across most of the width (from about 80% to 20%, at mid height): it turned the page
  cleanly. A `flick` sideways **didn't** turn the page (too short a move on iPadOS 16).
- **Long-press** an icon (`long_press`, default 800 ms): a menu with **Edit Home Screen** and a red **Remove App**. Never
  tap Remove App. `dismiss` **doesn't** close this menu; `home` does.

## Opening apps

`open_app` with the name under the icon works from the Home Screen or from inside an app. It takes 5 to 10 s on an
iPad: Spotlight shows the typed name and then its results a few seconds late. It opens the Top Hit with Enter when the
first app there is the one asked for, and otherwise taps that app's icon. Check the screenshot shows the app.

If `open_app` fails, open the app by hand:

1. Tap the app's icon if it's on the screen (Dock or Home Screen); an icon is a safe target.
2. Otherwise from the Home Screen: tap an **empty part of the wallpaper** first (⌘Space is ignored right after `home`),
   then `press_key` `space` with `command`. Spotlight is a search field at the top centre of the screen.
3. `type_text` the name under the app's icon, then `wait` about 3000: the results appear seconds after typing.
4. When the **Top Hit** shows the app (its icon and name, under the field), `press_key` `enter` opens it. Check the
   screenshot shows the app.
5. To search again: `a` with `command` selects the field's text, then type the new name.

## Split View and Slide Over

- The three dots at the top centre of an app (•••) open the multitasking menu: full screen, Split View, Slide Over. Don't tap them unless the job needs two apps.
- **Two apps side by side** (a thin divider between them): the app you need is the one whose dots are highlighted, or tap inside it. To go back to one app: tap the dots of the app to keep and choose full screen *(unverified)*.
- **An app floating over another** (Slide Over, a narrow window at a side edge): it came from the pointer hitting the right edge or a swipe. Drag it off the right edge by its top bar, or ignore it if it isn't in the way *(unverified)*.
- An app opened from Spotlight shows "◀ Search" at the top left of the status bar: it goes back to Spotlight. Ignore it.

## System surfaces

The pointer opens these when it's pushed into an edge; a job never needs them.

| Edge | Opens | Close with |
|---|---|---|
| Top, middle | Notification Center | `home` |
| Top right | Control Center | `home` |
| Bottom | The Dock over an app; pushed again, the Home Screen | Move on |
| Right | Slide Over | See above |

Seen working: taps 12 px from the top edge (the status bar), 15 px from the right edge, and on a row half hidden at the
bottom opened nothing extra.

## Taps near controls

iPadOS pulls a resting pointer onto the button or icon under or near it (the icon lifts or highlights). A tap aimed **at**
a control lands on its centre, which is what you want. A tap aimed at empty space **next to** a control can be pulled
onto the control. Zeptap reads where the pointer stopped, and when it's more than about 20 points from the spot it
presses nothing and returns `Nothing pressed: the pointer stopped N points from the spot`. Seen 2026-11-04: a tap
between two Dock icons returned that, 37 points off, and opened nothing. Re-aim at the control itself, or well clear of
controls.

## Keyboard shortcuts

| Keys | Does |
|---|---|
| ⌘H | Home (what `home` sends) |
| ⌘Space | Spotlight (after a tap on the Home Screen; see Opening apps) |
| ⌘Tab | Switch to the previous app (seen: Clock → Settings, where it was left) |
| ⌘A | Select all in a field |
| Enter in Spotlight | Opens the Top Hit |
| ⌘ held down | Shows the app's shortcut overlay. `press_key` releases at once, so it doesn't appear |
