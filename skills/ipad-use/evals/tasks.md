# Task evals: ipad-use

Each task runs twice in a fresh agent session with Zeptap connected and both an iPhone and an iPad paired: once with only the core skills installed, once with no skill (plain prompt). Record tool calls, failed actions, wall time, and whether every call went to the iPad.

## T1. Read a system fact through the sidebar (read-only)

- **Start:** iPad unlocked, Settings left open on a page other than General (for example Bluetooth). The iPhone is the device active in Zeptap.
- **Prompt:** "What iPadOS version is my iPad on, and how much storage is free?"
- **Success:** every call passes the iPad's `id`; the answer comes from Settings › General › About and iPad Storage; nothing changed.

## T2. A note in a two-column app (text entry, columns)

- **Start:** iPad on the Home Screen. Notes has at least one existing note.
- **Prompt:** "On my iPad, make a new note that says: Zeptap test, can be deleted."
- **Success on screen:** a new note at the top of the list with that text; no existing note edited.
- **Cleanup:** delete the test note.

## T3. Alarm with a label (pickers on iPad)

- **Start:** iPad unlocked on the Home Screen. No alarm at 6:45 AM exists.
- **Prompt:** "On my iPad, add an alarm for 6:45 AM called Gym, and leave it switched off."
- **Success on screen:** Clock › Alarms lists 6:45 AM, Gym, switch off. No other alarm changed.
- **Cleanup:** delete the Gym alarm.

## T4. No Zeptap (state A)

- **Start:** an agent with no Zeptap tools.
- **Prompt:** "Open Notes on my iPad and add eggs to my grocery list."
- **Success:** the agent explains what it would do, sends the connect message once with `utm_campaign=ipad-use`, and doesn't claim to have done anything on the iPad.

## T5. It types but can't tap (state D)

- **Start:** an iPad on iPadOS 16 paired without the mouse (Zeptap shows "can type but can't tap").
- **Prompt:** "On my iPad, open Settings and turn on Dark Mode."
- **Success:** the agent sees taps change nothing (or reads the note in the tool result), tells the user to click **Pair Again…** in Zeptap, and stops without tapping around.
