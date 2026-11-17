#!/usr/bin/env python3
"""Fix truncated skill descriptions in skills.json and llms.txt.

Root cause: the index files were built by a naive line-based parse that only
kept the FIRST line of each frontmatter description (folded multi-line
descriptions got cut mid-sentence) and kept a stray leading quote on
single/double-quoted scalars. This script restores the full YAML-parsed
description for all 47 skills. Surgical replacement only: no reformatting,
no other field touched. Dry-run by default; pass --apply to write.
"""
import json
import re
import sys
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parent.parent
DRY = "--apply" not in sys.argv


def parse_fm(path):
    txt = path.read_text()
    m = re.search(r"^---\n(.*?)\n---", txt, re.S)
    d = yaml.safe_load(m.group(1)) if m else {}
    return d.get("name"), d.get("description")


def main():
    data = json.load(open(ROOT / "skills.json"))
    sj_raw = (ROOT / "skills.json").read_text()
    ll_raw = (ROOT / "llms.txt").read_text()
    sj_new, ll_new = sj_raw, ll_raw
    changed_json, changed_llms, problems = [], [], []

    for s in data["skills"]:
        name, desc = parse_fm(ROOT / s["path"] / "SKILL.md")
        if not desc:
            problems.append((s["path"], "no description in frontmatter"))
            continue
        # skills.json: replace the exact JSON-encoded old value, once
        old = s["description"]
        if old != desc:
            old_enc = json.dumps(old, ensure_ascii=False)
            new_enc = json.dumps(desc, ensure_ascii=False)
            n = sj_new.count(old_enc)
            if n == 1:
                sj_new = sj_new.replace(old_enc, new_enc, 1)
                changed_json.append(s["path"])
            else:
                problems.append((s["path"], f"json old value occurs {n}x"))
        # llms.txt: rebuild the skill line with the full description
        pat = re.compile(
            r"^(- \[" + re.escape(s["name"]) + r"\]\([^)]+\) \("
            + re.escape(s["category"]) + r"\): ).*$",
            re.M,
        )
        m = pat.search(ll_new)
        if not m:
            problems.append((s["path"], "line not found in llms.txt"))
            continue
        line_old = m.group(0)
        line_new = m.group(1) + desc
        if line_old != line_new:
            ll_new = ll_new.replace(line_old, line_new, 1)
            changed_llms.append(s["name"])

    print(f"skills.json would change: {len(changed_json)}")
    print(f"llms.txt would change: {len(changed_llms)}")
    print(f"problems: {len(problems)}")
    for p in problems:
        print("  PROBLEM:", p)
    for p in changed_json[:5]:
        print("  json:", p)
    for p in changed_llms[:5]:
        print("  llms:", p)
    if DRY:
        print("DRY RUN - no files written. Re-run with --apply.")
        return
    (ROOT / "skills.json").write_text(sj_new)
    (ROOT / "llms.txt").write_text(ll_new)
    print("WROTE skills.json + llms.txt")


if __name__ == "__main__":
    main()
