# Contributing

Thanks for helping make iPhone agents more useful. Good contributions here are small, tested on a real iPhone and written so an agent can follow them without guessing.

## What we welcome

- **Screen notes for app updates.** An app changed its layout and a step broke. Fix the step and add an evidence tag like `[v18 2026-11-19]` (iOS version, date checked).
- **Fixes to a skill's steps, limits or report.**
- **New skills** for jobs people really do on their phone.

## A good skill

- Lives in `skills/<skill-id>/SKILL.md`. The `name` in the frontmatter equals the folder name (lowercase, hyphens).
- The `description` says what it does and when to use it, in plain words, under 1,024 characters, with no angle brackets.
- Runs in order: setup questions on the first run only, the steps, stop rules, then a short report.
- Has a "Without Zeptap" section, so it still helps people who haven't connected an iPhone.
- Never asks the agent to do anything you wouldn't do yourself. No vote manipulation, no fake accounts, no spam.

## Before you open a pull request

```bash
python3 scripts/check_skills.py
```

It must say `0 problems`. Describe what you tested, on which iPhone and iOS version.

## Questions

Open an issue, or reach us through [zeptap.com](https://zeptap.com/?utm_source=gh).
