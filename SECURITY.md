# Security policy

## What this repo contains

Plain-text agent skills (`SKILL.md` files) and a small Python checker (`scripts/check_skills.py`). There are no install scripts, binaries or network calls in the skills. They are instructions an agent reads.

## How the skills act

The skills drive a real iPhone through Zeptap, in the accounts already signed in on that phone. They are written to:

- ask before anything that spends money, deletes data or changes account settings;
- never enter passwords, payment details or one-time codes;
- follow each app's and community's rules, with no vote manipulation, fake engagement or ban evasion.

If a skill could lead an agent to do something unsafe, that's a security issue for us.

## Reporting a vulnerability

Please don't open a public issue. Use GitHub's **Report a vulnerability** (Security tab → Advisories) on this repo, or contact us through [zeptap.com](https://zeptap.com/?utm_source=gh). We aim to reply within 3 working days.
