# iPad connection cases

The cases below are the ones only iPads have. For every other Zeptap message, use `iphone-use` › `references/connection.md`: the messages are the same, and they say "iPhone" for iPads too.

Fixes marked **user** need a person at the Mac or the iPad: say what to do, then wait for them to say it's done.

## Finding it

| You see | Do |
|---|---|
| `list_phones` has no row with an `iPad…` model | **User:** plug the iPad into the Mac, open Zeptap and follow **Pair New iPhone** (it pairs iPads too) |
| The iPad's row says `ready=no (not connected over Bluetooth; …)` | Name it as `phone` in your next call: Zeptap connects it then. If that call says it `isn't answering over Bluetooth`, see below |
| A result starts with another device's name (`[Saransh's iPhone]`) | You left out `phone`. Repeat the call with the iPad's `id` |

## Taps, scrolls and drags do nothing

Typing reaches the iPad (Spotlight opens, text appears) but nothing you tap changes anything.

| You see | Do |
|---|---|
| Zeptap shows "<iPad> can type but can't tap" or "<iPad> didn't finish pairing", or the iPad's subtitle reads "Can't tap, pair again" or "Pairing didn't finish" | **User:** in Zeptap, click **Pair Again…** in that banner and follow its steps: on the iPad, **Settings › Bluetooth**, tap ⓘ next to the Mac, **Forget This Device**, then tap the Mac to pair again. Stop until they say it's done |
| The iPad says "Pairing Unsuccessful: "<Mac>" is not supported" while pairing again | **User:** tap OK and tap the Mac again. Seen 2026-11-04: it failed three times, then paired on the next try |
| A tap did nothing, and Zeptap shows no banner | `wait` 5000 (Zeptap checks a newly connected iPad's pointer in its first few seconds), then try the tap once more. Still nothing: **user:** open Zeptap and check the iPad's subtitle |

Why: an iPad on iPadOS 16 can only be moved by the mouse that's part of its Bluetooth pairing. A pairing made while Zeptap was set up for an iPhone lacks it, and only pairing again adds it. iPadOS 17 and later don't need it.

## Slow taps are normal

On iPadOS 16 a tap takes about a second before the press (Zeptap steers the pointer onto the spot and checks where it landed); a move after the iPad sat idle for a while can take about two. Don't send the tap again while you wait for its screenshot. Measured 2026-11-04: six moves landed within about a point of their targets, in 0.55 to 2.1 s.

## The iPad stops answering after Zeptap restarts

| You see | Do |
|---|---|
| `<iPad> isn't answering over Bluetooth, …` right after Zeptap was quit and reopened, while the iPad is on and nearby | **User:** turn Bluetooth off and on in the iPad's Control Center, then ask again *(unverified: seen 2026-11-04 on an iPhone and an iPad, cleared from the Mac by closing the Bluetooth link)* |

## Locking

`unlock` and `lock` work as on iPhone, with the passcode saved for the iPad in **Zeptap › Settings › Phones** *(unverified on iPad)*. An iPad with Touch ID or Face ID may unlock itself first; `unlock` then says so.
