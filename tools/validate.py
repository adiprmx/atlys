#!/usr/bin/env python3
"""Validasi repo atlys — dijalankan CI tiap push + bisa lokal.

Cek:
1. Setiap folder skill punya SKILL.md dengan frontmatter valid (name, description)
2. Jumlah skill per kategori sesuai (design 17, writing 12, engineering 18)
3. Badge jumlah skill di README utama sesuai hitungan aktual
4. Relative link antar README tidak broken
"""
import re
import sys
from pathlib import Path

try:
    import yaml
except ImportError:
    yaml = None

ROOT = Path(__file__).resolve().parent.parent
EXPECTED = {"design": 17, "writing": 12, "engineering": 18}
fails = []


def fail(msg):
    fails.append(msg)
    print(f"FAIL: {msg}")


def main():
    # 1. frontmatter
    n_total = 0
    per_cat = {}
    for cat in EXPECTED:
        per_cat[cat] = 0
        for d in sorted((ROOT / cat).iterdir()):
            if not d.is_dir():
                continue
            n_total += 1
            per_cat[cat] += 1
            sm = d / "SKILL.md"
            if not sm.exists():
                fail(f"{d}: SKILL.md hilang")
                continue
            t = sm.read_text()
            m = re.match(r"^---\n(.*?)\n---\n", t, re.S)
            if not m:
                fail(f"{d}: SKILL.md tanpa frontmatter")
                continue
            if yaml is None:
                continue
            try:
                fm = yaml.safe_load(m.group(1))
            except Exception as e:
                fail(f"{d}: frontmatter YAML rusak: {e}")
                continue
            if not isinstance(fm, dict) or not fm.get("name") or not fm.get("description"):
                fail(f"{d}: frontmatter tanpa name/description")

    # 2. jumlah per kategori
    for cat, exp in EXPECTED.items():
        if per_cat[cat] != exp:
            fail(f"{cat}/: {per_cat[cat]} skill, expected {exp}")

    # 3. badge README utama
    main_rm = (ROOT / "README.md").read_text()
    m = re.search(r"img\.shields\.io/badge/skills-(\d+)-", main_rm)
    if not m:
        fail("README.md: badge skills tidak ketemu")
    elif int(m.group(1)) != n_total:
        fail(f"README.md: badge skills-{m.group(1)}, aktual {n_total}")

    # 4. relative links
    for rm in sorted(ROOT.rglob("README.md")):
        base = rm.parent
        for lm in re.finditer(r"\]\(([^)\"'#]+)\)", rm.read_text()):
            link = lm.group(1)
            if link.startswith(("http", "mailto:", "#", "assets/")):
                continue
            # abaikan badge/shields
            if "shields.io" in link or link.startswith("!["):
                continue
            target = (base / link).resolve()
            # file atau dir (dengan README.md di dalamnya)
            ok = target.is_file() or (target.is_dir() and (target / "README.md").exists())
            if not ok:
                fail(f"{rm.relative_to(ROOT)}: broken link -> {link}")

    print(f"\n{47 - len(fails)}/{47} skill OK" if False else "")
    if fails:
        print(f"\n{len(fails)} FAIL")
        sys.exit(1)
    print(f"OK: {n_total} skills, frontmatter valid, links valid")


if __name__ == "__main__":
    main()
