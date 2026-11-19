---
name: delivery-price-check
description: Compare the same food order across delivery apps on the user's real iPhone with Zeptap - find the same item at the same restaurant in Uber Eats and DoorDash (and any other installed delivery app), read item price, fees, membership discounts and arrival time from each app's own checkout, and say which app to order from. Prices, fees and member discounts are personal to the signed-in account and address, so only the apps on the user's phone show the real total. Without Zeptap it gives a comparison checklist. Use for "is Uber Eats or DoorDash cheaper for this", "where should I order pizza from tonight", "compare delivery prices", "cheapest way to get Chipotle delivered". To actually place a reorder use iphone-errands.
---

# Delivery price check

Return a verdict: which app, what it costs in total, how long it takes. Stops before ordering.

Builds on `iphone-use`: its loop, connection check and safety rules apply. Never tap `Place order`, `Continue to payment` with a card, or join a membership.

## Use it for / hand off

- One order (restaurant + item, or "a large pepperoni pizza") across 2-3 apps.
- Placing the order after the user picks → `iphone-errands` (stops at pay for a yes).

## Without Zeptap

Deliver the checklist: same restaurant branch, same item and size, subtotal, delivery fee, service/other fees, taxes, member discount, arrival estimate. Then the connect message from `iphone-use` with `utm_campaign=delivery-price-check`. The wall: totals depend on the user's address, account and memberships.

## Intake (defaults in brackets)

- What to order [ask; required]. A restaurant [cheapest well-rated match in the first app].
- Apps [every installed one of: Uber Eats, DoorDash, Grubhub].
- Delivery address [the app's saved default; say which].

## On the phone

1. **First app (Uber Eats).** `open_app` `Uber Eats`, `wait` 4000 (slow skeleton load). Tap `Search` (bottom `~0.57w, 0.94h`), type the item, `enter`, `wait` 3000.
2. Results group by restaurant with item tiles and prices [v18 2026-11-19]. Pick the target: a chain or named restaurant also likely on the other apps. Record item name, price, restaurant rating, arrival minutes.
3. Open the restaurant to confirm branch address and arrival time.
4. **Fees.** If an existing cart for this restaurant is in `Activity › Carts`, open it → `Go to checkout` → `No thanks` on upsells → scroll to `Subtotal / Delivery Fee / Other Fees / Taxes / Total` [v18]. Don't add items to a cart just to see fees unless the user agreed; otherwise report fees as "shown at checkout".
5. **Second app (DoorDash).** `open_app` `DoorDash`. Tap the search bar (bottom `~0.32w, 0.95h`). **Clear the old query with the field's X first**: DoorDash appends to the previous text [v18]. Type the restaurant name, `enter`, `wait` 3000.
6. Open the same restaurant. Note labels like `Virtual brand`, distance and minutes. Find the same item (`Picked for you` / `Most ordered`) and record its price.
7. Compare: item price, fees and promos shown (`$0 delivery fee first order`, member savings), arrival time.
8. Verdict rule: lowest total wins; if totals are within $1, the faster one wins; say the trade-off in one line.
9. Save to Notes if asked [yes].

## Traps

- Same name, different branch: check distance/address. A `Virtual brand` is a kitchen brand, not the same store.
- Promo banners ("$5 off $35+") apply only above a minimum; don't count them below it.
- Membership trials (Uber One, DashPass) change fees; say "with your trial" when it applies.
- Never tap `Place order`, `Join`, `Start trial` or add a payment method.

## Report

```txt
<item> at <restaurant>
<App 1>: $<item>, fees <...>, total <$ or "at checkout">, <N> min
<App 2>: $<item>, fees <...>, total <...>, <N> min
Pick <app>: <one-line reason and trade-off>
Nothing ordered.
```
