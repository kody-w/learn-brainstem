#!/usr/bin/env python3
"""Every skill has the six Agent Skills frontmatter fields it needs, a teach-back, and a done-when."""
import re, sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
REQUIRED_SECTIONS = ("## Done when", "## Teach-back")
ok = True
skills = sorted((ROOT / "skills").glob("*/SKILL.md"))
if len(skills) < 7:
    print(f"expected at least 7 skills, found {len(skills)}"); ok = False
for path in skills:
    text = path.read_text(encoding="utf-8")
    m = re.match(r"^---\n(.*?)\n---\n", text, re.DOTALL)
    if not m:
        print(f"{path}: missing frontmatter"); ok = False; continue
    fm = m.group(1)
    try:
        import yaml  # type: ignore
        parsed = yaml.safe_load(fm)
        if not isinstance(parsed, dict) or "description" not in parsed:
            print(f"{path}: frontmatter is not a mapping with a description"); ok = False
    except ImportError:
        if re.search(r"^description: [^\"'].*: ", fm, re.M):
            print(f"{path}: unquoted description contains ': ' and will not parse as YAML"); ok = False
    except Exception as exc:
        print(f"{path}: frontmatter YAML error: {exc}"); ok = False
    name = re.search(r"^name: (.+)$", fm, re.M)
    if not name or name.group(1).strip() != path.parent.name:
        print(f"{path}: name must equal folder name"); ok = False
    desc = re.search(r"^description: (.+)$", fm, re.M)
    if not desc or len(desc.group(1)) < 80:
        print(f"{path}: description too short"); ok = False
    if "license: MIT" not in fm:
        print(f"{path}: license missing"); ok = False
    for section in REQUIRED_SECTIONS:
        if path.parent.name != "learn-brainstem" and section not in text:
            print(f"{path}: missing {section}"); ok = False
    if "customer" in text.lower() and "no customer data" not in text.lower() and "synthetic" not in text.lower():
        print(f"{path}: mentions customers without the synthetic-data rule"); ok = False
    for line in text.splitlines():
        if len(line) > 110 and not line.startswith(("http", "|", "  ", "```", "description:")) and "http" not in line:
            print(f"{path}: line over 110 chars: {line[:60]}..."); ok = False
print("ok" if ok else "FAIL"); sys.exit(0 if ok else 1)
