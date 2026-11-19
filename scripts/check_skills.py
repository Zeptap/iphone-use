#!/usr/bin/env python3
"""Check every skill in this folder against SPEC.md. Run: python3 -I check_skills.py"""
import pathlib, re, sys

ROOT = pathlib.Path(__file__).resolve().parent.parent / "skills"
EXPECTED = """iphone-use ipad-use instagram tiktok instagram-story-poster instagram-poster tiktok-uploader
youtube-shorts-uploader linkedin-poster short-video-cross-poster multi-account-poster instagram-dm-replies instagram-comment-to-dm
app-onboarding-teardown ios-real-device-testing ios-bug-repro
ios-dynamic-type-check testflight-smoke-test iphone-errands
iphone-shortcuts-builder content-gap-finder hook-and-format-scout content-ideas-from-comments app-store-rank-check app-review-digest
delivery-price-check reddit-poster flight-price-check instagram-warmup tiktok-warmup competitor-content-check weekly-creator-report
comment-replies reddit-research niche-engagement ad-creative-scout linkedin-engagement reddit reddit-karma-builder reddit-lead-finder""".split()
SHIPPED_ELSEWHERE = set()
BANNED = re.compile(r"\b(USB|Bluetooth|AssistiveTouch|OCR)\b")
APP_GUIDES = {"instagram", "tiktok", "reddit"}

problems = []
def bad(skill, msg):
    problems.append(f"{skill}: {msg}")

for name in EXPECTED:
    d = ROOT / name
    f = d / "SKILL.md"
    if not f.exists():
        bad(name, "missing SKILL.md"); continue
    text = f.read_text()
    m = re.match(r"---\nname: (.+)\ndescription: (.+?)\n---\n", text, re.S)
    if not m:
        bad(name, "frontmatter must be exactly name + description"); continue
    if m.group(1).strip() != name:
        bad(name, f"name is {m.group(1)!r}")
    desc = m.group(2).strip()
    if len(desc) > 1024:
        bad(name, f"description {len(desc)} chars (max 1024)")
    if name not in APP_GUIDES and "Zeptap" not in desc:
        bad(name, "description doesn't mention Zeptap")
    if desc.count('"') < 4 and name not in APP_GUIDES:
        bad(name, "description has fewer than 2 quoted trigger phrases")
    body = text[m.end():]
    for w in BANNED.findall(desc + body):
        if name == "iphone-use":
            continue  # its connection reference quotes Zeptap's own errors
        bad(name, f"internal term in skill text: {w}")
    if name not in APP_GUIDES:
        if f"utm_campaign={name}" not in body and "state A message" not in body and "connect message" not in body.lower():
            bad(name, "no connect message or pointer to it")
        if f"utm_campaign=" in body and f"utm_campaign={name}" not in body:
            bad(name, "connect link uses another skill's utm_campaign")
    if not re.search(r"\[(v18|v26|docs|unverified)[\]: ]", body):
        bad(name, "no evidence tags")
    n = len(body.splitlines())
    if n > 320:
        bad(name, f"SKILL.md body is {n} lines (aim under ~250)")
    ev = d / "evals" / "triggers.yaml"
    if not ev.exists():
        bad(name, "missing evals/triggers.yaml")
    else:
        e = ev.read_text()
        parts = e.split("should_not_trigger:")
        if len(parts) != 2:
            bad(name, "evals need should_trigger and should_not_trigger")
        else:
            pos = parts[0].count("\n  - "); neg = parts[1].count("\n  - ")
            if pos < 10 or neg < 5:
                bad(name, f"evals {pos}/{neg} (need 10/5)")
    for ref in re.findall(r"\]\((references/[^)]+)\)", body):
        if not (d / ref).exists():
            bad(name, f"broken link {ref}")
    for other in re.findall(r"`([a-z0-9]+(?:-[a-z0-9]+)+)`", body):
        if other.count("-") >= 1 and other not in EXPECTED and other not in SHIPPED_ELSEWHERE:
            if re.match(r"^(instagram|tiktok|ios|iphone|app|youtube|linkedin|short|multi|influencer|brand|creator|content|trending|camera|testflight)-", other):
                bad(name, f"refers to unknown skill `{other}`")

extra = sorted(p.name for p in ROOT.iterdir() if p.is_dir() and not p.name.startswith("_") and p.name not in EXPECTED)
for x in extra:
    problems.append(f"{x}: folder not in the skill list")

print("\n".join(problems) if problems else "All skills pass.")
print(f"{len(EXPECTED)} expected, {sum((ROOT/n/'SKILL.md').exists() for n in EXPECTED)} present, {len(problems)} problems")
sys.exit(1 if problems else 0)
