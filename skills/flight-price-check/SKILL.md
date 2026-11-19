---
name: flight-price-check
description: Compare the same flight across the travel apps the user picks on their real iPhone with Zeptap - search the route and dates in two or more installed flight apps (any of them, e.g. Skyscanner, Google Flights, Kayak, Hopper, Expedia or an airline app), read the cheapest and best fares, any buy-or-wait prediction or price calendar an app shows, and say whether to book now, wait, or shift dates. Stops before booking. Fares, alerts and predictions shown in the apps are not available through a free public API and change by the hour. Without Zeptap it gives the comparison checklist. Use for "should I book LAX to JFK now or wait", "check flight prices across my travel apps", "find the cheapest week to fly to Lisbon", "is this flight cheaper somewhere else".
---

# Flight price check

Return one decision: book now (where, which fare), wait (until when), or move dates (to which week). Never books.

Builds on `iphone-use`: its loop, connection check and safety rules apply. Never tap `Book`, `Select fare` to pay, `Watch this trip` (creates an alert and may ask to sign in) or any sign-in, unless the user asks.

## Use it for / hand off

- One route, one date range (round-trip or one-way), 2-3 travel apps of the user's choice.
- Hotels, rides → `iphone-errands`.

## Without Zeptap

Deliver the checklist: same airports, same dates, cabin, bags included or not, stops, total per traveller, and the decision rule below. Then the connect message from `iphone-use` with `utm_campaign=flight-price-check`.

## Intake (defaults in brackets)

- From, to, dates [ask; required]. Travellers [1]. Cabin [economy].
- Nonstop only [no]. Bags [carry-on only].
- Apps [ask once which travel apps to use and save it in Notes as `Flight apps`; default every installed flight app, plus Google Flights in Safari]. Any flight app works; the screen notes below cover the ones tested.

## Decision rule

1. Compare the **cheapest** and the **best nonstop** on each app, same dates and airports.
2. If an app gives buy-or-wait advice (e.g. Hopper's prediction, Kayak's price forecast) and predicts a drop over $50 within 7 days → "wait", say the predicted low and the date it rises.
3. If any app's price calendar shows a week at least 15% cheaper and the user's dates are flexible → name that week.
4. Otherwise → book the lowest total in the app that shows it; say which fare and why (nonstop vs stop trade-off in one line).

## On the phone

For any flight app: open it, set the same airports, dates, travellers and cabin, search, and read the cheapest and best (nonstop) result plus any prediction or calendar. Tested screens for two common apps [v18 2026-11-19]:


1. **KAYAK.** `open_app` `KAYAK`, `wait` 2000. The home form shows `Round-trip / One-way`, origin, `To?`, dates, travellers [v18 2026-11-19]. Tap each field to change it; origin defaults to the phone's region.
2. Tap `To?` → type the city → tap the exact airport row (not "All airports" unless asked). Set dates if different. Tap **Search**, `wait` 6000 (splash, then "Searching for lower prices…").
3. Read the first two result cards: **Best** and **Cheapest** labels, airline, times, stops, price [v18]. Skip the `Ad` card.
4. **Hopper.** `open_app` `Hopper`, `wait` 2000. It opens on **Stays**: tap the **Flights** tab by position (`~0.5w, 0.12h`; `tap_text` misses it), then the search bar (`~0.44w, 0.19h`).
5. Type the origin code (`LAX`), `wait` 2000 (first suggestions can be wrong until location loads), tap the matching airport row. Type the destination code, tap its row.
6. Tap **Departure Date**: the calendar is colour-coded by price ($370+ green … $400+ red) [v18]. Note the cheapest week. Tap the departure, then the return date, then `Select These Dates`, then `Search`, `wait` 12000 (two loading screens).
7. Read **Current Lowest Price**, the buy/wait advice, and the **Price Prediction** timeline (predicted low, when prices rise) [v18 2026-11-19]. Don't tap `Watch This Trip`.
8. Apply the decision rule. Save to Notes if asked [yes]: compose, line by line, `Done`.

## Traps

- Kayak prices are per person and may exclude bags; Hopper says "/ traveler". Compare like with like.
- Hopper's lowest can be higher than Kayak's (different inventory); report both, don't assume.
- Prices change between apps in minutes; report the time checked.

## Report

```txt
<from>-<to>, <dates>, <n> traveler(s), checked <time>
KAYAK: cheapest $<x> (<airline>, <stops>); best $<y> (<airline>, nonstop)
Hopper: lowest $<z>; advice <Buy|Wait>; predicted low $<p> by <date>
Cheapest week: <dates> (<price band>)
Decision: <Book X on Y | Wait until Z | Move to week W> - <reason>
Nothing booked.
```
